#!/usr/bin/env python
"""
pdf_to_verbatim.py <pdf> <slug>

Splits a pymupdf4llm page_chunks .md (same basename as the pdf) into per-page
verbatim files with YAML frontmatter, conservative cleanup, paragraph numbering,
and PNG renders of image-only pages. Also writes full.md and manifest.json.

Deterministic, dependency-light: fitz (pymupdf) + pyyaml + stdlib only.
"""
import sys
import os
import re
import json
import collections
from datetime import date

try:
    import yaml
except ImportError:
    yaml = None

import fitz  # pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import text_norm

PAGE_MARKER_RE = re.compile(r'^---\s*Page\s+(\d+)\s*---\s*$', re.MULTILINE)
EXTRACT_DATE = "2026-09-05"
# Pages with a text layer this short are true image-only pages (blank text layer,
# content is a scanned/flattened image). Empirically, true image-only pages in these
# proposals have 0 extracted chars; section-divider pages with a short heading label
# (e.g. "Resumes\nAppendix A", 19 chars) still have real, complete text and should NOT
# be flagged for vision transcription. Threshold set well below that natural gap.
IMAGE_ONLY_CHAR_THRESHOLD = 5

# --- backfill (default ON): recover raw text-layer blocks that the converter
# dropped or badly mangled. A block is a candidate for recovery when its 6-word
# shingles are mostly absent from the converter markdown (order-based signal:
# catches drops/heavy reflow) AND a good fraction of its individual words are
# also absent as a bag-of-words (content-based signal: guards against flagging
# a block that is simply reflowed/reordered elsewhere on the same page, e.g. a
# table whose cells the converter re-ordered but did not drop).
BACKFILL_MIN_BLOCK_WORDS = 6
BACKFILL_SHINGLE_MATCH_THRESHOLD = 0.5   # below this fraction of matched shingles -> candidate
BACKFILL_WORD_MISSING_THRESHOLD = 0.3    # and at least this fraction of words truly absent


def get_reading_order_blocks(page):
    """Return raw text blocks (type 0 = text) from the page in top-to-bottom,
    left-to-right reading order, as a list of raw block text strings."""
    raw = page.get_text("blocks")
    text_blocks = [b for b in raw if len(b) >= 7 and b[6] == 0 and b[4].strip()]
    text_blocks.sort(key=lambda b: (round(b[1] / 5) * 5, b[0]))
    return [b[4] for b in text_blocks]


def filter_block_text(block_text, repeating_norms):
    """Strip running header/footer lines out of a raw block's text before it is
    considered for backfill, so a boilerplate block (e.g. the running
    'CONFIDENTIAL | ... | SP2456 | 20' footer, already intentionally removed from the
    cleaned body) is never re-inserted as 'recovered' text.

    Deliberately does NOT apply is_page_number_only_line here: that check is meant
    for whole-page cleanup where a lone digit line at the page bottom is a footer
    page number, but inside individual raw blocks a bare number is just as likely
    to be real content (e.g. a chart's axis year/value labels, each its own
    single-token block) — stripping it there silently destroyed those labels."""
    lines = block_text.split('\n')
    kept = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        norm = normalize_line_for_repeat_detection(s)
        if len(s) <= 90 and norm in repeating_norms:
            continue
        kept.append(s)
    return '\n'.join(kept)


def group_blocks_for_backfill(filtered_block_texts):
    """Raw blocks that are individually too short to evaluate (e.g. a chart's
    axis/data labels, or a multi-line pull-quote that PyMuPDF splits one line per
    block) are merged with their immediate neighbors, in reading order, until the
    running group reaches BACKFILL_MIN_BLOCK_WORDS words. A block that already
    meets the threshold on its own is kept as its own group and does not absorb
    neighbors. Returns a list of group strings (each a '\\n'-joined run of
    consecutive raw blocks) in original reading order."""
    groups = []
    buffer = []

    def flush():
        if buffer:
            groups.append('\n'.join(buffer))
            buffer.clear()

    for text in filtered_block_texts:
        if not text.strip():
            continue
        wc = len(text_norm.words(text))
        if wc >= BACKFILL_MIN_BLOCK_WORDS:
            flush()
            groups.append(text)
        else:
            buffer.append(text)
    flush()
    return groups


