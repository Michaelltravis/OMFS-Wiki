#!/usr/bin/env python3
"""Find candidate duplicate/overlapping content blocks.

Usage:
    python work/dedupe_candidates.py [--min 0.25] [--out work/dedupe_candidates.json]

For every pair of blocks in the SAME category that are either:
  - from DIFFERENT sources, or
  - from the SAME source but whose titles share >= 3 significant words,

compute:
  - body_sim: 6-word-shingle Jaccard similarity on normalized bodies
  - title_sim: token-set Jaccard similarity on titles

Emits every pair with body_sim >= --min OR title_sim >= 0.5, sorted descending
(by body_sim, then title_sim), to --out (JSON) and to
work/dedupe_candidates.md (a table). Read-only — never touches wiki/ content.
"""
import re
import json
import argparse
import itertools
from pathlib import Path

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

ROOT = Path(__file__).resolve().parent.parent

CATEGORY_DIRS = [
    "technical-approach",
    "management-staffing",
    "win-themes",
    "qualifications",
    "compliance-plans",
    "resumes",
    "past-performance",
]

TITLE_STOPWORDS = {
    "a", "an", "the", "of", "for", "and", "in", "on", "to", "with", "is",
    "are", "at", "by", "from", "or", "program", "approach", "plan",
    "framework", "system", "management", "service", "services", "model",
    "overview", "process", "structure",
}

CLIENT_NAME_RE = re.compile(
    r"\[client\]|\bhull\b|\btown of hull\b|\bsanta monica\b|\bswip\b|\bwaterbury\b|"
    r"\bwesterly\b|\bsouthbridge\b",
    re.IGNORECASE,
)
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")
WORD_RE = re.compile(r"[a-z0-9]+")


def load_frontmatter_and_body(text):
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return {}, text
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}, text
    fm_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1:])
    fm = {}
    if HAVE_YAML:
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception:
            fm = {}
    return fm, body


def normalize_body(body):
    text = body.lower()
    text = CLIENT_NAME_RE.sub("cli", text)
    text = NON_ALNUM_RE.sub(" ", text)
    return text.split()


def shingles(words, n=6):
    if len(words) < n:
        return {tuple(words)} if words else set()
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def jaccard(a, b):
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def title_tokens(title):
    words = WORD_RE.findall(title.lower())
    return {w for w in words if w not in TITLE_STOPWORDS and len(w) > 2}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=0.25)
    ap.add_argument("--out", default=str(ROOT / "work" / "dedupe_candidates.json"))
    args = ap.parse_args()

    blocks = []  # dicts with path, category, source, title, words, shingle_set, title_toks
    for cat in CATEGORY_DIRS:
        cat_dir = ROOT / "wiki" / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm, body = load_frontmatter_and_body(text)
            title = fm.get("title") or path.stem
            source = fm.get("source") or ""
            words = normalize_body(body)
            blocks.append({
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "category": cat,
                "source": source,
                "title": title,
                "words": words,
                "shingles": shingles(words),
                "title_toks": title_tokens(str(title)),
            })

    candidates = []
    by_category = {}
    for b in blocks:
        by_category.setdefault(b["category"], []).append(b)

    for cat, items in by_category.items():
        for a, b in itertools.combinations(items, 2):
            different_source = a["source"] != b["source"]
            title_overlap = len(a["title_toks"] & b["title_toks"])
            same_source_title_match = (not different_source) and title_overlap >= 3
            if not (different_source or same_source_title_match):
                continue
            body_sim = jaccard(a["shingles"], b["shingles"])
            title_sim = jaccard(a["title_toks"], b["title_toks"])
            if body_sim >= args.min or title_sim >= 0.5:
                candidates.append({
                    "a": a["path"],
                    "b": b["path"],
                    "body_sim": round(body_sim, 4),
                    "title_sim": round(title_sim, 4),
                    "a_words": len(a["words"]),
                    "b_words": len(b["words"]),
                })

    candidates.sort(key=lambda c: (-c["body_sim"], -c["title_sim"]))

    Path(args.out).write_text(json.dumps(candidates, indent=2), encoding="utf-8")

    md_path = ROOT / "work" / "dedupe_candidates.md"
    lines = [
        "# Dedupe Candidates",
        "",
        f"Generated by `work/dedupe_candidates.py --min {args.min}`. "
        f"{len(candidates)} candidate pair(s) found.",
        "",
        "| body_sim | title_sim | a | b | a_words | b_words |",
        "|---|---|---|---|---|---|",
    ]
    for c in candidates:
        lines.append(
            f"| {c['body_sim']:.4f} | {c['title_sim']:.4f} | {c['a']} | {c['b']} "
            f"| {c['a_words']} | {c['b_words']} |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Compared blocks in {len(by_category)} categories; {len(blocks)} blocks total.")
    print(f"Found {len(candidates)} candidate pair(s) at --min {args.min}.\n")
    print("Top 10:")
    for c in candidates[:10]:
        print(f"  body_sim={c['body_sim']:.3f} title_sim={c['title_sim']:.3f}  {c['a']}  <->  {c['b']}")
    print(f"\nWrote {args.out}")
    print(f"Wrote {md_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
