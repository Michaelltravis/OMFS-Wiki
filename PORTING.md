# Porting note — finishing the content bank on another system

This document lets a different AI assistant or a person finish the extraction work without any access to the conversation that started it. It is self-contained. Read it top to bottom before touching a file.

Written 2026-09-06. The bank lives at `C:\Users\micha\Desktop\Wiki` and is a git repository; commit as you go.

---

## 1. The one thing that must not go wrong

**Blocks must contain the source's prose, not a summary of it.**

This library was rebuilt precisely because the first extraction failed this rule. A quantitative check against the source text layer measured the Hull proposal at 37% verbatim, with 15% of its narrative reduced to instructional recipes like "Paragraph 1 — acknowledge the investment, then name the gap." The largest section, an 11,500-word technical approach, came out 9% verbatim. The result looked complete and was nearly useless: writers got the architecture of the winning prose but had to reinvent the sentences.

Summarizing is the natural default for any capable model told to "extract content into reusable blocks." It feels like the helpful thing to do. It is the failure mode. Two mechanisms prevent it, and **both must be carried over**:

1. Rule 1 and Rule 3 of the builder prompt in §5 below, stated explicitly to every extraction agent.
2. A separate judge pass (§6) that re-reads each block against its cited source paragraphs and fails anything that keeps the ideas but not the sentences. The judge must be a different agent instance from the builder, so it grades work it did not do.

If you keep nothing else from this document, keep these two.

---

## 2. What the bank is

```
raw/                    Source PDFs — immutable, never edit
verbatim/<slug>/        SOURCE OF TRUTH FOR PROSE. Page-anchored markdown, one file per
                        PDF page, paragraphs numbered with <!-- ¶n --> comments.
                        pages/pNNNN.md, full.md, manifest.json, coverage.md, renders/
wiki/<category>/*.md    Sanitized, reusable content blocks with schema-v2 frontmatter.
                        Seven categories: technical-approach, management-staffing,
                        win-themes, qualifications, compliance-plans, resumes,
                        past-performance
proof-points/registry.  One row per quantified claim: id, claim, values with as-of dates
  md / .json            and sources, conflict status, approval status
testimonials/           Every client quote with speaker, source page, permission status
stories/catalog.md      House narratives with "the beat" that makes each one land
vocabulary/tags.md      Controlled tag vocabulary, ~128 tags
voice/                  Voice guide, scoring rubric, metrics.py
pursuits/<pursuit>/     Per-pursuit spec sheet and requirement exports
work/*.py               19 portable scripts (see §7)
```

The layering matters. `verbatim/` is exact source text with no interpretation. `wiki/` blocks are the selection and metadata layer *over* it, and every block carries a `verbatim-ref` pointer back to the paragraph it came from. A writer who needs the full passage follows the pointer. A fact-checker validates a claim by following the pointer. Break the pointers and the bank degrades into unsourced boilerplate.

**Authoritative rules live in `CLAUDE.md`** (schema, sanitization, extraction workflow) and `templates/content-block.md` (the frontmatter template). Those two files govern; this document explains how to execute against them.

---

## 3. Current state — extraction COMPLETE

**Status as of 2026-09-07: all four proposals are extracted, and the bank passes every gate.** The extraction was finished by a second system working from this document; the sections below record the verified result. Sections 4 through 8 remain the operating manual for the *next* proposal you ingest.

| Metric | Result |
|---|---|
| Blocks | 542 across 7 categories |
| Lint violations | **0** |
| Index rows | 542, matching disk exactly |
| Client-name leakage in narrative body text | **0** |
| Verbatim-refs resolving | all |

**Fidelity, measured by `work/map_blocks_to_pages.py` (shingle overlap against source pages):**

| Class | Before the rebuild (155 blocks) | Now (542 blocks) |
|---|---|---|
| verbatim | 34% | **65.3%** |
| partial | 46% | 28.1% |
| recipe | 16% | 5.1% |
| absent | 3% | 1.5% |

Captured prose (verbatim + partial) went from 80% to **93.4%**, and the recipe tier — blocks that describe prose instead of containing it, the original failure — fell from 16% to 5%. This is the check that matters most; re-run it after any future extraction.

### Defects found and fixed on 2026-09-07

