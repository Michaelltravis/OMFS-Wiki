#!/usr/bin/env python3
"""find_uncovered.py — which substantive verbatim paragraphs have no content block?

Usage:
    python work/find_uncovered.py <slug> [--min-covered 0.2] [--partial 0.5]
                                         [--min-words 25] [--include-recovered] [--pages A-B]

Paragraph-level inversion of work/map_blocks_to_pages.py: the union of 6-word
shingles over every block of the source (bodies minus "## Reuse guidance") is
compared against each substantive paragraph of the verbatim pages. A paragraph
is `uncovered` below --min-covered, `partial` below --partial, else `covered`.
Client / facility names and their placeholders ([CLIENT], [FACILITY A], ...)
normalize to one token so sanitized blocks still match.

Scope: pages listed in work/gap_scope.json for the slug are skipped (cover/TOC,
commercial sections, forms, out-of-scope appendices). Substantive = >= --min-words,
not a heading / caption / picture text / running line / recovered tail.

Writes work/gaps/<slug>.json and work/gaps/<slug>.md and prints the counts.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verbatim_sections import (  # noqa: E402
    ROOT, is_substantive, load_pages, load_sanitize, load_sections, plain_text, section_for,
)
from map_blocks_to_pages import normalize, shingles, parse_frontmatter, strip_reuse_guidance  # noqa: E402

CATEGORY_DIRS = ["technical-approach", "management-staffing", "win-themes", "qualifications",
                 "compliance-plans", "resumes", "past-performance"]
PLACEHOLDER_RE = re.compile(r"\[(?:client|facility [a-z]|project|pump station|the region|the service area|product)\]", re.IGNORECASE)


def name_normalizer(cfg: dict | None):
    names = []
    if cfg:
        names += list(cfg.get("client_names") or []) + list(cfg.get("client_aliases") or [])
        for fac in cfg.get("facility_names") or []:
            names += list(fac.get("names") or [])
        for prod in cfg.get("product_names") or []:
            names += list(prod.get("names") or [])
            if prod.get("replacement"):
                names.append(prod["replacement"])
    names = sorted({n for n in names if n}, key=len, reverse=True)
    rx = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(n) for n in names) + r")(?![A-Za-z0-9])", re.IGNORECASE) if names else None

    def norm(text: str) -> str:
        text = PLACEHOLDER_RE.sub(" cli ", text)
        if rx:
            text = rx.sub(" cli ", text)
        # verbatim table cells often fuse words ("ProcessSpecialists", "OFCITY'S", "water2025")
        # where the block's cleaned table has spaces; split at case and letter/digit boundaries
        text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
        text = re.sub(r"([A-Za-z])(\d)", r"\1 \2", text)
        text = re.sub(r"(\d)([A-Za-z])", r"\1 \2", text)
        text = re.sub(r"[»•▪■µ|]", " ", text)
        return normalize(text)
    return norm


def load_skips(slug: str) -> dict:
    """Writer decisions from earlier fill-gaps runs: {(page, para): reason}. A paragraph a writer
    skipped as duplicate-of / exhibit-internal / commercial is reported as such, not as uncovered."""
    p = ROOT / "work" / "gaps" / f"{slug}.skips.json"
    if not p.is_file():
        return {}
    out = {}
    for r in json.loads(p.read_text(encoding="utf-8")):
        out[(int(r["page"]), int(r["para"]))] = str(r.get("reason", "skipped"))
    return out


def in_scope(page: int, excl: list) -> bool:
    return not any(a <= page <= b for a, b in excl)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--min-covered", type=float, default=0.2)
    ap.add_argument("--partial", type=float, default=0.5)
    ap.add_argument("--min-words", type=int, default=25)
    ap.add_argument("--include-recovered", action="store_true")
    ap.add_argument("--pages", default=None, help="A-B: restrict to this page range")
    args = ap.parse_args()
    slug = args.slug

    doc = load_sections(slug)
    pages = load_pages(slug)
    repeating = set(doc.get("repeating_lines") or [])
    cfg = load_sanitize(slug)
    norm = name_normalizer(cfg)
    scope = json.loads((ROOT / "work" / "gap_scope.json").read_text(encoding="utf-8")).get(slug, {})
    excl = [tuple(x) for x in scope.get("exclude", [])]
    if args.pages:
        a, b = (int(x) for x in args.pages.split("-"))
        excl += [(1, a - 1), (b + 1, 10**6)]

    # union of block shingles for this source
    blocks = []  # (path, shingle set)
    for cat in CATEGORY_DIRS:
        for path in sorted((ROOT / "wiki" / cat).glob("*.md")):
            fm, body = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
            if fm.get("source") != slug:
                continue
            sh = shingles(norm(strip_reuse_guidance(body)))
            blocks.append((str(path.relative_to(ROOT)).replace("\\", "/"), sh))
    union = set()
    for _p, sh in blocks:
        union |= sh

    skips = load_skips(slug)
    rows = []
    counts = {"substantive": 0, "covered": 0, "partial": 0, "uncovered": 0, "writer_skipped": 0, "skipped": {}}
    for pno in sorted(pages):
        if not in_scope(pno, excl):
            continue
        for para in pages[pno][1]:
            ok, why = is_substantive(para, repeating, min_words=args.min_words, include_recovered=args.include_recovered)
            if not ok:
                counts["skipped"][why] = counts["skipped"].get(why, 0) + 1
                continue
            counts["substantive"] += 1
            sh = shingles(norm(para.text))
            frac = len(sh & union) / len(sh) if sh else 0.0
            if frac >= args.partial:
                counts["covered"] += 1
                continue
            status = "uncovered" if frac < args.min_covered else "partial"
            if (pno, para.n) in skips:
                status = "writer-skipped"
                counts["writer_skipped"] += 1
            if status in counts:
                counts[status] += 1
            best, best_f = None, 0.0
            for p, bsh in blocks:
                f = len(sh & bsh) / len(sh) if sh else 0.0
                if f > best_f:
                    best, best_f = p, f
            sec = section_for(doc, pno, para.n)
            words = plain_text(para.text).split()
            rows.append({
                "page": pno, "para": para.n, "status": status, "covered_fraction": round(frac, 3),
                "words": len(words), "kind": "table" if para.text.lstrip().startswith("|") else "prose",
                "section_id": sec["id"] if sec else None, "section_title": sec["title"] if sec else None,
                "best_block": best, "best_fraction": round(best_f, 3),
                "first_words": " ".join(words[:12]),
                "ref": f"verbatim/{slug}/pages/p{pno:04d}.md#¶{para.n}",
                "writer_reason": skips.get((pno, para.n)),
            })

    out_dir = ROOT / "work" / "gaps"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{slug}.json").write_text(json.dumps({"slug": slug, "params": vars(args), "counts": counts, "rows": rows},
                                                     indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    # markdown summary by section
    lines = [f"# Uncovered paragraphs — {slug}", "",
             f"substantive {counts['substantive']} · covered {counts['covered']} · partial {counts['partial']} · uncovered {counts['uncovered']} "
             f"· writer-skipped {counts['writer_skipped']} "
             f"(thresholds: uncovered < {args.min_covered}, partial < {args.partial}; min words {args.min_words}; blocks {len(blocks)})", "",
             "skipped: " + ", ".join(f"{k} {v}" for k, v in sorted(counts["skipped"].items())), ""]
    by_sec: dict[str, list] = {}
    for r in rows:
        by_sec.setdefault(r["section_title"] or "(no section)", []).append(r)
    for st, items in by_sec.items():
        u = sum(1 for r in items if r["status"] == "uncovered")
        p = sum(1 for r in items if r["status"] == "partial")
        lines.append(f"## {st} — uncovered {u}, partial {p}")
        lines.append("")
        for r in items:
            lines.append(f"- p{r['page']:04d}¶{r['para']} · {r['status']} {int(r['covered_fraction']*100)}% · {r['words']} w · {r['kind']}"
                         + (f" · best `{r['best_block']}` ({int(r['best_fraction']*100)}%)" if r["best_block"] and r["best_fraction"] > 0 else "")
                         + (f" · writer: {r['writer_reason']}" if r.get("writer_reason") else "")
                         + f" — {r['first_words']}…")
        lines.append("")
    (out_dir / f"{slug}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"[{slug}] substantive={counts['substantive']} covered={counts['covered']} partial={counts['partial']} uncovered={counts['uncovered']} writer-skipped={counts['writer_skipped']} blocks={len(blocks)}")
    print(f"  wrote work/gaps/{slug}.json and .md")


if __name__ == "__main__":
    main()
