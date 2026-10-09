#!/usr/bin/env python3
"""Validate every content block in wiki/<category>/*.md against schema v2.

Usage:
    python work/lint_blocks.py [--json out.json] [--today YYYY-MM-DD] [--strict]

Exits 0 by default (this is a report, not a gate); --strict exits 1 when any
structural rule fires (everything except the report-only rules
client-name-in-narrative and review-overdue). Prints a violation-count table
by rule, then a per-file list of violations.

Lifecycle rules (added with the curation layer, see CLAUDE.md "Keeping the bank
current"): supersedes / superseded-by / pairs-with links must be
wiki/<category>/<file>.md paths that resolve and are reciprocal; status must
agree with the links (preferred blocks carry no superseded-by, fallback blocks
name their winner, archived blocks carry archive-reason + archived-date);
dates are bare ISO; volatility / freshness-flags use the enums; review-overdue
is report-only and needs --today (defaults to the real date).
"""
import sys
import re
import json
import argparse
import datetime as _dt
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
    "quality", "reuse-notes", "section-id", "section-path", "section-order", "doc-order",
]

BLOCK_TYPE_ENUM = {"prose", "recipe", "table", "exhibit", "roster"}
STATUS_ENUM = {"preferred", "fallback", "archived"}
VOLATILITY_ENUM = {"people", "reference", "corporate-figure", "safety-stat", "regulatory",
                   "project-outcome", "evergreen"}
FLAG_ENUM = {"open-ended-date", "divergent-figure", "newer-source-same-claim", "newer-year-available", "unresolved-conflict",
             "person-duplicate", "dead-link", "link-nonreciprocal", "link-format", "status-link-mismatch",
             "stale-contact", "feedback"}
LINK_KEYS = ("supersedes", "superseded-by", "pairs-with")
LINK_PATH_RE = re.compile(r"^wiki/[a-z-]+/[^/]+\.md$")
DATE_KEYS = ("extracted", "last-verified", "review-due", "archived-date")
BARE_ISO_LINE_RE = re.compile(r"^(" + "|".join(DATE_KEYS) + r"):\s*\d{4}-\d{2}-\d{2}\s*$")
REPORT_ONLY_RULES = {"client-name-in-narrative", "review-overdue"}
REVERSE_LINK = {"supersedes": "superseded-by", "superseded-by": "supersedes"}

NARRATIVE_CATEGORIES = {
    "technical-approach", "management-staffing", "win-themes",
    "qualifications", "compliance-plans",
}
CLIENT_NAME_PATTERNS_FALLBACK = {
    "hull-wwtf-om-2026": re.compile(r"\b(Hull|Town of Hull)\b"),
    "santamonica-swip-om-2025": re.compile(r"\b(Santa Monica|SWIP)\b"),
}


def load_client_patterns():
    """One regex per source from verbatim/<slug>/sanitize.json (client_names + facility names,
    proper names only — never aliases like 'the County'). Case-sensitive, and bounded so a
    name inside a graphic asset id (135_Hull_0091KO_2) never matches."""
    patterns = dict(CLIENT_NAME_PATTERNS_FALLBACK)
    for sj in sorted((ROOT / "verbatim").glob("*/sanitize.json")):
        try:
            cfg = json.loads(sj.read_text(encoding="utf-8"))
        except Exception:
            continue
        names = list(cfg.get("client_names") or [])
        for fac in cfg.get("facility_names") or []:
            names += list(fac.get("names") or [])
        for prod in cfg.get("product_names") or []:
            names += list(prod.get("names") or [])
        names = [n for n in names if n]
        if not names:
            continue
        names.sort(key=len, reverse=True)
        alt = "|".join(re.escape(n) for n in names)
        patterns[sj.parent.name] = re.compile(r"(?<![A-Za-z0-9_])(" + alt + r")(?![A-Za-z0-9_])")
    return patterns


CLIENT_NAME_PATTERNS = load_client_patterns()

VERBATIM_REF_RE = re.compile(r"^(?P<file>[^#]+)#¶(?P<n>\d+)$")
VERBATIM_REF_POS_RE = re.compile(r"verbatim/(?P<slug>[^/]+)/pages/p(?P<page>\d{4})\.md#¶(?P<para>\d+)")

_sections_cache = {}


def sections_for(slug):
    """Cached verbatim/<slug>/sections.json (None when absent)."""
    if slug in _sections_cache:
        return _sections_cache[slug]
    doc = None
    try:
        sys.path.insert(0, str(ROOT / "work"))
        from verbatim_sections import load_sections
        doc = load_sections(slug)
    except Exception:
        doc = None
    _sections_cache[slug] = doc
    return doc


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


def link_targets(v):
    """supersedes/superseded-by values: a list, a path, a bare filename, or (legacy)
    a comma-separated string. Returns the individual target strings."""
    out = []
    for item in as_list(v):
        for part in str(item).split(","):
            part = part.strip().replace("\\", "/")
            if part:
                out.append(part)
    return out


def link_stem(v):
    return Path(str(v)).stem


