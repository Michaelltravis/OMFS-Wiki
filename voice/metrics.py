#!/usr/bin/env python3
"""
voice/metrics.py — deterministic prose-metrics tool for proposal writing.

Usage:
    python voice/metrics.py <file.md|file.docx|file.txt> [--client "Richmond" --client "the City" ...] [--json]

Computes a fixed set of readability / "proposal voice" metrics against a
markdown, docx, or plain text file, reports PASS/FAIL against targets where
a target exists, and (optionally) dumps the raw metrics as JSON.

No external dependencies beyond python-docx and pyyaml (both already
available in this environment). Everything else is stdlib.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Optional deps
# --------------------------------------------------------------------------
try:
    import docx  # python-docx
except ImportError:  # pragma: no cover
    docx = None

try:
    import yaml  # pyyaml
except ImportError:  # pragma: no cover
    yaml = None


# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

BANNED_WORDS = [
    "world-class",
    "best-in-class",
    "leverage",  # handled specially below (verb usage "leverage our/the/its")
    "synergy",
    "cutting-edge",
    "state-of-the-art",
    "robust",
    "seamless",
    "holistic",
    "utilize",
    "passionate",
    "unparalleled",
    "proven track record",
    "we are pleased",
    "as a leading",
    "comprehensive suite",
]

TAG_PATTERNS = ["[PLACEHOLDER", "[VERIFY", "[CONFIRM", "[TBD"]

SO_WHAT_CUES = re.compile(
    r"which means|so that|so the|saving|reduc\w*|because|result\w*|allow\w*|"
    r"enabl\w*|giving|therefore|—",
    re.IGNORECASE,
)

HEADING_VERBS = [
    "is", "are", "provides", "delivers", "ensures", "supports", "drives",
    "improves", "reduces", "protects", "manages", "builds", "creates",
    "delivering", "providing", "ensuring", "supporting", "driving",
    "improving", "reducing", "protecting", "managing", "building",
    "creating", "positioning", "leading", "serving", "meeting", "exceeding",
    "achieving", "committing", "investing", "will", "helps", "enables",
    "enabling", "keeping", "keeps", "brings", "bringing",
]

PAST_PARTICIPLE_AUX = re.compile(
    r"\b(was|were|been|is|are|be)\s+\w+(ed|en)\b", re.IGNORECASE
)

NUMERIC_TOKEN = re.compile(r"(?<![A-Za-z])(\$?\d[\d,]*(?:\.\d+)?%?|\d+%)")

WE_OUR = re.compile(r"\b(we|our)\b", re.IGNORECASE)
YOU_YOUR_CITY = re.compile(r"\b(you|your)\b", re.IGNORECASE)

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'“])")

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*|\d[\d,]*\.?\d*%?")


# --------------------------------------------------------------------------
# Data structures
# --------------------------------------------------------------------------

class Block:
    """A unit of content: either prose text or table text, optionally a heading."""

    __slots__ = ("kind", "text", "is_heading")

    def __init__(self, kind: str, text: str, is_heading: bool = False):
        self.kind = kind  # "prose" | "table"
        self.text = text
        self.is_heading = is_heading


# --------------------------------------------------------------------------
# File loading / parsing
# --------------------------------------------------------------------------

def strip_yaml_frontmatter(text: str) -> str:
    """Remove a leading --- ... --- YAML frontmatter block, if present."""
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?\n)---\s*\n?", text, re.DOTALL)
        if m:
            return text[m.end():]
    return text


def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def is_table_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("|"):
        return True
    # GFM table separator row: |---|---| or ---|--- (rare without leading pipe)
    if re.match(r"^:?-{2,}:?(\s*\|\s*:?-{2,}:?)+$", stripped):
        return True
    return False


def parse_markdown(text: str) -> list[Block]:
    text = strip_yaml_frontmatter(text)
    text = strip_html_comments(text)
    text = strip_code_fences(text)

    blocks: list[Block] = []
    lines = text.split("\n")

    para_buf: list[str] = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            joined = " ".join(l.strip() for l in para_buf if l.strip())
            if joined.strip():
                blocks.append(Block("prose", joined.strip()))
        para_buf = []

    for raw_line in lines:
        line = raw_line.rstrip("\n")

        if is_table_line(line):
            flush_para()
            # Skip pure separator rows (---|---), keep cell text otherwise.
            stripped = line.strip()
            if re.match(r"^:?-{2,}:?(\s*\|\s*:?-{2,}:?)*\s*\|?\s*$", stripped) and set(
                stripped.replace("|", "").replace(":", "").replace("-", "").strip()
            ) == set():
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            cell_text = " ".join(c for c in cells if c and not re.match(r"^:?-{2,}:?$", c))
            # Strip markdown emphasis/html breaks from cell text
            cell_text = re.sub(r"<br\s*/?>", " ", cell_text)
            cell_text = re.sub(r"[*_`]", "", cell_text)
            if cell_text.strip():
                blocks.append(Block("table", cell_text.strip()))
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if heading_match:
            flush_para()
            htext = heading_match.group(2)
            htext = re.sub(r"[*_`]", "", htext).strip()
            if htext:
                blocks.append(Block("prose", htext, is_heading=True))
            continue

        if not line.strip():
            flush_para()
            continue

        para_buf.append(line)

    flush_para()
    return blocks


def parse_docx(path: Path) -> list[Block]:
    if docx is None:
        raise RuntimeError("python-docx is required to parse .docx files")
    document = docx.Document(str(path))
    blocks: list[Block] = []

    # python-docx does not give a simple ordered mix of paragraphs+tables at
    # the document body level without walking XML; walk body children.
    body = document.element.body
    for child in body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "p":
            para = docx.text.paragraph.Paragraph(child, document)
            txt = para.text.strip()
            if not txt:
                continue
            style_name = (para.style.name or "").lower() if para.style else ""
            is_heading = "heading" in style_name or "title" in style_name
            blocks.append(Block("prose", txt, is_heading=is_heading))
        elif tag == "tbl":
            table = docx.table.Table(child, document)
            for row in table.rows:
                cells_text = [c.text.strip() for c in row.cells]
                cell_text = " ".join(c for c in cells_text if c)
                if cell_text.strip():
                    blocks.append(Block("table", cell_text.strip()))
    return blocks


def parse_txt(text: str) -> list[Block]:
    blocks: list[Block] = []
    para_buf: list[str] = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            joined = " ".join(l.strip() for l in para_buf if l.strip())
            if joined.strip():
                blocks.append(Block("prose", joined.strip()))
        para_buf = []

    for line in text.split("\n"):
        if not line.strip():
            flush_para()
            continue
        para_buf.append(line)
    flush_para()
    return blocks


def load_blocks(path: Path) -> list[Block]:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return parse_docx(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".md":
        return parse_markdown(raw)
    return parse_txt(raw)


# --------------------------------------------------------------------------
# Tokenization helpers
# --------------------------------------------------------------------------

def words_in(text: str) -> list[str]:
    return WORD_RE.findall(text)


def sentences_in(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    parts = SENTENCE_SPLIT.split(text)
    return [p.strip() for p in parts if p.strip()]


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * (pct / 100.0)
    f = int(k)
    c = min(f + 1, len(s) - 1)
    if f == c:
        return s[f]
    return s[f] + (s[c] - s[f]) * (k - f)


# --------------------------------------------------------------------------
# Metric computation
# --------------------------------------------------------------------------

def compute_metrics(blocks: list[Block], clients: list[str]) -> dict:
    prose_blocks = [b for b in blocks if b.kind == "prose"]
    table_blocks = [b for b in blocks if b.kind == "table"]
    heading_blocks = [b for b in prose_blocks if b.is_heading]
    body_prose_blocks = [b for b in prose_blocks if not b.is_heading]

    words_prose = sum(len(words_in(b.text)) for b in prose_blocks)
    words_table = sum(len(words_in(b.text)) for b in table_blocks)
    total_words = words_prose + words_table
    table_share = (words_table / total_words) if total_words else 0.0

    # Sentences: drawn from non-heading prose paragraphs only.
    all_sentences: list[str] = []
    for b in body_prose_blocks:
        all_sentences.extend(sentences_in(b.text))

    sentence_count = len(all_sentences)
    sentence_lengths = [len(words_in(s)) for s in all_sentences]
    sentence_median_words = statistics.median(sentence_lengths) if sentence_lengths else 0
    sentence_p90_words = percentile(sentence_lengths, 90) if sentence_lengths else 0

    punch_sentences = sum(1 for n in sentence_lengths if n <= 8)
    punch_sentences_per_120_words = (
        (punch_sentences / words_prose * 120) if words_prose else 0.0
    )

    # Headings
    heading_count = len(heading_blocks)
    words_per_heading = (words_prose / heading_count) if heading_count else 0.0

    def heading_is_assertion(h: str) -> bool:
        low = h.lower()
        if ":" in h:
            return True
        if len(words_in(h)) >= 5:
            return True
        for v in HEADING_VERBS:
            if re.search(rf"\b{re.escape(v)}\b", low):
                return True
        return False

    assertive_headings = sum(1 for b in heading_blocks if heading_is_assertion(b.text))
    pct_headings_assertion = (
        (assertive_headings / heading_count) if heading_count else 0.0
    )

    # Client paragraph density (prose paragraphs only, non-heading)
    def mentions_client(text: str) -> bool:
        for c in clients:
            if not c:
                continue
            if re.search(re.escape(c), text, re.IGNORECASE):
                return True
        return False

    if clients:
        mentioning = sum(1 for b in body_prose_blocks if mentions_client(b.text))
        client_paragraph_density = (
            (mentioning / len(body_prose_blocks)) if body_prose_blocks else 0.0
        )
    else:
        client_paragraph_density = None

    # we/you ratio
    prose_text_all = " ".join(b.text for b in prose_blocks)
    we_count = len(WE_OUR.findall(prose_text_all))
    you_count = len(YOU_YOUR_CITY.findall(prose_text_all))
    for c in clients:
        if c:
            you_count += len(re.findall(re.escape(c), prose_text_all, re.IGNORECASE))
    we_you_ratio = (we_count / you_count) if you_count else (float("inf") if we_count else 0.0)

    # numbers per 100 words (prose only)
    numeric_tokens = 0
    for b in prose_blocks:
        numeric_tokens += len(NUMERIC_TOKEN.findall(b.text))
    numbers_per_100_words = (numeric_tokens / words_prose * 100) if words_prose else 0.0

    # so-what rate: sentences containing a number, followed same/next sentence
    # by a consequence cue.
    numbered_sentence_idxs = [
        i for i, s in enumerate(all_sentences) if NUMERIC_TOKEN.search(s)
    ]
    so_what_hits = 0
    for i in numbered_sentence_idxs:
        window = all_sentences[i]
        if i + 1 < len(all_sentences):
            window = window + " " + all_sentences[i + 1]
        if SO_WHAT_CUES.search(window):
            so_what_hits += 1
    so_what_rate = (
        (so_what_hits / len(numbered_sentence_idxs)) if numbered_sentence_idxs else 0.0
    )

    # tags in body
    full_text_all = " ".join(b.text for b in blocks)
    tags_in_body = sum(full_text_all.count(t) for t in TAG_PATTERNS)

    # banned words
    banned_counts = {}
    low_full = full_text_all.lower()
    for w in BANNED_WORDS:
        if w == "leverage":
            cnt = len(re.findall(r"\bleverage\s+(our|the|its)\b", low_full))
        elif w == "we are pleased":
            cnt = len(re.findall(r"\bwe are pleased\b", low_full))
        else:
            cnt = len(re.findall(rf"\b{re.escape(w)}\b", low_full))
        if cnt:
            banned_counts[w] = cnt
    banned_words_total = sum(banned_counts.values())

    # passive voice rate: fraction of sentences matching aux+participle pattern
    passive_hits = sum(1 for s in all_sentences if PAST_PARTICIPLE_AUX.search(s))
    passive_voice_rate = (passive_hits / sentence_count) if sentence_count else 0.0

    # avg paragraph words (prose paragraphs, non-heading)
    para_word_counts = [len(words_in(b.text)) for b in body_prose_blocks]
    avg_paragraph_words = statistics.mean(para_word_counts) if para_word_counts else 0.0

    # callouts / devices (informational) — only meaningful for markdown source,
    # counted from raw block text heuristically.
    callouts = 0
    for b in blocks:
        if b.text.strip().startswith(">"):
            callouts += 1
        if re.match(r"^\*\*[^*]+\*\*", b.text.strip()):
            callouts += 1
        if re.search(r"\b(Figure|Table)\s+\d", b.text):
            callouts += 1

    metrics = {
        "words_prose": words_prose,
        "words_table": words_table,
        "total_words": total_words,
        "table_share": round(table_share, 4),
        "sentence_count": sentence_count,
        "sentence_median_words": round(sentence_median_words, 1),
        "sentence_p90_words": round(sentence_p90_words, 1),
        "punch_sentences_per_120_words": round(punch_sentences_per_120_words, 2),
        "heading_count": heading_count,
        "words_per_heading": round(words_per_heading, 1),
        "pct_headings_assertion": round(pct_headings_assertion, 4),
        "client_paragraph_density": (
            round(client_paragraph_density, 4)
            if client_paragraph_density is not None
            else None
        ),
        "we_count": we_count,
        "you_count": you_count,
        "we_you_ratio": (
            round(we_you_ratio, 2) if we_you_ratio != float("inf") else None
        ),
        "numbers_per_100_words": round(numbers_per_100_words, 2),
        "so_what_rate": round(so_what_rate, 4),
        "tags_in_body": tags_in_body,
        "banned_words_total": banned_words_total,
        "banned_words_detail": banned_counts,
        "passive_voice_rate": round(passive_voice_rate, 4),
        "avg_paragraph_words": round(avg_paragraph_words, 1),
        "callouts_or_devices": callouts,
    }
    return metrics


# --------------------------------------------------------------------------
# Targets / PASS-FAIL
# --------------------------------------------------------------------------

TARGETS = [
    # (metric key, label, check function, target description)
    ("table_share", "Table share of words", lambda v: v <= 0.35, "<= 0.35"),
    (
        "sentence_median_words",
        "Sentence median words",
        lambda v: 18 <= v <= 25,
        "18-25",
    ),
    ("sentence_p90_words", "Sentence p90 words", lambda v: v <= 40, "<= 40"),
    (
        "punch_sentences_per_120_words",
        "Punch sentences / 120 words",
        lambda v: v >= 1,
        ">= 1",
    ),
    (
        "words_per_heading",
        "Words per heading",
        lambda v: 150 <= v <= 220,
        "150-220",
    ),
    (
        "client_paragraph_density",
        "Client paragraph density",
        lambda v: v is not None and v >= 0.8,
        ">= 0.8",
    ),
    (
        "numbers_per_100_words",
        "Numbers per 100 words",
        lambda v: v >= 1.5,
        ">= 1.5",
    ),
    ("so_what_rate", "So-what rate", lambda v: v >= 0.6, ">= 0.6"),
    ("tags_in_body", "Tags in body", lambda v: v == 0, "== 0"),
    ("banned_words_total", "Banned words", lambda v: v == 0, "== 0"),
    (
        "passive_voice_rate",
        "Passive voice rate",
        lambda v: v <= 0.15,
        "<= 0.15",
    ),
    (
        "avg_paragraph_words",
        "Avg paragraph words",
        lambda v: v <= 110,
        "<= 110",
    ),
]

INFORMATIONAL = {"we_you_ratio", "callouts_or_devices", "pct_headings_assertion"}


def render_table(metrics: dict, source_name: str) -> str:
    lines = []
    lines.append(f"Prose metrics: {source_name}")
    lines.append("-" * max(40, len(source_name) + 16))
    lines.append(f"{'Metric':<32}{'Value':<14}{'Target':<12}{'Result'}")
    lines.append("-" * 70)

    def fmt(v):
        if v is None:
            return "n/a"
        if isinstance(v, float):
            return f"{v:g}"
        return str(v)

    # informational-only, non-target rows shown first for context
    lines.append(f"{'words_prose':<32}{fmt(metrics['words_prose']):<14}{'':<12}")
    lines.append(f"{'words_table':<32}{fmt(metrics['words_table']):<14}{'':<12}")
    lines.append(f"{'sentence_count':<32}{fmt(metrics['sentence_count']):<14}{'':<12}")
    lines.append(f"{'heading_count':<32}{fmt(metrics['heading_count']):<14}{'':<12}")
    lines.append(
        f"{'pct_headings_assertion':<32}{fmt(metrics['pct_headings_assertion']):<14}{'':<12}"
    )
    lines.append(f"{'we_count':<32}{fmt(metrics['we_count']):<14}{'':<12}")
    lines.append(f"{'you_count':<32}{fmt(metrics['you_count']):<14}{'':<12}")
    lines.append(f"{'we_you_ratio':<32}{fmt(metrics['we_you_ratio']):<14}{'':<12}")
    lines.append(
        f"{'callouts_or_devices':<32}{fmt(metrics['callouts_or_devices']):<14}{'':<12}"
    )
    lines.append("-" * 70)

    for key, label, check, target_desc in TARGETS:
        v = metrics.get(key)
        try:
            passed = check(v)
        except TypeError:
            passed = False
        result = "PASS" if passed else "FAIL"
        lines.append(f"{label:<32}{fmt(v):<14}{target_desc:<12}{result}")

    if metrics.get("banned_words_detail"):
        lines.append("")
        lines.append("Banned word detail:")
        for w, c in metrics["banned_words_detail"].items():
            lines.append(f"  {w}: {c}")

    return "\n".join(lines)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Deterministic prose-metrics tool for proposal writing."
    )
    parser.add_argument("file", type=str, help="Path to .md, .docx, or .txt file")
    parser.add_argument(
        "--client",
        action="append",
        default=[],
        help="Client term to search for (repeatable)",
    )
    parser.add_argument(
        "--json", action="store_true", help="Also write metrics JSON alongside output"
    )
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    blocks = load_blocks(path)
    metrics = compute_metrics(blocks, args.client)

    print(render_table(metrics, str(path)))

    if args.json:
        out_path = path.with_suffix(path.suffix + ".metrics.json")
        out_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        print(f"\nJSON written to: {out_path}")


if __name__ == "__main__":
    main()
