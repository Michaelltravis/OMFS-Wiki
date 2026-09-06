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
| Hull WWTF & Collection System O&M (2026) | Extracted + completeness-audited — 72 content blocks (incl. 6 resumes/roster, 7 verbatim past-performance), 50 exhibits cataloged (pilot complete, pending review) |
| Santa Monica SWIP O&M (2025) | Extracted + completeness-audited — 83 content blocks (incl. 8 resumes, 6 verbatim past-performance), 76 exhibits cataloged. Four dollar figures redacted in Section 4 blocks after being traced to the commercial pricing schedule; the Exec Summary/Section 2.4 "$4.1M value-added wheel" figures were reviewed and kept as no-cost value-add framing — flagged for proposal-team judgment before reuse. |
| OCWUT 16-26 | Pending |
| Fulton County 25RFP146289K | Pending |
