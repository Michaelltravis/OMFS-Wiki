#!/usr/bin/env python3
"""apply_curation.py — apply the maintainer's ticked decisions from a curation queue.

Usage:
    python work/apply_curation.py [work/curation/queue.md | queue.json | decisions.json]
                                  [--dry-run] [--by NAME] [--today YYYY-MM-DD]
                                  [--only CQ-0003,CQ-0010] [--no-regen]

Input forms (default: work/curation/queue.md):
  queue.md        the checklist the curate workflow wrote; a ticked line `- [x] CQ-0001 …`
                  approves that item as proposed. `- [ ]` lines are skipped.
  queue.json      every item is approved only when --only names it.
  decisions.json  {"decisions":[{"id":"CQ-0001","choice":"approve|skip|change","note":"…"}]}
                  — the same shape work/read_spec_decisions.py produces; "change" items are
                  skipped and listed so the maintainer can re-issue them as curate.py commands.

Item actions (from work/curation/queue.json) → what is written:
  archive         curate.act_archive(path, reason=rationale, superseded_by=target)
  supersede-with  curate.act_supersede(loser=path, winner=target)
  merge-into      same as supersede-with, plus a TODO line in the summary (bodies are never merged here)
  verify / keep   curate.act_verify(path): last-verified = today, verified-by = NAME
  update-figure   NO body edit; logged as feedback-resolved and left flagged — the figure change
                  is a writer's job, listed in the summary

Nothing is written with --dry-run. After applying: regen_index, lint, status_counts --md
(the README status line), and one log.jsonl line per item.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "work"))

import curate  # noqa: E402

CURATION = ROOT / "work" / "curation"
TICK_RE = re.compile(r"^\s*-\s*\[(?P<tick>[xX ])\]\s*(?P<id>CQ-\d{4})\b")


def load_queue() -> dict:
    q = CURATION / "queue.json"
    if not q.is_file():
        raise SystemExit("work/curation/queue.json not found — run the curate workflow first")
    data = json.loads(q.read_text(encoding="utf-8"))
    return {it["id"]: it for it in data.get("items", [])}


def decisions_from(path: Path, only: set[str] | None) -> dict[str, dict]:
    """{CQ-id: {"choice": approve|skip|change, "note": str}}"""
    out = {}
    if path.suffix == ".md":
        for line in path.read_text(encoding="utf-8").splitlines():
            m = TICK_RE.match(line)
            if m:
                out[m.group("id")] = {"choice": "approve" if m.group("tick").lower() == "x" else "skip", "note": ""}
    else:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "decisions" in data:
            for d in data["decisions"]:
                out[d["id"]] = {"choice": d.get("choice", "skip"), "note": d.get("note", "")}
        else:  # queue.json itself: nothing approved unless --only
            for it in (data.get("items", []) if isinstance(data, dict) else data):
                out[it["id"]] = {"choice": "skip", "note": ""}
    if only:
        for cid in only:
            out[cid] = {"choice": "approve", "note": out.get(cid, {}).get("note", "")}
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("decisions", nargs="?", default=str(CURATION / "queue.md"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--by", default=curate.DEFAULT_BY)
    ap.add_argument("--today", default=None)
    ap.add_argument("--only", default=None, help="comma-separated CQ ids to approve regardless of ticks")
    ap.add_argument("--no-regen", action="store_true")
    args = ap.parse_args()
    today = args.today or dt.date.today().isoformat()

    items = load_queue()
    only = {x.strip() for x in args.only.split(",") if x.strip()} if args.only else None
    decisions = decisions_from(Path(args.decisions), only)

    all_fm, by_stem = curate.load_all()
    patches, events, todo, skipped, changed = [], [], [], [], []
    for cid, dec in sorted(decisions.items()):
        it = items.get(cid)
        if not it:
            skipped.append(f"{cid}: not in queue.json")
            continue
        if dec["choice"] == "change":
            changed.append(f"{cid}: {dec['note'] or 'change requested'} — re-issue as a curate.py command")
            continue
        if dec["choice"] != "approve":
            continue
        action, path, target = it.get("action"), it.get("path"), it.get("target")
        reason = it.get("rationale") or f"curation queue {cid}"
        try:
            if action == "archive":
                p, e = curate.act_archive(path, reason, args.by, today, superseded_by=target or None,
                                          all_fm=all_fm, by_stem=by_stem)
            elif action in ("supersede-with", "merge-into"):
                if not target:
                    raise SystemExit("no target")
                p, e = curate.act_supersede(path, target, reason=reason, by=args.by, all_fm=all_fm, by_stem=by_stem)
                if action == "merge-into":
                    todo.append(f"{cid}: merge the body of {path} into {target} (writer task; frontmatter done)")
            elif action in ("verify", "keep"):
                p, e = curate.act_verify(path, args.by, today, all_fm=all_fm, by_stem=by_stem)
            elif action == "update-figure":
                p, e = [], [{"by": args.by, "action": "update-figure-approved", "path": path, "to": target or "",
                             "reason": f"{cid}: {it.get('proposed_value') or ''} — body edit pending"}]
                todo.append(f"{cid}: update the figure in {path} to {it.get('proposed_value') or target} (writer task)")
            else:
                skipped.append(f"{cid}: unknown action {action}")
                continue
        except SystemExit as ex:
            skipped.append(f"{cid}: {ex}")
            continue
        for ev in e:
            ev["run_id"] = cid
        patches += p
        events += e

    # merge patches that touch the same file (later sets win)
    merged: dict[str, dict] = {}
    for p in patches:
        m = merged.setdefault(p["path"], {"path": p["path"], "set": {}, "delete": []})
        m["set"].update(p.get("set", {}))
        m["delete"] += [k for k in p.get("delete", []) if k not in m["delete"]]
    patches = [{k: v for k, v in m.items() if v or k == "path"} for m in merged.values()]

    print(f"{len(events)} approved item(s) → {len(patches)} file(s) to patch; {len(skipped)} skipped; {len(changed)} change requests")
    for s in skipped:
        print(f"  SKIP   {s}")
    for c in changed:
        print(f"  CHANGE {c}")
    if not patches and not events:
        return
    results = curate.apply_patches(patches, dry_run=args.dry_run) if patches else []
    if args.dry_run:
        print(f"--dry-run: {sum(1 for r in results if r['action'] == 'WOULD WRITE')} file(s) would change; nothing written, nothing logged")
        for t in todo:
            print(f"  TODO   {t}")
        return
    for ev in events:
        curate.log_event(**ev)
    print(f"{sum(1 for r in results if r['action'] == 'WRITE')} file(s) written; {len(events)} event(s) logged")
    for t in todo:
        print(f"  TODO   {t}")
    if not args.no_regen:
        for cmd in (["regen_index.py"], ["lint_blocks.py", "--json", str(ROOT / "work" / "lint_report.json"), "--today", today]):
            rc = subprocess.call([sys.executable, str(ROOT / "work" / cmd[0]), *cmd[1:]],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=str(ROOT))
            print(f"  {cmd[0]}: {'ok' if rc == 0 else 'exit ' + str(rc)}")
        subprocess.call([sys.executable, str(ROOT / "work" / "freshness.py"), "--today", today, "--quiet"], cwd=str(ROOT))
        print("  README status table (python work/status_counts.py --md):")
        subprocess.call([sys.executable, str(ROOT / "work" / "status_counts.py"), "--md"], cwd=str(ROOT))


if __name__ == "__main__":
    main()
