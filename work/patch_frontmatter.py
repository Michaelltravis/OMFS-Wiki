#!/usr/bin/env python3
"""Patch YAML frontmatter on content-block files, in place, without touching the body.

Usage:
    python work/patch_frontmatter.py <patches.json> [--dry-run]

patches.json is a list of patch objects:
    [
      {
        "path": "wiki/qualifications/x.md",
        "set":    {"status": "preferred", "proof-point-ids": ["PP-0012"]},
        "append": {"tags": ["odor-control"]},
        "delete": ["obsolete-key"]
      },
      ...
    ]

Guarantees:
  - Only the frontmatter block (between the opening and closing `---` lines) is
    rewritten. The body (everything after the closing `---`) is copied through
    byte-for-byte.
  - Existing key ORDER is preserved. Keys touched by "set" keep their original
    line position. Keys added by "set" (that don't already exist) are inserted
    immediately before the `context` key, or at the end of the frontmatter if
    there is no `context` key.
  - Untouched frontmatter lines are copied through byte-for-byte (not
    reformatted by round-tripping through a YAML dumper).
  - Lists are always written in flow style: [a, b, c].
  - Exits 1 if any patch references a path that does not exist (nothing is
    written in that case).
"""
import sys
import json
import re
import argparse
import datetime as _dt
from pathlib import Path

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

# Matches a top-level "key: value" line in the (flat) frontmatter. All schema
# v2 fields are flat scalars or flow lists, one per physical line.
KEY_LINE_RE = re.compile(r'^([A-Za-z0-9_.\-]+):(\s.*|)$')

NEW_KEY_ANCHOR = "context"
ROOT = Path(__file__).resolve().parent.parent
ISO_DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


def render_scalar(value):
    """Render a python value (scalar, list of scalars, or bool/None) the way
    it should appear after 'key: ' in the frontmatter. Lists -> flow style."""
    if isinstance(value, str) and "\n" in value:
        raise ValueError(
            f"Cannot patch a frontmatter value containing a newline: {value!r}"
        )
    # ISO dates (str or datetime.date) are written bare: yaml.safe_dump would quote
    # the string form ('2026-09-05'), which is how 22 blocks ended up with quoted dates.
    if isinstance(value, _dt.date):
        return value.isoformat()
    if isinstance(value, str) and ISO_DATE_RE.match(value):
        return value
    if HAVE_YAML:
        dumped = yaml.safe_dump(
            value, default_flow_style=True, allow_unicode=True, width=10**6
        )
        lines = [ln for ln in dumped.splitlines() if ln != "..."]
        return "\n".join(lines).strip()
    return _minimal_render(value)


def _minimal_scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    s = str(v)
    needs_quote = (
        s == ""
        or re.search(r'[:#\[\]{}",\n]', s)
        or s != s.strip()
        or s.lower() in ("true", "false", "null", "~")
        or re.match(r'^[-?!&*>|%@`]', s)
    )
    if needs_quote:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def _minimal_render(value):
    if isinstance(value, list):
        return "[" + ", ".join(_minimal_scalar(v) for v in value) + "]"
    return _minimal_scalar(value)


def split_frontmatter(text):
    """Return (fm_lines, body) where fm_lines is the list of raw lines
    strictly between the opening and closing '---' delimiters (no trailing
    newlines), and body is everything after the closing delimiter line,
    preserved byte-for-byte (including its own leading newline character)."""
    if not text.startswith("---"):
        raise ValueError("file does not start with a frontmatter delimiter")
    # Normalize line endings for splitting only; we reconstruct explicitly.
    lines = text.split("\n")
    if lines[0].strip() != "---":
        raise ValueError("file does not start with '---'")
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        raise ValueError("no closing '---' found for frontmatter")
    fm_lines = lines[1:end_idx]
    body = "\n".join(lines[end_idx + 1:])
    return fm_lines, body


def parse_key_positions(fm_lines):
    """Map key -> line index for top-level keys in fm_lines."""
    positions = {}
    for i, line in enumerate(fm_lines):
        m = KEY_LINE_RE.match(line)
        if m:
            positions[m.group(1)] = i
    return positions


def get_current_value(fm_lines, key, positions):
    """Best-effort parse of the current value of `key` (for append)."""
    if key not in positions:
        return None
    line = fm_lines[positions[key]]
    m = KEY_LINE_RE.match(line)
    raw = m.group(2).strip()
    if not raw:
        return None
    if HAVE_YAML:
        try:
            return yaml.safe_load(raw)
        except Exception:
            return raw
    # minimal fallback: flow list
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip('"').strip("'") for x in inner.split(",")]
    return raw.strip('"').strip("'")


