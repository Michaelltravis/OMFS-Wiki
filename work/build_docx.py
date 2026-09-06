#!/usr/bin/env python3
"""
build_docx.py — Generic Jacobs-branded Markdown -> Word (.docx) renderer.

Usage:
    python build_docx.py <input.md> <output.docx> --section-label "Section 3" \
        --header "City of Richmond - WPCP, Collection and Stormwater O&M"

No pandoc / LibreOffice on this machine: this script parses a constrained
Markdown schema directly and builds the .docx with python-docx.

Schema supported (see project instructions / SKILL references for the
full spec):
    # Title                       -> standing head "SECTION n" + Title
    _deck line_                   -> italic deck line right after title
    ## 3.1 Heading                -> Heading 1 (16pt bold, P1 blue)
    ### Heading                   -> Heading 2 (13pt bold, black)
    paragraphs                    -> body text, 12pt Arial, 1.15 spacing
    **bold** _italic_ `code`      -> inline formatting
    [PLACEHOLDER: ...] / [VERIFY..]-> yellow-highlighted inline run
    - bullet / 1. numbered        -> List Bullet / List Number
    Table n-n. Caption            -> caption line above a GFM table
    | a | b |  GFM tables         -> Word table, styled per brand rules
    > CALLOUT: text               -> shaded single-cell callout block
    [FIGURE n-n: caption - desc]  -> bordered figure placeholder + caption
    ## Draft notes                -> page break + grey "DRAFT NOTES" banner
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

# --------------------------------------------------------------------------
# Brand palette (Blue family / neutrals only — see word-templates.md)
# --------------------------------------------------------------------------

BLUE_1 = "231EDC"      # P1 anchor
BLUE_2 = "0A7DFF"      # P2 bright
BLUE_3 = "5AE6FF"      # P3 light
NAVY = "001E55"        # P4 deep
BLACK = "000000"
TEXT = "333333"
GRAY = "A5A5A5"
BORDER = "C8C8C8"
FILL = "E6E6E6"
WHITE = "FFFFFF"

FONT = "Arial"  # Jacobs Chronos not installed on this machine

# --------------------------------------------------------------------------
# Module-level render policy (set from CLI flags in main())
# --------------------------------------------------------------------------

_KEEP_TAGS = False      # --keep-tags: render [PLACEHOLDER/VERIFY/CONFIRM/TBD]
                        # inline with yellow highlight instead of stripping
_TAG_HITS: list[str] = []   # sentences containing a stripped tag
_TAG_COUNT = 0          # number of tags stripped from the main body

TAG_RE = re.compile(r"\[(?:PLACEHOLDER|VERIFY|CONFIRM|TBD)[^\]]*\]")


def _extract_sentence(text: str, start: int, end: int) -> str:
    """Return the sentence (roughly) surrounding text[start:end]."""
    left = 0
    for m in re.finditer(r"[.!?]\s+", text[:start]):
        left = m.end()
    right = len(text)
    m2 = re.search(r"[.!?](\s|$)", text[end:])
    if m2:
        right = end + m2.end()
    return text[left:right].strip()


def strip_and_collect_tags(text: str) -> str:
    """Remove [PLACEHOLDER/VERIFY/CONFIRM/TBD ...] tags from text, recording
    the surrounding sentence of each hit into _TAG_HITS for the notes
    companion doc. Returns the cleaned text."""
    global _TAG_COUNT

    def repl(m: "re.Match[str]") -> str:
        global _TAG_COUNT
        _TAG_COUNT += 1
        _TAG_HITS.append(_extract_sentence(text, m.start(), m.end()))
        return ""

    new_text = TAG_RE.sub(repl, text)
    new_text = re.sub(r"[ \t]+([.,;:])", r"\1", new_text)
    new_text = re.sub(r"[ \t]{2,}", " ", new_text).strip()
    return new_text


# --------------------------------------------------------------------------
# Low-level OOXML helpers (adapted from build_richmond_sections.py)
# --------------------------------------------------------------------------

def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=40, start=80, bottom=40, end=80) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def set_table_borders_none(table) -> None:
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = f"w:{edge}"
        node = borders.find(qn(tag))
        if node is None:
            node = OxmlElement(tag)
            borders.append(node)
        node.set(qn("w:val"), "nil")


def set_cell_border(cell, edge: str, color: str, size: str) -> None:
    """edge in top/left/bottom/right. size in eighths of a point (string)."""
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = tc_pr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tc_pr.append(borders)
    tag = f"w:{edge}"
    node = borders.find(qn(tag))
    if node is None:
        node = OxmlElement(tag)
        borders.append(node)
    node.set(qn("w:val"), "single")
    node.set(qn("w:sz"), size)
    node.set(qn("w:space"), "0")
    node.set(qn("w:color"), color)


def set_row_cant_split(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tr_pr.append(OxmlElement("w:cantSplit"))


def set_repeat_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_table_autofit_window(table) -> None:
    tbl_pr = table._tbl.tblPr
    layout = tbl_pr.find(qn("w:tblLayout"))
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        tbl_pr.append(layout)
    layout.set(qn("w:type"), "autofit")
    width = tbl_pr.find(qn("w:tblW"))
    if width is None:
        width = OxmlElement("w:tblW")
        tbl_pr.append(width)
    width.set(qn("w:type"), "pct")
    width.set(qn("w:w"), "5000")


def add_field(paragraph, instruction: str) -> None:
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for node in (begin, instr, separate, text, end):
        run._r.append(node)


def add_page_break(doc: Document) -> None:
    doc.add_page_break()


# --------------------------------------------------------------------------
# Styles
# --------------------------------------------------------------------------

def configure_styles(doc: Document) -> None:
    styles = doc.styles

    normal = styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(12)
    normal.font.color.rgb = RGBColor.from_string(TEXT)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.1

    # Heading 1 -> "## n.n Heading"
    h1 = styles["Heading 1"]
    h1.font.name = FONT
    h1.font.size = Pt(16)
    h1.font.bold = True
    h1.font.color.rgb = RGBColor.from_string(BLUE_1)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(4)
    h1.paragraph_format.keep_with_next = True

    # Heading 2 -> "### Heading"
    h2 = styles["Heading 2"]
    h2.font.name = FONT
    h2.font.size = Pt(13)
    h2.font.bold = True
    h2.font.color.rgb = RGBColor.from_string(BLACK)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(2)
    h2.paragraph_format.keep_with_next = True

    for name, size, color, bold, spacing in (
        ("Standing Head", 10, BLUE_1, True, 1.0),
        ("Section Title", 24, BLACK, True, 1.05),
        ("Deck Line", 13, TEXT, False, 1.1),
        ("Caption", 10, GRAY, False, 1.0),
        ("Callout Label", 10, BLUE_1, True, 1.0),
        ("Callout Text", 10.5, TEXT, False, 1.15),
        ("Figure Placeholder", 11, GRAY, False, 1.0),
        ("Draft Banner", 12, TEXT, True, 1.0),
        ("Table Body", 10, TEXT, False, 1.05),
        ("Table Header", 10, BLACK, True, 1.05),
        ("Draft Body", 10, TEXT, False, 1.1),
    ):
        if name not in styles:
            style = styles.add_style(name, 1)
        else:
            style = styles[name]
        style.font.name = FONT
        style.font.size = Pt(size)
        style.font.bold = bold
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.space_after = Pt(4)
        style.paragraph_format.line_spacing = spacing

    # Captions keep with the block that follows them (table/figure).
    styles["Caption"].paragraph_format.keep_with_next = True

    # List Bullet -> square bullet char (best-effort; falls back to default
    # bullet glyph if the numbering XML edit is not supported by the
    # renderer, but the style text is still List Bullet).
    if "List Bullet" in styles:
        lb = styles["List Bullet"]
        lb.font.name = FONT
        lb.font.size = Pt(12)
        lb.font.color.rgb = RGBColor.from_string(TEXT)
        lb.paragraph_format.space_after = Pt(3)
        lb.paragraph_format.line_spacing = 1.15

    if "List Number" in styles:
        ln = styles["List Number"]
        ln.font.name = FONT
        ln.font.size = Pt(12)
        ln.font.color.rgb = RGBColor.from_string(TEXT)
        ln.paragraph_format.space_after = Pt(3)
        ln.paragraph_format.line_spacing = 1.15


def use_square_bullets(doc: Document) -> None:
    """Best-effort: set the numbering glyph for List Bullet to a square (Wingdings ▪)."""
    try:
        numbering_part = doc.part.numbering_part
    except Exception:
        return
    if numbering_part is None:
        return
    try:
        num_elem = numbering_part.element
        for lvl in num_elem.findall(".//" + qn("w:lvl")):
            num_fmt = lvl.find(qn("w:numFmt"))
            if num_fmt is not None and num_fmt.get(qn("w:val")) == "bullet":
                lvl_text = lvl.find(qn("w:lvlText"))
                r_fonts = lvl.find(qn("w:rPr"))
                if lvl_text is not None:
                    lvl_text.set(qn("w:val"), "")  # Wingdings square
                if r_fonts is not None:
                    fonts = r_fonts.find(qn("w:rFonts"))
                    if fonts is None:
                        fonts = OxmlElement("w:rFonts")
                        r_fonts.append(fonts)
                    fonts.set(qn("w:ascii"), "Wingdings")
                    fonts.set(qn("w:hAnsi"), "Wingdings")
                    fonts.set(qn("w:hint"), "default")
    except Exception:
        pass


# --------------------------------------------------------------------------
# Header / footer / page setup
# --------------------------------------------------------------------------

def setup_page(doc: Document, header_text: str, section_label: str) -> None:
    for section in doc.sections:
        section.page_height = Inches(11)
        section.page_width = Inches(8.5)
        section.top_margin = Inches(0.85)
        section.bottom_margin = Inches(0.85)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)
        section.header_distance = Inches(0.4)
        section.footer_distance = Inches(0.4)

        # ---- Header: "Jacobs" left, header text right, rule below ----
        header = section.header
        header.is_linked_to_previous = False
        htable = header.add_table(rows=1, cols=2, width=Inches(6.8))
        htable.alignment = WD_TABLE_ALIGNMENT.CENTER
        htable.autofit = False
        htable.columns[0].width = Inches(1.5)
        htable.columns[1].width = Inches(5.3)
        c1, c2 = htable.rows[0].cells
        c1.width = Inches(1.5)
        c2.width = Inches(5.3)

        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1 = p1.add_run("Jacobs")
        r1.bold = True
        r1.font.name = FONT
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor.from_string(BLACK)

        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r2 = p2.add_run(header_text)
        r2.font.name = FONT
        r2.font.size = Pt(9)
        r2.font.color.rgb = RGBColor.from_string(TEXT)

        for cell in (c1, c2):
            set_cell_margins(cell, top=0, start=0, bottom=40, end=0)
            set_cell_border(cell, "bottom", BORDER, "4")
        set_table_borders_none(htable)
        for cell in (c1, c2):
            set_cell_border(cell, "bottom", BORDER, "4")

        # ---- Footer: section label left | copyright right | page # center ----
        footer = section.footer
        footer.is_linked_to_previous = False
        ftable = footer.add_table(rows=1, cols=3, width=Inches(6.8))
        ftable.alignment = WD_TABLE_ALIGNMENT.CENTER
        ftable.autofit = False
        widths = [2.3, 2.2, 2.3]
        for i, w in enumerate(widths):
            ftable.columns[i].width = Inches(w)
        left, center, right = ftable.rows[0].cells
        left.width = Inches(widths[0])
        center.width = Inches(widths[1])
        right.width = Inches(widths[2])

        pL = left.paragraphs[0]
        pL.alignment = WD_ALIGN_PARAGRAPH.LEFT
        rL = pL.add_run(section_label)
        rL.font.name = FONT
        rL.font.size = Pt(9)
        rL.font.color.rgb = RGBColor.from_string(GRAY)

        pC = center.paragraphs[0]
        pC.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rC = pC.add_run("Page ")
        rC.font.name = FONT
        rC.font.size = Pt(9)
        rC.font.color.rgb = RGBColor.from_string(GRAY)
        add_field(pC, "PAGE")
        rC2 = pC.add_run()
        rC2.font.name = FONT
        rC2.font.size = Pt(9)
        rC2.font.color.rgb = RGBColor.from_string(GRAY)

        pR = right.paragraphs[0]
        pR.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rR = pR.add_run("© Jacobs 2026 — Confidential — DRAFT")
        rR.font.name = FONT
        rR.font.size = Pt(9)
        rR.font.color.rgb = RGBColor.from_string(GRAY)

        for cell in (left, center, right):
            set_cell_margins(cell, top=40, start=0, bottom=0, end=0)
        set_table_borders_none(ftable)


# --------------------------------------------------------------------------
# Inline markdown -> runs
# --------------------------------------------------------------------------

# Order matters: placeholder/verify tags first so ** inside them doesn't
# get mis-split; then bold, then italic, then inline code.
INLINE_TOKEN_RE = re.compile(
    r"(\[(?:PLACEHOLDER|VERIFY)[^\]]*\])"
    r"|(\*\*.+?\*\*)"
    r"|(_.+?_)"
    r"|(`[^`]+?`)"
)


def render_inline(paragraph, text: str) -> None:
    pos = 0
    for m in INLINE_TOKEN_RE.finditer(text):
        if m.start() > pos:
            _add_plain_run(paragraph, text[pos:m.start()])
        token = m.group(0)
        if token.startswith("[PLACEHOLDER") or token.startswith("[VERIFY"):
            run = paragraph.add_run(token)
            run.font.name = FONT
            run.font.color.rgb = RGBColor.from_string(TEXT)
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        elif token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            run.bold = True
            run.font.name = FONT
        elif token.startswith("_"):
            run = paragraph.add_run(token[1:-1])
            run.italic = True
            run.font.name = FONT
        elif token.startswith("`"):
            run = paragraph.add_run(token[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(11)
        pos = m.end()
    if pos < len(text):
        _add_plain_run(paragraph, text[pos:])


def _add_plain_run(paragraph, text: str) -> None:
    if not text:
        return
    run = paragraph.add_run(text)
    run.font.name = FONT


# --------------------------------------------------------------------------
# GFM table parsing
# --------------------------------------------------------------------------

def parse_gfm_table(lines: list[str], start: int) -> tuple[list[list[str]], int]:
    """lines[start] is the header row of a GFM table. Returns (rows, next_index)."""
    rows: list[list[str]] = []

    def split_row(line: str) -> list[str]:
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]
        return [c.strip() for c in line.split("|")]

    header = split_row(lines[start])
    rows.append(header)
    i = start + 1
    # separator row (---|---|---)
    if i < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i]):
        i += 1
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append(split_row(lines[i]))
        i += 1
    return rows, i


CONTENT_WIDTH_IN = 6.8  # page width (8.5in) minus 0.85in margins each side
ITEM_COL_WIDTH_IN = 1.9


def build_table(doc: Document, rows: list[list[str]]) -> None:
    if not rows:
        return
    header, body = rows[0], rows[1:]
    ncols = len(header)
    table = doc.add_table(rows=1, cols=ncols)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = True
    set_table_autofit_window(table)

    first_col_is_item = header[0].strip().lower() == "item"
    col_widths = None
    if first_col_is_item and ncols >= 2:
        rest = (CONTENT_WIDTH_IN - ITEM_COL_WIDTH_IN) / (ncols - 1)
        col_widths = [ITEM_COL_WIDTH_IN] + [rest] * (ncols - 1)

    all_rows = [table.rows[0]]

    hdr_row = table.rows[0]
    set_repeat_header(hdr_row)
    set_row_cant_split(hdr_row)

    for i, h in enumerate(header):
        cell = hdr_row.cells[i]
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        para.style = doc.styles["Table Header"]
        render_inline(para, h)
        for run in para.runs:
            run.bold = True
        set_cell_margins(cell)
        # 1.5pt black bottom border on header row
        set_cell_border(cell, "bottom", BLACK, "12")
        if col_widths:
            cell.width = Inches(col_widths[i])

    for row_vals in body:
        row = table.add_row()
        all_rows.append(row)
        set_row_cant_split(row)
        for i, val in enumerate(row_vals):
            if i >= ncols:
                break
            cell = row.cells[i]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
            para = cell.paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.style = doc.styles["Table Body"]
            render_inline(para, val)
            if i == 0 and first_col_is_item:
                for run in para.runs:
                    run.bold = True
            set_cell_margins(cell)
            # 0.5pt horizontal rule (bottom border) in light grey, no verticals
            set_cell_border(cell, "bottom", "E6E6E6", "4")
            if col_widths:
                cell.width = Inches(col_widths[i])

    # Never let a table break leaving a lone header row at the foot of a
    # page: keep every row glued to the next one, except the very last row.
    for row in all_rows[:-1]:
        for cell in row.cells:
            for para in cell.paragraphs:
                para.paragraph_format.keep_with_next = True

    doc.add_paragraph().paragraph_format.space_after = Pt(4)


# --------------------------------------------------------------------------
# Callout / figure blocks
# --------------------------------------------------------------------------

def add_callout(doc: Document, text: str) -> None:
    label = doc.add_paragraph(style="Callout Label")
    label.add_run("COMMITMENT")

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = True
    set_table_autofit_window(table)
    set_table_borders_none(table)
    cell = table.rows[0].cells[0]
    set_cell_shading(cell, FILL)
    set_cell_margins(cell, top=160, start=160, bottom=160, end=160)
    para = cell.paragraphs[0]
    para.style = doc.styles["Callout Text"]
    render_inline(para, text)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


FIGURE_RE = re.compile(r"^\[FIGURE\s+([^:\]]+):\s*(.+?)(?:\s*[—-]\s*(.+))?\]$")
MID_FIGURE_RE = re.compile(r"\[FIGURE\s+([^:\]]+):\s*(.+?)(?:\s*[—-]\s*(.+?))?\]")


def figure_caption_from_match(m: "re.Match[str]") -> tuple[str, str]:
    fig_id = m.group(1).strip()
    cap1 = m.group(2).strip() if m.group(2) else ""
    cap2 = m.group(3).strip() if m.group(3) else ""
    caption = cap1 if not cap2 else f"{cap1} — {cap2}"
    return fig_id, caption


def add_figure_placeholder(doc: Document, fig_id: str, caption: str) -> None:
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = True
    set_table_autofit_window(table)
    cell = table.rows[0].cells[0]
    for edge in ("top", "left", "bottom", "right"):
        set_cell_border(cell, edge, BORDER, "8")
    set_cell_margins(cell, top=100, start=100, bottom=100, end=100)
    # Force a fixed-height row of 1.6in.
    tr = table.rows[0]._tr
    tr_pr = tr.get_or_add_trPr()
    tr_height = OxmlElement("w:trHeight")
    tr_height.set(qn("w:val"), str(int(1.6 * 1440)))
    tr_height.set(qn("w:hRule"), "atLeast")
    tr_pr.append(tr_height)

    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    para = cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run("Figure slot")
    run.font.name = FONT
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor.from_string(GRAY)

    cap = doc.add_paragraph(style="Caption")
    render_inline(cap, f"Figure {fig_id}. {caption}")


# --------------------------------------------------------------------------
# Draft-notes banner
# --------------------------------------------------------------------------

def add_draft_banner(doc: Document) -> None:
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = True
    set_table_autofit_window(table)
    set_table_borders_none(table)
    cell = table.rows[0].cells[0]
    set_cell_shading(cell, FILL)
    set_cell_margins(cell, top=120, start=120, bottom=120, end=120)
    para = cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.style = doc.styles["Draft Banner"]
    para.add_run("DRAFT NOTES — REMOVE BEFORE ISSUE")
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


# --------------------------------------------------------------------------
# Markdown parsing / rendering driver
# --------------------------------------------------------------------------

TABLE_CAPTION_RE = re.compile(r"^Table\s+([\w.\-]+)\.\s*(.+)$")


def render_markdown(doc: Document, md_text: str, section_label: str) -> dict:
    """Parses md_text line-by-line and appends content to doc.
    Returns a stats dict (heading/table counts) for verification."""
    lines = md_text.splitlines()
    stats = {"h1": 0, "h2": 0, "tables": 0, "figures": 0, "callouts": 0}

    i = 0
    n = len(lines)
    title_seen = False
    draft_notes_started = False

    while i < n:
        raw = lines[i]
        line = raw.rstrip("\n")
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # --- Title (# ...) ---
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title_text = stripped[2:].strip()
            standing = doc.add_paragraph(style="Standing Head")
            standing.add_run(section_label.upper())
            title_p = doc.add_paragraph(style="Section Title")
            render_inline(title_p, title_text)
            title_seen = True
            i += 1
            # Deck line: next non-blank line if it's _italic_
            if i < n and lines[i].strip().startswith("_") and lines[i].strip().endswith("_") and len(lines[i].strip()) > 1:
                deck_p = doc.add_paragraph(style="Deck Line")
                deck_p.add_run(lines[i].strip()[1:-1])
                i += 1
            continue

        # --- Draft notes section trigger ---
        if stripped.startswith("## ") and stripped[3:].strip().lower() == "draft notes":
            add_page_break(doc)
            add_draft_banner(doc)
            draft_notes_started = True
            i += 1
            continue

        # --- Heading 2 (## n.n Heading) ---
        if stripped.startswith("## "):
            h_text = stripped[3:].strip()
            h = doc.add_paragraph(style="Heading 1")
            render_inline(h, h_text)
            stats["h1"] += 1
            i += 1
            continue

        # --- Heading 3 (### Heading) ---
        if stripped.startswith("### "):
            h_text = stripped[4:].strip()
            h = doc.add_paragraph(style="Heading 2")
            render_inline(h, h_text)
            stats["h2"] += 1
            i += 1
            continue

        # --- Callout ---
        if stripped.startswith("> CALLOUT:"):
            text = stripped[len("> CALLOUT:"):].strip()
            add_callout(doc, text)
            stats["callouts"] += 1
            i += 1
            continue

        # --- Figure placeholder (whole line) ---
        fig_match = FIGURE_RE.match(stripped)
        if fig_match:
            fig_id, caption = figure_caption_from_match(fig_match)
            add_figure_placeholder(doc, fig_id, caption)
            stats["figures"] += 1
            i += 1
            continue

        # --- Table caption immediately preceding a GFM table ---
        cap_match = TABLE_CAPTION_RE.match(stripped)
        if cap_match:
            # Look ahead for a blank line then a table, or table directly next.
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and lines[j].strip().startswith("|"):
                cap_p = doc.add_paragraph(style="Caption")
                cap_p.add_run(f"Table {cap_match.group(1)}. {cap_match.group(2)}")
                rows, next_i = parse_gfm_table(lines, j)
                build_table(doc, rows)
                stats["tables"] += 1
                i = next_i
                continue
            # else fall through as plain paragraph

        # --- Bare GFM table (no caption line before it) ---
        if stripped.startswith("|"):
            rows, next_i = parse_gfm_table(lines, i)
            build_table(doc, rows)
            stats["tables"] += 1
            i = next_i
            continue

        # --- Bullet list ---
        if re.match(r"^[-*]\s+", stripped):
            para = doc.add_paragraph(style="List Bullet")
            render_inline(para, re.sub(r"^[-*]\s+", "", stripped))
            if draft_notes_started:
                _shrink_runs(para, 10)
            i += 1
            continue

        # --- Numbered list ---
        if re.match(r"^\d+\.\s+", stripped):
            para = doc.add_paragraph(style="List Number")
            render_inline(para, re.sub(r"^\d+\.\s+", "", stripped))
            if draft_notes_started:
                _shrink_runs(para, 10)
            i += 1
            continue

        # --- Plain paragraph (with mid-paragraph [FIGURE ...] support) ---
        mid_fig = MID_FIGURE_RE.search(stripped)
        if mid_fig:
            before = stripped[:mid_fig.start()].strip()
            after = stripped[mid_fig.end():].strip()
            if before:
                body_style = "Draft Body" if draft_notes_started else "Normal"
                para = doc.add_paragraph(style=body_style)
                render_inline(para, before)
            fig_id, caption = figure_caption_from_match(mid_fig)
            add_figure_placeholder(doc, fig_id, caption)
            stats["figures"] += 1
            if after:
                body_style = "Draft Body" if draft_notes_started else "Normal"
                para = doc.add_paragraph(style=body_style)
                render_inline(para, after)
            i += 1
            continue

        body_style = "Draft Body" if draft_notes_started else "Normal"
        para = doc.add_paragraph(style=body_style)
        render_inline(para, stripped)
        i += 1

    return stats


def _shrink_runs(paragraph, size_pt: float) -> None:
    for run in paragraph.runs:
        run.font.size = Pt(size_pt)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Jacobs-branded Markdown draft to .docx")
    parser.add_argument("input_md", type=Path)
    parser.add_argument("output_docx", type=Path)
    parser.add_argument("--section-label", required=True, help='e.g. "Section 3"')
    parser.add_argument("--header", required=True, help="Header text shown top-right of every page")
    args = parser.parse_args()

    md_text = args.input_md.read_text(encoding="utf-8")

    doc = Document()
    configure_styles(doc)
    setup_page(doc, args.header, args.section_label)
    use_square_bullets(doc)

    stats = render_markdown(doc, md_text, args.section_label)

    args.output_docx.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(args.output_docx))

    print(f"Wrote {args.output_docx}")
    print(f"Headings: Heading1={stats['h1']} Heading2={stats['h2']} "
          f"Tables={stats['tables']} Figures={stats['figures']} Callouts={stats['callouts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
