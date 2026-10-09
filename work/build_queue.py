#!/usr/bin/env python3
"""build_queue.py — merge a curate run's triage and judge fragments into the curation queue.

Usage:
    python work/build_queue.py --run <runId> --today YYYY-MM-DD [--fragments work/fragments/curation/<runId>]
                               [--out-json work/curation/queue.json] [--out-md work/curation/queue.md]

Reads  <fragments>/triage_*.json   {"items":[{path, action, target, proposed_value, evidence, confidence, rationale, ...}]}
       <fragments>/judge_*.json    {"decisions":[{path, target, action_proposed, verdict, reason}]}
       (judge verdicts override triage: approve keeps the proposal; reverse swaps path/target;
        distinct/reject turn the item into keep with the judge's reason; archive-path/-target set archive)
Writes work/curation/queue.json  {run, today, items:[CQ item]}
       work/curation/queue.md    a tick list grouped by owner: "- [ ] CQ-0001 archive `path` → `target` — rationale"
Every evidence ref is checked (block paths exist, PP ids are in the registry, verbatim refs resolve);
unresolvable refs are kept but marked `(unverified ref)` so the maintainer sees them.
Zero model tokens; read-only on wiki/.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATION = ROOT / "work" / "curation"
ACTIONS = ["archive", "supersede-with", "merge-into", "update-figure", "verify", "keep"]
ACTION_RANK = {a: i for i, a in enumerate(ACTIONS)}
PP_RE = re.compile(r"\bPP-\d{4}\b")
VREF_RE = re.compile(r"(verbatim/[^#\s]+\.md)(?:#¶(\d+))?")


def load_fragments(folder: Path, prefix: str, key: str):
    out = []
    for p in sorted(folder.glob(f"{prefix}_*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  skipping unreadable {p.name}: {e}", file=sys.stderr)
            continue
        rows = data.get(key, []) if isinstance(data, dict) else data
        for r in rows:
            r["_fragment"] = p.name
        out += rows
    return out


def ref_resolves(ref: str, registry_ids: set[str]) -> bool:
    ref = str(ref or "").strip().replace("\\", "/")
    if not ref:
        return False
    if PP_RE.fullmatch(ref):
        return ref in registry_ids
    m = VREF_RE.search(ref)
    if m:
        page = ROOT / m.group(1)
        if not page.is_file():
            return False
        return (f"<!-- ¶{m.group(2)} -->" in page.read_text(encoding="utf-8")) if m.group(2) else True
    if ref.startswith("wiki/") or ref.startswith("work/") or ref.startswith("proof-points/") or ref.startswith("pursuits/"):
        return (ROOT / ref.split("#")[0]).exists()
    return (ROOT / ref).exists()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--today", required=True)
    ap.add_argument("--fragments", default=None)
    ap.add_argument("--out-json", default=str(CURATION / "queue.json"))
    ap.add_argument("--out-md", default=str(CURATION / "queue.md"))
    args = ap.parse_args()

    frag = Path(args.fragments) if args.fragments else ROOT / "work" / "fragments" / "curation" / args.run
    if not frag.is_dir():
        raise SystemExit(f"no fragments folder {frag}")
    triage = load_fragments(frag, "triage", "items")
    verdicts = load_fragments(frag, "judge", "decisions")
    reg_ids = {r["id"] for r in json.loads((ROOT / "proof-points" / "registry.json").read_text(encoding="utf-8")) if r.get("id")}

    # last verdict per path wins
    vmap = {}
    for v in verdicts:
        vmap[str(v.get("path", "")).replace("\\", "/")] = v

    items = []
    seen = set()
    for t in triage:
        path = str(t.get("path", "")).replace("\\", "/")
        if not path or path in seen:
            continue
        seen.add(path)
        action = t.get("action") or "keep"
        target = str(t.get("target") or "").replace("\\", "/")
        rationale = t.get("rationale") or ""
        judge_note = ""
        v = vmap.get(path)
        if v:
            verdict = v.get("verdict")
            judge_note = f"Judge ({verdict}): {v.get('reason', '')}"
            if verdict == "reverse" and target:
                path, target = target, path
                action = "supersede-with" if action != "archive" else "supersede-with"
            elif verdict in ("distinct", "reject"):
                action, target = "keep", ""
            elif verdict == "archive-path":
                action = "archive"
            elif verdict == "archive-target" and target:
                path, target, action = target, "", "archive"
        evidence = []
        for e in t.get("evidence") or []:
            ref = str(e.get("ref") or "")
            ok = ref_resolves(ref, reg_ids)
            evidence.append({"kind": e.get("kind") or "", "ref": ref, "text": e.get("text") or "", "resolves": ok})
        items.append({
            "id": "", "path": path, "action": action, "target": target,
            "proposed_value": t.get("proposed_value") or "",
            "evidence": evidence, "confidence": t.get("confidence") or "low",
            "rationale": rationale, "judge": judge_note,
            "flags": t.get("flags") or [], "volatility": t.get("volatility") or "",
            "owner": t.get("owner") or "", "rank": int(t.get("rank") or 10**6),
            "fragment": t.get("_fragment", ""),
        })

    items.sort(key=lambda it: (ACTION_RANK.get(it["action"], 99), it["rank"], it["path"]))
    for i, it in enumerate(items, 1):
        it["id"] = f"CQ-{i:04d}"

    by_action = Counter(it["action"] for it in items)
    bad_refs = sum(1 for it in items for e in it["evidence"] if not e["resolves"])
    Path(args.out_json).write_text(json.dumps({"run": args.run, "today": args.today, "counts": dict(by_action),
                                               "unresolved_evidence_refs": bad_refs, "items": items},
                                              indent=1, ensure_ascii=False), encoding="utf-8")

    L = [f"# Curation queue — run {args.run} ({args.today})", "",
         "_Tick `[x]` the items to apply as proposed, leave the rest, then run_ "
         "`python work/apply_curation.py --dry-run` _and, when the dry run looks right,_ `python work/apply_curation.py`. "
         "_Items you want done differently: leave unticked and issue the exact `python work/curate.py …` command instead. "
         "`update-figure` items change nothing in the body — they record the approved new value for a writer._", "",
         "Counts: " + ", ".join(f"{a} {by_action[a]}" for a in ACTIONS if by_action.get(a))
         + (f" · evidence refs that did not resolve: {bad_refs}" if bad_refs else ""), ""]
    by_owner = defaultdict(list)
    for it in items:
        by_owner[it["owner"] or "(unassigned)"].append(it)
    for owner in sorted(by_owner):
        L += [f"## {owner}", ""]
        for it in by_owner[owner]:
            arrow = f" → `{it['target']}`" if it["target"] else ""
            val = f" = **{it['proposed_value']}**" if it["proposed_value"] else ""
            L.append(f"- [ ] {it['id']} **{it['action']}** `{it['path']}`{arrow}{val} — {it['rationale']} "
                     f"_(confidence {it['confidence']}; {it['volatility']}; flags: {', '.join(it['flags']) or 'none'})_")
            if it["judge"]:
                L.append(f"    - {it['judge']}")
            for e in it["evidence"]:
                mark = "" if e["resolves"] else " (unverified ref)"
                L.append(f"    - {e['kind']}: `{e['ref']}`{mark} — {e['text']}")
        L.append("")
    Path(args.out_md).write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")

    print(f"queue: {len(items)} items — " + ", ".join(f"{a} {by_action[a]}" for a in ACTIONS if by_action.get(a))
          + f"; {len(verdicts)} judge verdicts applied; {bad_refs} evidence refs unresolved")
    print(f"wrote {Path(args.out_json).relative_to(ROOT) if Path(args.out_json).is_relative_to(ROOT) else args.out_json} and "
          f"{Path(args.out_md).relative_to(ROOT) if Path(args.out_md).is_relative_to(ROOT) else args.out_md}")


if __name__ == "__main__":
    main()
