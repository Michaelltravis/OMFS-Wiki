---
title: <Human-readable block name>
category: <technical-approach | management-staffing | win-themes | qualifications | compliance-plans | resumes | past-performance>
block-type: <prose | recipe | table | exhibit | roster>
pairs-with: <for recipe blocks only — path of the prose block this recipe describes>
tags: [<controlled tags from vocabulary/tags.md>]
source: <source-slug from CLAUDE.md registry>
source-section: "<Section X, Title>"
source-pages: [<PDF page numbers>]
verbatim-ref: ["verbatim/<slug>/pages/p0076.md#¶3"]
section-id: <set by work/assign_block_sections.py from the first verbatim-ref — the deepest subsection; do not hand-edit>
section-path: <set by the same script — breadcrumb of titles from the proposal section down to section-id>
section-order: <set by the same script — 1..N reading-order ordinal within the proposal (PDF-bookmarked) section>
doc-order: <set by the same script — 1..N reading-order ordinal across the whole source proposal>
pursuit-type: [<wwtp-om | collections | stormwater | reuse-dpr | water-treatment | solids | multi-facility>]
client-type: <municipal | county | authority | trust | private>
client-size: "<e.g. 3 MGD / 42 mi / 10k pop>"
geography: "<Region / State / regulator>"
rfp-section-type: [<cover-letter | exec-summary | qualifications | staffing | tech-approach | transition | compliance | past-performance | resume | forms>]
win-theme-map: [<partner-transparency | compliance-leadership | regional-bench | odor-control | incumbent-displacement | asset-management | safety-culture | innovation-value-add | ...>]
proof-point-ids: [<PP-0001, ...>]
testimonial-ids: []
story-ids: []
status: <preferred | fallback | archived — archived only via work/curate.py archive / apply_curation.py; then also archive-reason, archived-date, archived-by>
supersedes: <path of the fallback block this one replaces, if any>
house-favorite: false
sanitized: true
sanitization-loss: <none | low | high>
extracted: <YYYY-MM-DD, bare — never quoted>
last-verified: <YYYY-MM-DD; moves only when a person checks the block (python work/curate.py verify), which also sets verified-by>
volatility: <set by python work/freshness.py --write — people | reference | corporate-figure | safety-stat | regulatory | project-outcome | evergreen; do not hand-edit>
review-due: <set by the same script — basis date (last-verified if verified-by, else the source proposal date in work/curation/sources.json) + the class interval in work/curation/policy.json>
freshness-flags: [<set by the same script — machine-detected currency problems; [] when clean>]
context: <Generalized pursuit context — size, scope, region, client type>
quality: <why this content was selected>
reuse-notes: <what must be tailored per pursuit — never "do not restate the figure">
---

# <Block title>

<The prose itself, sanitized: pursuit client → [CLIENT] with a generalized descriptor on
first use. Keep facility sizes, outcomes, savings, awards, staff names, reference clients.
No commercial fee/rate figures. Every number here has a registry id above.
Reference graphics inline by asset ID.>

## Reuse guidance

<What is universal, what is pursuit-specific, which blocks pair with this one, which
verbatim pages to read for the full passage.>
