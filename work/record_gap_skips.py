#!/usr/bin/env python3
"""record_gap_skips.py — copy a fill-gaps run's writer skip decisions into work/gaps/<slug>.skips.json.

Usage:
    python work/record_gap_skips.py <slug> <workflow-output.json> [--run <run-id>]

<workflow-output.json> is the file the Workflow tool writes when a fill-gaps run
completes ({"summary", "logs", "result": {"slug", "ranges": [{"range", "created",
"skipped", "skipped_reasons": [{"page", "para", "reason"}], ...}], ...}}).
Entries are merged by (page, para); an existing entry is overwritten by the newer run.
find_uncovered.py reports these paragraphs as writer-skipped instead of uncovered.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("output_json")
    ap.add_argument("--run", default="")
    args = ap.parse_args()

    doc = json.loads(Path(args.output_json).read_text(encoding="utf-8"))
    result = doc.get("result") or doc
    if result.get("slug") and result["slug"] != args.slug:
        raise SystemExit(f"output is for {result['slug']}, not {args.slug}")
    path = ROOT / "work" / "gaps" / f"{args.slug}.skips.json"
    existing = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else []
    by_pos = {(int(r["page"]), int(r["para"])): r for r in existing}
    added = 0
    for rng in result.get("ranges") or []:
        for s in rng.get("skipped_reasons") or []:
            key = (int(s["page"]), int(s["para"]))
            rec = {"page": key[0], "para": key[1], "reason": str(s.get("reason", "skipped")).strip(),
                   "range": rng.get("range", ""), "run": args.run}
            if key not in by_pos:
                added += 1
            by_pos[key] = rec
    rows = [by_pos[k] for k in sorted(by_pos)]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    created = sum(int(r.get("created") or 0) for r in result.get("ranges") or [])
    print(f"[{args.slug}] skips recorded: {len(rows)} total ({added} new) -> {path.relative_to(ROOT)}; ranges={len(result.get('ranges') or [])} created={created}")


if __name__ == "__main__":
    main()