def find_recoverable_blocks(block_texts, cleaned_body, repeating_norms):
    """Given raw reading-order block texts and the cleaned (pre-numbering, header/
    footer-stripped) page body, return (recovered_group_texts, recovered_word_count).
    Short adjacent blocks (chart labels, wrapped pull-quote lines) are grouped so they
    can clear the word-count floor together; boilerplate lines are filtered out first
    so a stripped running header/footer is never recovered as 'new' content."""
    filtered = [filter_block_text(b, repeating_norms) for b in block_texts]
    groups = group_blocks_for_backfill(filtered)

    body_words = text_norm.words(cleaned_body)
    body_word_set = set(body_words)
    body_shingle_set = set(text_norm.shingles(body_words, BACKFILL_MIN_BLOCK_WORDS))

    recovered = []
    recovered_words = 0
    for group_text in groups:
        group_words = text_norm.words(group_text)
        if len(group_words) < BACKFILL_MIN_BLOCK_WORDS:
            continue  # still short even after grouping with neighbors
        group_shingles = text_norm.shingles(group_words, BACKFILL_MIN_BLOCK_WORDS)
        if group_shingles:
            match_frac = sum(1 for s in group_shingles if s in body_shingle_set) / len(group_shingles)
        else:
            match_frac = 1.0
        if match_frac >= BACKFILL_SHINGLE_MATCH_THRESHOLD:
            continue  # present/well-ordered already
        missing_words = [w for w in group_words if w not in body_word_set]
        missing_frac = len(missing_words) / len(group_words)
        if missing_frac < BACKFILL_WORD_MISSING_THRESHOLD:
            continue  # words all present elsewhere on the page -> reflow, not a drop
        recovered.append(group_text.strip())
        recovered_words += len(group_words)
    return recovered, recovered_words


def find_md_path(pdf_path):
    base, _ = os.path.splitext(pdf_path)
    md_path = base + ".md"
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Expected converter markdown at {md_path}")
    return md_path


def split_pages(md_text):
    """Split md_text by '--- Page N ---' markers. Returns dict {page_num: body_text}."""
    matches = list(PAGE_MARKER_RE.finditer(md_text))
    pages = {}
    for i, m in enumerate(matches):
        pno = int(m.group(1))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        pages[pno] = md_text[start:end]
    return pages


def build_outline_map(doc):
    """Return sorted list of (page_index_0based, title) from the PDF outline (toc level 1 only kept,
    but we keep all levels and just pick nearest preceding by page number)."""
    toc = doc.get_toc()  # list of [level, title, page(1-based)]
    entries = []
    for level, title, pageno in toc:
        entries.append((pageno - 1, title))
    entries.sort(key=lambda x: x[0])
    return entries


def section_for_page(outline_entries, page_index_0based):
    section = ""
    for pidx, title in outline_entries:
        if pidx <= page_index_0based:
            section = title
        else:
            break
    return section


def normalize_line_for_repeat_detection(line):
    s = line.strip()
    s = re.sub(r'\d+', '#', s)  # collapse numbers so "Page 3" and "Page 4" match
    s = re.sub(r'\s+', ' ', s)
    return s


def is_page_number_only_line(line):
    s = line.strip()
    if not s:
        return False
    # plain number, or "Page N", "Page N of M", "- N -", "N of M"
    if re.fullmatch(r'\d+', s):
        return True
    if re.fullmatch(r'[-–—]\s*\d+\s*[-–—]', s):
        return True
    if re.fullmatch(r'(?i)page\s+\d+(\s+of\s+\d+)?', s):
        return True
    if re.fullmatch(r'\d+\s+of\s+\d+', s):
        return True
    return False


MOJIBAKE_RE = re.compile(r'(?<=[A-Za-z])�(?=[A-Za-z])')


def normalize_mojibake(text):
    # U+FFFD between letters -> apostrophe (e.g. Jacob<FFFD>s -> Jacob's)
    return MOJIBAKE_RE.sub("'", text)