- **Two content-free blocks deleted.** `fulton-service-disabled-veterans-preference-response.md` existed in both `compliance-plans/` and `qualifications/`, with a Salesforce opportunity identifier (`0063F000009OMF7AAE`) as its entire body. It was built from Fulton page 187, a section divider that was on the skip list and whose only content is a heading plus that identifier. Both files were removed.
- **Two blocks flagged as synthesis.** `sensor-dispersion-model-odor-early-warning-system.md` and `swip-predictive-maintenance-technologies.md` are labelled `block-type: prose` but measure ~0% and ~1% overlap with their sources — they restructure rather than reproduce. Both are pre-existing blocks from the original library that no range covered during the rebuild. Their `reuse-notes` now open with a SYNTHESIS, NOT SOURCE PROSE warning directing the writer to the verbatim-ref. Promote them to real prose in a future pass.

### Known false positives in the leakage check

These are proper names of third-party organizations, not references to a pursuit client. **Leave them as written**; a leakage grep will flag them every time.

- `Senior Services North Fulton` — a senior-centre partner organization
- `North Fulton Community Charities` — a food-security partner
- `North Fulton Neighbor`, `North Fulton News (AJC)` — local newspapers

## 4. Historical: what remained before completion

*Superseded on 2026-09-07 — kept as a record of the handoff state. All of this work is now done; `work/fragments/ranges_REMAINING.json` is spent.*

At handoff the bank held 385 blocks. Hull and Santa Monica were complete and clean; Oklahoma City was partially built; Fulton County had barely started.

| Source proposal | Slug | Verbatim layer | Blocks | State |
|---|---|---|---|---|
| Hull, MA WWTF 2026 | `hull-wwtf-om-2026` | 104 pp, complete | 89 | Done, lint clean |
| Santa Monica SWIP 2025 | `santamonica-swip-om-2025` | 119 pp, complete | 98 | Done, lint clean |
| Oklahoma City Water Utilities Trust | `ocwut-16-26` | 184 pp, complete | 194 | 18 of 27 ranges built |
| Fulton County (JC Solutions JV) | `fulton-county-2025` | 507 pp (body ends p195) | 2 | 0 of 26 ranges built |

The two Fulton blocks are orphans from a range that was interrupted before it finished. Treat that range as unbuilt: when its builder runs, it will find those files listed as existing blocks and bring them up to standard.

**Remaining work, in order:**

1. **35 section ranges** still need blocks. The exact list, with page ranges, target categories and all builder arguments, is in `work/fragments/ranges_REMAINING.json`. Nine are Oklahoma City, twenty-six are Fulton County.
2. **Registry increment.** Harvest the `work/fragments/<slug>/*.facts.json` files into `proof-points/registry.json`, reconciling against existing ids so they stay stable. Same for `*.quotes.json` into `testimonials/inventory.md`, and narratives into `stories/catalog.md`.
3. **Duplicate resolution.** Run `python work/dedupe_candidates.py --min 0.12`, judge each candidate pair, and mark one `status: preferred` and the other `status: fallback` with `supersedes` / `superseded-by` pointers.
4. **Vocabulary and index.** Fold any new tags into `vocabulary/tags.md` (keep the total near 130), then `python work/regen_index.py`.
5. **Lint to zero.** `python work/lint_blocks.py` currently reports **44 violations across 44 files**. These are new blocks missing schema-v2 fields because the cleanup stage never ran. This is a known mid-run state, not the standard. The standard is zero.

**Do not treat the current 44 violations as acceptable.** They are unfinished work.

---

## 5. The builder prompt (port verbatim)

Give this to one agent per range, with the placeholders filled from that range's entry in `ranges_REMAINING.json`. A capable mid-tier model is sufficient; this is careful transcription, not creative writing. Do not batch multiple ranges into one agent, because fidelity decays with context length.

