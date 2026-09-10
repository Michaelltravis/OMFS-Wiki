---
name: content-plan
description: Build a pursuit's content plan — the topics each proposal section will cover — from the Proposal Directive, publish an interactive checklist page for the proposal manager to tick, and write the selections back. Use when the user says "content plan", "select topics", "what goes in each section", "set up the plan for <pursuit>", or hands over a Proposal Directive before the spec sheet exists. Runs on Sonnet; no Fable needed.
---

# Content plan (selection sheet)

The content plan sits before the spec sheet: sections in Proposal Directive order, each with the RFP-required topics (already ticked) and the Jacobs-standard topics from `templates/standard-topics.md` that the proposal manager decides on. Ticked topics are the only ones the spec sheet plans for and the writers draft. This skill does selection work only — run it on **Sonnet**.

## Inputs to collect

- Pursuit slug (`pursuits/<slug>/`) and the Proposal Directive `.docx` path (it must carry the PROPOSAL OUTLINE and EVALUATION CRITERIA tables from `proposal-directive-creator`).
- Optional: the RFP requirement exports in `pursuits/<slug>/reqs/` (from the same skill) for the cross-check; a display name for the pursuit.

## Steps

1. **Scaffold** (zero tokens):
   `python work/new_content_plan.py <slug> --directive "<Directive.docx>" --name "<pursuit name>"`
   Refuses to overwrite an existing plan; pass `--force` only if the user says to start over. Read the WARNING lines — a missing block path means `templates/standard-topics.md` needs fixing.
2. **Build the checklist page** (zero tokens):
   `python work/content_plan_page.py <slug>` → `pursuits/<slug>/content-plan-page.html`
3. **Publish** it with the Artifact tool: `file_path` = that html, `capabilities: {db: {}}`, `favicon: "☑"`, a one-sentence `description`. Republish to the same file path after any regeneration so the link stays stable. Give the proposal manager the link; they tick topics, set marks (include / lead / brief), add angles and pursuit-specific topics, optionally point any row at a specific block or page range with **Pull from** (type-ahead over every wiki block and every source section), optionally pick a **Start from** source section for any section (a past proposal section the writer adapts first — the dropdown lists every extracted proposal's sections with page ranges), and press **Save selections**. Anyone in the organization with the link can edit; the page shows the last save time.
4. **Read the selections back** when the user says they are done: Artifact `action: "read_db"`, `db_op: "get"`, `collection: "plans"`, `doc_id: "<slug>"`, `out_dir: "<scratchpad>"` → `<scratchpad>/plans/<slug>.json`.
5. **Apply and render**:
   `python work/apply_content_plan.py <slug> "<scratchpad>/plans/<slug>.json" --docx`
   Sets `status: selected`, writes the marks and pursuit-specific rows into `content-plan.md`, and renders `Content_Plan_SELECTED.docx`. Send the docx with SendUserFile and summarize: topics ticked per section, pursuit-specific topics added, anything the PM noted for the writers.
6. Hand off: the spec-sheet workflow (`.claude/workflows/spec-sheet.js`) and `write-section.js` read `content-plan.md` automatically.

## Rules

- Never tick or untick a topic yourself; the selections are the proposal manager's. If they ask for a recommendation, give it in chat and let them tick.
- Never edit `templates/standard-topics.md` during a pursuit without saying so — it is the house list for every pursuit.
- Fee/cost sections are headings only (estimating owns them); do not add topics there.
- If the db capability is unavailable in the viewer, the page still works for on-screen selection; ask the PM to tell you their picks and apply them by editing `content-plan.md` directly.