def collapse_blank_lines(text):
    return re.sub(r'\n{3,}', '\n\n', text)


def detect_repeating_lines(page_bodies_by_page):
    """Detect lines (normalized) that repeat verbatim (post-normalization) on >=30% of pages.
    Only considers short lines (likely headers/footers), not body paragraphs."""
    n_pages = len(page_bodies_by_page)
    if n_pages == 0:
        return set()
    counts = collections.Counter()
    for pno, body in page_bodies_by_page.items():
        seen_this_page = set()
        for line in body.splitlines():
            s = line.strip()
            if not s:
                continue
            if len(s) > 90:  # not a header/footer candidate
                continue
            norm = normalize_line_for_repeat_detection(s)
            if norm and norm not in seen_this_page:
                seen_this_page.add(norm)
        for norm in seen_this_page:
            counts[norm] += 1
    threshold = max(2, int(0.30 * n_pages))
    repeating = {norm for norm, c in counts.items() if c >= threshold}
    return repeating


def clean_page_body(body, repeating_norms):
    lines = body.split('\n')
    out_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            out_lines.append(line)
            continue
        if is_page_number_only_line(stripped):
            continue
        norm = normalize_line_for_repeat_detection(stripped)
        if len(stripped) <= 90 and norm in repeating_norms:
            continue
        out_lines.append(line)
    text = '\n'.join(out_lines)
    text = normalize_mojibake(text)
    text = collapse_blank_lines(text)
    return text.strip('\n')


def number_paragraphs(text, start_n=0):
    """Split on blank-line-separated blocks; prefix each with an HTML comment <!-- pN -->.
    Numbering continues from start_n so recovered blocks can follow normal ones."""
    if not text.strip():
        return text, start_n
    blocks = re.split(r'\n\s*\n', text.strip('\n'))
    numbered = []
    n = start_n
    for block in blocks:
        if not block.strip():
            continue
        n += 1
        numbered.append(f"<!-- ¶{n} -->\n{block.strip()}")
    return '\n\n'.join(numbered), n


def frontmatter_str(fm_dict):
    if yaml is not None:
        return "---\n" + yaml.safe_dump(fm_dict, sort_keys=False, allow_unicode=True) + "---\n"
    # manual fallback
    lines = ["---"]
    for k, v in fm_dict.items():
        if isinstance(v, bool):
            v = "true" if v else "false"
        if isinstance(v, str) and (':' in v or v == ''):
            v = f'"{v}"'
        lines.append(f"{k}: {v}")
    lines.append("---")
    return '\n'.join(lines) + "\n"


