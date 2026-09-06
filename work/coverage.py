#!/usr/bin/env python
"""
coverage.py <pdf> <slug> [--threshold 0.99]

Compares each page's raw fitz text layer against the cleaned/numbered verbatim
page body (produced by pdf_to_verbatim.py, including any backfilled/recovered
blocks) using two complementary metrics:

  word_recall     = fraction of raw text-layer word tokens (multiset, after
                    header/footer removal) present in the verbatim page body
                    (multiset-aware: a word repeated N times in the raw layer
                    must appear at least N times in the verbatim body to count
                    fully covered). This is the PRIMARY gate.
  shingle_coverage = fraction of raw 8-word shingles present in the verbatim
                    page (secondary, order-sensitive signal)
  extra           = fraction of verbatim 8-word shingles NOT found in raw
                    (flags hallucinated/misplaced text)
  order           = LCS-over-shingle-index-sequence / n (approximate order
                    preservation)

A page is flagged when word_recall < 0.99 OR the longest contiguous run of
raw words missing from the verbatim body is >= 15 words.

Writes verbatim/<slug>/coverage.md and coverage.json. Always exits 0.
"""
import sys
import os
import re
import json
import collections

import fitz  # pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import text_norm

DEFAULT_THRESHOLD = 0.99
LONGEST_MISSING_RUN_FLAG = 15

NUM_RE = re.compile(r'\d+')


def normalize_line_for_repeat_detection(line):
    s = line.strip()
    s = NUM_RE.sub('#', s)
    s = re.sub(r'\s+', ' ', s)
    return s


def is_page_number_only_line(line):
    s = line.strip()
    if not s:
        return False
    if re.fullmatch(r'\d+', s):
        return True
    if re.fullmatch(r'[-‑–—]\s*\d+\s*[-‑–—]', s):
        return True
    if re.fullmatch(r'(?i)page\s+\d+(\s+of\s+\d+)?', s):
        return True
    if re.fullmatch(r'\d+\s+of\s+\d+', s):
        return True
    return False


RUNNING_TITLE_WITH_PAGENO_RE = re.compile(
    r'^(.{0,120}?\|.{0,120}?\|.{0,80}?)\s*\|?\s*#+\s*$'
)


def detect_repeating_lines(raw_texts_by_page):
    """Same algorithm as pdf_to_verbatim.py's detect_repeating_lines, applied here to
    the PDF's raw fitz text-layer lines (not the converter markdown) so coverage.py's
    header/footer stripping matches what was already stripped from the verbatim body."""
    n_pages = len(raw_texts_by_page)
    if n_pages == 0:
        return set()
    counts = collections.Counter()
    for pno, raw_text in raw_texts_by_page.items():
        seen_this_page = set()
        for line in raw_text.splitlines():
            s = line.strip()
            if not s or len(s) > 90:
                continue
            norm = normalize_line_for_repeat_detection(s)
            if norm and norm not in seen_this_page:
                seen_this_page.add(norm)
        for norm in seen_this_page:
            counts[norm] += 1
    threshold = max(2, int(0.30 * n_pages))
    return {norm for norm, c in counts.items() if c >= threshold}


def strip_header_footer_lines(raw_text, repeating_norms):
    """Remove running header/footer lines (detected as repeating across >=30% of
    pages, digits normalized to '#') and bare page-number lines from a raw
    text-layer string, plus any line matching a running-title-with-trailing-page-
    number shape (e.g. 'CONFIDENTIAL | CITY OF SANTA MONICA | SWIP RFP (SP2456) | 12')
    even if its exact normalized form didn't clear the repeat threshold."""
    out_lines = []
    for line in raw_text.splitlines():
        s = line.strip()
        if not s:
            out_lines.append(line)
            continue
        if is_page_number_only_line(s):
            continue
        norm = normalize_line_for_repeat_detection(s)
        if len(s) <= 90 and norm in repeating_norms:
            continue
        if len(s) <= 140 and s.count('|') >= 2 and re.search(r'\d+\s*$', s):
            continue
        out_lines.append(line)
    return '
'.join(out_lines)



def shingles(word_list, k=8):
    return text_norm.shingles(word_list, k)


def word_recall(raw_words, verb_words):
    """Multiset recall: fraction of raw word tokens matched against the verbatim
    body's word multiset (each verbatim occurrence can satisfy at most one raw
    occurrence)."""
    if not raw_words:
        return 1.0
    verb_counts = collections.Counter(verb_words)
    matched = 0
    for w in raw_words:
        if verb_counts[w] > 0:
            matched += 1
            verb_counts[w] -= 1
    return matched / len(raw_words)


