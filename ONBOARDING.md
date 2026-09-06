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

See the status table in `README.md`. As of September 2026: the Hull WWTF proposal (2026) and Santa Monica SWIP proposal (2025) are both fully extracted and completeness-audited (89 and 98 content blocks, respectively); OCWUT and Fulton County are queued.
