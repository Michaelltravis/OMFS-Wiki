# Proposal Content Wiki — Agent Schema

This is a curated library of reusable, sanitized proposal content extracted from winning/excellent Jacobs water & wastewater O&M proposals. Agents use it to draft new proposal sections. **Read this file first**, then `wiki/index.md` to find content.

## How this wiki is organized

```
raw/                        Original source proposal PDFs — IMMUTABLE. Never edit,
                            never quote from directly into deliverables (unsanitized).
wiki/index.md               Master index of every content block.
wiki/technical-approach/    O&M methodology, process optimization, asset management,
                            collection systems, biosolids, odor control, energy.
wiki/management-staffing/   Org structures, transition plans, staffing models,
                            key-personnel role descriptions.
wiki/win-themes/            Executive summary language, value propositions, benefit
                            framing, differentiators, proof points, cover letter patterns.
wiki/qualifications/        Firm qualifications (Section 3-type content): corporate
                            scale/portfolio proof points, regional presence, financial
                            strength, legal/entity details, workforce culture,
                            past-performance narrative patterns.
wiki/compliance-plans/      Safety, QA/QC, environmental compliance, emergency response.
wiki/resumes/               Key personnel resumes, verbatim (names, certs, experience),
                            one file per person, plus proposed-team rosters.
wiki/past-performance/      Project descriptions, reference lists, similar-facility
                            tables — verbatim, real client names and contacts.
wiki/graphics/              Graphics catalog — one file per source proposal. Text
                            references only (no image files); IDs resolve in the
                            Jacobs graphics library/DAM.
verbatim/<slug>/            THE SOURCE OF TRUTH FOR PROSE. Page-anchored, paragraph-
                            numbered (`<!-- ¶n -->`) markdown of every source proposal,
                            produced by a local converter (zero model tokens) and
                            coverage-checked against the PDF text layer
                            (pages/pNNNN.md, full.md, manifest.json, coverage.md,
                            renders/ for image-only pages). Immutable once verified.
                            Writers and fact-checkers read prose HERE; blocks are the
                            selection/metadata layer that points into it.
                            sections.json = every heading with its (page, ¶) span, nested
                            under the PDF outline (work/build_sections.py) — the reading
                            order every block's `section-id`/`section-order` points into.
                            sanitize.json = the client, location, facility and product
                            names a section pull generalizes (review_status: draft until
                            the proposal team confirms).
proof-points/registry.md    One row per quantified claim: id, claim, number, unit,
                            as-of, source page/¶, owner, approved-for-external-use,
                            conflicts-with. Blocks cite `proof-point-ids`; a number that
                            is not in the registry is `unregistered`.
testimonials/inventory.md   Every client quote: speaker, title, org, verbatim text,
                            source page, permission status (on-file | unknown).
stories/catalog.md          House narratives (turnarounds, transitions, savings) with the
                            beat that makes each work, proof-point ids, best-for sections.
vocabulary/tags.md          Controlled tag vocabulary (~120 tags) + tag-aliases.yaml.
voice/                      Voice guide, scoring rubric, metrics.py, exemplar/.
pursuits/<pursuit>/         Per-pursuit content plan (content-plan.md: the Directive
                            outline in order, each section's RFP-required topics plus the
                            Jacobs-standard topics from templates/standard-topics.md,
                            ticked by the proposal manager) and spec sheet (locked numbers, approved proofs,
                            preferred references, stories, gap decisions, page/device
                            budgets, win-theme evidence map). Writers obey the spec sheet.
work/                       Scripts: pdf_to_verbatim.py, coverage.py,
                            render_flagged_pages.py, build_sections.py,
                            assign_block_sections.py, assemble_section.py,
                            find_uncovered.py, make_gap_ranges.py,
                            map_blocks_to_pages.py, regen_index.py, build_docx.py,
                            validate_v2.py.
templates/content-block.md  Template for new content blocks (schema v2).
templates/standard-topics.md  The topics Jacobs includes in every cover letter, exec
                            summary, qualifications, staffing and approach section whether
                            or not the RFP asks (3+ of 4 source proposals); one preferred
                            block per topic. templates/content-plan.md shows the sheet shape;
                            work/new_content_plan.py builds it from a Proposal Directive.
```

## Content block format

One modular, reusable block per file. Frontmatter fields (schema v2 — all required unless marked optional):