def lcs_length_index_sequence(seq):
    """Longest increasing subsequence of the index-mapping list (approximates
    order preservation of raw shingles inside the verbatim page)."""
    if not seq:
        return 0
    import bisect
    tails = []
    for x in seq:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def longest_missing_run(raw_words, verbatim_word_multiset):
    """Longest contiguous run of raw words not consumable from the verbatim
    word multiset (multiset-aware, so a word already 'used' earlier in the run
    can't cover a second occurrence)."""
    avail = collections.Counter(verbatim_word_multiset)
    best_start, best_len = -1, 0
    cur_start, cur_len = -1, 0
    # Two-pass: first determine which positions are "missing" using a fresh
    # multiset per evaluation window is expensive; approximate by first
    # computing global availability, consuming greedily in raw order.
    consumed = collections.Counter()
    missing_flags = []
    for w in raw_words:
        if avail[w] - consumed[w] > 0:
            consumed[w] += 1
            missing_flags.append(False)
        else:
            missing_flags.append(True)
    for i, missing in enumerate(missing_flags):
        if missing:
            if cur_len == 0:
                cur_start = i
            cur_len += 1
            if cur_len > best_len:
                best_len = cur_len
                best_start = cur_start
        else:
            cur_len = 0
    if best_start < 0:
        return 0, ""
    sample = ' '.join(raw_words[best_start:best_start + 12])
    return best_len, sample


