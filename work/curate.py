#!/usr/bin/env python3
"""curate.py — the human-confirmed lifecycle actions on content blocks (zero model tokens).

Every mutating subcommand builds frontmatter patches, shows them, applies them through
work/patch_frontmatter.py (bodies are never touched), appends a line to
work/curation/log.jsonl, and then rebuilds wiki/index.md and runs lint (skip with
--no-regen). --dry-run shows the patches and writes nothing. <path> may be a repo-relative
path or a bare block stem (resolved against wiki/*/).

    python work/curate.py archive   <path> --reason "<why>" [--superseded-by <path>] [--by NAME] [--today D] [--force] [--dry-run]
    python work/curate.py unarchive <path> [--status preferred|fallback] [--dry-run]
    python work/curate.py supersede <loser> --by <winner> [--reason "<why>"] [--dry-run]
    python work/curate.py verify    <path> [--by NAME] [--today D] [--dry-run]
    python work/curate.py flag      <path> (--flag <freshness-flag> | --note "<text>") [--dry-run]
    python work/curate.py owner     PP-0001 --set "<name>"
    python work/curate.py normalize-links [--dry-run]
    python work/curate.py feedback  --pursuit <slug> --section <id> --json <fact-check.json> [--by NAME]
    python work/curate.py log       [--last N]
    python work/curate.py note-update <path> --note "<what changed, from which source>" [--pp PP-0001,PP-0002] [--today D] [--by NAME]

Rules the subcommands enforce:
  - archive refuses (without --force) a block that is the superseded-by winner of a live
    block, or that templates/standard-topics.md names as a preferred topic block.
  - supersede sets loser: status fallback + superseded-by winner; winner: supersedes
    += loser. Reciprocity is always written to both sides.
  - verify sets last-verified = today and verified-by = NAME, so the block's review clock
    (work/freshness.py) restarts from the human check rather than the source proposal date.
  - Only the maintainer's confirmation (or an explicit instruction in chat) should trigger
    archive / unarchive / supersede; the curate skill never calls them on its own.
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

from lint_blocks import CATEGORY_DIRS, FLAG_ENUM, LINK_PATH_RE, as_list, link_stem, link_targets, load_frontmatter  # noqa: E402
from patch_frontmatter import apply_patches  # noqa: E402

CURATION = ROOT / "work" / "curation"
LOG = CURATION / "log.jsonl"
FEEDBACK = CURATION / "feedback.jsonl"
DEFAULT_BY = "Michael Travis"
PP_RE = re.compile(r"\bPP-\d{4}\b")
PATH_RE = re.compile(r"wiki/[a-z-]+/[^\s)\]|`'\"]+\.md")


# --- shared -----------------------------------------------------------------------------
def load_all():
    """{repo-relative path: frontmatter} for every block, plus stem -> [paths]."""
    all_fm, by_stem = {}, {}
    for cat in CATEGORY_DIRS:
        d = ROOT / "wiki" / cat
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            fm, _b, err = load_frontmatter(p.read_text(encoding="utf-8"))
            if err:
                continue
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            all_fm[rel] = fm
            by_stem.setdefault(p.stem, []).append(rel)
    return all_fm, by_stem


def resolve(target: str, all_fm, by_stem) -> str | None:
    t = str(target).replace("\\", "/").strip()
    t = t[len(str(ROOT).replace("\\", "/")) + 1:] if t.startswith(str(ROOT).replace("\\", "/")) else t
    if t in all_fm:
        return t
    hits = by_stem.get(link_stem(t), [])
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        raise SystemExit(f"ambiguous block '{target}': {', '.join(hits)}")
    return None


def must_resolve(target, all_fm, by_stem) -> str:
    r = resolve(target, all_fm, by_stem)
    if r is None:
        raise SystemExit(f"no such block: {target}")
    return r


def today_of(args) -> str:
    return args.today if getattr(args, "today", None) else dt.date.today().isoformat()


def log_event(**row):
    CURATION.mkdir(parents=True, exist_ok=True)
    row = {"ts": dt.datetime.now().isoformat(timespec="seconds"), **row}
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def merged_links(current, add: list[str], drop: list[str] = ()) -> list[str]:
    out = []
    for t in link_targets(current) + list(add):
        if t not in out and t not in drop:
            out.append(t)
    return out


def link_value(paths: list[str]):
    return paths[0] if len(paths) == 1 else paths


def finish(patches, args, events):
    """Show, apply (unless dry-run), log, regen + lint."""
    if not patches:
        print("nothing to change")
        return
    results = apply_patches(patches, dry_run=args.dry_run)
    if args.dry_run:
        print(f"--dry-run: {sum(1 for r in results if r['action'] == 'WOULD WRITE')} file(s) would change; nothing written")
        return
    for ev in events:
        log_event(**ev)
    print(f"{sum(1 for r in results if r['action'] == 'WRITE')} file(s) written; logged {len(events)} event(s) to {LOG.relative_to(ROOT)}")
    if not getattr(args, "no_regen", False):
        for cmd in (["regen_index.py"], ["lint_blocks.py", "--json", str(ROOT / "work" / "lint_report.json")]):
            rc = subprocess.call([sys.executable, str(ROOT / "work" / cmd[0]), *cmd[1:]],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=str(ROOT))
            print(f"  {cmd[0]}: {'ok' if rc == 0 else 'exit ' + str(rc)}")


# --- actions (return patches + log events; also used by apply_curation.py) --------------
def act_archive(path, reason, by, today, superseded_by=None, force=False, all_fm=None, by_stem=None):
    all_fm, by_stem = (all_fm, by_stem) if all_fm else load_all()
    path = must_resolve(path, all_fm, by_stem)
    fm = all_fm[path]
    if fm.get("status") == "archived":
        raise SystemExit(f"{path} is already archived")
    if not force:
        dependents = [p for p, f in all_fm.items() if f.get("status") != "archived" and p != path
                      and link_stem(path) in {link_stem(t) for t in link_targets(f.get("superseded-by"))}]
        if dependents:
            raise SystemExit(f"refusing: {path} is the superseded-by winner of live block(s) {', '.join(dependents)} "
                             f"(re-point them first, or --force)")
        st = ROOT / "templates" / "standard-topics.md"
        if st.is_file() and (path in st.read_text(encoding="utf-8") or (Path(path).stem + ".md") in st.read_text(encoding="utf-8")):
            raise SystemExit(f"refusing: {path} is named in templates/standard-topics.md as a standard-topic block "
                             f"(replace it there first, or --force)")
    sets = {"status": "archived", "archive-reason": reason, "archived-date": today, "archived-by": by}
    sets["archived-from-status"] = str(fm.get("status") or "preferred")
    if fm.get("house-favorite") is True:
        sets["house-favorite"] = False
    events = []
    patches = []
    if superseded_by:
        winner = must_resolve(superseded_by, all_fm, by_stem)
        sets["superseded-by"] = link_value(merged_links(fm.get("superseded-by"), [winner]))
        wfm = all_fm[winner]
        patches.append({"path": winner, "set": {"supersedes": link_value(merged_links(wfm.get("supersedes"), [path]))}})
    patches.insert(0, {"path": path, "set": sets})
    events.append({"by": by, "action": "archive", "path": path, "from": fm.get("status"), "to": "archived",
                   "reason": reason, "to_block": superseded_by and winner})
    return patches, events


def act_unarchive(path, status=None, by=DEFAULT_BY, all_fm=None, by_stem=None):
    all_fm, by_stem = (all_fm, by_stem) if all_fm else load_all()
    path = must_resolve(path, all_fm, by_stem)
    fm = all_fm[path]
    if fm.get("status") != "archived":
        raise SystemExit(f"{path} is not archived (status {fm.get('status')})")
    new_status = status or str(fm.get("archived-from-status") or "preferred")
    if new_status == "fallback" and not link_targets(fm.get("superseded-by")):
        new_status = "preferred"
    patches = [{"path": path, "set": {"status": new_status},
                "delete": ["archive-reason", "archived-date", "archived-by", "archived-from-status"]}]
    events = [{"by": by, "action": "unarchive", "path": path, "from": "archived", "to": new_status, "reason": ""}]
    return patches, events


def act_supersede(loser, winner, reason="", by=DEFAULT_BY, all_fm=None, by_stem=None):
    all_fm, by_stem = (all_fm, by_stem) if all_fm else load_all()
    loser = must_resolve(loser, all_fm, by_stem)
    winner = must_resolve(winner, all_fm, by_stem)
    if loser == winner:
        raise SystemExit("loser and winner are the same block")
    lfm, wfm = all_fm[loser], all_fm[winner]
    if wfm.get("status") == "archived":
        raise SystemExit(f"winner {winner} is archived")
    lsets = {"status": "fallback" if lfm.get("status") != "archived" else "archived",
             "superseded-by": link_value(merged_links(lfm.get("superseded-by"), [winner]))}
    if lfm.get("house-favorite") is True:
        lsets["house-favorite"] = False
    wsets = {"supersedes": link_value(merged_links(wfm.get("supersedes"), [loser]))}
    if wfm.get("status") == "fallback":
        wsets["status"] = "preferred"  # a winner is by definition the live block
    # the winner must not still claim to be superseded by the loser
    w_by = [t for t in link_targets(wfm.get("superseded-by")) if link_stem(t) != link_stem(loser)]
    if len(w_by) != len(link_targets(wfm.get("superseded-by"))):
        if w_by:
            wsets["superseded-by"] = link_value(w_by)
    patches = [{"path": loser, "set": lsets}, {"path": winner, "set": wsets}]
    if not w_by and link_targets(wfm.get("superseded-by")):
        patches[1]["delete"] = ["superseded-by"]
    events = [{"by": by, "action": "supersede", "path": loser, "to": winner, "from": lfm.get("status"),
               "reason": reason}]
    return patches, events


def act_verify(path, by, today, all_fm=None, by_stem=None):
    all_fm, by_stem = (all_fm, by_stem) if all_fm else load_all()
    path = must_resolve(path, all_fm, by_stem)
    patches = [{"path": path, "set": {"last-verified": today, "verified-by": by}}]
    events = [{"by": by, "action": "verify", "path": path, "from": str(all_fm[path].get("last-verified") or ""),
               "to": today, "reason": ""}]
    return patches, events


def act_flag(path, flag=None, note=None, by=DEFAULT_BY, all_fm=None, by_stem=None):
    all_fm, by_stem = (all_fm, by_stem) if all_fm else load_all()
    path = must_resolve(path, all_fm, by_stem)
    fm = all_fm[path]
    patches, events = [], []
    if flag:
        if flag not in FLAG_ENUM:
            raise SystemExit(f"unknown flag {flag}; one of {sorted(FLAG_ENUM)}")
        flags = sorted({*[str(x) for x in as_list(fm.get("freshness-flags"))], flag})
        patches.append({"path": path, "set": {"freshness-flags": flags}})
        events.append({"by": by, "action": "flag", "path": path, "to": flag, "reason": note or ""})
    if note:
        # a free-text note is a feedback entry: the next freshness run surfaces it as the `feedback` flag
        CURATION.mkdir(parents=True, exist_ok=True)
        with FEEDBACK.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": dt.datetime.now().isoformat(timespec="seconds"), "pursuit": "", "section": "",
                                "text": note, "reason": "maintainer note", "fix": "", "pp_ids": [],
                                "block_paths": [path], "source": f"curate.py flag ({by})"}, ensure_ascii=False) + "\n")
        if not flag:
            flags = sorted({*[str(x) for x in as_list(fm.get("freshness-flags"))], "feedback"})
            patches.append({"path": path, "set": {"freshness-flags": flags}})
            events.append({"by": by, "action": "flag", "path": path, "to": "feedback", "reason": note})
    return patches, events


# --- normalize-links --------------------------------------------------------------------
def normalize_links(dry_run: bool, by=DEFAULT_BY):
    all_fm, by_stem = load_all()
    patches, events, decisions = [], [], []
    desired = {p: {} for p in all_fm}  # path -> {key: [targets]}

    # 1. canonical form for every link value
    for path, fm in all_fm.items():
        for key in ("supersedes", "superseded-by"):
            if key not in fm or fm.get(key) in (None, "", []):
                continue
            targets = []
            for t in link_targets(fm.get(key)):
                r = resolve(t, all_fm, by_stem)
                if r is None:
                    print(f"  dead link kept as-is: {path} {key}: {t}")
                    targets.append(t)
                else:
                    targets.append(r)
            desired[path][key] = targets

    # 2. reciprocity
    for path, keys in list(desired.items()):
        for key, targets in list(keys.items()):
            rev = "superseded-by" if key == "supersedes" else "supersedes"
            for t in targets:
                if t not in all_fm:
                    continue
                have = desired[t].get(rev)
                if have is None:
                    have = [resolve(x, all_fm, by_stem) or x for x in link_targets(all_fm[t].get(rev))]
                    desired[t][rev] = have
                if path not in have:
                    have.append(path)

    # 3. patches where the canonical value differs from what is on disk
    for path, keys in desired.items():
        sets = {}
        for key, targets in keys.items():
            cur = link_targets(all_fm[path].get(key))
            if cur != targets:
                sets[key] = link_value(targets)
        if sets:
            patches.append({"path": path, "set": sets})
            events.append({"by": by, "action": "normalize-links", "path": path, "to": json.dumps(sets), "reason": "canonical paths + reciprocity"})

    # 4. status contradictions are decisions, not fixes
    for path, fm in all_fm.items():
        st = fm.get("status")
        winners = desired[path].get("superseded-by", link_targets(fm.get("superseded-by")))
        if st == "preferred" and winners:
            decisions.append(f"{path}: preferred but superseded-by {winners} — delete superseded-by, or flip to fallback?")
        if st == "fallback" and not winners:
            decisions.append(f"{path}: fallback with no winner — archive, or flip to preferred?")
        if st == "fallback" and fm.get("house-favorite") is True:
            decisions.append(f"{path}: fallback AND house-favorite — make it the preferred block, or drop house-favorite?")

    print(f"normalize-links: {len(patches)} block(s) to rewrite, {len(decisions)} decision(s) for the maintainer")
    for d in decisions:
        print(f"  DECIDE  {d}")
    return patches, events


def act_note_update(path, note, by, today, pp_ids=(), all_fm=None, by_stem=None):
    """Stamp a block that just had a figure brought to a newer source's value: `updated`,
    `update-notes` (appended, newest first), proof-point-ids extended; logged."""
    all_fm, by_stem = (all_fm, by_stem) if all_fm else load_all()
    path = must_resolve(path, all_fm, by_stem)
    fm = all_fm[path]
    prev = str(fm.get("update-notes") or "").strip()
    text = f"{today}: {note}" + (f" | {prev}" if prev else "")
    patch = {"path": path, "set": {"updated": today, "update-notes": text}}
    if pp_ids:
        patch["append"] = {"proof-point-ids": list(pp_ids)}
    events = [{"by": by, "action": "update-figure-applied", "path": path, "to": note, "from": "", "reason": "see update-notes"}]
    return [patch], events


# --- owner, feedback, log ---------------------------------------------------------------
def set_owner(pp_id: str, owner: str, by=DEFAULT_BY):
    reg_path = ROOT / "proof-points" / "registry.json"
    rows = json.loads(reg_path.read_text(encoding="utf-8"))
    hit = next((r for r in rows if r.get("id") == pp_id), None)
    if not hit:
        raise SystemExit(f"no registry row {pp_id}")
    old = hit.get("owner", "")
    hit["owner"] = owner
    reg_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    log_event(by=by, action="owner", path=pp_id, **{"from": old}, to=owner, reason="")
    print(f"{pp_id}: owner {old!r} -> {owner!r} (registry.json; rerun build_proof_point_registry.py to refresh registry.md)")


def record_feedback(pursuit: str, section: str, json_path: str, by=DEFAULT_BY):
    """Turn a write-section fact-check result ({unsupported:[{text, reason, fix}]}) into
    feedback.jsonl lines, resolving PP ids and block paths through the registry."""
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))
    items = data.get("unsupported") if isinstance(data, dict) else data
    items = items or []
    reg = {r["id"]: r for r in json.loads((ROOT / "proof-points" / "registry.json").read_text(encoding="utf-8")) if r.get("id")}
    n = 0
    CURATION.mkdir(parents=True, exist_ok=True)
    with FEEDBACK.open("a", encoding="utf-8") as f:
        for it in items:
            blob = json.dumps(it, ensure_ascii=False)
            pp_ids = sorted(set(PP_RE.findall(blob)))
            paths = set(PATH_RE.findall(blob))
            for pid in pp_ids:
                for v in (reg.get(pid) or {}).get("values", []):
                    if v.get("block"):
                        paths.add(str(v["block"]).replace("\\", "/"))
            row = {"ts": dt.datetime.now().isoformat(timespec="seconds"), "pursuit": pursuit, "section": section,
                   "text": it.get("text") if isinstance(it, dict) else str(it),
                   "reason": (it.get("reason") if isinstance(it, dict) else "") or "",
                   "fix": (it.get("fix") if isinstance(it, dict) else "") or "",
                   "pp_ids": pp_ids, "block_paths": sorted(paths), "source": f"write-section/fact-check ({by})"}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            n += 1
    log_event(by=by, action="feedback", path=f"pursuits/{pursuit}", to=section, reason=f"{n} fact-check finding(s) recorded")
    print(f"recorded {n} feedback line(s) in {FEEDBACK.relative_to(ROOT)}; run python work/freshness.py to surface them")


def show_log(last: int):
    if not LOG.is_file():
        print("no curation log yet")
        return
    lines = LOG.read_text(encoding="utf-8").splitlines()
    for line in lines[-last:]:
        try:
            r = json.loads(line)
            print(f"{r.get('ts','')}  {r.get('action',''):16} {r.get('path','')}  {('-> ' + str(r.get('to'))) if r.get('to') else ''}  {r.get('reason','')}")
        except Exception:
            print(line)


# --- CLI --------------------------------------------------------------------------------
def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, today=False):
        p.add_argument("--by", default=DEFAULT_BY)
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--no-regen", action="store_true", help="skip regen_index + lint afterwards")
        if today:
            p.add_argument("--today", default=None)

    p = sub.add_parser("archive"); p.add_argument("path"); p.add_argument("--reason", required=True)
    p.add_argument("--superseded-by", default=None); p.add_argument("--force", action="store_true"); common(p, today=True)
    p = sub.add_parser("unarchive"); p.add_argument("path"); p.add_argument("--status", choices=["preferred", "fallback"], default=None); common(p)
    p = sub.add_parser("supersede"); p.add_argument("loser"); p.add_argument("--by-block", "--winner", dest="winner", required=True)
    p.add_argument("--reason", default=""); common(p)
    p = sub.add_parser("verify"); p.add_argument("path"); common(p, today=True)
    p = sub.add_parser("flag"); p.add_argument("path"); p.add_argument("--flag", default=None); p.add_argument("--note", default=None); common(p)
    p = sub.add_parser("owner"); p.add_argument("pp_id"); p.add_argument("--set", dest="owner", required=True); p.add_argument("--by", default=DEFAULT_BY)
    p = sub.add_parser("normalize-links"); common(p)
    p = sub.add_parser("feedback"); p.add_argument("--pursuit", required=True); p.add_argument("--section", required=True)
    p.add_argument("--json", dest="json_path", required=True); p.add_argument("--by", default=DEFAULT_BY)
    p = sub.add_parser("log"); p.add_argument("--last", type=int, default=30)
    p = sub.add_parser("note-update"); p.add_argument("path"); p.add_argument("--note", required=True)
    p.add_argument("--pp", default="", help="comma-separated PP ids to add to proof-point-ids"); common(p, today=True)
    args = ap.parse_args()

    if args.cmd == "archive":
        patches, events = act_archive(args.path, args.reason, args.by, today_of(args), superseded_by=args.superseded_by, force=args.force)
    elif args.cmd == "unarchive":
        patches, events = act_unarchive(args.path, status=args.status, by=args.by)
    elif args.cmd == "supersede":
        patches, events = act_supersede(args.loser, args.winner, reason=args.reason, by=args.by)
    elif args.cmd == "verify":
        patches, events = act_verify(args.path, args.by, today_of(args))
    elif args.cmd == "flag":
        if not (args.flag or args.note):
            raise SystemExit("flag needs --flag <enum> and/or --note <text>")
        patches, events = act_flag(args.path, flag=args.flag, note=args.note, by=args.by)
    elif args.cmd == "owner":
        return set_owner(args.pp_id, args.owner, by=args.by)
    elif args.cmd == "normalize-links":
        patches, events = normalize_links(args.dry_run, by=args.by)
    elif args.cmd == "feedback":
        return record_feedback(args.pursuit, args.section, args.json_path, by=args.by)
    elif args.cmd == "log":
        return show_log(args.last)
    elif args.cmd == "note-update":
        patches, events = act_note_update(args.path, args.note, args.by, today_of(args),
                                          pp_ids=[x.strip() for x in args.pp.split(",") if x.strip()])
    else:
        raise SystemExit(ap.format_usage())
    finish(patches, args, events)


if __name__ == "__main__":
    main()