| Field | Meaning |
|---|---|
| `title` | Human-readable block name |
| `category` | Folder it lives in |
| `block-type` | `prose` (paste-ready sanitized prose) · `recipe` (instructions describing how a passage is built — NOT prose; must name the prose block it describes in `pairs-with`) · `table` · `exhibit` · `roster` |
| `tags` | Retrieval keywords from `vocabulary/tags.md` only (validated) |
| `source` | Slug of source proposal (see Source registry below) |
| `source-section` | Section title in the original PDF |
| `source-pages` | List of PDF page numbers the block was drawn from |
| `verbatim-ref` | Back-pointer(s) into `verbatim/<slug>/pages/pNNNN.md#¶n` for the primary passage |
| `section-id` | The section in `verbatim/<slug>/sections.json` that contains the first `verbatim-ref` — set by `work/assign_block_sections.py`, never hand-edited |
| `section-order` | 1-based reading-order ordinal of the block within its `section-id` — set by the same script |
| `pursuit-type` | `wwtp-om` · `collections` · `stormwater` · `reuse-dpr` · `water-treatment` · `solids` · `multi-facility` · `mbr-membrane` · `jv-delivery` (list) |
| `client-type` | `municipal` · `county` · `authority` · `trust` · `private` |
| `geography` values in use | `Northeast / MA / MassDEP` · `West / CA / SWRCB-DDW` · `Southcentral / OK / ODEQ` · `Southeast / GA / GA EPD` |
| `client-size` | e.g. `3 MGD / 42 mi / 10k pop` — capacity, collection miles, population band |
| `geography` | Region + state + regulatory regime (e.g. `Northeast / MA / MassDEP`) |
| `rfp-section-type` | `cover-letter` · `exec-summary` · `qualifications` · `staffing` · `tech-approach` · `transition` · `compliance` · `past-performance` · `resume` · `forms` (list) |
| `win-theme-map` | Which win-theme archetypes this block proves (e.g. `partner-transparency`, `compliance-leadership`, `regional-bench`, `odor-control`, `incumbent-displacement`) |
| `proof-point-ids` | Registry ids for every number stated in the body |
| `testimonial-ids` / `story-ids` | Optional links into testimonials/ and stories/ |
| `status` | `preferred` · `fallback` (duplicate topic — `supersedes`/`superseded-by` names the pair) |
| `house-favorite` | `true` for the narratives the proposal team reaches for first |
| `sanitized` | `true` once client identifiers are generalized |
| `sanitization-loss` | `none` · `low` · `high` — how much proof value the generalization removed; `high` requires a `verbatim-ref` the writer should read instead |
| `extracted` / `last-verified` | ISO dates; `verified-by` optional |
| `context` | Generalized context of the original pursuit |
| `quality` | Why this content was selected |
| `reuse-notes` | What must be tailored per pursuit |

Body = the prose itself (sanitized), then a **Reuse guidance** section. **A block must contain the prose, not a description of the prose.** Instructional summaries ("Paragraph 1 — acknowledge investment, then name the gap") are `block-type: recipe` and are only valid when paired with the `prose` block they describe. Related blocks are linked with relative markdown links; graphics referenced by asset ID.

## Sanitization rules

The wiki supports sales work — most real information is KEPT. Only two things are generalized/removed:

1. **Pursuit client name in reusable narrative blocks** (technical-approach, management-staffing, win-themes, qualifications, compliance-plans) → `[CLIENT]` with a generalized descriptor on first use — this is what makes narrative blocks drop-in reusable. Does NOT apply to `past-performance/` or `resumes/`, which are verbatim.
2. **Commercial pricing from commercial sections only** (fee tables, rates, cost proposals, commercial terms) → removed. Outcome figures ("saved $134K/year", "$12.7 million estimated savings", "55% fewer complaints"), operational stats, awards, and financial-qualification figures (bonding capacity, revenues) are KEPT — they are the proof value of the library. Any reuse-note that says "do not restate the dollar savings figure" is wrong and must be deleted; register the figure in `proof-points/registry.md` instead and mark its approval status there.

Everything else is kept:

3. Staff names, titles, phone numbers, emails → **keep**.
4. Facility specifics (MGD, miles of sewer, pump stations, process types) → **keep**. In narrative blocks, generalize the pursuit location to region level; verbatim elsewhere.
5. Corporate/legal qualifications (entity details, tax IDs, legal standing, litigation/termination disclosures, violation history) → **keep** — clients request these.
6. Past performance, project descriptions, and reference sections → **capture verbatim**, including reference client names, locations, contacts, dates, and outcomes. The proposal team QCs before external use.
7. Graphics → never embed images. Catalog by graphic asset ID (gray text on each exhibit, e.g., `126_Hull_0091KO_2`) in `wiki/graphics/<source-slug>.md`.

