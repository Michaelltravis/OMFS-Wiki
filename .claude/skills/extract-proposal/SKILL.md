---
name: extract-proposal
description: Ingest a proposal PDF from raw/ into the content bank — verbatim page layer (local conversion, zero tokens), coverage gate, vision transcription for image-only pages, schema-v2 content blocks with back-pointers, registry and index updates. Use when the user asks to extract, process, ingest, or re-extract a proposal into the wiki.
---

# Extract a proposal into the content bank (v2)

Read the repo's `CLAUDE.md` first — it is the source of truth for the schema, sanitization rules, and folder layout. This skill is the runbook.

**Argument:** the PDF filename in `raw/` and its registry slug (ask if not given; register a new slug in the CLAUDE.md Source registry before starting).

## Principles (learned from the 2026 Hull pilot and its audit)

- **Script first.** The PDF text layer is exact. No model reads a page to transcribe text that has a text layer; the pilot did, and captured 37% of the Hull narrative verbatim with 15% reduced to recipes.
- **Measure, don't opine.** Completeness is a number per page (word-level recall against the PDF text layer), not a subagent's verdict.
- **Verbatim is the product.** `verbatim/<slug>/` holds the prose writers actually read. Sanitized blocks are the selection/metadata layer over it and must carry `verbatim-ref` back-pointers.
- **Keep every outcome figure.** Savings, complaint reductions, awards, compliance rates are proof value. Only commercial fee/rate figures are removed.
- **Prose, not descriptions of prose.** A block that says "Paragraph 1 — acknowledge investment" is `block-type: recipe` and must pair with the prose block it describes.

## Step 1 — Convert locally (zero model tokens)

```bash
python "<end-game-sales-suite>/scripts/convert.py" "raw/<file>.pdf"        # → raw/<file>.md, page-markered
python work/pdf_to_verbatim.py "raw/<file>.pdf" <slug>                       # → verbatim/<slug>/pages, full.md, manifest.json, renders/
python work/coverage.py "raw/<file>.pdf" <slug>                              # → verbatim/<slug>/coverage.md + .json
```

`pdf_to_verbatim.py` strips repeating headers/footers, numbers paragraphs (`<!-- ¶n -->`), backfills text blocks the converter dropped (from the raw text layer, under `<!-- recovered from text layer -->`), renders image-only pages at 300 DPI, and — when `verbatim/<slug>/vision/pNNNN.json` exists — writes vision-transcribed pages with `method: vision`.

**Gate:** word recall ≥0.99 per page and no missing run ≥15 words. Read `coverage.md`; flagged pages go to Step 2.

## Step 2 — Agent stages (Workflow tool, `.claude/workflows/extract-proposal.js`)

Run with `args: {slug, pdf, flaggedPages, imagePages}` taken from `coverage.json` and `manifest.json`. Stages:

1. **Page repair** (Sonnet, effort low) — one agent per flagged page reorders/repairs the page markdown using `renders/pNNNN.png` as reference; re-run `coverage.py`; loop until clean or 3 rounds, then flag residuals in `coverage.md`.
2. **Vision transcription** (image-only pages) — two independent Opus transcriptions per page (effort low) + a Sonnet refuting verifier that reconciles against the image. Verdicts: accept (≥97% agreement), accept-with-flags (`[illegible]` spans), reject (<85%, escalate). Results saved to `verbatim/<slug>/vision/pNNNN.json`; re-run `pdf_to_verbatim.py` to merge.
3. **Block build** (Opus, effort medium) — one writer per source section, reading only `verbatim/<slug>/pages/`. Writes schema-v2 blocks per `templates/content-block.md` with `source-pages`, `verbatim-ref`, `block-type`, facets, `proof-point-ids` placeholders (`PP-NEW-n`) for every number. Never overwrite an existing file; pick a more specific name.
4. **Prose judge** (Fable, effort medium) — for each new `prose` block: "is this the prose or a paraphrase of `verbatim-ref`?" Paraphrases are rewritten from the verbatim text.
5. **Registry increment** (Opus) — harvest new quantified claims → `proof-points/registry.md` (reconcile against existing ids; mark conflicts), quotes → `testimonials/inventory.md` (permission `unknown` by default), narratives → `stories/catalog.md` (Fable names the beat).
6. **Merge and index** — Sonnet finds duplicate-topic candidates against existing blocks; Fable judge sets `status: preferred|fallback` (links as `wiki/<cat>/<file>.md`, reciprocal; every decision appended to `work/curation/log.jsonl` as `ingest-merge`); `python work/regen_index.py` rebuilds `wiki/index.md` and `index.json`; tags validated against `vocabulary/tags.md`.
7. **Currency pass** — `python work/freshness.py --today <today> --write --source <slug>` stamps `volatility` / `review-due` / `freshness-flags` on the new blocks; `python work/dedupe_candidates.py --min 0.12 --new-only <slug> --skip-linked` lists what the new source still duplicates in the bank — those pairs go to the next `/curate` run, not decided here. Pass `today` in the workflow args (scripts cannot read the clock).

Agents write fragments; scripts merge shared files (index, registry). Resume with the run id if interrupted.

## Step 3 — Verify and report

- Narrative categories: zero body-text hits for the pursuit client's name (`source:` slug and asset IDs exempt). No commercial fee/rate figures anywhere.
- Every block resolves its `verbatim-ref`; every number resolves to a registry id or is tagged `unregistered`.
- Update the status table in `README.md` (pages, image-only pages, mean word recall, blocks by category, registry rows added) and note source-document defects verbatim (never silently fix source data).

## Model and effort policy

Scripts for conversion, cleanup, coverage, indexing. Sonnet low for page repair, verification, dedupe candidates. Opus low for vision transcription (dual), Opus medium for block writing and registry harvest. Fable medium for prose/paraphrase and preferred/fallback judgments. The main session never reads proposal pages.
