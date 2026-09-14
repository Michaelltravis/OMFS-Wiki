#!/usr/bin/env python3
"""verbatim_sections.py — shared library for the section layer of verbatim/<slug>/.

Parses page files (verbatim/<slug>/pages/pNNNN.md), detects section headings,
nests them under the PDF outline, derives (page, ¶) spans, and answers
"which section is (page, ¶) in" / "which section matches this query".
Also loads verbatim/<slug>/sanitize.json and applies it.

Used by: work/build_sections.py, work/assign_block_sections.py,
work/assemble_section.py, work/find_uncovered.py, work/regen_index.py,
work/lint_blocks.py. No CLI here.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERBATIM = ROOT / "verbatim"

RULES_VERSION = 1
SEP = chr(31)  # unit separator: mask token delimiter, never appears in prose

PARA_MARKER_RE = re.compile(r"<!--\s*¶(\d+)\s*-->")
RECOVERED_MARKER = "<!-- recovered from text layer -->"
PICTURE_END = "End of picture text"
PICTURE_START = "Start of picture text"
GRAPHIC_ID_RE = re.compile(r"\b\d{3}_[A-Za-z0-9]+(?:_[A-Za-z0-9]+){0,2}\b")
CAPTION_RE = re.compile(r"^(EXHIBIT|TABLE|FIGURE)\s+[\w.\-]+", re.IGNORECASE)
TRAILING_STOPWORDS = {
    "be", "for", "and", "to", "of", "the", "with", "a", "an", "in", "on", "is",
    "will", "or", "by", "at", "as", "that", "our", "your",
}
HEADING_LINE_RE = re.compile(r"^(#{1,6})\s+(.*)$")
NUMBERED_RE = re.compile(
    r"^(?P<num>(?:\d+(?:\.\d+)*\.?)|(?:[IVXLC]+\.(?:[A-Z]\.)?(?:\d+\.)*)|(?:[A-Z]\.))"
    r"(?:\s+\|?\s*|\s*\|\s*)(?P<rest>\S.*)$"   # the number must be followed by whitespace or '|' ("99.98% ..." is not a number)
)


# --------------------------------------------------------------------------
# page parsing
# --------------------------------------------------------------------------

@dataclass
class Para:
    n: int
    text: str
    recovered: bool = False
    picture: bool = False

    @property
    def first_line(self) -> str:
        for ln in self.text.splitlines():
            if ln.strip():
                return ln.strip()
        return ""

    @property
    def is_heading(self) -> bool:
        return bool(HEADING_LINE_RE.match(self.first_line))


def parse_frontmatter(text: str):
    """Simple key: value frontmatter parser (no yaml dependency). Returns (dict, body)."""
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    fm = {}
    for ln in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", ln.rstrip())
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
                v = v[1:-1]
            fm[m.group(1)] = v
    return fm, "\n".join(lines[end + 1:])


def parse_page(path: Path):
    """Return (frontmatter, [Para]) for one verbatim page file."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(raw)
    parts = PARA_MARKER_RE.split(body)
    paras: list[Para] = []
    recovered = RECOVERED_MARKER in parts[0] if parts else False
    for i in range(1, len(parts), 2):
        n = int(parts[i])
        txt = parts[i + 1] if i + 1 < len(parts) else ""
        flag_after = RECOVERED_MARKER in txt
        txt = txt.replace(RECOVERED_MARKER, "")
        txt = txt.strip("\n")
        paras.append(Para(n=n, text=txt.strip(), recovered=recovered,
                          picture=(PICTURE_END in txt or PICTURE_START in txt)))
        if flag_after:
            recovered = True
    return fm, paras


def page_paths(slug: str) -> list[Path]:
    return sorted((VERBATIM / slug / "pages").glob("p*.md"))


def load_pages(slug: str) -> dict[int, tuple[dict, list[Para]]]:
    out = {}
    for p in page_paths(slug):
        fm, paras = parse_page(p)
        try:
            pno = int(fm.get("page") or p.stem[1:])
        except ValueError:
            pno = int(p.stem[1:])
        out[pno] = (fm, paras)
    return dict(sorted(out.items()))


