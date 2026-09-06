#!/usr/bin/env python3
"""Validate every content block in wiki/<category>/*.md against schema v2.

Usage:
    python work/lint_blocks.py [--json out.json]

Always exits 0 (this is a report, not a gate). Prints a violation-count table
by rule, then a per-file list of violations.
"""
import sys
import re
import json
import argparse
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
# graphics/ is a catalog format (no per-block frontmatter), not a schema-v2
# block category — intentionally excluded from block validation.

REQUIRED_KEYS = [
    "title", "category", "block-type", "tags", "source", "source-section",
    "source-pages", "verbatim-ref", "pursuit-type", "client-type",
    "client-size", "geography", "rfp-section-type", "win-theme-map",
    "proof-point-ids", "status", "house-favorite", "sanitized",
    "sanitization-loss", "extracted", "last-verified", "context",
    "quality", "reuse-notes",
]

BLOCK_TYPE_ENUM = {"prose", "recipe", "table", "exhibit", "roster"}
STATUS_ENUM = {"preferred", "fallback"}

NARRATIVE_CATEGORIES = {
    "technical-approach", "management-staffing", "win-themes",
    "qualifications", "compliance-plans",
}
CLIENT_NAME_PATTERNS = {
    "hull-wwtf-om-2026": re.compile(r"\b(Hull|Town of Hull)\b"),
    "santamonica-swip-om-2025": re.compile(r"\b(Santa Monica|SWIP)\b"),
}

VERBATIM_REF_RE = re.compile(r"^(?P<file>[^#]+)#¶(?P<n>\d+)$")


def load_frontmatter(text):
    """Return (frontmatter_dict_or_None, body, error_or_None)."""
    if not text.startswith("---"):
        return None, text, "no frontmatter delimiter at start of file"
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None, text, "no frontmatter delimiter at start of file"
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, text, "no closing '---' for frontmatter"
    fm_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1:])
    if not HAVE_YAML:
        return None, body, "pyyaml not available — cannot parse frontmatter"
    try:
        data = yaml.safe_load(fm_text) or {}
    except Exception as e:
        return None, body, f"YAML parse error: {e}"
    return data, body, None