> You are rebuilding content-bank blocks for ONE section of a winning proposal. Work only from the verbatim page files; they are the source of truth.
>
> Read first: `CLAUDE.md` (schema v2, sanitization rules) and `templates/content-block.md`.
> Section: "**{name}**" of proposal slug **{slug}**. Pages **{first}–{last}**: *(list every `verbatim/{slug}/pages/pNNNN.md` path in the range)*
> Target category folder: `wiki/{category}/`. rfp-section-type: **{rfpSectionType}**. Pursuit context line for frontmatter: "**{context}**". Pursuit client names to generalize to `[CLIENT]` in narrative categories (NOT in past-performance/resumes): **{clientNames}**.
> Existing blocks already mapped to these pages (UPDATE these in place — keep the filename, rewrite the body so it is the prose from the verbatim pages, sanitized, and upgrade the frontmatter to schema v2; never delete a file): **{existingBlocks or "(none)"}**
>
> Rules:
> 1. **Coverage:** after you finish, every substantive paragraph in these pages (≥25 words, not headers/footers/TOC/boilerplate forms) must live in exactly one block, as prose — near-verbatim, sanitized only per CLAUDE.md. Create new blocks for anything the existing blocks do not cover. One topic per block; 150–900 words per block body.
> 2. `block-type` is `prose` for narrative, `table` for tables (keep GFM), `exhibit` for caption-only, `roster` for team lists. If an existing block is an instructional recipe ("Paragraph 1 — ..."), keep it but set `block-type: recipe` and `pairs-with: <the prose block you created for that passage>`.
> 3. **Keep every number, outcome, award, client reference name, staff name.** Strip only commercial fee/rate figures from commercial sections. Never write "do not restate".
> 4. **Frontmatter v2:** fill `source-pages` and `verbatim-ref` (e.g. `"verbatim/{slug}/pages/p0012.md#¶3"` — cite the ¶ of the primary passage), `pursuit-type`, `client-type`, `client-size`, `geography`, `rfp-section-type`, `win-theme-map` (choose from partner-transparency, compliance-leadership, regional-bench, odor-control, incumbent-displacement, asset-management, safety-culture, innovation-value-add, transition-continuity, workforce-development, energy-chemical-efficiency, collection-system, stormwater, community-engagement, digital-tools), `proof-point-ids: []` (left empty — the registry stage fills it), `status: preferred`, `house-favorite: false`, `sanitized: true`, `sanitization-loss` (none|low|high — high if removing the client name removes the proof value), `extracted` and `last-verified` dates, `tags` (kebab-case, from `vocabulary/tags.md`). Keep any existing title/quality/reuse-notes that are still accurate.
> 5. Body ends with `## Reuse guidance`.
> 6. **Write two fragment files:** `work/fragments/{slug}/{name-slugified}.facts.json` = `[{"claim","number","unit","as_of","page","para","block","category"}]` for EVERY quantified claim in the pages, where category is one of outcome|scale|safety|financial|compliance|schedule|other; and `.quotes.json` = `[{"quote","speaker","title","org","page","para","block"}]` for every client or third-party quotation (empty list if none).
> 7. Do not read any other proposal's pages. Do not edit files outside `wiki/{category}/` and `work/fragments/`.
>
> Return: range name, files updated, files created, the two fragment paths, count of substantive paragraphs you could not place (should be 0), notes.

### Pursuit-specific rules for the two remaining proposals

Append this to every builder prompt for these two sources. It is also stored in `ranges_REMAINING.json` under `builderAddendum`.

**Fulton County.** The proposer is **JC Solutions, a Jacobs/CERM joint venture** — keep the JV voice. Attribute capability to Jacobs and local presence and workforce development to CERM. Never collapse it to "Jacobs." Add the tag `jv-structure` and `pursuit-type: jv-delivery` on such blocks. Generalize client facility names (Big Creek WRF, Johns Creek Environmental Campus / JCEC, Little River WRF) to `[FACILITY A/B/C]` with a descriptor on first use, in narrative categories only. "The County" becomes `[CLIENT]` **only** where it means the pursuit client.

**Oklahoma City.** "The City" frequently refers to *other* cities in case studies. Sanitize only the pursuit client: OCWUT, Oklahoma City Water Utilities Trust, City of Oklahoma City, Oklahoma City, OKC. Keep "Oklahoma" and "ODEQ" — they are regulatory context, not client identity. NexGen EAM consultant statements: keep verbatim, tag `nexgen-eam`, and note in reuse-notes "approved-for-external-use: pending — sourced from a live pursuit." The Waterbury odor reduction figure appears on several pages with **different stated time windows**; keep every wording exactly as written and do not harmonize them — the registry records the conflict. Keep the Sludge Management, Solids Management and Operational Integration plans as three separate blocks.