def load_manifest(slug: str) -> dict:
    return json.loads((VERBATIM / slug / "manifest.json").read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# repeating lines (running headers / footers / tab bars)
# --------------------------------------------------------------------------

DASHES = "‐‑‒–—―−"


def norm_repeat(line: str) -> str:
    s = line.strip()
    s = re.sub(r"<[^>]+>", " ", s)          # html tags incl <br>, <mark>
    s = re.sub(r"[#*_~`]+", " ", s)         # markdown marks
    for d in DASHES:
        s = s.replace(d, "-")
    s = re.sub(r"\d+", "#", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def repeating_lines(pages: dict[int, tuple[dict, list[Para]]], min_pages: int = 3) -> set[str]:
    counts: dict[str, set[int]] = {}
    for pno, (_fm, paras) in pages.items():
        for para in paras:
            for ln in re.split(r"<br\s*/?>|\n", para.text):
                s = ln.strip()
                if not s or s.startswith("<!--"):
                    continue
                if len(s) > 160:
                    continue
                n = norm_repeat(s)
                if len(n) < 8:
                    continue
                counts.setdefault(n, set()).add(pno)
    return {n for n, ps in counts.items() if len(ps) >= min_pages}


# --------------------------------------------------------------------------
# heading classification
# --------------------------------------------------------------------------

@dataclass
class HeadingInfo:
    md_level: int
    text: str            # plain text, markup stripped
    bold: bool
    italic: bool
    caps: bool
    numbered_depth: int  # 0 if unnumbered
    has_mark: bool
    excluded: str | None = None

    @property
    def style(self) -> int:
        if self.bold and self.caps:
            return 0
        if self.bold and self.italic:
            return 1
        if self.bold:
            return 2
        return 3

    @property
    def rank(self) -> tuple:
        if self.numbered_depth:
            return (1, self.numbered_depth)
        return (2, self.md_level, self.style)


def plain_text(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_~`]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def numbered_depth(text: str) -> int:
    m = NUMBERED_RE.match(text)
    if not m:
        return 0
    num = m.group("num").rstrip(".")
    if re.fullmatch(r"[A-Z]", num):
        return 1
    return len([c for c in num.split(".") if c])


def classify_heading(first_line: str, repeating: set[str], in_recovered: bool = False) -> HeadingInfo | None:
    m = HEADING_LINE_RE.match(first_line.strip())
    if not m:
        return None
    md_level = len(m.group(1))
    body = m.group(2).strip()
    has_mark = "<mark>" in body
    inner = re.sub(r"<[^>]+>", "", body).strip()
    bold = bool(re.fullmatch(r"\*\*.+\*\*", inner))
    core = inner[2:-2].strip() if bold else inner
    italic = bool(re.fullmatch(r"_.+_", core)) or bool(re.fullmatch(r"\*.+\*", core))
    text = plain_text(inner)
    letters = re.sub(r"[^A-Za-z]", "", text)
    caps = len(letters) > 3 and letters.isupper()
    depth = numbered_depth(text)
    info = HeadingInfo(md_level, text, bold, italic, caps, depth, has_mark)

    words = text.split()
    if CAPTION_RE.match(text):
        info.excluded = "caption"
    elif norm_repeat(inner) in repeating:
        info.excluded = "repeating"
    elif has_mark:
        info.excluded = "mark"
    elif re.match(r"^[–—•µ\-]", text):
        info.excluded = "bullet-or-dash"
    elif len(words) > 12:
        info.excluded = "too-long"
    elif not words:
        info.excluded = "empty"
    elif text[-1] in ".:,;" or text[-1] in DASHES or text.endswith("-") \
            or words[-1].lower().strip("*_") in TRAILING_STOPWORDS:
        info.excluded = "fragment"
    elif in_recovered:
        info.excluded = "recovered-tail"
    elif not (bold or italic or depth):
        info.excluded = "plain"
    return info


# --------------------------------------------------------------------------
# section building
# --------------------------------------------------------------------------

@dataclass
class Section:
    id: str
    title: str
    level: int
    parent: str | None
    outline_index: int
    outline_title: str
    kind: str                     # outline | outline+body | body | front
    start: dict                   # {page, para}
    end: dict
    anchor: str
    heading_line: str = ""
    minor: bool = False
    rank: tuple = field(default=(0, 1), repr=False, compare=False)

    def to_json(self) -> dict:
        d = asdict(self)
        d.pop("rank", None)
        return d


def slugify(text: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s[:maxlen].rstrip("-") or "untitled"


def _tokens(s: str) -> set[str]:
    toks = re.findall(r"[a-z0-9]+", s.lower())
    return {t for t in toks if t not in {"section", "the", "and", "of", "to", "a", "an", "in", "for", "on"} and not re.fullmatch(r"[ivxlc]+|[a-z]|\d+", t)}


def title_overlap(body_title: str, outline_title: str) -> float:
    a, b = _tokens(body_title), _tokens(outline_title)
    if not b:
        return 0.0
    return len(a & b) / len(b)


def toc_levels(manifest: dict) -> dict[int, int]:
    """outline index -> bookmark level, via fitz when the PDF is present; fallback by numbering depth."""
    outline = manifest.get("outline") or []
    levels = {}
    toc = None
    pdf = manifest.get("pdf")
    try:
        import fitz  # type: ignore
        pdf_path = (ROOT / pdf) if pdf and not Path(pdf).is_absolute() else Path(pdf or "")
        if pdf_path.is_file():
            toc = fitz.open(str(pdf_path)).get_toc()
    except Exception:
        toc = None
    if toc:
        by_key: dict[tuple, list[int]] = {}
        for lvl, title, page in toc:
            by_key.setdefault((page, title.strip()), []).append(lvl)
        for i, o in enumerate(outline):
            key = (int(o["page"]), (o.get("title") or "").strip())
            if key in by_key and by_key[key]:
                levels[i] = by_key[key].pop(0)
    for i, o in enumerate(outline):
        # Title numbering is more reliable than bookmark depth (PDFs often flatten
        # "I." and "I.A." to one level); use it whenever the title is numbered.
        d = numbered_depth((o.get("title") or "").strip())
        if d:
            levels[i] = d
        elif i not in levels:
            levels[i] = 1
    return levels


def build_sections(slug: str, rules: dict | None = None) -> dict:
    """Build the section layer for one source. Returns the sections.json document (dict)."""
    rules = rules or {}
    manifest = load_manifest(slug)
    pages = load_pages(slug)
    if not pages:
        raise SystemExit(f"no pages for {slug}")
    repeating = repeating_lines(pages, min_pages=int(rules.get("repeat_min_pages", 3)))
    extra_excl = [re.compile(p, re.IGNORECASE) for p in rules.get("exclude_heading_regex", [])]

    outline = manifest.get("outline") or []
    levels = toc_levels(manifest)
    counts = {pno: (max((p.n for p in paras), default=0)) for pno, (_fm, paras) in pages.items()}
    page_list = sorted(pages)
    first_page, last_page = page_list[0], page_list[-1]

    # --- candidate body headings ------------------------------------------
    body_heads = []   # dicts: page, para, info, line
    stats = {"body_headings": 0, "excluded": {}, "merged": 0}
    for pno, (_fm, paras) in pages.items():
        for para in paras:
            if not para.is_heading or para.picture:
                continue
            info = classify_heading(para.first_line, repeating, in_recovered=para.recovered)
            if info is None:
                continue
            stats["body_headings"] += 1
            if not info.excluded and any(rx.search(info.text) for rx in extra_excl):
                info.excluded = "rule"
            body_heads.append({"page": pno, "para": para.n, "info": info, "line": para.first_line})

    # --- outline entries, merged with a matching body heading on the same page
    stream = []  # entries: dict(pos, order, kind, title, rank, outline_index, outline_title, line)
    consumed = set()
    for i, o in enumerate(outline):
        title = (o.get("title") or "").strip()
        page = int(o["page"])
        if page not in pages:
            # outline points to a page without a file (should not happen) — clamp
            page = min(page_list, key=lambda p: abs(p - page))
        best, best_r = None, 0.0
        for h in body_heads:
            if h["page"] != page or (h["page"], h["para"]) in consumed:
                continue
            r = title_overlap(h["info"].text, title)
            if r > best_r:
                best, best_r = h, r
        if best is not None and best_r >= 0.6:
            consumed.add((best["page"], best["para"]))
            stats["merged"] += 1
            stream.append(dict(pos=(page, best["para"]), order=(0, i), kind="outline+body",
                               title=title, rank=(0, levels[i]), outline_index=i,
                               outline_title=title, line=best["line"]))
        else:
            stream.append(dict(pos=(page, 1), order=(0, i), kind="outline", title=title,
                               rank=(0, levels[i]), outline_index=i, outline_title=title, line=""))
    if outline and int(outline[0]["page"]) > first_page:
        stream.append(dict(pos=(first_page, 1), order=(-1, 0), kind="front", title="Front matter",
                           rank=(0, 1), outline_index=-1, outline_title="", line=""))

    for h in body_heads:
        info = h["info"]
        if (h["page"], h["para"]) in consumed:
            continue
        if info.excluded:
            stats["excluded"][info.excluded] = stats["excluded"].get(info.excluded, 0) + 1
            continue
        stream.append(dict(pos=(h["page"], h["para"]), order=(1, 0), kind="body", title=info.text,
                           rank=info.rank, outline_index=None, outline_title=None, line=h["line"]))

    stream.sort(key=lambda e: (e["pos"], e["order"]))

    # --- nesting via stack walk --------------------------------------------
    sections: list[Section] = []
    stack: list[Section] = []
    cur_outline_idx, cur_outline_title = -1, ""
    id_seen: dict[str, int] = {}
    for e in stream:
        if e["kind"] in ("outline", "outline+body", "front"):
            cur_outline_idx, cur_outline_title = e["outline_index"], e["outline_title"]
            base = f"{slug}:{cur_outline_idx:02d}" if cur_outline_idx >= 0 else f"{slug}:00-front"
            sid = base
        else:
            sid = f"{slug}:{max(cur_outline_idx, 0):02d}.{slugify(e['title'])}"
        if sid in id_seen:
            id_seen[sid] += 1
            sid = f"{sid}-p{e['pos'][0]}"
            if sid in id_seen:
                sid = f"{sid}-{e['pos'][1]}"
        id_seen[sid] = id_seen.get(sid, 0) + 1
        # Pop everything of equal or lower standing — but never a section that starts
        # at this very position (two outline entries on one page nest instead of
        # becoming zero-length siblings).
        while stack and stack[-1].rank >= e["rank"] and \
                (stack[-1].start["page"], stack[-1].start["para"]) != e["pos"]:
            stack.pop()
        parent = stack[-1].id if stack else None
        sec = Section(id=sid, title=e["title"], level=len(stack) + 1, parent=parent,
                      outline_index=cur_outline_idx, outline_title=cur_outline_title or "",
                      kind=e["kind"], start={"page": e["pos"][0], "para": e["pos"][1]},
                      end={"page": e["pos"][0], "para": e["pos"][1]},
                      anchor=f"verbatim/{slug}/pages/p{e['pos'][0]:04d}.md#¶{e['pos'][1]}",
                      heading_line=e["line"], rank=e["rank"])
        sections.append(sec)
        stack.append(sec)

    # --- spans --------------------------------------------------------------
    def prev_pos(pos):
        page, para = pos
        if para > 1:
            return (page, para - 1)
        idx = page_list.index(page)
        while idx > 0:
            idx -= 1
            p = page_list[idx]
            if counts[p] > 0:
                return (p, counts[p])
        return pos

    last_pos = None
    for p in reversed(page_list):
        if counts[p] > 0:
            last_pos = (p, counts[p])
            break
    for i, sec in enumerate(sections):
        end = last_pos
        for nxt in sections[i + 1:]:
            if nxt.rank <= sec.rank:
                end = prev_pos((nxt.start["page"], nxt.start["para"]))
                break
        if end < (sec.start["page"], sec.start["para"]):
            end = (sec.start["page"], sec.start["para"])
        sec.end = {"page": end[0], "para": end[1]}

    # --- minor demotion -----------------------------------------------------
    has_child = {s.parent for s in sections if s.parent}
    by_id = {s.id: s for s in sections}
    for sec in sections:
        if sec.kind != "body" or sec.id in has_child:
            continue
        words = 0
        for pno, (_fm, paras) in pages.items():
            if pno < sec.start["page"] or pno > sec.end["page"]:
                continue
            for para in paras:
                pos = (pno, para.n)
                if pos < (sec.start["page"], sec.start["para"]) or pos > (sec.end["page"], sec.end["para"]):
                    continue
                if pos == (sec.start["page"], sec.start["para"]) or para.picture or para.recovered or para.is_heading:
                    continue
                words += len(plain_text(para.text).split())
        if words < int(rules.get("minor_min_words", 15)):
            sec.minor = True

    doc = {
        "slug": slug,
        "rules_version": RULES_VERSION,
        "page_count": manifest.get("page_count"),
        "repeating_lines": sorted(repeating),
        "stats": {"sections": len(sections), "outline": len(outline), "merged": stats["merged"],
                  "body_headings": stats["body_headings"], "excluded": stats["excluded"],
                  "minor": sum(1 for s in sections if s.minor)},
        "sections": [s.to_json() for s in sections],
    }
    return doc


# --------------------------------------------------------------------------
# queries over a built section layer
# --------------------------------------------------------------------------

def load_sections(slug: str) -> dict:
    p = VERBATIM / slug / "sections.json"
    if not p.is_file():
        raise FileNotFoundError(f"{p} — run: python work/build_sections.py {slug}")
    return json.loads(p.read_text(encoding="utf-8"))


def _pos(d: dict) -> tuple:
    return (int(d["page"]), int(d["para"]))


def contains(sec: dict, page: int, para: int) -> bool:
    return _pos(sec["start"]) <= (page, para) <= _pos(sec["end"])


def section_for(doc: dict, page: int, para: int, allow_minor: bool = False) -> dict | None:
    best = None
    for sec in doc["sections"]:
        if sec.get("minor") and not allow_minor:
            continue
        if contains(sec, page, para) and (best is None or sec["level"] > best["level"]):
            best = sec
    return best


def subtree_ids(doc: dict, sid: str) -> list[str]:
    children: dict[str, list[str]] = {}
    for sec in doc["sections"]:
        if sec.get("parent"):
            children.setdefault(sec["parent"], []).append(sec["id"])
    out, todo = [], [sid]
    while todo:
        cur = todo.pop(0)
        out.append(cur)
        todo.extend(children.get(cur, []))
    return out


def _qnorm(s: str) -> str:
    s = re.sub(r"^\s*(?:\d+(?:\.\d+)*\.?|[IVXLC]+\.(?:[A-Z]\.)?(?:\d+\.)*|[A-Z]\.)\s*[|:.\-]?\s*", "", s)
    s = re.sub(r"^section\s+\d+\s*[-:|.]*\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def resolve_query(doc: dict, query: str, include_minor: bool = False) -> list[dict]:
    """Return candidate sections ordered best-first; [best] if unambiguous, several if not."""
    by_id = {s["id"]: s for s in doc["sections"]}
    if query in by_id:
        return [by_id[query]]
    q = _qnorm(query)
    qt = set(q.split())
    scored = []
    for sec in doc["sections"]:
        if sec.get("minor") and not include_minor:
            continue
        t = _qnorm(sec["title"])
        if not t:
            continue
        if q and (q == t):
            score = 1.2
        elif q and q in t:
            score = 1.0
        else:
            tt = set(t.split())
            score = len(qt & tt) / len(qt | tt) if (qt | tt) else 0.0
        if score >= 0.5:
            scored.append((score, sec["level"], sec))
    scored.sort(key=lambda x: (-x[0], x[1], x[2]["start"]["page"]))
    if not scored:
        return []
    if len(scored) == 1:
        return [scored[0][2]]
    # Title matches (score >= 1.0): if the shallowest of them contains all the others,
    # it is the section the user means ("safety" -> the whole safety section, not its
    # 4.1 child); otherwise the matches are genuinely different places -> ambiguous.
    strong = [s for sc, _, s in scored if sc >= 1.0]
    if len(strong) >= 2:
        # the candidate whose subtree holds the most title matches wins if it holds at
        # least three quarters of them (a stray resume heading elsewhere should not block
        # "the safety section"); ties go to the shallowest.
        top_match = scored[0][2]
        best, best_n = None, 0
        for s in sorted(strong, key=lambda s: (s["level"], s["start"]["page"])):
            inside = set(subtree_ids(doc, s["id"]))
            if top_match["id"] not in inside:
                continue
            n = sum(1 for t in strong if t["id"] in inside)
            if n > best_n:
                best, best_n = s, n
        if best is not None and best_n >= max(2, 0.6 * len(strong)):
            return [best]
        return strong
    if scored[0][0] - scored[1][0] >= 0.15:
        return [scored[0][2]]
    return [s for _, _, s in scored]


# --------------------------------------------------------------------------
# sanitization
# --------------------------------------------------------------------------

def load_sanitize(slug: str) -> dict | None:
    p = VERBATIM / slug / "sanitize.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


class Sanitizer:
    """Apply a source's sanitize.json to text: client → [CLIENT], facilities → [FACILITY A],
    locations → [the region], products → replacement; protected phrases are never touched."""

    def __init__(self, cfg: dict):
        self.cfg = cfg or {}
        self.counts: dict[str, int] = {}
        self._first_client = True
        self._first_fac: dict[str, bool] = {}
        self.descriptor = self.cfg.get("descriptor", "")
        rules = []  # (regex, kind, payload)
        for name in self._names("client_names"):
            rules.append((self._rx(name), "client", None))
        for name in self._names("client_aliases"):
            # aliases ("the Town", "Town", "the County") are written exactly as the proposal
            # uses them and are matched case-sensitively so "a small town" is left alone
            rules.append((self._rx(name, exact_case=True), "client", None))
        for fac in self.cfg.get("facility_names", []) or []:
            for name in fac.get("names", []):
                rules.append((self._rx(name), "facility", fac))
        for prod in self.cfg.get("product_names", []) or []:
            for name in prod.get("names", []):
                rules.append((self._rx(name), "product", prod))
        for name in self._names("location_names"):
            rules.append((self._rx(name), "location", None))
        # longest names first so "Town of Hull" wins over "Hull"
        rules.sort(key=lambda r: -len(r[0].pattern))
        self.rules = rules
        self.protect = [p for p in (self.cfg.get("protect") or [])]

    def _names(self, key: str) -> list[str]:
        return [n for n in (self.cfg.get(key) or []) if n]

    @staticmethod
    def _rx(name: str, exact_case: bool = False) -> re.Pattern:
        # Boundaries exclude letters/digits only (not '_'), so a name touching markdown
        # italics ("for the Town_") still matches; graphic asset ids are masked separately.
        acronym = name.isupper() and " " not in name
        pat = r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])"
        return re.compile(pat) if (acronym or exact_case) else re.compile(pat, re.IGNORECASE)

    def apply(self, text: str, descriptor: bool = True) -> str:
        """descriptor=False suppresses the first-use "(a coastal New England town)" insertion
        (used for headings, so the descriptor lands in the first body paragraph instead)."""
        if not self.rules:
            return text
        masks: dict[str, str] = {}
        for i, phrase in enumerate(self.protect):
            token = f"{SEP}P{i}{SEP}"
            new = re.sub(r"(?<![A-Za-z0-9_])" + re.escape(phrase) + r"(?![A-Za-z0-9_])", token, text, flags=re.IGNORECASE)
            if new != text:
                masks[token] = phrase
                text = new
        # graphic ids are protected implicitly
        gids: dict[str, str] = {}
        def _mask_gid(m):
            token = f"{SEP}G{len(gids)}{SEP}"
            gids[token] = m.group(0)
            return token
        text = GRAPHIC_ID_RE.sub(_mask_gid, text)

        for rx, kind, payload in self.rules:
            def _sub(m, kind=kind, payload=payload):
                self.counts[kind] = self.counts.get(kind, 0) + 1
                if kind == "client":
                    if descriptor and self._first_client and self.descriptor:
                        self._first_client = False
                        return f"[CLIENT] ({self.descriptor})"
                    return "[CLIENT]"
                if kind == "facility":
                    ph = payload.get("placeholder", "[FACILITY]")
                    if descriptor and not self._first_fac.get(ph) and payload.get("descriptor"):
                        self._first_fac[ph] = True
                        return f"{ph} ({payload['descriptor']})"
                    return ph
                if kind == "product":
                    return payload.get("replacement", "[PRODUCT]")
                return self.cfg.get("location_placeholder", "[the region]")
            text = rx.sub(_sub, text)

        for token, phrase in list(gids.items()) + list(masks.items()):
            text = text.replace(token, phrase)
        return text


# --------------------------------------------------------------------------
# substantive-paragraph test (shared by find_uncovered and the assembler trailer)
# --------------------------------------------------------------------------

def is_substantive(para: Para, repeating: set[str], min_words: int = 25, include_recovered: bool = False):
    """Return (True, '') if the paragraph is prose worth a block, else (False, reason)."""
    if para.picture:
        return False, "picture-text"
    if para.recovered and not include_recovered:
        return False, "recovered-tail"
    if para.is_heading:
        return False, "heading"
    t = para.text
    if "[illegible]" in t or "[IMAGE-ONLY PAGE" in t:
        return False, "illegible"
    first = para.first_line
    if CAPTION_RE.match(plain_text(first)):
        return False, "caption"
    if norm_repeat(first) in repeating:
        return False, "repeating"
    words = plain_text(t).split()
    if len(words) < min_words:
        return False, "short"
    return True, ""
