#!/usr/bin/env python3
"""build_sections.py — write verbatim/<slug>/sections.json (zero model tokens).

Usage:
    python work/build_sections.py <slug> | --all  [--check] [--print-tree] [--pages A-B] [--dry-run]

Every section and subsection heading in the proposal with its (page, ¶) span,
nesting level, parent, and a stable id — built from the PDF outline in
manifest.json plus the heading lines in pages/pNNNN.md. Per-slug overrides
(exclude_heading_regex, repeat_min_pages, minor_min_words) may be given in
work/sections_rules.json as {"<slug>": {...}}.

--check   assert every paragraph falls in at least one section and that all its
          containers form one ancestor chain; exits 1 on failure.
--print-tree [--pages A-B]   print the tree (restricted to sections starting in
          the page range) for eyeballing.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verbatim_sections import (ROOT, VERBATIM, build_sections, load_pages)  # noqa: E402


def check(doc: dict, slug: str) -> int:
    pages = load_pages(slug)
    secs = doc["sections"]
    by_id = {s["id"]: s for s in secs}
    orphan = inconsistent = 0
    for pno, (_fm, paras) in pages.items():
        for para in paras:
            cont = [s for s in secs
                    if (s["start"]["page"], s["start"]["para"]) <= (pno, para.n) <= (s["end"]["page"], s["end"]["para"])]
            if not cont:
                orphan += 1
                if orphan <= 5:
                    print(f"  ORPHAN p{pno:04d} ¶{para.n}")
                continue
            cont.sort(key=lambda s: s["level"])
            for a, b in zip(cont, cont[1:]):
                # b must have a as an ancestor
                cur = b
                ok = False
                while cur and cur.get("parent"):
                    cur = by_id.get(cur["parent"])
                    if cur and cur["id"] == a["id"]:
                        ok = True
                        break
                if not ok:
                    inconsistent += 1
                    if inconsistent <= 5:
                        print(f"  INCONSISTENT p{pno:04d} ¶{para.n}: {a['id']} vs {b['id']}")
    print(f"  check: orphan={orphan} inconsistent={inconsistent}")
    return 0 if (orphan == 0 and inconsistent == 0) else 1


def print_tree(doc: dict, pages: tuple[int, int] | None):
    for s in doc["sections"]:
        sp = s["start"]["page"]
        if pages and not (pages[0] <= sp <= pages[1]):
            continue
        indent = "  " * (s["level"] - 1)
        flag = " (minor)" if s.get("minor") else ""
        print(f"{indent}{s['title']}  [{s['kind']}] p{sp}¶{s['start']['para']}→p{s['end']['page']}¶{s['end']['para']}{flag}  <{s['id']}>")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows consoles default to cp1252
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--print-tree", action="store_true")
    ap.add_argument("--pages", default=None, help="A-B page range for --print-tree")
    ap.add_argument("--dry-run", action="store_true", help="do not write sections.json")
    args = ap.parse_args()

    if args.all:
        slugs = sorted(p.parent.name for p in VERBATIM.glob("*/manifest.json"))
    elif args.slug:
        slugs = [args.slug]
    else:
        ap.error("give a slug or --all")

    rules_path = ROOT / "work" / "sections_rules.json"
    rules_all = json.loads(rules_path.read_text(encoding="utf-8")) if rules_path.is_file() else {}
    pages = None
    if args.pages:
        a, b = args.pages.split("-")
        pages = (int(a), int(b))

    rc = 0
    for slug in slugs:
        doc = build_sections(slug, rules_all.get(slug))
        doc["generated"] = dt.date.today().isoformat()
        st = doc["stats"]
        print(f"[{slug}] sections={st['sections']} outline={st['outline']} merged={st['merged']} "
              f"body_headings={st['body_headings']} minor={st['minor']} excluded={st['excluded']}")
        if args.check:
            rc |= check(doc, slug)
        if args.print_tree:
            print_tree(doc, pages)
        if not args.dry_run:
            out = VERBATIM / slug / "sections.json"
            out.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  wrote {out.relative_to(ROOT)}")
    sys.exit(rc)


if __name__ == "__main__":
    main()
