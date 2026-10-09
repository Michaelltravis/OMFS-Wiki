#!/usr/bin/env python3
"""Find candidate duplicate/overlapping content blocks.

Usage:
    python work/dedupe_candidates.py [--min 0.25] [--out work/dedupe_candidates.json]
                                     [--skip-linked] [--exclude-archived]
                                     [--new-only <slug>] [--decided work/curation/log.jsonl]

For every pair of blocks in the SAME category that are either:
  - from DIFFERENT sources, or
  - from the SAME source but whose titles share >= 3 significant words,

compute:
  - body_sim: 6-word-shingle Jaccard similarity on normalized bodies
  - title_sim: token-set Jaccard similarity on titles

Emits every pair with body_sim >= --min OR title_sim >= 0.5, sorted descending
(by body_sim, then title_sim), to --out (JSON) and to
work/dedupe_candidates.md (a table). Read-only — never touches wiki/ content.

Curation filters:
  --skip-linked       drop pairs already joined by supersedes / superseded-by / pairs-with
  --exclude-archived  ignore blocks with status: archived
  --new-only <slug>   keep only pairs where at least one side comes from <slug>
                      (the ingest hook: reconcile a newly extracted source against the bank)
  --decided <log>     drop pairs with a recorded pair decision in work/curation/log.jsonl
                      (actions distinct / supersede / ingest-merge with path + to set)

`load_blocks()` and `find_pairs()` are importable (work/freshness.py reuses them).
"""
import re
import json
import argparse
import itertools
import sys
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

PAIR_DECISION_ACTIONS = {"distinct", "supersede", "ingest-merge", "supersede-with", "merge-into"}


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


def _as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _norm_link(v):
    """A supersedes/superseded-by/pairs-with value as a repo-relative path when it
    already is one, else the bare stem (so bare-filename links still match)."""
    s = str(v).replace("\\", "/").strip()
    return s if s.startswith("wiki/") else Path(s).stem


def load_blocks(exclude_archived=False):
    """Every block with the fields the pair finder and freshness need."""
    blocks = []
    for cat in CATEGORY_DIRS:
        cat_dir = ROOT / "wiki" / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm, body = load_frontmatter_and_body(text)
            if exclude_archived and fm.get("status") == "archived":
                continue
            title = fm.get("title") or path.stem
            words = normalize_body(body)
            links = set()
            for key in ("supersedes", "superseded-by", "pairs-with"):
                for v in _as_list(fm.get(key)):
                    links.add(_norm_link(v))
            blocks.append({
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "stem": path.stem,
                "category": cat,
                "source": fm.get("source") or "",
                "title": title,
                "status": fm.get("status"),
                "links": links,
                "words": words,
                "shingles": shingles(words),
                "title_toks": title_tokens(str(title)),
            })
    return blocks


def load_decided_pairs(log_path):
    """frozenset({a, b}) for every pair decision recorded in a curation log."""
    decided = set()
    p = Path(log_path)
    if not p.is_file():
        return decided
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except Exception:
            continue
        if row.get("action") in PAIR_DECISION_ACTIONS and row.get("path") and row.get("to"):
            decided.add(frozenset((str(row["path"]).replace("\\", "/"), str(row["to"]).replace("\\", "/"))))
    return decided


def _linked(a, b):
    return (b["path"] in a["links"] or b["stem"] in a["links"]
            or a["path"] in b["links"] or a["stem"] in b["links"])


def find_pairs(blocks, min_body=0.25, skip_linked=False, new_only=None, decided=None):
    """Candidate duplicate pairs across `blocks` (from load_blocks)."""
    decided = decided or set()
    candidates = []
    by_category = {}
    for b in blocks:
        by_category.setdefault(b["category"], []).append(b)

    for cat, items in by_category.items():
        for a, b in itertools.combinations(items, 2):
            if new_only and new_only not in (a["source"], b["source"]):
                continue
            different_source = a["source"] != b["source"]
            title_overlap = len(a["title_toks"] & b["title_toks"])
            same_source_title_match = (not different_source) and title_overlap >= 3
            if not (different_source or same_source_title_match):
                continue
            if skip_linked and _linked(a, b):
                continue
            if decided and frozenset((a["path"], b["path"])) in decided:
                continue
            body_sim = jaccard(a["shingles"], b["shingles"])
            title_sim = jaccard(a["title_toks"], b["title_toks"])
            if body_sim >= min_body or title_sim >= 0.5:
                candidates.append({
                    "a": a["path"],
                    "b": b["path"],
                    "a_source": a["source"],
                    "b_source": b["source"],
                    "a_status": a["status"],
                    "b_status": b["status"],
                    "body_sim": round(body_sim, 4),
                    "title_sim": round(title_sim, 4),
                    "a_words": len(a["words"]),
                    "b_words": len(b["words"]),
                })

    candidates.sort(key=lambda c: (-c["body_sim"], -c["title_sim"]))
    return candidates


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=0.25)
    ap.add_argument("--out", default=str(ROOT / "work" / "dedupe_candidates.json"))
    ap.add_argument("--skip-linked", action="store_true")
    ap.add_argument("--exclude-archived", action="store_true")
    ap.add_argument("--new-only", default=None, metavar="SLUG")
    ap.add_argument("--decided", default=None, metavar="LOG_JSONL")
    args = ap.parse_args()

    if not HAVE_YAML:
        print("ERROR: pyyaml not available — cannot parse frontmatter. Run: python -m pip install pyyaml",
              file=sys.stderr)
        sys.exit(1)

    blocks = load_blocks(exclude_archived=args.exclude_archived)
    decided = load_decided_pairs(args.decided) if args.decided else set()
    candidates = find_pairs(blocks, min_body=args.min, skip_linked=args.skip_linked,
                            new_only=args.new_only, decided=decided)

    Path(args.out).write_text(json.dumps(candidates, indent=2), encoding="utf-8")

    filters = []
    if args.skip_linked:
        filters.append("--skip-linked")
    if args.exclude_archived:
        filters.append("--exclude-archived")
    if args.new_only:
        filters.append(f"--new-only {args.new_only}")
    if args.decided:
        filters.append(f"--decided {args.decided}")

    md_path = ROOT / "work" / "dedupe_candidates.md"
    lines = [
        "# Dedupe Candidates",
        "",
        f"Generated by `work/dedupe_candidates.py --min {args.min}{(' ' + ' '.join(filters)) if filters else ''}`. "
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

    cats = {b["category"] for b in blocks}
    print(f"Compared blocks in {len(cats)} categories; {len(blocks)} blocks total.")
    print(f"Found {len(candidates)} candidate pair(s) at --min {args.min}"
          f"{(' with ' + ', '.join(filters)) if filters else ''}.\n")
    print("Top 10:")
    for c in candidates[:10]:
        print(f"  body_sim={c['body_sim']:.3f} title_sim={c['title_sim']:.3f}  {c['a']}  <->  {c['b']}")
    print(f"\nWrote {args.out}")
    print(f"Wrote {md_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
