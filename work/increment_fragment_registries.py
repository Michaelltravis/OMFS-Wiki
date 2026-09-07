"""Deterministically merge completed OCWUT/Fulton fragment facts and quotes.

Usage: python work/increment_fragment_registries.py
Only the two supplied slugs are read. Fulton facts above source page 187 are excluded.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {"ocwut-16-26": None, "fulton-county-2025": 187}
# Extraction bookkeeping is not reusable evidence.  Keep the source fragment as
# an audit note, but do not allow it into the proof-point registry.
EXCLUDED_BOOKKEEPING_CLAIMS = {
    "The discounted-engineering rate exhibit is excluded because it consists of commercial fee and rate figures.",
}


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fact_records():
    for slug, cutoff in SOURCES.items():
        folder = ROOT / "work" / "fragments" / slug
        for path in sorted(folder.glob("*.facts.json")):
            for fact in load_json(path):
                if not isinstance(fact, dict) or not fact.get("claim"):
                    continue
                if (
                    clean(fact["claim"]) in EXCLUDED_BOOKKEEPING_CLAIMS
                    and clean(fact.get("category")) == "commercial-excluded"
                ):
                    continue
                page = fact.get("page")
                if cutoff is not None and isinstance(page, int) and page > cutoff:
                    continue
                value = {
                    "number": clean(fact.get("number")),
                    "unit": clean(fact.get("unit")),
                    "as_of": clean(fact.get("as_of")),
                    "source_slug": slug,
                    "page": page,
                    "para": fact.get("para"),
                    "block": clean(fact.get("block")),
                }
                yield clean(fact["claim"]), clean(fact.get("category") or "other"), value


def quote_records():
    for slug, cutoff in SOURCES.items():
        folder = ROOT / "work" / "fragments" / slug
        for path in sorted(folder.glob("*.quotes.json")):
            for quote in load_json(path):
                if not isinstance(quote, dict) or not quote.get("quote"):
                    continue
                page = quote.get("page")
                if cutoff is not None and isinstance(page, int) and page > cutoff:
                    continue
                yield slug, quote


def value_key(value: dict):
    return tuple(clean(value.get(k)) for k in ("number", "unit", "as_of", "source_slug", "page", "para", "block"))


def resolve_block(block: str) -> str:
    """Resolve legacy bare block stems to their unique wiki path."""
    block = clean(block)
    if not block or block.startswith("wiki/"):
        return block
    matches = list((ROOT / "wiki").glob(f"**/{block}.md"))
    return matches[0].as_posix().replace(ROOT.as_posix() + "/", "") if len(matches) == 1 else block


def render_registry_md(registry):
    path = ROOT / "proof-points" / "registry.md"
    values = [value for entry in registry for value in entry.get("values", [])]
    statuses = {status: sum(entry.get("status") == status for entry in registry)
                for status in ("conflict", "consistent", "single-source")}
    blocks = {clean(value.get("block")) for value in values if clean(value.get("block"))}
    chunks = [
        "# Proof-Point Registry\n\n"
        "Every reusable numeric claim swept from the content-bank fragments, clustered so that one underlying fact carries one stable ID.\n\n"
        "| Metric | Count |\n| --- | ---: |\n"
        f"| Raw claims swept | {len(values)} |\n"
        f"| Proof-point IDs | {len(registry)} |\n"
        f"| Conflicts to resolve | {statuses['conflict']} |\n"
        f"| Consistent (multi-observation) | {statuses['consistent']} |\n"
        f"| Single-source | {statuses['single-source']} |\n"
        f"| Distinct blocks referenced | {len(blocks)} |\n\n"
        "`owner` is unassigned and `approved_for_external_use` is `pending` for every ID; both are for the proposal team to fill in.\n\n"
        "## Registry\n"
    ]
    for entry in registry:
        chunks.append(f"\n### {entry['id']} — {entry['claim']}\n")
        chunks.append("| Value | As of | Source | Page/Para | Block |\n| --- | --- | --- | --- | --- |\n")
        for value in entry["values"]:
            page = f"p{value.get('page', '')} ¶{value.get('para', '')}"
            def cell(item):
                return clean(item).replace("|", "\\|")
            chunks.append(
                f"| {cell(value.get('number', ''))} {cell(value.get('unit', ''))}".rstrip()
                + f" | {cell(value.get('as_of', ''))} | {cell(value.get('source_slug', ''))} | {page} | `{cell(value.get('block', ''))}` |\n"
            )
        if entry.get("conflicts_with"):
            chunks.append("\nAlso conflicts with: " + ", ".join(entry["conflicts_with"]) + "\n")
    path.write_text("".join(chunks).rstrip() + "\n", encoding="utf-8")


def parse_inventory_quotes(text: str):
    existing = set()
    for line in text.splitlines():
        if not line.startswith("| TM-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5:
            existing.add(clean(cells[4]).strip('"“”'))
    return existing


def main():
    registry_path = ROOT / "proof-points" / "registry.json"
    registry = load_json(registry_path)
    registry = [
        entry for entry in registry
        if not (
            clean(entry.get("claim")) in EXCLUDED_BOOKKEEPING_CLAIMS
            and clean(entry.get("category")) == "commercial-excluded"
            and any(not clean(value.get("block")) for value in entry.get("values", []))
        )
    ]
    for entry in registry:
        for value in entry.get("values", []):
            value["block"] = resolve_block(value.get("block"))
    by_claim = {clean(entry["claim"]): entry for entry in registry}
    next_id = max(int(entry["id"].split("-")[1]) for entry in registry) + 1
    added_entries = added_values = 0
    for claim, category, value in fact_records():
        value["block"] = resolve_block(value["block"])
        entry = by_claim.get(claim)
        if entry is None:
            entry = {
                "id": f"PP-{next_id:04d}", "claim": claim, "values": [],
                "status": "single-source", "category": category, "owner": "",
                "approved_for_external_use": "pending", "conflicts_with": [],
            }
            next_id += 1
            registry.append(entry)
            by_claim[claim] = entry
            added_entries += 1
        known = {value_key(v) for v in entry["values"]}
        if value_key(value) not in known:
            entry["values"].append(value)
            added_values += 1
        numbers = {clean(v.get("number")) for v in entry["values"]}
        entry["status"] = "single-source" if len(entry["values"]) == 1 else ("consistent" if len(numbers) == 1 else "conflict")
    write_json(registry_path, registry)
    render_registry_md(registry)

    inv_path = ROOT / "testimonials" / "inventory.md"
    inventory = inv_path.read_text(encoding="utf-8")
    existing_quotes = parse_inventory_quotes(inventory)
    ids = [int(x) for x in re.findall(r"\| TM-(\d+) \|", inventory)]
    next_tm = max(ids, default=0) + 1
    additions = []
    for slug, quote in quote_records():
        text = clean(quote["quote"]).strip('"“”')
        if text in existing_quotes:
            continue
        tm = f"TM-{next_tm:04d}"
        next_tm += 1
        existing_quotes.add(text)
        additions.append(
            "| {id} | {speaker} | {title} | {org} | \"{quote}\" | {slug}/p{page} ¶{para} | unknown | — | {block} | Added from completed fragment; permission unknown. |".format(
                id=tm, speaker=clean(quote.get("speaker") or "unknown"), title=clean(quote.get("title") or "unknown"),
                org=clean(quote.get("org") or "unknown"), quote=text.replace("|", "\\|"), slug=slug,
                page=quote.get("page", ""), para=quote.get("para", ""), block=clean(quote.get("block") or "—"),
            )
        )
    if additions:
        marker = "\n## Counts\n"
        inventory = inventory.replace(marker, "\n" + "\n".join(additions) + marker, 1)
        inv_path.write_text(inventory, encoding="utf-8")
    print(json.dumps({"new_registry_entries": added_entries, "new_registry_values": added_values, "new_testimonials": len(additions), "registry_total": len(registry)}, indent=2))


if __name__ == "__main__":
    main()
