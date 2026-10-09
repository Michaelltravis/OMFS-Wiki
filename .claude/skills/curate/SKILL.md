---
name: curate
description: Keep the content bank current — report what is stale or contradicted, run the curation pass that proposes keep / verify / update-figure / supersede / archive with evidence, apply the maintainer's ticked decisions, and carry out direct lifecycle instructions. Use when the user says "what's stale", "what needs review", "curate the wiki", "run a curation pass", "archive X", "X is out of date", "X was superseded by Y", "I verified X", "mark X as current", "apply the curation queue", "approve CQ-…", or asks what changed in the bank since a date. Scripts run at zero tokens; the curation pass runs Sonnet triage and Fable judging.
---

# Curate the content bank

Content decays: people move, reference contacts change, corporate figures and safety stats are restated every year, legislation moves, and a newer proposal supersedes an older one's claim. The curation layer makes that computable and keeps the human in the loop for every status change. Read the repo `CLAUDE.md` section **Keeping the bank current** first.

**The rule that never bends:** scripts and agents *propose*; the maintainer *confirms*; `curate.py` / `apply_curation.py` *apply*. Nothing flips `status`, sets `supersedes`, or archives a block without a yes from the user in this chat (or their own ticks in `work/curation/queue.md`). Derived metadata (`volatility`, `review-due`, `freshness-flags`) may be written without asking — it is computed, not decided. Bodies and `verbatim/` are never edited by anything here.

## 0. Environment

`python -c "import yaml, docx, fitz"` must succeed (`python -m pip install pyyaml python-docx pymupdf`). Without pyyaml the index scripts refuse to run.

## 1. "What's stale?" — answer from the report (zero tokens)

```
python work/freshness.py --today <today ISO> --write
```

writes `work/curation/report.md` + `report.json` and stamps the derived fields. Answer from `report.md`: counts (flagged, overdue, registry conflicts, unlinked duplicate pairs), **Overdue by owner**, the top-ranked blocks, duplicate people, registry conflicts. Send `report.md` with `SendUserFile` if the user wants the whole thing. `--only-overdue`, `--only-flagged`, `--source <slug>` narrow it. Do not start the agent pass for a question.

## 2. "Curate the wiki" — the curation pass (Workflow tool)

```
Workflow({ scriptPath: "<repo>\\.claude\\workflows\\curate.js",
           args: { wiki: "<repo>", today: "<today ISO>", scope: "attention", maxItems: 120 } })
```

- `today` is **required** — workflow scripts cannot read the clock; pass the session date.
- `scope`: `attention` (flagged or overdue, default) · `flagged` · `overdue` · `source:<slug>` · `paths` (with `paths: [...]`). Start with `maxItems: 40` on a first run.
- Phases: Detect (scripts) → Triage (Sonnet, batches of 8) → Judge (Fable, supersede / merge / archive proposals only) → Queue (`work/build_queue.py`). Resume with `resumeFromRunId` if interrupted.
- The workflow **applies nothing**. It writes `work/curation/queue.md` (tick list grouped by owner) and `queue.json`.
- Send `queue.md` (and `report.md`) with `SendUserFile`; reply with the counts by action and the top five items in one line each. Mark any `(unverified ref)` evidence.

## 3. Applying decisions

The user ticks `- [x]` in `queue.md`, or says "approve CQ-0001, CQ-0004" / "apply all the verify items":

```
python work/apply_curation.py --dry-run [--only CQ-0001,CQ-0004] --today <today ISO>
python work/apply_curation.py [--only ...] --today <today ISO>
```

Always show the dry run first and get a yes. The apply step patches frontmatter, logs each item to `work/curation/log.jsonl`, regenerates the index, lints, refreshes the report, and prints the README status table (paste it into `README.md`'s status section). `update-figure` and `merge-into` items print TODO lines — the body edits are a writer's job; offer to do them as a separate step.

## 4. Direct instructions → `work/curate.py`

| user says | run (always `--dry-run` first, then without) |
|---|---|
| "archive X", "retire X", "X is dead" | `python work/curate.py archive <path-or-stem> --reason "<their words>" [--superseded-by <winner>] --today <today>` |
| "bring X back" | `python work/curate.py unarchive <path-or-stem>` |
| "X was superseded by Y", "use Y instead of X" | `python work/curate.py supersede <X> --winner <Y> --reason "<why>"` |
| "I verified X", "X is current", "the account team confirmed X" | `python work/curate.py verify <X> --by "<name>" --today <today>` |
| "X is out of date", "flag X", "note that X …" | `python work/curate.py flag <X> --note "<their words>"` (and `--flag <enum>` if it maps to one) |
| "PP-0167 is Rachel's number" | `python work/curate.py owner PP-0167 --set "Rachel …"` |
| "what did we change" | `python work/curate.py log --last 30` |

`archive` refuses a block that is the winner for a live fallback block or is named in `templates/standard-topics.md`; relay the message and ask how to re-point before using `--force`. `<path-or-stem>` accepts the bare filename stem.

## 5. After the pass

Commit `work/curation/{report,queue,log,policy,sources}.*`, the touched blocks, `wiki/index.*`, and the README status line. Mention in the reply how many items remain unticked in the queue.

## Rules

- Never archive, unarchive, supersede or flip status on your own judgment — not even for an obvious duplicate. Propose; wait for the yes.
- Never edit a block body, `verbatim/`, `proof-points/registry.json` values, or `sources.json` dates to make a flag go away. Tune `work/curation/policy.json` intervals only when the user asks.
- The date comes from the session (`today`), never from inside a workflow script.
- Fable only in the Judge phase; Sonnet for triage and runners; scripts for everything deterministic.