**Fulton pages 4–7** hold an RFP wayfinding crosswalk (RFP criterion → page number). Capture it as one `block-type: table` block at `wiki/win-themes/rfp-wayfinding-crosswalk-pattern.md` with generalized rows, `house-favorite: true`. It is a proven compliance device worth reusing.

**New facet values allowed:** geography `Southcentral / OK / ODEQ` and `Southeast / GA / GA EPD`; pursuit-type may include `multi-facility`, `solids`, `mbr-membrane`, `jv-delivery`; client-type `trust` (Oklahoma City) or `county` (Fulton).

---

## 6. The judge prompt (port verbatim)

Run after each range, as a **separate agent instance** from the builder. This is the guard against the failure described in §1.

> You are the prose judge for the content bank. For each block listed, decide whether its body **is** the sanitized prose of its verbatim source or merely a paraphrase or summary of it.
>
> Blocks: *(list the files the builder created and updated)*
>
> For each block: read its frontmatter `verbatim-ref` and `source-pages`, open the referenced verbatim pages under `verbatim/{slug}/pages/`, and compare. Verdicts:
> - **prose** — the body reproduces the source sentences near-verbatim, with only `[CLIENT]` and location generalization and commercial figures removed
> - **paraphrase** — rewritten, condensed, or instructional. Fails.
> - **missing-ref** — the verbatim-ref does not resolve or points at the wrong passage
> - **recipe-ok** — a `block-type: recipe` block with a valid `pairs-with`
>
> **Be strict: a block that keeps the ideas but not the sentences is a paraphrase.** Read-only — do not edit files.

Anything returning `paraphrase` or `missing-ref` goes back for a rewrite with this instruction, then is judged again. Two rewrite rounds, then flag whatever still fails rather than accepting it silently.

> Rewrite these blocks so each body is the sanitized PROSE of its verbatim source, not a paraphrase. Read the CLAUDE.md sanitization rules first. For each: open the block, open its verbatim-ref pages (fix the ref if it was wrong), replace the body with the source sentences (generalize pursuit client names to `[CLIENT]` in narrative categories only; keep every number; strip commercial fee and rate figures only), and keep the frontmatter v2 fields and the `## Reuse guidance` section.

---

## 7. Acceptance gates

These are deterministic and portable. **If the output passes them, the work is good regardless of which system produced it.** Run all five from the Wiki root before declaring the extraction finished.

```bash
# 1. Schema: every block valid against schema v2. Target: 0 violations.
python work/lint_blocks.py

# 2. Index rebuilds and row count matches the block count.
python work/regen_index.py
ls wiki/*/*.md | wc -l

# 3. Client-name leakage in the five narrative categories. Frontmatter hits are
#    legitimate (source slug, context); BODY hits are failures. resumes/ and
#    past-performance/ are verbatim by design and exempt.
grep -rn "OCWUT\|Oklahoma City Water\|Fulton County\|North Fulton\|Big Creek WRF\|Johns Creek Environmental" \
  wiki/technical-approach wiki/management-staffing wiki/win-themes wiki/qualifications wiki/compliance-plans

# 4. Every verbatim-ref resolves to a real page and paragraph (lint covers this,
#    but confirm no block lacks one).
grep -L "verbatim-ref:" wiki/*/*.md

# 5. Coverage of the verbatim layer against the source PDF text layer.
#    Word recall >= 0.99 per page. Already passing; re-run only if you
#    regenerate verbatim pages.
python work/coverage.py "raw/<file>.pdf" <slug>
```

**A sixth, judgment-based check worth doing once at the end:** ask a fresh agent, using only `wiki/index.md`, "what wins for a multi-facility membrane pursuit in the Southeast?" It should return ten or more outcome proof points with registry ids drawn from the Fulton material. If it cannot, the blocks are indexed but not usable, which is the real thing being tested.

---

## 8. The portable toolkit

All 19 scripts use only standard library plus `python-docx`, `PyMuPDF` (`fitz`), `pypdf`, `pypdfium2` and `Pillow`. No dependency on any particular AI system.

