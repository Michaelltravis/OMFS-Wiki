#!/usr/bin/env python3
"""make_gap_ranges.py — turn work/gaps/<slug>.json into fill-gaps.js ranges.

Usage:
    python work/make_gap_ranges.py <slug> [--max-pages 8] [--max-paras 20] [--status uncovered]

Groups the uncovered paragraphs by their nearest non-minor section ancestor of
level <= 3, splits any group wider than --max-pages pages or --max-paras
paragraphs, and writes work/fragments/ranges_gapfill_<slug>.json — the `args`
for .claude/workflows/fill-gaps.js:

  {"wiki": ..., "slug": ..., "clientNames": [...], "context": "...", "ranges": [
     {"slug", "name", "pages": [a, b], "category", "rfpSectionType",
      "existingBlocks": [...], "uncovered": [{"page", "para", "words", "first_words", "ref"}]} ]}

category / rfpSectionType come from the majority of existing blocks in the same
section subtree (fallback: a keyword map on the section title).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verbatim_sections import ROOT, load_sanitize, load_sections, subtree_ids  # noqa: E402

CONTEXT = {
    "hull-wwtf-om-2026": "Coastal New England municipal WWTF (3.07 MGD) + collection system O&M, 2026; MassDEP",
    "santamonica-swip-om-2025": "Southern California sustainable water infrastructure O&M, 2025; SWRCB-DDW",
    "ocwut-16-26": "Southcentral US water utility trust, four WWTPs >110 MGD + biosolids, 2026 challenger bid; ODEQ",
    "fulton-county-2025": "Southeast US county, three MBR WRFs + 33 pump stations, 2025, bid as JC Solutions (Jacobs/CERM JV); GA EPD",
    "mmsd-om-2028": "Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid vs. incumbent operator; WDNR",
}
KEYWORDS = [
    (r"resume|key staff|key personnel|\bbio\b|, (pe|phd|crl|csp|pmp|sphr|cmrt)\b", "resumes", ["resume"]),
    (r"reference|past performance|project description|similar (facilities|projects)|pump station experience|experience$", "past-performance", ["past-performance"]),
    (r"safety|security|emergency|compliance record|environmental compliance|qa/qc|quality control", "compliance-plans", ["compliance"]),
    (r"transition|mobiliz|pre-term|commencement|exit plan|succession|compensation|employee|retention", "management-staffing", ["transition"]),
    (r"staff|personnel|training|workforce|culture|subcontract|labor|union|organization|leadership team|team organization", "management-staffing", ["staffing"]),
    (r"disclosure|enforcement|violation|statutory|exception|litigation|identity|financial|insurance|legal|corporate|qualifications of the firm", "qualifications", ["qualifications"]),
    (r"executive summary|cover letter|transmittal|why (jacobs|us)|partnership|community|outreach", "win-themes", ["exec-summary"]),
]


def guess(title: str):
    """(category, rfp-section-type) from the section title, or None when no keyword matches."""
    t = title.lower()
    for rx, cat, rst in KEYWORDS:
        if re.search(rx, t):
            return cat, rst
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--max-pages", type=int, default=8)
    ap.add_argument("--max-paras", type=int, default=20)
    ap.add_argument("--status", default="uncovered", help="uncovered | uncovered,partial")
    args = ap.parse_args()
    slug = args.slug
    statuses = set(args.status.split(","))

    gaps = json.loads((ROOT / "work" / "gaps" / f"{slug}.json").read_text(encoding="utf-8"))
    doc = load_sections(slug)
    by_id = {s["id"]: s for s in doc["sections"]}
    idx = json.loads((ROOT / "wiki" / "index.json").read_text(encoding="utf-8"))
    blocks = [b for b in idx if str(b.get("source")) == slug]

    def anchor(sid: str | None):
        """nearest non-minor ancestor with level <= 3 (or the section itself)."""
        s = by_id.get(sid or "")
        while s and (s["level"] > 3 or s.get("minor")):
            s = by_id.get(s.get("parent") or "")
        return s

    groups: dict[str, list] = {}
    for r in gaps["rows"]:
        if r["status"] not in statuses:
            continue
        a = anchor(r.get("section_id"))
        key = a["id"] if a else f"{slug}:00-front"
        groups.setdefault(key, []).append(r)

    ranges = []
    for sid, rows in groups.items():
        rows.sort(key=lambda r: (r["page"], r["para"]))
        sec = by_id.get(sid)
        title = sec["title"] if sec else "Front matter"
        sub = set(subtree_ids(doc, sid)) if sec else set()
        existing = sorted(b["path"] for b in blocks if b.get("section-id") in sub)
        # category: a title keyword wins (a disclosures or transition heading should not inherit
        # its neighbours' folder); otherwise the majority of existing blocks in the subtree;
        # otherwise technical-approach.
        cats = Counter(b.get("category") for b in blocks if b.get("section-id") in sub)
        rsts = Counter(tuple(b.get("rfp-section-type") or []) for b in blocks if b.get("section-id") in sub)
        g = guess(title) or (guess(sec["outline_title"]) if sec and sec.get("outline_title") else None)
        if g:
            category, rst = g
        elif cats:
            category = cats.most_common(1)[0][0]
            rst = list(rsts.most_common(1)[0][0]) if rsts and rsts.most_common(1)[0][0] else ["tech-approach"]
        else:
            category, rst = "technical-approach", ["tech-approach"]
        # split into chunks by page width / paragraph count
        chunk, chunks = [], []
        for r in rows:
            if chunk and (r["page"] - chunk[0]["page"] + 1 > args.max_pages or len(chunk) >= args.max_paras):
                chunks.append(chunk)
                chunk = []
            chunk.append(r)
        if chunk:
            chunks.append(chunk)
        for i, ch in enumerate(chunks, 1):
            name = title if len(chunks) == 1 else f"{title} (part {i})"
            ranges.append({
                "slug": slug, "name": name, "sectionId": sid,
                "pages": [ch[0]["page"], ch[-1]["page"]],
                "category": category, "rfpSectionType": rst,
                "existingBlocks": existing,
                "uncovered": [{"page": r["page"], "para": r["para"], "words": r["words"],
                               "kind": r["kind"], "first_words": r["first_words"], "ref": r["ref"]} for r in ch],
            })
    ranges.sort(key=lambda r: (r["pages"][0], r["pages"][1]))

    # merge adjacent ranges of the same category when the combined span stays small —
    # one writer can handle a few nearby gaps, and it halves the number of agent calls
    merged = []
    for r in ranges:
        prev = merged[-1] if merged else None
        if prev and prev["category"] == r["category"] and prev["rfpSectionType"] == r["rfpSectionType"] \
                and r["pages"][1] - prev["pages"][0] + 1 <= args.max_pages \
                and len(prev["uncovered"]) + len(r["uncovered"]) <= args.max_paras:
            prev["pages"] = [prev["pages"][0], max(prev["pages"][1], r["pages"][1])]
            prev["name"] = f"{prev['name']} + {r['name']}" if len(prev["name"]) < 120 else prev["name"] + " +"
            prev["sectionIds"] = sorted(set(prev.get("sectionIds", [prev["sectionId"]]) + [r["sectionId"]]))
            prev["existingBlocks"] = sorted(set(prev["existingBlocks"]) | set(r["existingBlocks"]))
            prev["uncovered"] += r["uncovered"]
        else:
            r["sectionIds"] = [r["sectionId"]]
            merged.append(r)
    ranges = merged

    cfg = load_sanitize(slug) or {}
    names = list(cfg.get("client_names") or []) + list(cfg.get("client_aliases") or [])
    for fac in cfg.get("facility_names") or []:
        names += list(fac.get("names") or [])
    for prod in cfg.get("product_names") or []:
        names += list(prod.get("names") or [])
    out = {"wiki": str(ROOT), "slug": slug, "clientNames": names, "context": CONTEXT.get(slug, slug),
           "ranges": ranges}
    frag = ROOT / "work" / "fragments"
    frag.mkdir(parents=True, exist_ok=True)
    p = frag / f"ranges_gapfill_{slug}.json"
    p.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    n = sum(len(r["uncovered"]) for r in ranges)
    print(f"[{slug}] ranges={len(ranges)} paragraphs={n} -> {p.relative_to(ROOT)}")
    for r in ranges:
        print(f"  pp.{r['pages'][0]}-{r['pages'][1]:<4} {len(r['uncovered']):>3} ¶  {r['category']:<20} {r['name'][:70]}")


if __name__ == "__main__":
    main()
