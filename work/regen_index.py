#!/usr/bin/env python3
"""Rebuild wiki/index.md and wiki/index.json from block frontmatter.

Usage:
    python work/regen_index.py [--dry-run] [--md OUT.md] [--json OUT.json]

Without --dry-run, overwrites wiki/index.md and wiki/index.json in place.
With --dry-run, writes to --md / --json paths instead (defaults land in the
scratchpad-style location the caller passes) and never touches wiki/.

Tolerates missing schema-v2 keys on any block (renders "—" in table cells).
Facet sections (By rfp-section-type, By win-theme-map) are included only if
at least one block in the wiki defines that key; otherwise a note explains
why the section was omitted.
"""
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

DASH = "—"


def load_frontmatter(text):
    if not text.startswith("---"):
        return {}
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return {}
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}
    fm_text = "\n".join(lines[1:end_idx])
    if not HAVE_YAML:
        return {}
    try:
        return yaml.safe_load(fm_text) or {}
    except Exception:
        return {}


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return v
    return [v]


def cell(v, joiner=", "):
    if v is None or v == "" or v == [] or v == {}:
        return DASH
    if isinstance(v, list):
        return joiner.join(str(x) for x in v) if v else DASH
    return str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--md", default=None, help="output path for index.md (dry-run only)")
    ap.add_argument("--json", dest="json_out", default=None, help="output path for index.json (dry-run only)")
    args = ap.parse_args()

    if not HAVE_YAML:
        print("WARNING: pyyaml not available — cannot parse frontmatter, index would be empty.")

    blocks_by_category = {cat: [] for cat in CATEGORY_DIRS}
    all_blocks = []  # for index.json: full frontmatter dict + path

    for cat in CATEGORY_DIRS:
        cat_dir = ROOT / "wiki" / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm = load_frontmatter(text)
            rel = str(path.relative_to(ROOT / "wiki")).replace("\\", "/")
            rel_from_root = str(path.relative_to(ROOT)).replace("\\", "/")
            entry = dict(fm)
            entry["path"] = rel_from_root
            all_blocks.append(entry)
            blocks_by_category[cat].append({"fm": fm, "rel": rel})

    has_rfp_section_type = any(b["fm"].get("rfp-section-type") for cat in blocks_by_category for b in blocks_by_category[cat])
    has_win_theme_map = any(b["fm"].get("win-theme-map") for cat in blocks_by_category for b in blocks_by_category[cat])

    lines = []
    lines.append("# Wiki Index")
    lines.append("")
    sources = sorted({str(b["fm"].get("source")) for cat in blocks_by_category for b in blocks_by_category[cat] if b["fm"].get("source")})
    lines.append(
        "Master index of all content blocks, regenerated from block frontmatter "
        "(`python work/regen_index.py`). Sources: "
        + ", ".join(f"`{s}`" for s in sources)
        + " (see each block's `source:` frontmatter field and `graphics/<source>.md` "
        "for the exhibit/graphics catalogs). The **By source section** facet at the end "
        "lists every block in its proposal's reading order."
    )
    lines.append("")
    lines.append(
        "**Verbatim-categories QC warning:** `resumes/` and `past-performance/` "
        "are VERBATIM content (real names, contacts, and client identities) — "
        "the proposal team must QC these before any external use. Other "
        "categories use `[CLIENT]`-style generalized placeholders and are "
        "safe to reuse across pursuits as-is."
    )
    lines.append("")
    lines.append(
        "**How to select:** don't scan every block — filter by facet. Use the "
        "`rfp-section-type` and `win-theme-map` facet sections below (or a "
        "block's `pursuit-type`, `client-size`, and `status`/`house-favorite` "
        "frontmatter) to narrow to the blocks relevant to the section you're "
        "drafting and the win theme you're proving; prefer `status: preferred` "
        "and `house-favorite: true` blocks first."
    )
    lines.append("")

    for cat in CATEGORY_DIRS:
        items = blocks_by_category[cat]
        if not items:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| Title | block-type | status | house-favorite | rfp-section-type | pursuit-type | client-size | proof-point-ids | tags |")
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for item in items:
            fm, rel = item["fm"], item["rel"]
            title = fm.get("title") or Path(rel).stem
            link = f"[{title}]({rel})"
            block_type = cell(fm.get("block-type"))
            status = cell(fm.get("status"))
            house_fav = cell(fm.get("house-favorite"))
            rfp_section = cell(fm.get("rfp-section-type"))
            pursuit_type = cell(fm.get("pursuit-type"))
            client_size = cell(fm.get("client-size"))
            pp_count = len(as_list(fm.get("proof-point-ids")))
            pp_count_cell = str(pp_count) if pp_count else DASH
            tags = cell(fm.get("tags"))
            lines.append(
                f"| {link} | {block_type} | {status} | {house_fav} | {rfp_section} "
                f"| {pursuit_type} | {client_size} | {pp_count_cell} | {tags} |"
            )
        lines.append("")

    # Facet: By rfp-section-type
    lines.append("## By rfp-section-type")
    lines.append("")
    if has_rfp_section_type:
        by_value = {}
        for cat in CATEGORY_DIRS:
            for item in blocks_by_category[cat]:
                fm, rel = item["fm"], item["rel"]
                for v in as_list(fm.get("rfp-section-type")):
                    by_value.setdefault(v, []).append((fm.get("title") or Path(rel).stem, rel))
        for value in sorted(by_value):
            lines.append(f"### {value}")
            lines.append("")
            for title, rel in by_value[value]:
                lines.append(f"- [{title}]({rel})")
            lines.append("")
    else:
        lines.append(
            "_No block in the wiki currently sets `rfp-section-type` — omitted "
            "until schema-v2 migration adds this key._"
        )
        lines.append("")

    # Facet: By win-theme-map
    lines.append("## By win-theme-map")
    lines.append("")
    if has_win_theme_map:
        by_value = {}
        for cat in CATEGORY_DIRS:
            for item in blocks_by_category[cat]:
                fm, rel = item["fm"], item["rel"]
                for v in as_list(fm.get("win-theme-map")):
                    by_value.setdefault(v, []).append((fm.get("title") or Path(rel).stem, rel))
        for value in sorted(by_value):
            lines.append(f"### {value}")
            lines.append("")
            for title, rel in by_value[value]:
                lines.append(f"- [{title}]({rel})")
            lines.append("")
    else:
        lines.append(
            "_No block in the wiki currently sets `win-theme-map` — omitted "
            "until schema-v2 migration adds this key._"
        )
        lines.append("")

    # Facet: By source section (reading order from section-id / section-order)
    lines.append("## By source section")
    lines.append("")
    lines.append(
        "_Every block in its source proposal's reading order, under the section it was "
        "drawn from (`section-id` / `section-order`, set by `work/assign_block_sections.py` "
        "from `verbatim/<source>/sections.json`). Sections with no blocks are omitted. "
        "Pull a whole section with `python work/assemble_section.py <source> \"<section>\"`._"
    )
    lines.append("")
    try:
        import sys as _sys
        _sys.path.insert(0, str(ROOT / "work"))
        from verbatim_sections import load_sections as _load_sections
    except Exception:  # pragma: no cover
        _load_sections = None
    ref_re = __import__("re").compile(r"p(\d{4})\.md#¶(\d+)")
    any_facet = False
    if _load_sections is not None:
        for slug in sources:
            try:
                doc = _load_sections(slug)
            except Exception:
                continue
            by_sec = {}
            for cat in CATEGORY_DIRS:
                for item in blocks_by_category[cat]:
                    fm, rel = item["fm"], item["rel"]
                    if str(fm.get("source")) != slug or not fm.get("section-id"):
                        continue
                    refs = as_list(fm.get("verbatim-ref"))
                    m = ref_re.search(str(refs[0])) if refs else None
                    ref = f"p{m.group(1)}¶{m.group(2)}" if m else DASH
                    order = fm.get("section-order")
                    try:
                        order = int(order)
                    except (TypeError, ValueError):
                        order = 0
                    by_sec.setdefault(str(fm["section-id"]), []).append(
                        (order, fm.get("title") or Path(rel).stem, rel, ref, cell(fm.get("block-type")), cell(fm.get("status"))))
            if not by_sec:
                continue
            any_facet = True
            lines.append(f"### {slug}")
            lines.append("")
            for sec in doc["sections"]:
                items = by_sec.get(sec["id"])
                if not items:
                    continue
                indent = "  " * max(0, sec["level"] - 1)
                a, b = sec["start"]["page"], sec["end"]["page"]
                pages = f"p. {a}" if a == b else f"pp. {a}–{b}"
                lines.append(f"{indent}- **{sec['title']}** (`{sec['id']}`, {pages})")
                for order, title, rel, ref, bt, st in sorted(items, key=lambda x: (x[0], x[2])):
                    lines.append(f"{indent}  - {order}. [{title}]({rel}) — {ref} · {bt} · {st}")
            lines.append("")
    if not any_facet:
        lines.append("_No block carries `section-id` yet — run `python work/build_sections.py --all` "
                     "then `python work/assign_block_sections.py`._")
        lines.append("")

    md_text = "\n".join(lines).rstrip() + "\n"
    json_text = json.dumps(all_blocks, indent=2, default=str)

    total_rows = len(all_blocks)

    if args.dry_run:
        md_out = Path(args.md) if args.md else ROOT / "work" / "index.dry-run.md"
        json_out = Path(args.json_out) if args.json_out else ROOT / "work" / "index.dry-run.json"
        md_out.write_text(md_text, encoding="utf-8")
        json_out.write_text(json_text, encoding="utf-8")
        print(f"[DRY RUN] wrote {md_out}")
        print(f"[DRY RUN] wrote {json_out}")
        print("wiki/index.md and wiki/index.json were NOT modified.")
    else:
        (ROOT / "wiki" / "index.md").write_text(md_text, encoding="utf-8")
        (ROOT / "wiki" / "index.json").write_text(json_text, encoding="utf-8")
        print("Wrote wiki/index.md")
        print("Wrote wiki/index.json")

    print(f"Total blocks indexed: {total_rows}")


if __name__ == "__main__":
    main()
