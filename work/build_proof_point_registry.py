"""Build / refresh proof-points/registry.json + registry.md from fragment facts.

Reads every work/fragments/<slug>/*.facts.json, clusters claims that describe the
same underlying fact into one stable PP id, and emits:
  proof-points/registry.json
  proof-points/registry.md
  work/fragments/pp_patches.json   (patch_frontmatter.py format)

Existing ids in registry.json are never renumbered and existing entries are never
merged with each other; new observations are routed onto the lowest-id entry that
already describes the same fact.

Usage: python work/build_proof_point_registry.py
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAG = ROOT / "work" / "fragments"

# Curation decisions carried over from work/increment_fragment_registries.py.
PAGE_CUTOFF = {"fulton-county-2025": 187}
EXCLUDED_BOOKKEEPING_CLAIMS = {
    "The discounted-engineering rate exhibit is excluded because it consists of "
    "commercial fee and rate figures.",
}

STOPWORDS = {
    "a", "an", "the", "of", "for", "to", "in", "on", "at", "by", "with", "and",
    "or", "is", "are", "was", "were", "be", "been", "that", "this", "which",
    "its", "it", "as", "from", "per", "over", "under", "into", "jacobs",
    "client", "clients", "team", "proposal", "proposed", "total", "number",
    "approximately", "about", "each", "our", "we", "their", "all", "any",
}

# Cross-source fact families: restatements of the same corporate/operational fact
# that rarely share wording.  (name, claim-regex, optional unit-regex)
FAMILIES = [
    ("corporate-revenue",
     r"\b(annual|corporate|company|companywide|firm|global|worldwide|gross|total)\b.{0,40}\brevenue|"
     r"\brevenue\b.{0,40}\b(jacobs|corporation|company|firm|global|worldwide|annual)\b",
     r"\$|billion|million"),
    ("permit-compliance-rate",
     r"(npdes|permit|discharge|effluent)\b.{0,40}complian|complian.{0,40}\b(npdes|permit|discharge|effluent)\b",
     r"%|percent"),
    ("collection-system-miles",
     r"\b(collection system|sewer|gravity main|force main|pipeline|interceptor)\b.{0,50}\bmile|"
     r"\bmiles?\b.{0,30}\b(sewer|collection system|pipeline|interceptor|force main)\b",
     r"mile"),
    ("global-employee-count",
     r"\b(global|worldwide|companywide|corporate|firm ?wide|jacobs)\b.{0,40}\b(employee|staff member|professional|people)\b|"
     r"\b(employee|professional|people)\b.{0,30}\b(worldwide|globally|company ?wide|across the (globe|world))\b",
     r"employee|staff|people|professional"),
    ("corporate-bonding-capacity",
     r"bonding capacity|aggregate surety|single-project surety",
     r"\$|billion|million"),
]


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value if value is not None else "")).strip()


def norm_key(claim: str) -> str:
    """Order-independent, punctuation-insensitive key for a claim sentence."""
    text = claim.lower()
    text = re.sub(r"[^a-z0-9%$./ ]+", " ", text)
    tokens = []
    for tok in text.split():
        tok = tok.rstrip(".")
        if not tok or tok in STOPWORDS:
            continue
        if len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
            tok = tok[:-1]
        tokens.append(tok)
    return " ".join(sorted(set(tokens)))


def family_of(claim: str, unit: str) -> str | None:
    c = claim.lower()
    u = (unit or "").lower()
    for name, claim_re, unit_re in FAMILIES:
        if re.search(claim_re, c) and (unit_re is None or re.search(unit_re, u)):
            return name
    return None


def resolve_block(block: str) -> str:
    block = clean(block)
    if not block or block.startswith("wiki/"):
        return block
    matches = list((ROOT / "wiki").glob(f"**/{block}.md"))
    if len(matches) == 1:
        return matches[0].as_posix().replace(ROOT.as_posix() + "/", "")
    return block


def value_key(value: dict):
    return tuple(clean(value.get(k)) for k in
                 ("number", "unit", "as_of", "source_slug", "page", "para", "block"))


def fact_records():
    for folder in sorted(p for p in FRAG.iterdir() if p.is_dir()):
        slug = folder.name
        cutoff = PAGE_CUTOFF.get(slug)
        for path in sorted(folder.glob("*.facts.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            for fact in data if isinstance(data, list) else []:
                if not isinstance(fact, dict) or not fact.get("claim"):
                    continue
                claim = clean(fact["claim"])
                category = clean(fact.get("category") or "other")
                if claim in EXCLUDED_BOOKKEEPING_CLAIMS and category == "commercial-excluded":
                    continue
                page = fact.get("page")
                if cutoff is not None and isinstance(page, int) and page > cutoff:
                    continue
                yield claim, category, {
                    "number": clean(fact.get("number")),
                    "unit": clean(fact.get("unit")),
                    "as_of": clean(fact.get("as_of")),
                    "source_slug": slug,
                    "page": page,
                    "para": fact.get("para"),
                    "block": resolve_block(fact.get("block")),
                }


def entry_num(entry) -> int:
    return int(entry["id"].split("-")[1])


def set_status(entry) -> None:
    numbers = {clean(v.get("number")) for v in entry["values"]}
    if len(entry["values"]) <= 1:
        entry["status"] = "single-source"
    elif len(numbers) == 1:
        entry["status"] = "consistent"
    else:
        entry["status"] = "conflict"


def main() -> None:
    registry_path = ROOT / "proof-points" / "registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.is_file() else []
    registry = [
        e for e in registry
        if not (clean(e.get("claim")) in EXCLUDED_BOOKKEEPING_CLAIMS
                and clean(e.get("category")) == "commercial-excluded")
    ]
    for entry in registry:
        entry.setdefault("values", [])
        entry.setdefault("conflicts_with", [])
        entry.setdefault("owner", "")
        entry.setdefault("approved_for_external_use", "pending")
        for value in entry["values"]:
            value["block"] = resolve_block(value.get("block"))

    # Routing indexes. Existing entries are never merged with one another; the
    # lowest id wins when several existing entries answer to the same key.
    by_exact: dict[str, dict] = {}
    by_norm: dict[str, dict] = {}
    by_family: dict[str, dict] = {}
    for entry in sorted(registry, key=entry_num):
        by_exact.setdefault(clean(entry["claim"]), entry)
        by_norm.setdefault(norm_key(entry["claim"]), entry)
        unit = clean(entry["values"][0].get("unit")) if entry["values"] else ""
        fam = family_of(entry["claim"], unit)
        if fam:
            by_family.setdefault(fam, entry)

    next_id = max((entry_num(e) for e in registry), default=0) + 1
    raw_claims = new_entries = new_values = 0

    for claim, category, value in fact_records():
        raw_claims += 1
        fam = family_of(claim, value["unit"])
        entry = (by_exact.get(claim)
                 or by_norm.get(norm_key(claim))
                 or (by_family.get(fam) if fam else None))
        if entry is None:
            entry = {
                "id": f"PP-{next_id:04d}",
                "claim": claim,
                "values": [],
                "status": "single-source",
                "category": category,
                "owner": "",
                "approved_for_external_use": "pending",
                "conflicts_with": [],
            }
            next_id += 1
            registry.append(entry)
            new_entries += 1
            by_exact.setdefault(claim, entry)
            by_norm.setdefault(norm_key(claim), entry)
            if fam:
                by_family.setdefault(fam, entry)
        else:
            by_exact.setdefault(claim, entry)
            by_norm.setdefault(norm_key(claim), entry)
        known = {value_key(v) for v in entry["values"]}
        if value_key(value) not in known:
            entry["values"].append(value)
            new_values += 1

    for entry in registry:
        set_status(entry)

    # Cross-id conflicts inside a declared fact family.
    fam_members: dict[str, list] = defaultdict(list)
    for entry in registry:
        unit = clean(entry["values"][0].get("unit")) if entry["values"] else ""
        fam = family_of(entry["claim"], unit)
        if fam:
            fam_members[fam].append(entry)
    for members in fam_members.values():
        for entry in members:
            mine = {clean(v.get("number")) for v in entry["values"]}
            others = sorted(
                other["id"] for other in members
                if other["id"] != entry["id"]
                and {clean(v.get("number")) for v in other["values"]} - mine
            )
            entry["conflicts_with"] = others

    registry.sort(key=entry_num)
    registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
                             encoding="utf-8")

    render_md(registry)
    blocks_patched = write_patches(registry)

    conflicts = sum(1 for e in registry if e["status"] == "conflict")
    print(json.dumps({
        "raw_claims_swept": sum(len(e["values"]) for e in registry),
        "claims_read_this_run": raw_claims,
        "ids": len(registry),
        "new_entries": new_entries,
        "new_values": new_values,
        "conflicts": conflicts,
        "blocks_patched": blocks_patched,
    }, indent=2))


def render_md(registry) -> None:
    path = ROOT / "proof-points" / "registry.md"
    values = [v for e in registry for v in e["values"]]
    statuses = {s: sum(e["status"] == s for e in registry)
                for s in ("conflict", "consistent", "single-source")}
    blocks = {clean(v.get("block")) for v in values if clean(v.get("block"))}
    slugs = sorted({clean(v.get("source_slug")) for v in values if clean(v.get("source_slug"))})

    def cell(item):
        return clean(item).replace("|", "\\|")

    out = ["# Proof-Point Registry\n\n",
           "Every reusable numeric claim swept from the content-bank fragments, clustered so "
           "that one underlying fact carries one stable ID.\n\n",
           f"Sources: {', '.join(slugs)}\n\n",
           "| Metric | Count |\n| --- | ---: |\n",
           f"| Raw claims swept | {len(values)} |\n",
           f"| Proof-point IDs | {len(registry)} |\n",
           f"| Conflicts to resolve | {statuses['conflict']} |\n",
           f"| Consistent (multi-observation) | {statuses['consistent']} |\n",
           f"| Single-source | {statuses['single-source']} |\n",
           f"| Distinct blocks referenced | {len(blocks)} |\n\n",
           "`owner` is unassigned and `approved_for_external_use` is `pending` for every ID; "
           "both are for the proposal team to fill in.\n\n"]

    conflicts = [e for e in registry if e["status"] == "conflict"]
    out.append("## Conflicts to resolve\n\n")
    if not conflicts:
        out.append("None — every multi-observation ID reports one number.\n")
    else:
        out.append(f"{len(conflicts)} IDs carry more than one number for the same fact. "
                   "Each must be reconciled (or split) before the number is used externally.\n\n")
        out.append("| ID | Claim | Competing values | Also conflicts with |\n| --- | --- | --- | --- |\n")
        for e in conflicts:
            seen, competing = set(), []
            for v in e["values"]:
                label = f"{cell(v.get('number'))} {cell(v.get('unit'))}".strip()
                src = f"{cell(v.get('source_slug'))} p{v.get('page','')} ¶{v.get('para','')}"
                if label in seen:
                    continue
                seen.add(label)
                competing.append(f"{label} ({src})")
            out.append(f"| {e['id']} | {cell(e['claim'])} | " + "; ".join(competing)
                       + f" | {', '.join(e.get('conflicts_with') or []) or '—'} |\n")
    out.append("\n## Registry\n")

    for e in registry:
        out.append(f"\n### {e['id']} — {cell(e['claim'])}\n")
        out.append(f"*status:* {e['status']} · *category:* {cell(e.get('category'))}\n\n")
        out.append("| Value | As of | Source | Page/Para | Block |\n| --- | --- | --- | --- | --- |\n")
        for v in e["values"]:
            page = f"p{v.get('page', '')} ¶{v.get('para', '')}"
            out.append(f"| {cell(v.get('number'))} {cell(v.get('unit'))}".rstrip()
                       + f" | {cell(v.get('as_of'))} | {cell(v.get('source_slug'))} | {page} | "
                       + f"`{cell(v.get('block'))}` |\n")
        if e.get("conflicts_with"):
            out.append("\nAlso conflicts with: " + ", ".join(e["conflicts_with"]) + "\n")
    path.write_text("".join(out).rstrip() + "\n", encoding="utf-8")


def write_patches(registry) -> int:
    by_block: dict[str, set] = defaultdict(set)
    for e in registry:
        for v in e["values"]:
            block = clean(v.get("block"))
            if block:
                by_block[block].add(e["id"])
    patches, skipped = [], []
    for block in sorted(by_block):
        if not (ROOT / block).is_file():
            skipped.append(block)
            continue
        patches.append({
            "path": block,
            "set": {"proof-point-ids": sorted(by_block[block])},
        })
    out = FRAG / "pp_patches.json"
    out.write_text(json.dumps(patches, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if skipped:
        (FRAG / "pp_patches_skipped.json").write_text(
            json.dumps(sorted(skipped), indent=2) + "\n", encoding="utf-8")
        print(f"(skipped {len(skipped)} unresolved block paths -> pp_patches_skipped.json)")
    return len(patches)


if __name__ == "__main__":
    main()
