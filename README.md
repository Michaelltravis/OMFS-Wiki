# Proposal Content Wiki

A curated, reusable library of Jacobs' best water & wastewater O&M proposal content — extracted from winning proposals and broken into modular blocks so it can be leveraged on future pursuits by both people and AI agents. Reusable narrative blocks generalize the pursuit client to `[CLIENT]` and exclude commercial pricing; resumes, past performance, and references are captured verbatim (staff names, reference clients, contacts, legal qualifications all kept — the proposal team QCs before external use).

## How it works

- **`raw/`** holds the original proposal PDFs, untouched.
- **`wiki/`** holds the extracted content as markdown "content blocks," organized by category (technical approach, management & staffing, win themes, qualifications, compliance plans, resumes, past performance). Each block carries metadata (tags, source, context, reuse notes) so agents can find and apply it.
- **`wiki/graphics/`** catalogs every exhibit by its Jacobs graphics-library asset ID (e.g., `126_Hull_0091KO_2`) — no image files, just retrievable references.
- **`CLAUDE.md`** is the schema agents read first: organization, sanitization rules, and how to use content.

## Golden rule

Content blocks are **starting points, not final text**. Tailor everything to the pursuit. Verbatim boilerplate loses evaluations.

## Status

| Proposal | Status |
|---|---|
| Hull WWTF & Collection System O&M (2026) | Extracted + completeness-audited — 89 content blocks (23 technical-approach, 10 management-staffing, 21 win-themes, 9 qualifications, 13 compliance-plans, 6 resumes, 7 past-performance), 104 verbatim pages, 47 proof-point registry rows (pilot complete, pending review) |
| Santa Monica SWIP O&M (2025) | Extracted + completeness-audited — 98 content blocks (31 technical-approach, 17 management-staffing, 16 win-themes, 9 qualifications, 11 compliance-plans, 8 resumes, 6 past-performance), 119 verbatim pages, 45 proof-point registry rows. Four dollar figures redacted in Section 4 blocks after being traced to the commercial pricing schedule; the Exec Summary/Section 2.4 "$4.1M value-added wheel" figures were reviewed and kept as no-cost value-add framing — flagged for proposal-team judgment before reuse. |
| OCWUT 16-26 | Extracted + completeness-audited — 225 content blocks; 184 verbatim pages; extraction complete |
| Fulton County 25RFP146289K | Extracted through Section 8 / page 187 — 130 content blocks; pages 188+ intentionally out of scope. Two content-free blocks built from the p187 divider (Salesforce opportunity id as body) were removed 2026-09-07. |


**Bank status 2026-09-07:** 542 blocks across 7 categories, lint 0 violations, index 542 rows, zero client-name leakage in narrative body text. Fidelity (work/map_blocks_to_pages.py): 65.3% verbatim, 28.1% partial, 5.1% recipe, 1.5% absent — captured prose 93.4%. All four source proposals extracted. See PORTING.md §3 for the verified result and §7 for the acceptance gates.