def main():
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_verbatim.py <pdf> <slug>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    slug = sys.argv[2]

    md_path = find_md_path(pdf_path)
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    pages_md = split_pages(md_text)

    doc = fitz.open(pdf_path)
    n_pages = doc.page_count
    outline_entries = build_outline_map(doc)
    if not outline_entries:
        print(f"WARNING: no outline/bookmarks found in {pdf_path}; section will be blank for all pages")

    out_root = os.path.join("verbatim", slug)
    pages_dir = os.path.join(out_root, "pages")
    renders_dir = os.path.join(out_root, "renders")
    vision_dir = os.path.join(out_root, "vision")
    os.makedirs(pages_dir, exist_ok=True)
    os.makedirs(renders_dir, exist_ok=True)

    # Pass 1: gather raw bodies (pre-clean) per page for repeat-line detection
    raw_bodies = {}
    page_meta_pre = {}
    for pno in range(1, n_pages + 1):
        body = pages_md.get(pno, "")
        raw_bodies[pno] = body
        page = doc[pno - 1]
        text_layer = page.get_text("text")
        chars_text_layer = len(text_layer)
        images = page.get_images()
        image_only = chars_text_layer < IMAGE_ONLY_CHAR_THRESHOLD
        page_meta_pre[pno] = {
            "chars_text_layer": chars_text_layer,
            "image_only": image_only,
            "images": len(images),
        }
        if pno not in pages_md:
            print(f"WARNING: page {pno} missing from converter markdown ({md_path})")

    repeating_norms = detect_repeating_lines(raw_bodies)

    manifest_pages = []
    image_only_pages = []

    full_md_parts = []

    for pno in range(1, n_pages + 1):
        meta = page_meta_pre[pno]
        section = section_for_page(outline_entries, pno - 1)
        raw_body = raw_bodies.get(pno, "")

        vision_agreement_pct = None
        vision_verdict = None

        if meta["image_only"]:
            image_only_pages.append(pno)
            # render page to png at 300 dpi (kept even when a vision transcript exists,
            # so the render is always available for re-review)
            page = doc[pno - 1]
            zoom = 300 / 72
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            render_path = os.path.join(renders_dir, f"p{pno:04d}.png")
            pix.save(render_path)
            recovered_blocks_count = 0
            recovered_words_count = 0

            vision_path = os.path.join(vision_dir, f"p{pno:04d}.json")
            if os.path.exists(vision_path):
                with open(vision_path, 'r', encoding='utf-8') as f:
                    vision_data = json.load(f)
                final_markdown = vision_data.get("final_markdown", "") or ""
                vision_agreement_pct = vision_data.get("agreement_pct")
                vision_verdict = vision_data.get("verdict")
                cleaned = final_markdown.strip()
                body_numbered, n_paras = number_paragraphs(cleaned)
                numbered_body = (
                    "<!-- transcribed from image by dual vision + verifier -->\n\n"
                    + body_numbered
                )
                method = "vision"
            else:
                cleaned = ""
                numbered_body = "[IMAGE-ONLY PAGE — requires vision transcription]"
                n_paras = 0
                method = "image-only"
        else:
            cleaned = clean_page_body(raw_body, repeating_norms)
            numbered_body, n_paras = number_paragraphs(cleaned)
            method = "text"

            page = doc[pno - 1]
            raw_blocks = get_reading_order_blocks(page)
            recovered, recovered_words_count = find_recoverable_blocks(raw_blocks, cleaned, repeating_norms)
            recovered_blocks_count = len(recovered)
            if recovered:
                recovered_body, n_paras = number_paragraphs(
                    '\n\n'.join(recovered), start_n=n_paras
                )
                numbered_body = (
                    numbered_body.rstrip('\n')
                    + "\n\n<!-- recovered from text layer -->\n\n"
                    + recovered_body
                )

        fm = {
            "slug": slug,
            "page": pno,
            "section": section,
            "method": method,
            "chars_text_layer": meta["chars_text_layer"],
            "chars_markdown": len(cleaned),
            "image_only": meta["image_only"],
            "images": meta["images"],
            "paragraphs": n_paras,
            "recovered_blocks": recovered_blocks_count,
            "recovered_words": recovered_words_count,
            "extracted": EXTRACT_DATE,
        }
        if vision_agreement_pct is not None:
            fm["vision_agreement_pct"] = vision_agreement_pct
        if vision_verdict is not None:
            fm["vision_verdict"] = vision_verdict

        fm_text = frontmatter_str(fm)
        page_file_content = fm_text + "\n" + numbered_body + "\n"
        page_path = os.path.join(pages_dir, f"p{pno:04d}.md")
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_file_content)

        manifest_pages.append(fm)
        full_md_parts.append(f"## Page {pno}\n\n{numbered_body}\n")

    full_md_path = os.path.join(out_root, "full.md")
    with open(full_md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_md_parts))

    manifest = {
        "pdf": pdf_path,
        "slug": slug,
        "page_count": n_pages,
        "outline": [{"page": p + 1, "title": t} for p, t in outline_entries],
        "image_only_pages": image_only_pages,
        "pages": manifest_pages,
    }
    manifest_path = os.path.join(out_root, "manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"[{slug}] pages: {n_pages}  image-only: {image_only_pages}")
    print(f"[{slug}] repeating header/footer lines detected: {len(repeating_norms)}")
    print(f"[{slug}] wrote {pages_dir}, {full_md_path}, {manifest_path}")


if __name__ == "__main__":
    main()