def load_tag_vocab():
    path = ROOT / "vocabulary" / "tags.md"
    if not path.is_file():
        return None
    tags = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*-\s*(\S+)", line)
        if m:
            tags.add(m.group(1))
    return tags


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return v
    return [v]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    if not HAVE_YAML:
        print("WARNING: pyyaml not available — frontmatter cannot be parsed; "
              "all files will fail as unparseable.", file=sys.stderr)

    tag_vocab = load_tag_vocab()
    if tag_vocab is None:
        print("NOTE: vocabulary/tags.md not found — skipping tag-vocabulary check.\n")

    violations = []  # list of dicts: {rule, path, detail}
    files_checked = 0

    def add(rule, path, detail):
        violations.append({"rule": rule, "path": path, "detail": detail})

    for cat in CATEGORY_DIRS:
        cat_dir = ROOT / "wiki" / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob("*.md")):
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            files_checked += 1
            text = path.read_text(encoding="utf-8")
            fm, body, err = load_frontmatter(text)
            if err:
                add("parse-error", rel, err)
                continue

            # 1. required keys present and non-empty
            missing = []
            for key in REQUIRED_KEYS:
                if key not in fm or fm[key] in (None, "", [], {}):
                    missing.append(key)
            if missing:
                add("missing-required-keys", rel, ", ".join(missing))

            # 2. category matches folder
            if fm.get("category") is not None and fm.get("category") != cat:
                add("category-mismatch", rel, f"frontmatter category '{fm.get('category')}' != folder '{cat}'")

            # 3. block-type enum
            bt = fm.get("block-type")
            if bt is not None and bt not in BLOCK_TYPE_ENUM:
                add("block-type-invalid", rel, f"'{bt}' not in {sorted(BLOCK_TYPE_ENUM)}")

            # 4. status enum
            status = fm.get("status")
            if status is not None and status not in STATUS_ENUM:
                add("status-invalid", rel, f"'{status}' not in {sorted(STATUS_ENUM)}")

            # 5. tags subset of vocabulary
            if tag_vocab is not None:
                tags = as_list(fm.get("tags"))
                bad_tags = [t for t in tags if t not in tag_vocab]
                if bad_tags:
                    add("tag-not-in-vocab", rel, ", ".join(bad_tags))

            # 6. verbatim-ref resolves
            refs = as_list(fm.get("verbatim-ref"))
            for ref in refs:
                if not isinstance(ref, str):
                    add("verbatim-ref-malformed", rel, repr(ref))
                    continue
                m = VERBATIM_REF_RE.match(ref)
                if not m:
                    add("verbatim-ref-malformed", rel, ref)
                    continue
                target = ROOT / m.group("file")
                if not target.is_file():
                    add("verbatim-ref-missing-file", rel, ref)
                    continue
                anchor = f"<!-- ¶{m.group('n')} -->"
                target_text = target.read_text(encoding="utf-8")
                if anchor not in target_text:
                    add("verbatim-ref-missing-anchor", rel, ref)

            # 7. recipe blocks must pair with an existing prose block
            if bt == "recipe":
                pairs_with = fm.get("pairs-with")
                if not pairs_with:
                    add("recipe-missing-pairs-with", rel, "no pairs-with key")
                else:
                    target = ROOT / pairs_with if not str(pairs_with).startswith(str(ROOT)) else Path(pairs_with)
                    # pairs-with is documented as a path; try relative to repo root first
                    candidate = ROOT / pairs_with
                    if not candidate.is_file():
                        add("recipe-pairs-with-missing", rel, str(pairs_with))
                    else:
                        target_fm, _, target_err = load_frontmatter(candidate.read_text(encoding="utf-8"))
                        if target_err:
                            add("recipe-pairs-with-unparseable", rel, str(pairs_with))
                        elif target_fm.get("block-type") not in (None, "prose"):
                            add("recipe-pairs-with-not-prose", rel, str(pairs_with))

            # 8. no pursuit client name in body, for narrative categories
            if cat in NARRATIVE_CATEGORIES:
                src = fm.get("source")
                pattern = CLIENT_NAME_PATTERNS.get(src)
                if pattern:
                    hits = sorted(set(pattern.findall(body)))
                    if hits:
                        add("client-name-in-narrative", rel, ", ".join(hits))

            # 9. body has a "## Reuse guidance" section
            if not re.search(r"^##\s+Reuse guidance\s*$", body, re.MULTILINE | re.IGNORECASE):
                add("missing-reuse-guidance-section", rel, "no '## Reuse guidance' heading")

            # 10. no "do not restate" phrase anywhere in body
            if re.search(r"do not restate", body, re.IGNORECASE):
                add("do-not-restate-phrase", rel, "found 'do not restate' language")

    # ---- report ----
    by_rule = {}
    by_file = {}
    for v in violations:
        by_rule.setdefault(v["rule"], 0)
        by_rule[v["rule"]] += 1
        by_file.setdefault(v["path"], []).append(v)

    print(f"Checked {files_checked} blocks across {len(CATEGORY_DIRS)} categories.\n")
    print("Violations by rule:")
    print(f"{'rule':38} count")
    print("-" * 46)
    for rule, count in sorted(by_rule.items(), key=lambda kv: -kv[1]):
        print(f"{rule:38} {count}")
    print(f"\nTotal violations: {len(violations)} across {len(by_file)} files\n")

    print("Per-file violations:")
    for path in sorted(by_file):
        print(f"\n{path}")
        for v in by_file[path]:
            print(f"  - [{v['rule']}] {v['detail']}")

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps({
                "files_checked": files_checked,
                "by_rule": by_rule,
                "violations": violations,
            }, indent=2),
            encoding="utf-8",
        )
        print(f"\nWrote {args.json_out}")

    sys.exit(0)


if __name__ == "__main__":
    main()
