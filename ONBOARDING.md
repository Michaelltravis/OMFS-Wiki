# Proposal Content Wiki — Onboarding Guide

Welcome. This folder is Jacobs' water & wastewater O&M **proposal content wiki**: a library of our best proposal content, extracted from winning proposals into modular, tagged markdown blocks that both people and AI agents can use to draft full sections of future RFP responses.

Maintained by Michael Travis (Michael.Travis@jacobs.com). Questions and QC issues go to him.

## What's in here

```
CLAUDE.md          The rulebook. Claude Code reads it automatically; humans should too.
README.md          Short overview + extraction status per source proposal.
raw/               Original proposal PDFs. IMMUTABLE — never edit, never quote directly.
wiki/index.md      Master index of every content block (browse this first).
wiki/<category>/   The content: technical-approach, management-staffing, win-themes,
                   qualifications, compliance-plans, resumes, past-performance.
wiki/graphics/     Exhibit catalogs — text references only; asset IDs resolve in the
                   Jacobs graphics library/DAM.
templates/         The content-block template for new entries.
.claude/skills/    Reusable workflows (see below).
```

## The two content tiers — know the difference

1. **Reusable narrative blocks** (technical-approach, management-staffing, win-themes, qualifications, compliance-plans): the pursuit client is generalized to `[CLIENT]`, commercial pricing is excluded, everything else (facility specs, outcome figures, savings) is real. Drop-in starting points for new drafts.
2. **Verbatim blocks** (resumes, past-performance): real names, contacts, fees, clients — captured exactly as proposed. **The proposal team must QC these before anything goes external** (confirm contacts are current, figures are approved, references have consented to be named).

## Using the wiki to draft a proposal section

1. Open this folder in Claude Code.
2. Give Claude your pursuit documents: the client's RFP + addenda, scope of work, and the Jacobs proposal directive.
3. Ask for the section you need (e.g., "Draft the transition plan section for this RFP"). Claude follows the drafting workflow in `CLAUDE.md`: compliance-first outline from the RFP, pull blocks by tag, tailor, fill every `[PLACEHOLDER]`, and recommend graphics by asset ID.
4. Review the draft. Nothing leaves with an unreplaced placeholder or unverified fact.

## Adding a new proposal to the wiki

1. Drop the PDF in `raw/`.
2. In Claude Code, run `/extract-proposal <filename>`. The skill runs the full proven pipeline: parallel extraction agents, a mandatory second-pass completeness audit, graphics cataloging by asset ID, index regeneration, and a sanitization sweep.
3. Review the report it produces — especially any flagged source-document defects — and spot-check a few blocks.

## Golden rules

- **Content blocks are starting points, not final text.** Verbatim boilerplate loses evaluations — always tailor to the client's drivers and evaluation criteria.
- **Never edit `raw/`.** It is the provenance record.
- **Graphics are never embedded.** Look up the asset ID in `wiki/graphics/`, request the file from the Jacobs graphics library/DAM, and re-brand anything flagged `client-specific: true`.
- **Verbatim content gets QC'd** before external use. When a source document itself has an error, we capture it verbatim and flag it in reuse-notes — never silently fix source data.
- **Token efficiency:** heavy PDF reading always runs in Sonnet subagents, never the main session. The skills handle this automatically.

## Current status

See the status table in `README.md`. As of September 2026: Hull WWTF (2026), Santa Monica SWIP (2025), OCWUT 16-26, Fulton County 25RFP146289K, and MMSD O&M (2028) are all extracted and completeness-audited.

## Handing this repo to another person or account

Everything a new owner needs to read, search, pull sections and run the scripts is in git. Three things are deliberately **not** in git and must be copied by hand (a shared drive or a direct transfer) or regenerated:

| Not in git | Size | Why | How to get it |
|---|---|---|---|
| `raw/*.pdf` — the five source proposals | ~245 MB | `*.pdf` is gitignored (client documents) | Copy from the previous owner. The `raw/*.md` converter outputs ARE in git, and every `verbatim/<slug>/` page file is too, so all text work runs without the PDFs. The PDFs are only needed to re-run `work/coverage.py`, `work/render_flagged_pages.py`, or `work/pdf_to_verbatim.py`. |
| `verbatim/<slug>/renders/` — 300-DPI page images for image-only pages | ~205 MB | binary, regenerable | `python work/render_flagged_pages.py raw/<file>.pdf <slug> verbatim/<slug>/coverage.json` (needs the PDF). Only vision transcription and page repair use them. |
| `work/pulls/` — assembled section pulls | small | generated output | `python work/assemble_section.py <slug> "<section>"` regenerates any pull in seconds. |

Also outside the repo:

- **GitHub access.** The remote is `https://github.com/Michaelltravis/OMFS-Wiki.git`. The repo owner adds the new account as a collaborator (Settings › Collaborators) or transfers the repository (Settings › General › Transfer ownership). Nothing in the repo is tied to a GitHub account name.
- **Claude Code session memory.** The previous owner's Claude Code sessions kept a few notes outside the repo (pursuit status such as the Richmond 2026 spec-sheet decisions). The durable state of every pursuit is in `pursuits/<slug>/` (spec sheet, content plan, requirement exports); the notes only summarized those files. A new account starts from `CLAUDE.md` and this file with nothing lost.
- **The Richmond content-plan checklist artifact** (claude.ai link in `pursuits/richmond-2026/`) is bound to the account that published it; `pursuits/richmond-2026/content-plan.md` is the source of truth and `work/apply_content_plan.py` re-applies selections from it.

Python 3.12+ with `pymupdf`, `pyyaml`, `python-docx` (see `PORTING.md` for the full environment) is the only local dependency. Every script prints its usage with `--help`.

**Where the work stands (September 2026):** all five sources are extracted, every block carries `section-id` / `section-path` / `section-order` / `doc-order`, every `verbatim/<slug>/` has `sections.json` and a draft `sanitize.json` (the proposal team should confirm the name lists, `review_status: draft`), and the block layer is complete — `python work/find_uncovered.py <slug>` reports zero uncovered paragraphs per source, the remainder being writer-skipped with a recorded reason in `work/gaps/<slug>.skips.json`. `python work/status_counts.py --md` prints the current numbers.