def iso_str(v):
    if isinstance(v, (_dt.date, _dt.datetime)):
        return v.strftime("%Y-%m-%d")
    return str(v) if v is not None else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--today", default=None, help="ISO date for the review-overdue rule (default: today)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any non-report-only rule fires")
    args = ap.parse_args()
    today = _dt.date.fromisoformat(args.today) if args.today else _dt.date.today()

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

    # Pass 0: every block's frontmatter, keyed by repo-relative path and by stem, so
    # the link rules can look at the other side of a supersedes pair.
    all_fm = {}
    by_stem = {}
    for cat in CATEGORY_DIRS:
        cat_dir = ROOT / "wiki" / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob("*.md")):
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            fm0, _b0, err0 = load_frontmatter(path.read_text(encoding="utf-8"))
            if not err0:
                all_fm[rel] = fm0
                by_stem.setdefault(path.stem, []).append(rel)

    def resolve_link(target):
        t = str(target).replace("\\", "/")
        if t in all_fm:
            return t
        hits = by_stem.get(link_stem(t), [])
        return hits[0] if len(hits) == 1 else None

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
            raw_fm_lines = text.split("\n")[1:]

            # 1. required keys present and non-empty
            # proof-point-ids is the one required key whose valid range
            # legitimately includes an empty list (a block with no
            # quantified claim in its body has no proof point to cite) —
            # it must still be present as a key, but [] is not "missing".
            missing = []
            for key in REQUIRED_KEYS:
                if key not in fm:
                    missing.append(key)
                elif key == "proof-point-ids":
                    if fm[key] is None:
                        missing.append(key)
                elif fm[key] in (None, "", [], {}):
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

            # 11-13. section-id resolves, section-order is a positive int, first ref lies in the span
            sid = fm.get("section-id")
            if sid:
                doc = sections_for(str(fm.get("source") or ""))
                if doc is None:
                    add("section-id-unresolved", rel, f"no verbatim/{fm.get('source')}/sections.json")
                else:
                    sec = next((s for s in doc["sections"] if s["id"] == sid), None)
                    if sec is None:
                        add("section-id-unresolved", rel, str(sid))
                    else:
                        m = VERBATIM_REF_POS_RE.search(str(refs[0])) if refs else None
                        if m:
                            pos = (int(m.group("page")), int(m.group("para")))
                            lo = (sec["start"]["page"], sec["start"]["para"])
                            hi = (sec["end"]["page"], sec["end"]["para"])
                            if not (lo <= pos <= hi):
                                add("section-id-span-mismatch", rel,
                                    f"first ref p{pos[0]:04d}¶{pos[1]} outside {sid} (p{lo[0]}¶{lo[1]}–p{hi[0]}¶{hi[1]}) — rerun assign_block_sections.py")
            for key in ("section-order", "doc-order"):
                so = fm.get(key)
                if so is not None and (not isinstance(so, int) or isinstance(so, bool) or so < 1):
                    add(f"{key}-invalid", rel, repr(so))

            # 14. lifecycle: links are wiki/<cat>/<file>.md paths that resolve and are reciprocal
            for key in LINK_KEYS:
                if key not in fm or fm.get(key) in (None, "", []):
                    continue
                for target in link_targets(fm.get(key)):
                    if not LINK_PATH_RE.match(target):
                        add("supersedes-link-format", rel, f"{key}: {target}")
                    resolved = resolve_link(target)
                    if resolved is None:
                        add("supersedes-link-missing", rel, f"{key}: {target}")
                        continue
                    if key in REVERSE_LINK:
                        other = all_fm.get(resolved, {})
                        back = {link_stem(t) for t in link_targets(other.get(REVERSE_LINK[key]))}
                        if path.stem not in back:
                            add("supersedes-nonreciprocal", rel,
                                f"{key}: {resolved} has no {REVERSE_LINK[key]} pointing back")

            # 15. lifecycle: status agrees with the links and the archive fields
            has_winner = bool(link_targets(fm.get("superseded-by")))
            if status == "preferred" and has_winner:
                add("status-link-mismatch", rel, "preferred block carries superseded-by")
            if status == "fallback" and not has_winner:
                add("status-link-mismatch", rel, "fallback block names no superseded-by winner")
            if status == "fallback" and fm.get("house-favorite") is True:
                add("fallback-house-favorite", rel, "fallback block is house-favorite")
            if status == "archived":
                missing_arch = [k for k in ("archive-reason", "archived-date") if not fm.get(k)]
                if missing_arch:
                    add("archived-missing-fields", rel, ", ".join(missing_arch))
            if status != "archived":
                for target in link_targets(fm.get("superseded-by")):
                    resolved = resolve_link(target)
                    if resolved and all_fm.get(resolved, {}).get("status") == "archived":
                        add("status-link-mismatch", rel, f"live block's winner is archived: {resolved}")

            # 16. lifecycle: dates are bare ISO (not quoted), checked on the raw line
            for line in raw_fm_lines:
                if line.strip() == "---":
                    break
                m = re.match(r"^(" + "|".join(DATE_KEYS) + r"):(.*)$", line)
                if m and m.group(2).strip() and not BARE_ISO_LINE_RE.match(line):
                    add("date-not-bare-iso", rel, line.strip())

            # 17. lifecycle: enums for the derived fields
            vol = fm.get("volatility")
            if vol is not None and vol not in VOLATILITY_ENUM:
                add("volatility-invalid", rel, f"'{vol}' not in {sorted(VOLATILITY_ENUM)}")
            bad_flags = [f for f in as_list(fm.get("freshness-flags")) if f not in FLAG_ENUM]
            if bad_flags:
                add("freshness-flag-invalid", rel, ", ".join(map(str, bad_flags)))

            # 18. lifecycle (report-only): review-due in the past
            due = fm.get("review-due")
            if due and status != "archived":
                try:
                    due_d = _dt.date.fromisoformat(iso_str(due))
                    if due_d < today:
                        add("review-overdue", rel, f"review-due {due_d.isoformat()} ({(today - due_d).days} days ago)")
                except ValueError:
                    add("date-not-bare-iso", rel, f"review-due: {due}")

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

    structural = [v for v in violations if v["rule"] not in REPORT_ONLY_RULES]
    if args.strict and structural:
        print(f"\n--strict: {len(structural)} structural violation(s) -> exit 1")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