## Using this content in new proposals

**The purpose of this wiki is to draft FULL sections of future RFP responses**, with guidance from the user. A drafting session works from two inputs:

1. **Pursuit documents (provided per pursuit):** the client's RFP and addenda, scope of work documents, and the Jacobs proposal directive. These control the outline, compliance requirements, evaluation criteria, page limits, and win strategy.
2. **This wiki:** the content supply — proven language, frameworks, tables, narratives, and graphics references.

Drafting workflow (v2):
0. **Build and approve the content plan** (`python work/new_content_plan.py <slug> --directive <Directive.docx> --docx`): sections in Proposal Directive order, cross-checked against the RFP's requirement exports; the proposal manager ticks the Jacobs-standard topics to include under each section and adds pursuit-specific ones. Ticked topics are the only ones the spec sheet plans for and the writers draft. The `content-plan` skill (`.claude/skills/content-plan/SKILL.md`, Sonnet) runs this end to end: scaffold → interactive checklist page (Artifact, `db` capability) for the proposal manager → selections written back → docx.
1. **Start from the pursuit spec sheet** (`pursuits/<pursuit>/spec-sheet.md`, status `locked`): locked numbers, approved proof points, preferred references, ranked stories and "the closer", quotable inventory, gap decisions, page/device budget per section, win-theme evidence map. If no spec sheet exists, draft one and get it approved before writing sections.
2. Build the section outline from the RFP's requirements and evaluation criteria (answer what is asked, in the order asked) — but headings carry an assertion, not the RFP label.
3. Select blocks via the faceted `wiki/index.md` (rfp-section-type × pursuit-type × client-size); prefer `status: preferred`, `house-favorite: true`; read the **verbatim source** behind any block with `sanitization-loss: high`.
4. Write to the voice guide (`voice/voice-guide.md`) and its rubric. Lead with the client's outcome; every number carries its consequence for the client; win themes recur in identical words; proof is layered (inline number, stat callout, fact box, table); at least one client quote per persuasive section when permission is on file.
5. Every number in a draft must resolve to a registry id whose value matches the spec sheet's locked value; every quote to a testimonial id with permission `on-file`.
6. Gaps are decided in the spec sheet (DROP / SOURCE BY / WRITE AROUND) — **placeholders and [VERIFY] tags never appear in body text**; open items go to a companion notes file.
7. Recommend graphics from the catalog by asset ID; flag `client-specific: true` for re-branding.

Content blocks are **starting points, not final text**; the verbatim layer is where the winning prose lives.

**Pulling a whole section** ("give me the asset management section from Hull, in order, verbatim"): `python work/assemble_section.py <slug> "<section words>"` (the `pull-section` skill wraps it). Default output is the section's verbatim prose in PDF order, sanitized per `verbatim/<slug>/sanitize.json`, running headers/footers dropped, exhibit text reduced to `[graphic: <id>]` markers, written to `work/pulls/<slug>/` (gitignored). `--mode blocks` lists the wiki blocks in the section in `section-order` with a coverage trailer; `--docx` renders through `work/build_docx.py`; `--raw` keeps the real client name (QC before any external use). The faceted index ends with a **By source section** facet that lists every block in reading order.

## Source registry

| Slug | Original file | Pursuit |
|---|---|---|
| `hull-wwtf-om-2026` | `raw/Hull_Wastewater Treatment Facility and Collection System O&M.pdf` | Coastal New England municipal WWTF (3.07 MGD) + collection system O&M, 2026 |
| `santamonica-swip-om-2025` | `raw/SantaMonica_SWIP_OM_FINAL 09122025.pdf` | Southern California sustainable water infrastructure O&M, 2025 |
| `ocwut-16-26` | `raw/RFP-OCWUT-16-26_Proposal_Jacobs.pdf` | Southcentral US water utility trust, four WWTPs >110 MGD + biosolids, 2026 challenger bid; ODEQ |
| `fulton-county-2025` | `raw/Fulton-County_25RFP146289K-JAJ_Technical-Proposal_JC-Solutions.pdf` | Southeast US county, three MBR WRFs + 33 pump stations, 2025, bid as JC Solutions (Jacobs/CERM JV); GA EPD |
| `mmsd-om-2028` | `raw/007CAM_MMSD-OM_Combined.pdf` | Midwest US regional sewerage district, two large water reclamation facilities + biosolids (Milorganite) production, RFP P-3216, 2028 challenger bid vs. incumbent operator; WDNR |