| Script | Purpose |
|---|---|
| `work/pdf_to_verbatim.py` | PDF → page-anchored verbatim markdown. Strips repeating headers, numbers paragraphs, backfills text blocks the converter dropped, renders image-only pages |
| `work/coverage.py` | Measures word recall of verbatim pages against the PDF text layer. The extraction gate |
| `work/lint_blocks.py` | Validates every block against schema v2. The schema gate |
| `work/patch_frontmatter.py` | Bulk frontmatter edits from a JSON patch file; never touches bodies |
| `work/regen_index.py` | Rebuilds `wiki/index.md` and `index.json` with facets |
| `work/dedupe_candidates.py` | Finds duplicate-topic block pairs by shingle similarity |
| `work/map_blocks_to_pages.py` | Maps existing blocks to their source pages; classifies verbatim / partial / recipe / absent |
| `work/build_docx.py` | Markdown → branded Word, with stat callouts, pull quotes, fact boxes; strips draft tags into a separate notes file |
| `work/validate_v2.py` | Validates a finished proposal section: no placeholders in body, numbers trace to sources, page budget, brand colors, banned words |
| `voice/metrics.py` | Deterministic prose metrics against the calibrated rubric gates |
| `work/read_spec_decisions.py` | Reads approval ticks from a Word decisions table and locks the pursuit spec sheet |
| `work/make_ranges_ocwut_fulton.py` | Example of how a range list is constructed for a new proposal |

---

## 9. Ingesting a future proposal, end to end

This is the flawless-repeatability path. CLAUDE.md §"Adding new content" is the authority; this is the operational sequence.

1. **Drop the PDF in `raw/`** and add a row to the source registry table in `CLAUDE.md` with a kebab-case slug.
2. **Convert locally — no model reads pages that have a text layer.** Any pymupdf4llm-based converter produces page-markered markdown. Then:
   ```bash
   python work/pdf_to_verbatim.py "raw/<file>.pdf" <slug>
   python work/coverage.py "raw/<file>.pdf" <slug>
   ```
   This step costs nothing and is exact. The 2026 pilot transcribed pages by vision *instead* of using the text layer, which is where fidelity leaked. Never do that when a text layer exists.
3. **Repair what the gate flags.** Word recall below 0.99 or a missing run of 15+ words means the converter dropped or reordered something. Fix those pages against the 300-DPI render. For genuinely image-only pages, run two independent vision transcriptions and a third pass that reconciles them against the image; mark unreadable spans `[illegible]` and never guess. Record `method: vision` in the page frontmatter.
4. **Build the section map.** One range per coherent section, twelve pages maximum. Skip blank pages, dividers, required forms, cost and fee pages, contract exceptions, vendor brochures, insurance certificates and license copies. Keep resumes and past-performance — they are verbatim categories and among the most reused content in the bank.
5. **Run the builder and judge** from §5 and §6, one agent per range, judge as a separate instance.
6. **Increment the registries**, resolve duplicates, fold in tags, regenerate the index.
7. **Pass all five gates** in §7, update the `README.md` status table, and commit.

---

## 10. Known state you should not mistake for a standard

- **Lint is at zero as of 2026-09-07.** If it is ever non-zero, that is unfinished cleanup, not an accepted tolerance.
- **All 46 testimonials carry `permission: unknown`.** No client quote may be printed in a proposal until written consent is on file. The inventory records this deliberately.
- **31 proof-point conflicts** are unresolved in the registry, each with competing values and a recommended lock. They need a human owner, not a model's judgment. Examples: corporate revenue stated three ways across sources; a compliance percentage stated as both 99.8% and 99.98%; a collection-system length stated as both 310 and 320 miles.
- **`voice/exemplar/` is empty.** The voice guide was derived from the winning proposals themselves. If an exemplar of the target voice is supplied later, re-derive the guide with it as the primary authority.
- **The rubric gate `numbers_all >= 4.0`** is calibrated on full-section units. On short units the winning proposals themselves fall below it. Treat it as directional under about 1,000 words. The calibration log at the end of `voice/voice-guide.md` explains why.
- Two early snapshot commits for this Wiki also exist in the parent home-directory git repository. Harmless, Wiki files only.

---

## 11. If you are also continuing the writing stage

`HANDOFF-writing.md` in this directory covers that separately: what a pursuit spec sheet is, how a section gets drafted and validated, the model-cost profiles, and the items that remain human-owned. The short version: the pursuit spec sheet decides *what* goes in a section before any writing starts, the voice guide decides *how* it reads, and `work/validate_v2.py` plus `voice/metrics.py` are the gates. Placeholders and unverified tags never reach body text; they go to a companion notes file.
