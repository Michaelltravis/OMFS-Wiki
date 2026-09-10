#!/usr/bin/env python3
"""
apply_content_plan.py — write the selections saved from the checklist page
back into pursuits/<slug>/content-plan.md.

    python work/apply_content_plan.py <slug> <selections.json> [--docx] [--header "..."]

<selections.json> is the db document plans/<slug> as saved by the page
(fetched with the Artifact tool's read_db action):
  {"slug", "updatedAt", "sections": {<section-id>: {"rows": {<n>: {"on","mark","note"}}, "additional": [{"topic","mark","note"}]}}}
Section ids are the plan headings slugified the same way content_plan_page.py does.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_HEADINGS = {"how to use this sheet", "evaluation weights", "rfp cross-check"}


def slug_of(heading: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")


def mark_text(on: bool, mark: str) -> str:
    if not on:
        return "☐"
    return {"lead": "☑ lead", "brief": "☑ brief"}.get(mark or "include", "☑")


def row(n, topic, source, mark, note) -> str:
    return f"| {n} | {topic} | {source} | {mark} | {note} |"


def apply(md: str, sel: dict) -> tuple[str, dict]:
    out, stats = [], {"ticked": 0, "unticked": 0, "additional": 0}
    sec_id = None
    sec_sel: dict = {}
    pending_additional: list = []
    in_table = False

    def flush_additional():
        nonlocal pending_additional
        for a in pending_additional:
            if a.get("topic", "").strip():
                out.append(row("+", a["topic"].strip(), "Pursuit-specific", mark_text(True, a.get("mark")), a.get("note", "").strip()))
                stats["additional"] += 1
        out.append(row("—", "Additional topic", "", "☐", ""))
        pending_additional = []

    lines = md.splitlines()
    for i, l in enumerate(lines):
        if l.startswith("## "):
            if in_table:
                flush_additional(); in_table = False
            h = l[3:].strip()
            sec_id = None if h.lower() in SKIP_HEADINGS else slug_of(h)
            sec_sel = sel.get("sections", {}).get(sec_id, {}) if sec_id else {}
            pending_additional = list(sec_sel.get("additional", []))
            out.append(l)
            continue
        if sec_id and l.startswith("|"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 5 and c[0] not in ("#",) and not set(c[0]) <= {"-", ":"}:
                in_table = True
                n, topic, source, mark, note = c[:5]
                if n == "—":
                    continue  # blank rows are re-emitted by flush_additional
                if n == "+" :
                    continue  # previously applied additional rows are regenerated
                if n and not topic.startswith("**"):
                    r = sec_sel.get("rows", {}).get(n)
                    required = source.startswith("RFP")
                    if r is not None:
                        on = True if required else bool(r.get("on"))
                        new_note = (r.get("note") or "").strip() or ("required" if required else note)
                        out.append(row(n, topic, source, mark_text(on, r.get("mark")), new_note))
                        stats["ticked" if on else "unticked"] += 1
                        continue
            out.append(l)
            continue
        if in_table and l.strip() == "":
            flush_additional(); in_table = False
        out.append(l)
    if in_table:
        flush_additional()
    text = "\n".join(out) + ("\n" if md.endswith("\n") else "")
    text = re.sub(r"^status: .*$", "status: selected", text, count=1, flags=re.M)
    if sel.get("updatedAt"):
        text = re.sub(r"^generated: (.*)$", rf"generated: \1\nselected: {sel['updatedAt'][:10]}", text, count=1, flags=re.M)
    return text, stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("selections", type=Path)
    ap.add_argument("--docx", action="store_true")
    ap.add_argument("--header")
    a = ap.parse_args()
    plan = ROOT / "pursuits" / a.slug / "content-plan.md"
    sel = json.loads(a.selections.read_text(encoding="utf-8"))
    md = plan.read_text(encoding="utf-8")
    md = re.sub(r"^selected: .*\n", "", md, flags=re.M)
    text, stats = apply(md, sel)
    plan.write_text(text, encoding="utf-8")
    print(f"Updated {plan}: {stats['ticked']} ticked, {stats['unticked']} unticked, {stats['additional']} pursuit-specific topics")
    if a.docx:
        docx = plan.with_name("Content_Plan_SELECTED.docx")
        title = re.search(r"^# Content plan — (.*)$", text, re.M)
        subprocess.run([sys.executable, str(ROOT / "work" / "build_docx.py"), str(plan), str(docx),
                        "--section-label", "Content plan", "--header", a.header or (title.group(1) if title else a.slug), "--notes-inline"], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
