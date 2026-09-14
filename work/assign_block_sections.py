#!/usr/bin/env python3
"""assign_block_sections.py — set `section-id` and `section-order` on every content block.

Usage:
    python work/assign_block_sections.py [--slug <source-slug>] [--dry-run]

For each block under wiki/<category>/*.md, the FIRST `verbatim-ref`
(verbatim/<slug>/pages/pNNNN.md#¶n — the template's "primary passage") is
resolved to the deepest non-minor section in verbatim/<slug>/sections.json that
contains that (page, ¶). Four fields are set:

  section-id     that deepest section's id (the precise subsection)
  section-path   its breadcrumb of titles from the proposal section down
  section-order  1-based reading-order ordinal of the block within its PROPOSAL
                 SECTION — the PDF-bookmarked section that contains the subsection
                 (e.g. Hull "Section 5", MMSD "IV.A.3. Approach to PM and CM") —
                 by (min ref page, min ref ¶, path), so the numbers run 1..N
  doc-order      the same ordinal across every block of the source

Fallback blocks are included in the ordinals (the assembler hides them by default).

Writes work/fragments/section_patches.json and applies it with
work/patch_frontmatter.py (frontmatter only; bodies byte-checked; idempotent),
then work/section_assignment_report.md. Nothing else on the block is touched.
Run this after any block build (extract-proposal, fill-gaps).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verbatim_sections import ROOT, load_sections, section_for  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml is required", file=sys.stderr)
    sys.exit(1)

CATEGORY_DIRS = ["technical-approach", "management-staffing", "win-themes", "qualifications",
                 "compliance-plans", "resumes", "past-performance"]
REF_RE = re.compile(r"verbatim/(?P<slug>[^/]+)/pages/p(?P<page>\d{4})\.md#¶(?P<para>\d+)")


def load_frontmatter(text: str):
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            try:
                return yaml.safe_load("\n".join(lines[1:i])) or {}
            except Exception:
                return None
    return None


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def parse_refs(fm: dict):
    out = []
    for r in as_list(fm.get("verbatim-ref")):
        m = REF_RE.search(str(r))
        if m:
            out.append((m.group("slug"), int(m.group("page")), int(m.group("para"))))
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default=None, help="only blocks from this source")
    ap.add_argument("--dry-run", action="store_true", help="write the patch file and report, do not apply")
    args = ap.parse_args()

    sections_cache: dict[str, dict] = {}
    missing_sections: set[str] = set()
    rows = []          # dict(path, slug, sid, pos, spans, fm)
    unassigned = []    # (path, reason)
    unparseable = []

    for cat in CATEGORY_DIRS:
        for path in sorted((ROOT / "wiki" / cat).glob("*.md")):
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            fm = load_frontmatter(path.read_text(encoding="utf-8"))
            if fm is None:
                unparseable.append(rel)
                continue
            slug = str(fm.get("source") or "")
            if args.slug and slug != args.slug:
                continue
            if slug not in sections_cache:
                try:
                    sections_cache[slug] = load_sections(slug)
                except FileNotFoundError:
                    sections_cache[slug] = {}
                    missing_sections.add(slug)
            doc = sections_cache[slug]
            if not doc:
                unassigned.append((rel, f"no sections.json for source '{slug}'"))
                continue
            refs = [(p, q) for s, p, q in parse_refs(fm) if s == slug]
            if not refs:
                unassigned.append((rel, "no parseable verbatim-ref for its own source"))
                continue
            first = refs[0]
            sec = section_for(doc, *first)
            if sec is None:
                unassigned.append((rel, f"first ref p{first[0]:04d}¶{first[1]} is outside every section"))
                continue
            spans = sorted({s["id"] for s in (section_for(doc, p, q) for p, q in refs) if s})
            # breadcrumb from the proposal (outline) section down to the deepest section
            by_id = {s["id"]: s for s in doc["sections"]}
            chain, cur = [], sec
            while cur:
                chain.append(cur)
                cur = by_id.get(cur.get("parent") or "")
            chain.reverse()
            path_titles = [c["title"] for c in chain]
            outline_key = f"{slug}:{sec['outline_index']}"
            rows.append(dict(path=rel, slug=slug, sid=sec["id"], first=first, minpos=min(refs), spans=spans, fm=fm,
                             outline_key=outline_key, section_path=" › ".join(path_titles)))

    # ordinals: within the proposal (outline) section, and across the whole source
    by_outline: dict[str, list] = {}
    by_slug: dict[str, list] = {}
    for r in rows:
        by_outline.setdefault(r["outline_key"], []).append(r)
        by_slug.setdefault(r["slug"], []).append(r)
    for items in by_outline.values():
        items.sort(key=lambda r: (r["minpos"][0], r["minpos"][1], r["path"]))
        for i, r in enumerate(items, start=1):
            r["order"] = i
    for items in by_slug.values():
        items.sort(key=lambda r: (r["minpos"][0], r["minpos"][1], r["path"]))
        for i, r in enumerate(items, start=1):
            r["doc_order"] = i

    patches = [{"path": r["path"], "set": {"section-id": r["sid"], "section-path": r["section_path"],
                                           "section-order": r["order"], "doc-order": r["doc_order"]}} for r in rows]
    changed = sum(1 for r in rows if r["fm"].get("section-id") != r["sid"] or r["fm"].get("section-order") != r["order"]
                  or r["fm"].get("doc-order") != r["doc_order"] or r["fm"].get("section-path") != r["section_path"])

    frag = ROOT / "work" / "fragments"
    frag.mkdir(parents=True, exist_ok=True)
    patch_path = frag / "section_patches.json"
    patch_path.write_text(json.dumps(patches, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    # report
    multi = [r for r in rows if len(r["spans"]) > 1]
    per_slug: dict[str, int] = {}
    for r in rows:
        per_slug[r["slug"]] = per_slug.get(r["slug"], 0) + 1
    lines = ["# Section assignment report", "",
             f"Blocks assigned: {len(rows)} ({changed} with a new or changed value) · unassigned: {len(unassigned)} · unparseable frontmatter: {len(unparseable)}", ""]
    lines.append("| source | blocks assigned |")
    lines.append("|---|---:|")
    for s in sorted(per_slug):
        lines.append(f"| {s} | {per_slug[s]} |")
    if missing_sections:
        lines += ["", "## Sources without sections.json", ""] + [f"- `{s}` — run `python work/build_sections.py {s}`" for s in sorted(missing_sections)]
    lines += ["", f"## Blocks whose refs span more than one section ({len(multi)})", "",
              "The first ref decides `section-id`; the others are listed here for information only.", ""]
    for r in multi:
        lines.append(f"- `{r['path']}` → `{r['sid']}`; also touches {', '.join('`'+s+'`' for s in r['spans'] if s != r['sid'])}")
    lines += ["", f"## Unassigned ({len(unassigned)})", ""] + [f"- `{p}` — {why}" for p, why in unassigned]
    if unparseable:
        lines += ["", "## Unparseable frontmatter", ""] + [f"- `{p}`" for p in unparseable]
    (ROOT / "work" / "section_assignment_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"assigned={len(rows)} changed={changed} unassigned={len(unassigned)} unparseable={len(unparseable)} multi-section={len(multi)}")
    print(f"wrote {patch_path.relative_to(ROOT)} and work/section_assignment_report.md")
    if args.dry_run:
        print("dry run: patches not applied")
        return
    rc = subprocess.call([sys.executable, str(ROOT / "work" / "patch_frontmatter.py"), str(patch_path)])
    sys.exit(rc)


if __name__ == "__main__":
    main()
