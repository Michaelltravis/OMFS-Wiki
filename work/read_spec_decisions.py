#!/usr/bin/env python3
"""
read_spec_decisions.py — Read Michael's ticks from the Richmond spec-sheet
approval docx and lock the spec sheet. No model call.

Reads the last table in the approval .docx whose header row contains
"Approve" (the "Decisions -- tick one per row" table: Item | Recommendation
| checkbox Approve | checkbox Change (note)). For each data row, extracts
the D-id from the Item cell and classifies the row as approve / change /
default based on the Approve and Change cells (plain-text checkbox glyphs,
Word checkbox content controls, or the words yes/approve). --override
entries win over anything read from the docx.

Usage:
    python work/read_spec_decisions.py [--docx PATH] [--spec-md PATH]
        [--spec-json PATH] [--dry-run]
        [--override "D-04=change:Use Traverse City instead of Southbridge"]
        [--override "D-07=approve"] ...

--dry-run prints a table of id | choice | note and counts, and changes
nothing on disk.

Otherwise, it:
  - rewrites spec-sheet.md frontmatter: status: locked, adds
    locked: <today ISO> and approved-by: Michael Travis
  - appends a "## Approved decisions" section listing each id, choice, note
  - updates spec-sheet.json: sets choice/note on each decisions[] entry and
    sets top-level status to "locked"
  - leaves everything else byte-identical
  - prints a short JSON summary to stdout
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn

# --------------------------------------------------------------------------
# Defaults
# --------------------------------------------------------------------------

DEFAULT_DOCX = "pursuits/richmond-2026/Richmond_Spec_Sheet_v1_FOR_APPROVAL.docx"
DEFAULT_SPEC_MD = "pursuits/richmond-2026/spec-sheet.md"
DEFAULT_SPEC_JSON = "pursuits/richmond-2026/spec-sheet.json"

TICK_GLYPHS = {"\u2611", "\u2612", "\u2713", "\u2714"}  # ☑ ☒ ✓ ✔
ID_RE = re.compile(r"\b(D-\d+)\b")

APPROVED_BY = "Michael Travis"


# --------------------------------------------------------------------------
# Docx parsing
# --------------------------------------------------------------------------

def _cell_has_word_checkbox_checked(cell) -> bool:
    """Inspect a table cell's raw XML for a Word checkbox content control
    (legacy FORMCHECKBOX or SDT w14:checkbox) that is set to checked."""
    xml = cell._tc.xml
    # New-style content-control checkbox: <w14:checkbox><w14:checked w14:val="1"/>
    if re.search(r'<w14:checked[^>]*w14:val="1"', xml):
        return True
    # Legacy form-field checkbox: <w:checkBox><w:checked w:val="1"/> (or no val = checked)
    m = re.search(r"<w:checkBox\b.*?</w:checkBox>", xml, re.S)
    if m:
        block = m.group(0)
        if re.search(r'<w:checked\s+w:val="(1|true|on)"', block):
            return True
        if re.search(r"<w:checked\s*/>", block):
            return True
        if "<w:checked" not in block and "<w:default" in block:
            # default value with no explicit checked override -> not checked
            return False
    return False


def _cell_is_ticked(cell) -> bool:
    text = cell.text.strip()
    if any(g in text for g in TICK_GLYPHS):
        return True
    if re.search(r"\b[xX]\b", text):
        return True
    low = text.lower()
    if "yes" in low or "approve" in low:
        # avoid matching the literal header/instruction text accidentally;
        # callers only invoke this on data-row cells
        return True
    if _cell_has_word_checkbox_checked(cell):
        return True
    return False


def _cell_note_text(cell) -> str:
    """Strip checkbox glyphs / bare tick markers from a cell's text to get
    any free-form note the reviewer wrote."""
    text = cell.text
    for g in TICK_GLYPHS | {"\u2610"}:  # also strip the unticked box ☐
        text = text.replace(g, "")
    # strip a lone "x"/"X" token and the words yes/approve used as a tick
    text = re.sub(r"(?i)\byes\b", "", text)
    text = re.sub(r"(?i)\bapprove\b", "", text)
    text = re.sub(r"(?<![\w-])[xX](?![\w-])", "", text)
    return text.strip(" \t\n:-—–")


def find_decisions_table(docx_path: Path):
    doc = Document(str(docx_path))
    target = None
    for t in doc.tables:
        if not t.rows:
            continue
        header_cells = [c.text for c in t.rows[0].cells]
        if any("Approve" in h for h in header_cells):
            target = t  # keep going -> "last table whose header contains Approve"
    if target is None:
        raise SystemExit("No decisions table found (no table header contains 'Approve').")
    return target


def parse_docx_decisions(docx_path: Path) -> dict:
    """Returns {id: {"choice": "approve"|"change"|"default", "note": str}}"""
    table = find_decisions_table(docx_path)
    results: dict[str, dict] = {}
    for row in table.rows[1:]:
        cells = row.cells
        if len(cells) < 4:
            continue
        item_text = cells[0].text
        m = ID_RE.search(item_text)
        if not m:
            continue
        did = m.group(1)
        approve_cell, change_cell = cells[2], cells[3]

        approved = _cell_is_ticked(approve_cell)
        changed = _cell_is_ticked(change_cell)
        note = _cell_note_text(change_cell)

        if changed:
            choice = "change"
        elif approved:
            choice = "approve"
        else:
            choice = "default"
            note = ""

        results[did] = {"choice": choice, "note": note}
    return results


# --------------------------------------------------------------------------
# Overrides
# --------------------------------------------------------------------------

def parse_overrides(raw: list[str]) -> dict:
    """--override "D-04=change:Use Traverse City instead of Southbridge"
    --override "D-07=approve" """
    out = {}
    for item in raw or []:
        if "=" not in item:
            raise SystemExit(f"Bad --override (expected ID=choice[:note]): {item!r}")
        did, rest = item.split("=", 1)
        did = did.strip().upper()
        if ":" in rest:
            choice, note = rest.split(":", 1)
        else:
            choice, note = rest, ""
        choice = choice.strip().lower()
        note = note.strip()
        if choice not in ("approve", "change", "default"):
            raise SystemExit(f"Bad choice in --override {item!r}: must be approve|change|default")
        out[did] = {"choice": choice, "note": note}
    return out


# --------------------------------------------------------------------------
# spec-sheet.md rewriting
# --------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def rewrite_spec_md(md_text: str, decisions: dict, today: str) -> str:
    m = FRONTMATTER_RE.match(md_text)
    if not m:
        raise SystemExit("spec-sheet.md has no YAML frontmatter block to update.")
    fm_body = m.group(1)

    lines = fm_body.split("\n")
    new_lines = []
    saw_status = False
    for line in lines:
        if re.match(r"^status\s*:", line):
            new_lines.append("status: locked")
            saw_status = True
        elif re.match(r"^locked\s*:", line):
            continue  # drop, will re-add
        elif re.match(r"^approved-by\s*:", line):
            continue  # drop, will re-add
        else:
            new_lines.append(line)
    if not saw_status:
        new_lines.append("status: locked")
    new_lines.append(f"locked: {today}")
    new_lines.append(f"approved-by: {APPROVED_BY}")

    new_fm = "---\n" + "\n".join(new_lines) + "\n---\n"
    rest = md_text[m.end():]

    # Append "## Approved decisions" section (idempotent: replace if present)
    section_re = re.compile(r"\n## Approved decisions\n.*?(?=\n## |\Z)", re.S)
    section_lines = ["\n## Approved decisions\n",
                     "\nLocked " + today + " by " + APPROVED_BY + ".\n",
                     "\n| id | choice | note |\n|---|---|---|\n"]
    for did in sorted(decisions.keys(), key=lambda x: int(x.split("-")[1])):
        d = decisions[did]
        note = d["note"].replace("|", "\\|").replace("\n", " ").strip() or "—"
        section_lines.append(f"| {did} | {d['choice']} | {note} |\n")
    section_text = "".join(section_lines)

    if section_re.search(rest):
        rest = section_re.sub(section_text.rstrip("\n") + "\n", rest, count=1)
    else:
        if not rest.endswith("\n"):
            rest += "\n"
        rest = rest + section_text

    return new_fm + rest


# --------------------------------------------------------------------------
# spec-sheet.json rewriting
# --------------------------------------------------------------------------

def rewrite_spec_json(data: dict, decisions: dict) -> dict:
    for entry in data.get("decisions", []):
        did = entry.get("id")
        d = decisions.get(did, {"choice": "default", "note": ""})
        entry["choice"] = d["choice"]
        entry["note"] = d["note"]
    data["status"] = "locked"
    return data


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docx", default=DEFAULT_DOCX)
    ap.add_argument("--spec-md", default=DEFAULT_SPEC_MD)
    ap.add_argument("--spec-json", default=DEFAULT_SPEC_JSON)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--override", action="append", default=[])
    args = ap.parse_args()

    docx_path = Path(args.docx)
    spec_md_path = Path(args.spec_md)
    spec_json_path = Path(args.spec_json)

    if not docx_path.exists():
        raise SystemExit(f"docx not found: {docx_path}")

    decisions = parse_docx_decisions(docx_path)
    overrides = parse_overrides(args.override)
    decisions.update(overrides)

    counts = {"approve": 0, "change": 0, "default": 0}
    for d in decisions.values():
        counts[d["choice"]] += 1

    if args.dry_run:
        print(f"{'id':<6} {'choice':<8} note")
        for did in sorted(decisions.keys(), key=lambda x: int(x.split("-")[1])):
            d = decisions[did]
            note = d["note"][:80]
            print(f"{did:<6} {d['choice']:<8} {note}")
        print()
        print(json.dumps({"rows": len(decisions), "counts": counts, "dry_run": True}, indent=2))
        return 0

    if not spec_md_path.exists():
        raise SystemExit(f"spec-sheet.md not found: {spec_md_path}")
    if not spec_json_path.exists():
        raise SystemExit(f"spec-sheet.json not found: {spec_json_path}")

    today = datetime.date.today().isoformat()

    md_text = spec_md_path.read_text(encoding="utf-8")
    new_md = rewrite_spec_md(md_text, decisions, today)
    spec_md_path.write_text(new_md, encoding="utf-8")

    json_data = json.loads(spec_json_path.read_text(encoding="utf-8"))
    new_json = rewrite_spec_json(json_data, decisions)
    spec_json_path.write_text(
        json.dumps(new_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({
        "rows": len(decisions),
        "counts": counts,
        "locked": today,
        "approved_by": APPROVED_BY,
        "spec_md": str(spec_md_path),
        "spec_json": str(spec_json_path),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