def apply_patch(text, patch, path_for_errors):
    fm_lines, body = split_frontmatter(text)
    positions = parse_key_positions(fm_lines)

    summary = {"set": [], "appended": [], "deleted": [], "added": []}

    deletes = patch.get("delete", [])
    sets = patch.get("set", {})
    appends = patch.get("append", {})

    # Apply "set": modify existing lines in place, or queue new keys to insert.
    new_keys_to_add = []
    for key, value in sets.items():
        rendered = f"{key}: {render_scalar(value)}"
        if key in positions:
            fm_lines[positions[key]] = rendered
            summary["set"].append(key)
        else:
            new_keys_to_add.append((key, rendered))

    # Apply "append": extend an existing list value (or create it as a new key).
    for key, values_to_add in appends.items():
        if not isinstance(values_to_add, list):
            values_to_add = [values_to_add]
        if key in positions:
            current = get_current_value(fm_lines, key, positions)
            if current is None:
                current = []
            if not isinstance(current, list):
                raise ValueError(
                    f"{path_for_errors}: cannot append to non-list key '{key}'"
                )
            merged = list(current)
            for v in values_to_add:
                if v not in merged:
                    merged.append(v)
            fm_lines[positions[key]] = f"{key}: {render_scalar(merged)}"
            summary["appended"].append(key)
        else:
            rendered = f"{key}: {render_scalar(list(values_to_add))}"
            new_keys_to_add.append((key, rendered))
            summary["appended"].append(key)

    # Apply "delete": remove lines for the given keys.
    if deletes:
        del_idx = {positions[k] for k in deletes if k in positions}
        for k in deletes:
            if k in positions:
                summary["deleted"].append(k)
        fm_lines = [ln for i, ln in enumerate(fm_lines) if i not in del_idx]
        positions = parse_key_positions(fm_lines)

    # Insert brand-new keys before `context`, or at the end.
    if new_keys_to_add:
        insert_at = positions.get(NEW_KEY_ANCHOR, len(fm_lines))
        for offset, (key, rendered) in enumerate(new_keys_to_add):
            fm_lines.insert(insert_at + offset, rendered)
            if key not in summary["appended"]:
                summary["added"].append(key)

    new_text = "---\n" + "\n".join(fm_lines) + "\n---\n" + body
    return new_text, summary


def resolve_path(p):
    """Patch paths are repo-root-relative (the documented form); accept CWD-relative
    and absolute paths too so callers in another directory still work."""
    path = Path(p)
    if path.is_absolute():
        return path
    if (ROOT / path).is_file():
        return ROOT / path
    return path


def apply_patches(patches, dry_run=False, quiet=False):
    """Apply a list of patch dicts in-process. Returns a list of
    {"path", "action": WRITE | NO CHANGE | WOULD WRITE, "summary"}.
    Raises FileNotFoundError (before writing anything) if any path is missing,
    ValueError if a patch would change a body."""
    if not isinstance(patches, list):
        raise ValueError("patches must be a JSON list")
    missing = [p["path"] for p in patches if not resolve_path(p["path"]).is_file()]
    if missing:
        raise FileNotFoundError("unknown path(s), no files were modified: " + ", ".join(missing))

    results = []
    for p in patches:
        path = resolve_path(p["path"])
        original = path.read_text(encoding="utf-8")
        new_text, summary = apply_patch(original, p, p["path"])
        _, orig_body = split_frontmatter(original)
        _, new_body = split_frontmatter(new_text)
        if orig_body != new_body:
            raise ValueError(f"body would change for {p['path']} — aborting")
        changed = new_text != original
        action = "WOULD WRITE" if (dry_run and changed) else ("WRITE" if changed else "NO CHANGE")
        if not quiet:
            print(f"[{action}] {p['path']}")
            for k in ("set", "appended", "added", "deleted"):
                if summary[k]:
                    print(f"    {k}: {', '.join(summary[k])}")
        if changed and not dry_run:
            path.write_text(new_text, encoding="utf-8")
        results.append({"path": p["path"], "action": action, "summary": summary})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("patches_json")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    patches = json.loads(Path(args.patches_json).read_text(encoding="utf-8"))
    if not HAVE_YAML:
        print("(pyyaml not found — using minimal built-in scalar renderer)")
    try:
        results = apply_patches(patches, dry_run=args.dry_run)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    n_write = sum(1 for r in results if r["action"] == "WRITE")
    n_would = sum(1 for r in results if r["action"] == "WOULD WRITE")
    print(f"Done. {n_write} written, {n_would} would write, {len(results) - n_write - n_would} unchanged.")


if __name__ == "__main__":
    main()