def main():
    if len(sys.argv) < 3:
        print("Usage: python coverage.py <pdf> <slug> [--threshold 0.99]")
        sys.exit(1)
    pdf_path = sys.argv[1]
    slug = sys.argv[2]
    threshold = DEFAULT_THRESHOLD
    if "--threshold" in sys.argv:
        idx = sys.argv.index("--threshold")
        threshold = float(sys.argv[idx + 1])

    out_root = os.path.join("verbatim", slug)
    pages_dir = os.path.join(out_root, "pages")
    manifest_path = os.path.join(out_root, "manifest.json")

    if not os.path.exists(manifest_path):
        print(f"ERROR: manifest not found at {manifest_path}. Run pdf_to_verbatim.py first.")
        sys.exit(0)

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    doc = fitz.open(pdf_path)
    n_pages = doc.page_count

    per_page = []
    image_only_pages = set(manifest.get("image_only_pages", []))

    total_recovered_blocks = 0
    total_recovered_words = 0
    vision_pages = {}  # pno -> {agreement_pct, verdict}
    for pmeta in manifest.get("pages", []):
        total_recovered_blocks += pmeta.get("recovered_blocks", 0) or 0
        total_recovered_words += pmeta.get("recovered_words", 0) or 0
        if pmeta.get("method") == "vision":
            vision_pages[pmeta["page"]] = {
                "agreement_pct": pmeta.get("vision_agreement_pct"),
                "verdict": pmeta.get("vision_verdict"),
            }

    # Detect running header/footer lines on the RAW text layer (same 30%-of-pages
    # algorithm pdf_to_verbatim.py uses on the converter markdown) so coverage.py
    # strips the same boilerplate from the raw side before scoring recall, instead
    # of counting a page's own running header/footer as "missing" content.
    raw_texts_by_page = {}
    for pno in range(1, n_pages + 1):
        if pno in vision_pages or pno in image_only_pages:
            continue
        raw_texts_by_page[pno] = doc[pno - 1].get_text("text")
    repeating_norms = detect_repeating_lines(raw_texts_by_page)

    for pno in range(1, n_pages + 1):
        if pno in vision_pages:
            per_page.append({
                "page": pno, "image_only": True, "vision": True,
                "vision_agreement_pct": vision_pages[pno]["agreement_pct"],
                "vision_verdict": vision_pages[pno]["verdict"],
                "word_recall": None, "shingle_coverage": None, "extra": None, "order": None,
                "longest_missing_run_words": None, "missing_sample": "",
                "flagged": False,
            })
            continue
        if pno in image_only_pages:
            per_page.append({
                "page": pno, "image_only": True,
                "word_recall": None, "shingle_coverage": None, "extra": None, "order": None,
                "longest_missing_run_words": None, "missing_sample": "",
                "flagged": False,
            })
            continue

        page = doc[pno - 1]
        raw_text = page.get_text("text")
        raw_words = text_norm.words(raw_text)

        page_path = os.path.join(pages_dir, f"p{pno:04d}.md")
        if not os.path.exists(page_path):
            per_page.append({
                "page": pno, "image_only": False,
                "word_recall": 0.0, "shingle_coverage": 0.0, "extra": 0.0, "order": 0.0,
                "longest_missing_run_words": len(raw_words), "missing_sample": "MISSING VERBATIM PAGE FILE",
                "flagged": True,
            })
            continue
        with open(page_path, 'r', encoding='utf-8') as f:
            page_file_text = f.read()
        verbatim_body = text_norm.strip_page_file(page_file_text)
        verbatim_words = text_norm.words(verbatim_body)

        wr = word_recall(raw_words, verbatim_words)
        run_len, run_sample = longest_missing_run(raw_words, verbatim_words)

        raw_shingles = shingles(raw_words, 8)
        verb_shingles = shingles(verbatim_words, 8)
        verb_shingle_index = {}
        for i, s in enumerate(verb_shingles):
            verb_shingle_index.setdefault(s, []).append(i)

        if not raw_shingles:
            shingle_cov = wr  # short page fallback: reuse word-level recall
            order = 1.0
        else:
            found_count = 0
            index_seq = []
            for s in raw_shingles:
                if s in verb_shingle_index:
                    found_count += 1
                    index_seq.append(verb_shingle_index[s][0])
            shingle_cov = found_count / len(raw_shingles)
            order = lcs_length_index_sequence(index_seq) / len(raw_shingles) if index_seq else 0.0

        if not verb_shingles:
            extra = 0.0
        else:
            raw_shingle_set = set(raw_shingles)
            extra_count = sum(1 for s in verb_shingles if s not in raw_shingle_set)
            extra = extra_count / len(verb_shingles)

        flagged = (wr < threshold) or (run_len >= LONGEST_MISSING_RUN_FLAG)

        per_page.append({
            "page": pno, "image_only": False,
            "word_recall": round(wr, 4),
            "shingle_coverage": round(shingle_cov, 4),
            "extra": round(extra, 4),
            "order": round(order, 4),
            "longest_missing_run_words": run_len,
            "missing_sample": run_sample if flagged else "",
            "flagged": flagged,
        })

    text_pages = [p for p in per_page if not p["image_only"]]
    mean_word_recall = sum(p["word_recall"] for p in text_pages) / len(text_pages) if text_pages else 0.0
    mean_shingle_cov = sum(p["shingle_coverage"] for p in text_pages) / len(text_pages) if text_pages else 0.0
    flagged_pages = [p for p in text_pages if p["flagged"]]

    result = {
        "slug": slug,
        "pdf": pdf_path,
        "threshold": threshold,
        "longest_missing_run_flag": LONGEST_MISSING_RUN_FLAG,
        "page_count": n_pages,
        "image_only_pages": sorted(image_only_pages),
        "text_pages": len(text_pages),
        "mean_word_recall": round(mean_word_recall, 4),
        "mean_shingle_coverage": round(mean_shingle_cov, 4),
        "pages_flagged": len(flagged_pages),
        "total_recovered_blocks": total_recovered_blocks,
        "total_recovered_words": total_recovered_words,
        "vision_pages": sorted(vision_pages.keys()),
        "per_page": per_page,
    }

    json_path = os.path.join(out_root, "coverage.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    md_lines = []
    md_lines.append(f"# Coverage report — {slug}\n")
    md_lines.append("## Summary\n")
    md_lines.append("| pages | text pages | image-only pages | mean word_recall | mean shingle_coverage | flagged pages | recovered blocks | recovered words |")
    md_lines.append("|---|---|---|---|---|---|---|---|")
    md_lines.append(
        f"| {n_pages} | {len(text_pages)} | {len(image_only_pages)} "
        f"| {mean_word_recall:.4f} | {mean_shingle_cov:.4f} | {len(flagged_pages)} "
        f"(gate: word_recall<{threshold} OR longest_missing_run>={LONGEST_MISSING_RUN_FLAG}) "
        f"| {total_recovered_blocks} | {total_recovered_words} |"
    )
    md_lines.append("")
    if image_only_pages:
        md_lines.append(f"Image-only pages: {sorted(image_only_pages)}\n")

    if vision_pages:
        md_lines.append("## Vision-transcribed pages\n")
        md_lines.append("| page | agreement_pct | verdict |")
        md_lines.append("|---|---|---|")
        for pno in sorted(vision_pages.keys()):
            v = vision_pages[pno]
            md_lines.append(f"| {pno} | {v['agreement_pct']} | {v['verdict']} |")
        md_lines.append("")

    if flagged_pages:
        md_lines.append("## Flagged pages\n")
        md_lines.append("| page | word_recall | shingle_coverage | extra | order | longest_missing_run | missing sample (~12 words) |")
        md_lines.append("|---|---|---|---|---|---|---|")
        for p in sorted(flagged_pages, key=lambda x: x["page"]):
            md_lines.append(
                f"| {p['page']} | {p['word_recall']:.4f} | {p['shingle_coverage']:.4f} | {p['extra']:.4f} "
                f"| {p['order']:.4f} | {p['longest_missing_run_words']} | {p['missing_sample']} |"
            )
    else:
        md_lines.append("All text pages meet the word_recall / longest-missing-run gate.\n")

    md_path = os.path.join(out_root, "coverage.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join