## Adding new content (extraction workflow)

Script first, agents only where a script cannot do the job. No model reads proposal pages to transcribe text that has a text layer (the 2026 Hull pilot did, and captured only 37% of the narrative verbatim).

1. Drop the source PDF in `raw/` and register it above.
2. **Convert locally (zero tokens):** run the End Game suite converter (`end-game-sales-suite/scripts/convert.py`, pymupdf4llm page chunks) → `raw/<file>.md`, then `python work/pdf_to_verbatim.py raw/<file>.pdf <slug>` → `verbatim/<slug>/` (per-page files, ¶ numbering, header/footer cleanup, text-layer backfill of blocks the converter dropped, 300-DPI renders of image-only pages).
3. **Measure:** `python work/coverage.py raw/<file>.pdf <slug>` — gate is word-level recall ≥0.99 per page and no missing run ≥15 words. `pdf_to_verbatim.py` only auto-renders image-only pages, so for flagged text pages run `python work/render_flagged_pages.py raw/<file>.pdf <slug> verbatim/<slug>/coverage.json` first to populate `renders/` for them. Flagged pages are repaired (Sonnet, using the render as reference) and re-measured. Image-only pages get two independent Opus vision transcriptions and a Sonnet refuting verifier; unresolved spans are `[illegible]`, never guessed; frontmatter records `method: vision`. A source PDF's own font can drop ligature glyphs (fi/fl/ffi/ffl/ff → replacement char or dropped letter) in its text layer itself — this shows up as pages that stay flagged after repair even though the verbatim page is now more correct than the PDF's own text layer (the coverage gate's ground truth). Confirm with a `fitz` rawdict check before assuming this; when confirmed, correct the affected words against the render and record the explanation in `coverage.md` rather than chasing the score — see `verbatim/mmsd-om-2028/coverage.md` for the documented example.
4. **Blocks:** Opus writers build/rebuild blocks per source section from the verbatim pages, with `source-pages` and `verbatim-ref` on every block, schema-v2 frontmatter, `block-type: prose` for prose. A Fable judge fails any block that is a paraphrase of its verbatim source. Keep every outcome figure. Then `python work/build_sections.py <slug>` (writes `sections.json`; add `--check --print-tree` and eyeball the tree) and `python work/assign_block_sections.py --slug <slug>` so every block carries `section-id`/`section-order` — rerun the latter after ANY block build. Write `verbatim/<slug>/sanitize.json` (client, alias, location, facility, product names; `protect` for proper nouns that contain them).
5. **Registries:** harvest every quantified claim into `proof-points/registry.md` (reconcile conflicts explicitly), every quote into `testimonials/inventory.md`, every narrative into `stories/catalog.md`.
6. **Vocabulary, merge, index:** tags validated against `vocabulary/tags.md`; duplicate topics across sources resolved to one `preferred`; `python work/regen_index.py` rebuilds the faceted index.
7. Verify: narrative categories have zero pursuit-client-name hits in body text; no commercial fee/rate figures; every block resolves its `verbatim-ref`; every number resolves to a registry id. Resumes, past-performance, and graphics are verbatim and exempt from the client-name check — the proposal team QCs before external use.
8. **Complete the block layer:** `python work/find_uncovered.py <slug>` lists substantive paragraphs (≥25 words, not exhibit text / running lines / captions) that no block covers (`work/gaps/<slug>.md`); `python work/make_gap_ranges.py <slug>` groups them into small ranges; run `.claude/workflows/fill-gaps.js` with `args` = `{"wiki": "<repo path>", "slug": "<slug>", "rangesFile": "<absolute path to work/fragments/ranges_gapfill_<slug>.json>"}` (one source per run — the finalize step rewrites the shared registry and index — resumable with `resumeFromRunId`). Writers may skip a listed paragraph only with a reason (exhibit-internal, form-boilerplate, commercial, duplicate-of, continuation-of); copy those decisions into `work/gaps/<slug>.skips.json` so `find_uncovered.py` reports them as writer-skipped rather than uncovered. It creates blocks only for the listed paragraphs, judges them, then re-assigns section order, rebuilds the registry, index and lint. Existing blocks are never rewritten by this step. Page ranges skipped by design (cover/TOC, commercial sections, forms, out-of-scope appendices) live in `work/gap_scope.json`.

The `extract-proposal` skill (`.claude/skills/extract-proposal/SKILL.md`) runs this sequence.
