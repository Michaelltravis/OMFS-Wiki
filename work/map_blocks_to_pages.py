#!/usr/bin/env python3
"""
map_blocks_to_pages.py

For every content block under wiki/**/*.md (excluding index.md and graphics/),
find which verbatim source pages (verbatim/<slug>/pages/pNNNN.md) it was derived
from, using 6-word-shingle overlap. Writes work/block_page_map.json and
work/block_page_map.md. Does NOT modify anything under wiki/ or verbatim/.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
VERBATIM = ROOT / "verbatim"
WORK = ROOT / "work"

SHINGLE_N = 6

# --- normalization -----------------------------------------------------

CLIENT_PATTERNS = [
    r"town of hull",
    r"city of santa monica",
    r"santa monica",
    r"hull",
    r"swip",
    r"\[client\]",
]
CLIENT_RE = re.compile("|".join(CLIENT_PATTERNS), re.IGNORECASE)

APOSTROPHES = "'’‘ʼʻ"
APOSTROPHE_RE = re.compile(f"[{re.escape(APOSTROPHES)}]")


def normalize(text: str) -> str:
    text = text.replace("�", "")
    text = APOSTROPHE_RE.sub("", text)
    text = text.lower()
    text = CLIENT_RE.sub("cli", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def shingles(text: str, n: int = SHINGLE_N):
    words = text.split()
    if len(words) < n:
        return set([" ".join(words)]) if words else set()
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


# --- frontmatter / body parsing ----------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    fm = {}
    for line in fm_text.splitlines():
        line = line.rstrip()
        mm = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if mm:
            key = mm.group(1).strip()
            val = mm.group(2).strip()
            if val.startswith('"') and val.endswith('"') and len(val) >= 2:
                val = val[1:-1]
            fm[key] = val
    return fm, body


def strip_reuse_guidance(body: str) -> str:
    # Remove the "## Reuse guidance" section (editorial, not source-derived)
    return re.split(r"\n##\s+Reuse guidance\b", body, maxsplit=1, flags=re.IGNORECASE)[0]


# --- verbatim page parsing (read fresh each time; tolerate concurrent edits) --

PARA_MARKER_RE = re.compile(r"<!--\s*¶(\d+)\s*-->")


def load_verbatim_page(path: Path):
    """Returns (full_norm_text, {para_num: norm_text}).

    Tolerant of concurrent modification by another agent: retries briefly on
    PermissionError/OSError (e.g. transient Windows file lock), and gives up
    gracefully by returning empty content if the file truly can't be read.
    """
    import time
    raw = None
    for attempt in range(5):
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
            break
        except FileNotFoundError:
            return "", {}
        except OSError:
            time.sleep(0.2 * (attempt + 1))
    if raw is None:
        return "", {}
    _, body = parse_frontmatter(raw)
    # Split on paragraph markers
    parts = PARA_MARKER_RE.split(body)
    # parts alternates: [pre-text, num, text, num, text, ...]
    paras = {}
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            num = int(parts[i])
            txt = parts[i + 1] if i + 1 < len(parts) else ""
            paras[num] = normalize(txt)
    full_norm = normalize(body)
    return full_norm, paras


def get_slug_pages(slug: str):
    pages_dir = VERBATIM / slug / "pages"
    if not pages_dir.is_dir():
        return []
    return sorted(pages_dir.glob("p*.md"))


def classify(covered_fraction: float) -> str:
    if covered_fraction >= 0.6:
        return "verbatim"
    if covered_fraction >= 0.2:
        return "partial"
    if covered_fraction >= 0.05:
        return "recipe"
    return "absent"


def main():
    block_paths = []
    for p in sorted(WIKI.rglob("*.md")):
        rel = p.relative_to(WIKI)
        if rel.name == "index.md":
            continue
        if "graphics" in rel.parts:
            continue
        block_paths.append(p)

    result = {}
    missing_slug_folders = set()

    # cache slug -> list of page paths (file listing only; content read fresh per block)
    slug_page_paths_cache = {}

    for block_path in block_paths:
        rel_path = str(block_path.relative_to(ROOT)).replace("\\", "/")
        raw = block_path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(raw)
        slug = fm.get("source", "")
        body_for_shingles = strip_reuse_guidance(body)
        norm_block = normalize(body_for_shingles)
        block_shingles = shingles(norm_block)

        if slug not in slug_page_paths_cache:
            slug_page_paths_cache[slug] = get_slug_pages(slug)
        page_paths = slug_page_paths_cache[slug]

        if not page_paths:
            missing_slug_folders.add(slug)
            result[rel_path] = {
                "slug": slug,
                "best_pages": [],
                "covered_fraction": 0.0,
                "top_paragraphs": [],
                "verbatim_class": "absent",
            }
            continue

        if not block_shingles:
            result[rel_path] = {
                "slug": slug,
                "best_pages": [],
                "covered_fraction": 0.0,
                "top_paragraphs": [],
                "verbatim_class": "absent",
            }
            continue

        n_block_shingles = len(block_shingles)
        union_found = set()
        page_overlaps = []  # (page_label, overlap_fraction)
        para_overlaps = []  # (page_label, para_num, overlap_fraction)

        for page_path in page_paths:
            page_label = page_path.stem  # e.g. p0010
            full_norm, paras = load_verbatim_page(page_path)
            page_shingle_set = shingles(full_norm)
            found = block_shingles & page_shingle_set
            if found:
                union_found |= found
            overlap = len(found) / n_block_shingles if n_block_shingles else 0.0
            if overlap > 0:
                page_overlaps.append((page_label, overlap))

            for para_num, para_text in paras.items():
                para_shingle_set = shingles(para_text)
                if not para_shingle_set:
                    continue
                pfound = block_shingles & para_shingle_set
                if pfound:
                    poverlap = len(pfound) / n_block_shingles
                    if poverlap > 0:
                        para_overlaps.append((page_label, para_num, poverlap))

        covered_fraction = len(union_found) / n_block_shingles if n_block_shingles else 0.0

        page_overlaps.sort(key=lambda x: -x[1])
        best_pages = [
            {"page": pl, "overlap": round(ov, 4)}
            for pl, ov in page_overlaps if ov >= 0.05
        ][:5]

        para_overlaps.sort(key=lambda x: -x[2])
        top_paragraphs = [
            {"page": pl, "para": pn, "overlap": round(ov, 4)}
            for pl, pn, ov in para_overlaps
        ][:8]

        result[rel_path] = {
            "slug": slug,
            "best_pages": best_pages,
            "covered_fraction": round(covered_fraction, 4),
            "top_paragraphs": top_paragraphs,
            "verbatim_class": classify(covered_fraction),
        }

    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / "block_page_map.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # --- build markdown summary ---
    class_counts = defaultdict(int)
    category_class_counts = defaultdict(lambda: defaultdict(int))
    for rel_path, info in result.items():
        cls = info["verbatim_class"]
        class_counts[cls] += 1
        category = rel_path.split("/")[1] if rel_path.startswith("wiki/") else rel_path.split("/")[0]
        category_class_counts[category][cls] += 1

    classes = ["verbatim", "partial", "recipe", "absent"]
    lines = []
    lines.append("# Block-to-Page Verbatim Mapping Summary")
    lines.append("")
    lines.append(f"Total blocks: {len(result)}")
    lines.append("")
    lines.append("## Overall class counts")
    lines.append("")
    lines.append("| class | count |")
    lines.append("|---|---|")
    for c in classes:
        lines.append(f"| {c} | {class_counts.get(c, 0)} |")
    lines.append("")
    lines.append("## Class counts by category")
    lines.append("")
    header = "| category | " + " | ".join(classes) + " | total |"
    lines.append(header)
    lines.append("|---|" + "---|" * (len(classes) + 1))
    for category in sorted(category_class_counts):
        counts = category_class_counts[category]
        total = sum(counts.values())
        row = [category] + [str(counts.get(c, 0)) for c in classes] + [str(total)]
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    lines.append("## Per-block detail")
    lines.append("")
    lines.append("| path | class | covered% | pages |")
    lines.append("|---|---|---|---|")
    for rel_path in sorted(result):
        info = result[rel_path]
        pages_str = ", ".join(
            f"{bp['page']} ({bp['overlap']*100:.0f}%)" for bp in info["best_pages"]
        )
        lines.append(
            f"| {rel_path} | {info['verbatim_class']} | "
            f"{info['covered_fraction']*100:.1f}% | {pages_str} |"
        )

    (WORK / "block_page_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # --- report to stdout ---
    print("=== Overall class counts ===")
    for c in classes:
        print(f"  {c}: {class_counts.get(c, 0)}")

    print("\n=== Class counts by category ===")
    for category in sorted(category_class_counts):
        counts = category_class_counts[category]
        parts = ", ".join(f"{c}={counts.get(c, 0)}" for c in classes)
        print(f"  {category}: {parts}")

    print("\n=== 15 lowest-coverage blocks ===")
    lowest = sorted(result.items(), key=lambda kv: kv[1]["covered_fraction"])[:15]
    for rel_path, info in lowest:
        print(f"  {info['covered_fraction']*100:5.1f}%  {info['verbatim_class']:9s}  {rel_path}")

    if missing_slug_folders:
        print("\n=== Blocks with source slug missing verbatim folder ===")
        for slug in sorted(missing_slug_folders):
            print(f"  slug: {slug!r}")
    else:
        print("\n=== No blocks with missing verbatim slug folders ===")


if __name__ == "__main__":
    main()
