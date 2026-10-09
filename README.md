# Proposal Content Wiki

A curated, reusable library of Jacobs' best water & wastewater O&M proposal content — extracted from winning proposals and broken into modular blocks so it can be leveraged on future pursuits by both people and AI agents. Reusable narrative blocks generalize the pursuit client to `[CLIENT]` and exclude commercial pricing; resumes, past performance, and references are captured verbatim (staff names, reference clients, contacts, legal qualifications all kept — the proposal team QCs before external use).

## How it works

- **`raw/`** holds the original proposal PDFs, untouched.
- **`wiki/`** holds the extracted content as markdown "content blocks," organized by category (technical approach, management & staffing, win themes, qualifications, compliance plans, resumes, past performance). Each block carries metadata (tags, source, context, reuse notes) so agents can find and apply it.
- **`wiki/graphics/`** catalogs every exhibit by its Jacobs graphics-library asset ID (e.g., `126_Hull_0091KO_2`) — no image files, just retrievable references.
- **`CLAUDE.md`** is the schema agents read first: organization, sanitization rules, and how to use content.

## Keeping it current

Currency is computed, not remembered: `python work/freshness.py --today <date> --write` stamps every block with how fast its facts age (`volatility`), when it is next due for a check (`review-due`, counted from the source proposal's date until someone verifies it) and what the detectors flagged (`freshness-flags`: open-ended dates, registry conflicts, a newer source with a different value, duplicate people, unverified reference contacts, broken supersedes links, fact-check feedback from pursuits). `/curate` turns the flagged list into a tick-list of proposed actions with evidence (`work/curation/queue.md`); only the maintainer's ticks — `python work/apply_curation.py` — or a direct `python work/curate.py archive|supersede|verify` change a block's status. Archived blocks stay on disk, listed at the end of `wiki/index.md`, and are skipped by pulls and drafting. Every change is logged in `work/curation/log.jsonl`. See `CLAUDE.md`, **Keeping the bank current**.

## Golden rule

Content blocks are **starting points, not final text**. Tailor everything to the pursuit. Verbatim boilerplate loses evaluations.

## Status

| Proposal | Status |
|---|---|
| Hull WWTF & Collection System O&M (2026) | Complete — 92 content blocks (23 technical-approach, 10 management-staffing, 21 win-themes, 11 qualifications, 13 compliance-plans, 6 resumes, 8 past-performance), 104 verbatim pages, 570 proof-point registry rows; block layer complete (0 uncovered paragraphs, 10 writer-skipped with reasons) |
| Santa Monica SWIP O&M (2025) | Complete — 100 content blocks (32 technical-approach, 18 management-staffing, 16 win-themes, 9 qualifications, 11 compliance-plans, 8 resumes, 6 past-performance), 119 verbatim pages, 583 proof-point registry rows; block layer complete (0 uncovered, 17 writer-skipped). Four dollar figures redacted in Section 4 blocks after being traced to the commercial pricing schedule; the Exec Summary/Section 2.4 "$4.1M value-added wheel" figures were reviewed and kept as no-cost value-add framing — flagged for proposal-team judgment before reuse. |
| OCWUT 16-26 | Complete — 230 content blocks (71 technical-approach, 32 management-staffing, 25 win-themes, 25 qualifications, 53 compliance-plans, 14 resumes, 10 past-performance), 184 verbatim pages, 911 proof-point registry rows; block layer complete (0 uncovered, 27 writer-skipped) |
| Fulton County 25RFP146289K | Complete through Section 8 / page 187 — 163 content blocks (51 technical-approach, 30 management-staffing, 32 win-themes, 7 qualifications, 19 compliance-plans, 11 resumes, 13 past-performance), 507 verbatim pages, 337 proof-point registry rows; block layer complete (0 uncovered, 41 writer-skipped). Pages 188+ (appendices) intentionally out of scope. |
| MMSD O&M (2028) | Complete — 250 content blocks (133 technical-approach, 51 management-staffing, 27 win-themes, 6 qualifications, 13 compliance-plans, 20 resumes, 0 past-performance), 147 verbatim pages, 766 proof-point registry rows; block layer complete (0 uncovered, 26 writer-skipped). |


**Currency status 2026-10-09:** 834 live blocks, 1 archived, 180 past review-due (people 145, corporate-figure 18, reference 12, safety-stat 3, regulatory 2 — the 2025 Fulton and Santa Monica sources and the 180-day people interval drive most of it), 112 flagged (divergent-figure 63, open-ended-date 56, newer-source-same-claim 16, stale-contact 12, person-duplicate 6, newer-year-available 3), 84 registry conflicts, 30 unlinked duplicate pairs. First curation pass (run 2026-10-09, 40 items): 27 verify awaiting confirmation in `work/curation/queue.md`, 11 keep logged, 2 update-figure applied (2025 TRIR/EMR and 2025 training hours), 3 status/link decisions resolved, first archive. `python work/status_counts.py --md` prints the per-source table with Archived and Review-overdue columns.

**Bank status 2026-09-14:** 835 blocks across 7 categories in 5 sources; every block carries `section-id` / `section-path` / `section-order` / `doc-order` (reading order inside its PDF-bookmarked section); every source has `verbatim/<slug>/sections.json` (heading spans) and a draft `sanitize.json`; the block layer is complete (`python work/find_uncovered.py <slug>` reports 0 uncovered substantive paragraphs per source, 121 writer-skipped with recorded reasons in `work/gaps/<slug>.skips.json`). Lint: 0 schema violations; 85 report-only client-name-in-narrative hits (service-area and reference names such as "North Fulton", "Johns Creek", "Milwaukee" pending a sanitization-rule call). Whole sections pull in reading order with `python work/assemble_section.py <slug> "<section>"` (the `pull-section` skill). `python work/status_counts.py --md` prints this table's numbers. See PORTING.md §3 for the earlier verified result and §7 for the acceptance gates; ONBOARDING.md for the handoff checklist.

*Previous status (2026-09-07):* 542 blocks across 7 categories, lint 0 violations, index 542 rows, zero client-name leakage in narrative body text. Fidelity (work/map_blocks_to_pages.py): 65.3% verbatim, 28.1% partial, 5.1% recipe, 1.5% absent — captured prose 93.4%. All four source proposals extracted. See PORTING.md §3 for the verified result and §7 for the acceptance gates.
