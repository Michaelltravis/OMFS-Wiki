#!/usr/bin/env python3
"""status_counts.py — print the numbers the README status table reports, per source (read-only).

Usage:
    python work/status_counts.py [--md]

For each source slug: content blocks by category, verbatim pages, proof-point
registry rows that cite the source, uncovered / writer-skipped paragraphs from
work/gaps/, and whether every block carries section-order. --md prints a
markdown table ready to paste into README.md.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATS = ["technical-approach", "management-staffing", "win-themes", "qualifications",
        "compliance-plans", "resumes", "past-performance"]


def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true")
    args = ap.parse_args()

    idx = json.loads((ROOT / "wiki" / "index.json").read_text(encoding="utf-8"))
    by_src: dict[str, Counter] = defaultdict(Counter)
    missing_order: Counter = Counter()
    for b in idx:
        s = str(b.get("source"))
        by_src[s][str(b.get("category"))] += 1
        if not b.get("section-order") or not b.get("doc-order"):
            missing_order[s] += 1

    reg_rows: Counter = Counter()
    reg = ROOT / "proof-points" / "registry.json"
    if reg.is_file():
        for row in json.loads(reg.read_text(encoding="utf-8")):
            srcs = {v.get("source_slug") for v in row.get("values", [])}
            for s in srcs:
                reg_rows[s] += 1

    rows = []
    for slug in sorted(by_src):
        pages = len(list((ROOT / "verbatim" / slug / "pages").glob("p*.md"))) if (ROOT / "verbatim" / slug / "pages").is_dir() else 0
        gaps = ROOT / "work" / "gaps" / f"{slug}.json"
        unc = ws = "-"
        if gaps.is_file():
            g = json.loads(gaps.read_text(encoding="utf-8"))
            unc = g["counts"].get("uncovered", "-")
            ws = g["counts"].get("writer_skipped", "-")
        c = by_src[slug]
        total = sum(c.values())
        cats = ", ".join(f"{c[k]} {k}" for k in CATS if c.get(k))
        rows.append((slug, total, cats, pages, reg_rows.get(slug, 0), unc, ws, missing_order[slug]))

    if args.md:
        print("| Source | Blocks | By category | Verbatim pages | Registry rows | Uncovered ¶ | Writer-skipped ¶ | Blocks without order |")
        print("|---|---:|---|---:|---:|---:|---:|---:|")
        for r in rows:
            print(f"| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |")
    else:
        for r in rows:
            print(f"{r[0]}: blocks={r[1]} ({r[2]}); pages={r[3]}; registry_rows={r[4]}; uncovered={r[5]}; writer_skipped={r[6]}; missing_order={r[7]}")
    print(f"total blocks: {len(idx)}")


if __name__ == "__main__":
    main()
