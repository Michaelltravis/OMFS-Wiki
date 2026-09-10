#!/usr/bin/env python3
"""
new_content_plan.py — scaffold pursuits/<slug>/content-plan.md.

    python work/new_content_plan.py <slug> --directive <Directive.docx> [--reqs pursuits/<slug>/reqs] [--rfp <rfp.pdf>] [--docx] [--header "..."]

Section order and RFP-required topics come from the Directive's PROPOSAL OUTLINE
table; evaluation weights from its EVALUATION CRITERIA table; the Jacobs-standard
topics from templates/standard-topics.md. The reqs exports are used only to
cross-check the outline against the RFP. Never overwrites an existing plan.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[1]

FAMILY_KEYWORDS = [
    ("cover-letter", ("cover letter", "transmittal")),
    ("exec-summary", ("executive summary",)),
    ("qualifications", ("qualification", "corporate", "profile", "financial", "litigation", "reference")),
    ("staffing", ("staffing", "organizational chart", "key staff", "transition of management", "subcontractor", "backup resources")),
    ("approach", ("technical approach", "operational", "maintenance", "asset management", "energy")),
    ("forms", ("form",)),
    ("fee", ("fee", "cost", "price", "pricing")),
]

MARK_RE = re.compile(r"[☑☐]")


def cell_text(cell) -> str:
    return " ".join(cell.text.split())


def find_table(doc, title: str):
    for t in doc.tables:
        if t.rows and cell_text(t.rows[0].cells[0]).upper().startswith(title):
            return t
    return None


def read_outline(doc) -> "OrderedDict[str, dict]":
    t = find_table(doc, "PROPOSAL OUTLINE")
    if t is None:
        sys.exit("No PROPOSAL OUTLINE table found in the Directive")
    header_idx = next(i for i, r in enumerate(t.rows) if cell_text(r.cells[0]).lower() == "section")
    cols = [cell_text(c).lower() for c in t.rows[header_idx].cells]
    col = {name: cols.index(name) for name in cols}
    sections: "OrderedDict[str, dict]" = OrderedDict()
    for r in t.rows[header_idx + 1:]:
        cells = [cell_text(c) for c in r.cells]
        num = cells[col["section"]]
        desc = cells[col.get("description (sub-heading)", 1)]
        if not num or not desc:
            continue
        req = cells[col["requirements"]] if "requirements" in col else ""
        pages = cells[col["pgs"]] if "pgs" in col else ""
        sec = sections.setdefault(num, {"rows": [], "pages": "", "titles": []})
        sec["rows"].append((desc, req))
        sec["titles"].append(desc)
        if pages and not sec["pages"]:
            sec["pages"] = pages
    return sections


def read_weights(doc) -> list[tuple[str, str]]:
    t = find_table(doc, "EVALUATION CRITERIA")
    if t is None:
        return []
    out = []
    for r in t.rows:
        cells = [cell_text(c) for c in r.cells]
        if len(cells) >= 2 and cells[1] and cells[0].upper() not in ("EVALUATION CRITERIA", "SECTION NAME") and not cells[0].upper().startswith("INSERT"):
            out.append((cells[0], cells[1]))
    return out


def section_title(num: str, sec: dict, reqs_names: dict[str, str]) -> str:
    if num in reqs_names:
        return reqs_names[num]
    first = sec["titles"][0]
    return first.split(" - ")[0].strip()


STOPWORDS = {"and", "the", "plan", "project", "proposed", "firm", "of"}


def match_weight(title: str, weights: list[tuple[str, str]]) -> str:
    words = {w for w in re.findall(r"[a-z]+", title.lower()) if len(w) >= 3 and w not in STOPWORDS}
    for name, weight in weights:
        if name.lower() == "total":
            continue
        if words & {w for w in re.findall(r"[a-z]+", name.lower()) if w not in STOPWORDS}:
            return weight
    return ""


def section_family(title: str, sec: dict) -> str:
    for blob in (title.lower(), " ".join(sec["titles"]).lower()):
        for fam, keys in FAMILY_KEYWORDS:
            if any(k in blob for k in keys):
                return fam
    return ""


def read_reqs(reqs_dir: Path | None) -> tuple[dict[str, str], dict[str, int]]:
    """Returns ({section number: title}, {section number: requirement row count})."""
    names: dict[str, str] = {}
    counts: dict[str, int] = {}
    if not reqs_dir or not reqs_dir.is_dir():
        return names, counts
    for f in sorted(reqs_dir.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"#\s*Requirements\s*[—-]\s*(\d+(?:\.\d+)+)\s+([^(\n]+)", text)
        if not m:
            continue
        names[m.group(1)] = m.group(2).strip()
        counts[m.group(1)] = len(re.findall(r"^- \*\*C-\d+", text, re.M))
    return names, counts


def read_standard_topics(path: Path) -> dict[str, list[tuple[str, list[tuple[str, str, str]]]]]:
    """{family: [(group, [(topic, blocks, why), ...]), ...]}"""
    fams: dict[str, list] = {}
    fam = group = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            fam = line[3:].strip()
            fams[fam] = []
        elif line.startswith("### ") and fam:
            group = line[4:].strip()
            fams[fam].append((group, []))
        elif line.startswith("|") and fam and fams[fam]:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3 or cells[0].lower() == "topic" or set(cells[0]) <= {"-", ":"}:
                continue
            fams[fam][-1][1].append((cells[0], cells[1], cells[2]))
    return fams


def warn_missing_blocks(fams: dict) -> list[str]:
    missing = []
    for fam, groups in fams.items():
        for _, rows in groups:
            for topic, blocks, _ in rows:
                for b in [x.strip() for x in blocks.split(";") if x.strip() and x.strip() != "—"]:
                    if not (ROOT / b).exists():
                        missing.append(f"{fam}: {topic} -> {b}")
    return missing


def trim(text: str, n: int = 140) -> str:
    text = text.replace("|", "/").strip().strip('"')
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def build_plan(slug, name, directive, rfp, sections, weights, reqs_names, reqs_counts, fams) -> str:
    today = dt.date.today().isoformat()
    L = [
        "---", f"pursuit: {slug}", "version: 1", "status: draft", f"directive: {directive}",
        f"rfp: {rfp or ''}", f"generated: {today}", "---", "",
        f"# Content plan — {name}",
        "_One sheet that tells the writers which topics go in each section. Sections follow the Proposal Directive outline, checked against the RFP. Under each section, the RFP-required topics are already ticked; the Jacobs-standard topics are the ones the proposal manager decides on._",
        "", "## How to use this sheet", "",
        "**Selection rule.** A ticked topic (☑) is drafted; an unticked topic (☐) is not. A ticked topic with a note gets that angle. RFP-required rows stay ticked. Add pursuit-specific topics in the *Additional topic* rows under any section. The spec sheet locks the numbers, proofs and references the ticked topics will use; this sheet only decides what is covered.",
        "", "**Marks.** `☑ lead` — the topic carries the section's opener or closer · `☑` — include · `☑ brief` — one paragraph or a table row at most · `☐` — leave out.",
        "", "**Start from.** Each section can name a source proposal section (e.g. `hull-wwtf-om-2026 — Section 5 Technical Approach, pages 40–62`) that the writer reads first and adapts as the backbone of the draft, before searching the library for anything else. It is a starting point, not a copy: the client's outline still governs the structure. `—` means no steer; the writer selects from the library.",
        "", "**Pull from.** Any row can point at a specific wiki block (`wiki/<category>/<block>.md`) or verbatim pages (`<slug> — <section>, pages a–b`) to use for that topic. It overrides the preferred block in the Source column. Blank means the writer uses the Source column's block, or searches the library.",
        "", f"**Sources.** RFP-required rows come from the Directive's PROPOSAL OUTLINE table and the requirement exports in `pursuits/{slug}/reqs/`. Jacobs-standard rows come from `templates/standard-topics.md`, each with its preferred wiki block.",
        "", "## Evaluation weights", "", "| Section | Weight |", "|---|---|",
    ]
    L += [f"| {s} | {w} |" for s, w in weights] or ["| (no EVALUATION CRITERIA table in the Directive) | |"]

    L += ["", "## RFP cross-check", "",
          "Outline rows are the Directive's sub-headings; requirement rows are the RFP's shall/must statements exported to reqs/. The writer answers every requirement row, not only the outline rows.", "",
          "| Section | Directive outline rows | RFP requirement rows | Finding |", "|---|---|---|---|"]
    for num, sec in sections.items():
        title = section_title(num, sec, reqs_names)
        label = title if title.lower().startswith(num.lower()) else f"{num} {title}"
        if reqs_names and num not in reqs_names:
            L.append(f"| {label} | {len(sec['rows'])} | — | **No requirements export in reqs/ — confirm the RFP outline carries this section** |")
        else:
            L.append(f"| {label} | {len(sec['rows'])} | {reqs_counts.get(num, '—')} | |")
    for num in reqs_names:
        if num not in sections:
            L.append(f"| {num} {reqs_names[num]} | — | {reqs_counts.get(num, '—')} | **In the RFP but not in the Directive outline — add it or confirm it is folded into another section** |")

    for num, sec in sections.items():
        title = section_title(num, sec, reqs_names)
        fam = section_family(title, sec)
        weight = match_weight(title, weights)
        meta = ", ".join(x for x in (weight, f"{sec['pages']} pages" if sec["pages"] else "") if x)
        heading = title if title.lower().startswith(num.lower()) else f"{num} {title}"
        L += ["", f"## {heading}" + (f" ({meta})" if meta else "")]
        if fam == "fee":
            L += ["", "Prepared by the estimating team; not planned on this sheet."]
            continue
        L += ["", "**Start from:** —", "", "| # | Topic | Source | Include? | Pull from | Notes / angle |", "|---|---|---|---|---|---|"]
        n = 0
        for desc, req in sec["rows"]:
            n += 1
            topic = desc.split(" - ", 1)[1].strip() if " - " in desc else desc
            topic = topic[:1].upper() + topic[1:]
            L.append(f"| {n} | {topic} | RFP — {trim(req)} | ☑ | | required |")
        for group, rows in fams.get(fam, []):
            L.append(f"| | **{group}** | Jacobs standard | | | |")
            for topic, blocks, why in rows:
                n += 1
                L.append(f"| {n} | {topic} | {blocks} | ☐ | | {why} |")
        L += ["| — | Additional topic | | ☐ | | |"] * 3
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--directive", required=True, type=Path)
    ap.add_argument("--reqs", type=Path)
    ap.add_argument("--rfp", default="")
    ap.add_argument("--name", help="Pursuit display name (default: from the Directive filename)")
    ap.add_argument("--docx", action="store_true", help="Also render a review .docx with build_docx.py")
    ap.add_argument("--header", help="Header text for the docx")
    ap.add_argument("--force", action="store_true", help="Overwrite an existing plan")
    a = ap.parse_args()

    out_dir = ROOT / "pursuits" / a.slug
    out = out_dir / "content-plan.md"
    if out.exists() and not a.force:
        sys.exit(f"{out} already exists — edit it, or pass --force to regenerate")

    reqs_dir = a.reqs or (out_dir / "reqs")
    doc = Document(str(a.directive))
    sections = read_outline(doc)
    weights = read_weights(doc)
    reqs_names, reqs_counts = read_reqs(reqs_dir)
    fams = read_standard_topics(ROOT / "templates" / "standard-topics.md")
    for m in warn_missing_blocks(fams):
        print(f"WARNING missing block: {m}")

    name = a.name or a.directive.stem.replace("_", " ")
    out_dir.mkdir(parents=True, exist_ok=True)
    out.write_text(build_plan(a.slug, name, a.directive, a.rfp, sections, weights, reqs_names, reqs_counts, fams), encoding="utf-8")
    print(f"Wrote {out}: {len(sections)} sections, {sum(len(s['rows']) for s in sections.values())} RFP rows")

    if a.docx:
        docx = out_dir / "Content_Plan_v1_FOR_REVIEW.docx"
        subprocess.run([sys.executable, str(ROOT / "work" / "build_docx.py"), str(out), str(docx),
                        "--section-label", "Content plan v1", "--header", a.header or name, "--notes-inline"], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
