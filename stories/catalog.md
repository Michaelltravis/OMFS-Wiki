# Story Catalog — House Narratives for Proposal Writers

Every narrative in the wiki that tells a before/after story with an outcome, cataloged so a writer can pick the right story for the right section without re-reading source blocks. Built 2026-09-05, reconciled 2026-09-06, and **rebuilt 2026-09-11** to cover the three sources added since (`ocwut-16-26`, `fulton-county-2025`, `mmsd-om-2028`) against `proof-points/registry.md` (1,905 ids) and `testimonials/inventory.md` (71 ids). Scan scope this pass: every block under `wiki/past-performance/` (34) and `wiki/win-themes/` (130), every technical-approach block whose title carries turnaround / transition / case / savings / odor / optimization (75), plus the management-staffing and compliance-plans blocks that physically carry a cataloged quote, claim, or event (7). Story ids ST-0001 through ST-0027 are unchanged from the first pass; new stories start at ST-0028.

**Verification pass 2026-09-13.** Re-scanned the full scope against the current block set (34 past-performance, 115 win-themes, 70 technical-approach by title filter — fifteen win-theme and five technical-approach blocks have been merged or removed since 2026-09-11; every block path and verbatim page cited below still resolves). Fourteen in-scope blocks had never been checked; thirteen are framing or methodology with no delivered outcome and are now listed under *Not cataloged*, and one — the fallback WATS block — is the twin of the ST-0050 carrier and now points to ST-0050. No new story ids were needed: the catalog stands at 62. The pass also found that 54 of the 90 block patches written on 2026-09-11 had never been applied (the blocks still read `story-ids: []`); the full 91-entry map was re-applied through `work/patch_frontmatter.py` and every block was verified to carry its ids.

**How to read an entry**

- **Arc** — the before → after in one line.
- **THE BEAT** — the one sentence or fact that makes the story land. Quote it; do not paraphrase it away.
- **Proof-point claims** — every number the story depends on, with its registry id. Every id below has `approved_for_external_use: pending` and no owner; ids marked *(conflict)* have inconsistent values across sources and must be resolved in the spec sheet before use. Claims marked *(unregistered)* are non-numeric facts or figures the sweep did not capture — register them before they appear in a live draft.
- **Testimonial** — inventory id, speaker, title, organization. Permission is `unknown` for all 71 entries; nothing may be quoted externally until it is `on-file`. Quotes marked *(not in inventory)* were found in a block but never harvested — add them to `testimonials/inventory.md` before use.
- **Best for** — `rfp-section-type` values where the story earns its space.
- **Pursuit fit** — `wwtp-om` · `collections` · `stormwater` · `incumbent-displacement` · `regulatory-settlement` · `odor` (plus `reuse-dpr` / `water-treatment` / `solids` / `multi-facility` / `mbr-membrane` / `jv-delivery` where they apply).
- **Blocks / verbatim** — the wiki block(s) carrying the story and the verbatim page(s) and paragraphs that are the source of truth for the prose.
- **House favorite** — Yes / No / Conditional, with one line of reasoning.

**Rules that apply to every story:** past-performance blocks are verbatim (real names, contacts, quotes) — QC contact currency and figure currency with the account team before external use. Reference-client names stay; the pursuit client is `[CLIENT]`. A story about a third party (vendor case study, another firm's plant, a Jacobs capital program rather than an O&M contract) is labeled as such and is never presented as Jacobs O&M past performance. Blocks carry `story-ids` pointing back here; `work/fragments/st_patches.json` is the authoritative block → story map.

---

## Top 10 — reach for these first

Re-ranked 2026-09-11 across all 62 stories. Rank is by (1) hardness and checkability of the outcome, (2) whether a client witness exists, (3) breadth of pursuit fit.

| Rank | ID | Story | Why it ranks |
|---|---|---|---|
| 1 | ST-0032 | Jackson: "only Jacobs was willing to answer our calls" → lift stations from ~30% to 90% operational → 9-year wastewater award | Crisis entry, a sole-source re-award on performance, a before/after operating number, staff satisfaction 2.8 → 4.3, and three client quotes from the same speaker — the most complete turnaround in the library |
| 2 | ST-0005 | Waterbury: river overflows → up to $12.7M client-estimated savings, 99.57% compliance | Largest client-attributed dollar outcome, compliance-driven origin, now carried in three sources with a five-year compliance rate behind it |
| 3 | ST-0041 | Agua Nueva DBO: $77M under budget, 8 months early, $2M/yr lower opex, 20% energy cut | Hardest capital-delivery numbers in the library, a county director's quote, 80% of County staff retained, zero odor regulatory actions since 2013 |
| 4 | ST-0001 | Westerly first-18-months turnaround (six 30-yard containers, 32 callouts gone) | Still the most concrete, visual, itemized incumbent-displacement win list; the small-plant analog |
| 5 | ST-0034 | Vancouver: unseated a 37-year incumbent → 90% of transition in 90 days → $25M SCADA renewal with zero interruptions → Utility of the Future | The full incumbent-displacement arc with a dated schedule, a satisfaction survey, awards every year since 2017, and three Frank Dick quotes |
| 6 | ST-0028 | Waterbury odor: four scrubbers in disrepair → >55% fewer complaints between Year 1 and Year 2 → $2M upgrade | The odor story with a number; reused in three later proposals as the method proof |
| 7 | ST-0042 | San Marcos: ferric −65%, 174,000 kWh/yr, polymer −40%, hauling −50% — with no capital | Best "optimization without capital" number stack on a sensitive receiving water, 20-year tenure, 17 named awards |
| 8 | ST-0006 | Traverse City: noncompliant plant under enforcement → 35 years of compliance and awards | The regulatory-settlement story; now also carried in the Fulton source with the DNR standing restored |
| 9 | ST-0029 | Waterbury WFP: a 35-year sludge backlog cleared in the first contract quarter | "Solving a 35-year problem in the first contract quarter" is the best single early-win sentence in the set |
| 10 | ST-0013 | West Basin: nation's largest reuse facility won from Veolia — plus ST-0040, >40% hypochlorite savings after takeover | Flagship displacement with Board-level and engineering-side quotes, a satisfaction number, and now a post-takeover chemical result that only exists because the incumbent left margin on the table |

Honorable mentions: ST-0002 (Westerly "$100K more budget, $100K less cost" quote — the best client paradox), ST-0048 (five before/after staff-satisfaction pairs — the incumbent-workforce reassurance device), ST-0038 (Wilmington: operators' suggestion cut a capital schedule 40% and cost 20%), ST-0049 (North Hudson after Sandy: primary treatment back in 48 hours), ST-0008 (Southbridge odor without capital), ST-0014 (Auburn: Plant of the Year every year since 2012), ST-0012 (Annual Innovation Workshop, >$1M of Wilmington energy opportunities).

---

## Full catalog

### ST-0001 — Westerly: the first-18-months turnaround

- **Arc:** Small coastal RI plant long held by SUEZ Group, carrying DEM-mandated corrective actions from a 2016 inspection and an estimated 32 disinfection callouts a year → within 18 months Jacobs rehabilitated clarifiers in-house, closed the inherited corrective actions, eliminated the callouts, hauled six 30-yard containers of debris off the site, and refunded the scrap-metal proceeds to the Town.
- **THE BEAT:** "Removing six 30-yard containers of trash and debris from throughout the facility and pump stations, including scrap metal that was recycled with the money refunded to the client." A physical, countable, visual win an evaluator can picture — and the refund line says the operator was thinking about the Town's money.
- **Proof-point claims:** PP-0047 3.3 MGD · PP-0048 nine pump stations · PP-0057 July 2017 start · PP-0052 first 18 months · PP-0053 DEM corrective actions from 2016 inspection · PP-0054 ~32 callouts/yr eliminated (sodium hypochlorite dosing) · PP-0055 six 30-yard containers · PP-0059 RICWA Consistent Permit Compliance Award 2019–2023 · PP-0060 RICWA Three-or-More-Years Complete Permit Compliance Award 2022 · PP-0061 USEPA New England Regional O&M Excellence Award 2018 · PP-0058 $2.4M annual project fee. *(Unregistered: "SUEZ Group" as the named incumbent; in-house clarifier rehabilitation.)*
- **Testimonial:** TM-0007 — Sheila M. McGauvran, PE, Town Engineer, Town of Westerly: "Jacobs staff were on hand to take over hours before the contract inception and they hit the ground running." (permission unknown; full quote carried in ST-0002).
- **Best for:** transition, past-performance, exec-summary, tech-approach (as an embedded callout).
- **Pursuit fit:** wwtp-om, incumbent-displacement, solids; strongest when the incumbent is a large national operator.
- **Blocks / verbatim:** `wiki/past-performance/project-westerly-ri.md` (verbatim, named); `wiki/win-themes/project-narrative-contract-transition-turnaround.md` (sanitized drop-in); `wiki/past-performance/client-references.md` (Exhibit 3-5 summary) — verbatim `verbatim/hull-wwtf-om-2026/pages/p0077.md` ¶5–¶12, ¶23–¶25; `p0015.md` ¶2.
- **House favorite:** **Yes** — it is the incumbent-displacement story in miniature and the only one with a dated, itemized win list. Westerly also appears on the MMSD transitions-from-the-incumbent map (ST-0059).

### ST-0002 — Westerly: the biosolids gap becomes half a million in savings

- **Arc:** The incumbent's contract never included biosolids management and disposal; Jacobs saw the gap, took it on, adjusted hauling schedules, monitored energy, and deployed quality systems → more than $500,000 saved against the original 6-year forecast and about $250,000 against the adjusted forecast over three years — and the Town Engineer publicly described a proposal that raised the O&M budget while lowering contract cost.
- **THE BEAT:** "...Jacobs' innovative proposal, which increased the annual O&M budget by $100,000 while saving the Town $100,000 annually in contract costs." A client explaining, unprompted, how paying more for operations cost her less overall.
- **Proof-point claims:** PP-0049 >$500,000 vs. original forecast · PP-0051 6-year forecast period · PP-0050 ~$250,000 vs. adjusted forecast over 3 years · PP-0063 +$100,000/yr O&M budget (client quote) · PP-0062 −$100,000/yr contract cost (client quote). *(Unregistered: septage receiving and IPP in scope; biosolids excluded from the incumbent's contract.)*
- **Testimonial:** TM-0007 — Sheila M. McGauvran, PE, Town Engineer, Town of Westerly (permission unknown; page reference contact is Max Sposato, Utilities Director, 401.348.2561).
- **Best for:** exec-summary, past-performance, cover-letter (one line), tech-approach (biosolids).
- **Pursuit fit:** wwtp-om, solids, incumbent-displacement.
- **Blocks / verbatim:** `wiki/past-performance/project-westerly-ri.md`; `wiki/win-themes/project-narrative-contract-transition-turnaround.md`; `wiki/past-performance/client-references.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0077.md` ¶5, ¶26; `p0015.md` ¶2.
- **House favorite:** **Yes** — the "find the gap in the incumbent's scope" hook is the most reusable strategic move in the catalog, and the quote is the closer.

### ST-0003 — Westerly: consent agreement turns the operator into the designer

- **Arc:** RIDEM consent agreement in 2021 required lower nitrogen limits and a facilities-plan update → Jacobs ran hydraulic models, assessed equipment, made recommendations, and was selected as the progressive design-build designer specifically because of its operating knowledge of the plant.
- **THE BEAT:** "We were chosen as the designer due to our operational knowledge." The O&M contract became the on-ramp to a capital project without a separate procurement.
- **Proof-point claims:** PP-0056 2021 RIDEM consent agreement / nitrogen limits / Facilities Plan update. *(Unregistered: progressive design-build selection — non-numeric.)*
- **Testimonial:** none specific to this thread (TM-0007 is available on the same page).
- **Best for:** past-performance, qualifications, tech-approach (capital planning / full-service), exec-summary.
- **Pursuit fit:** wwtp-om, regulatory-settlement; any facility under a consent order or facing a nutrient limit.
- **Blocks / verbatim:** `wiki/past-performance/project-westerly-ri.md`; `wiki/win-themes/project-narrative-contract-transition-turnaround.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0077.md` ¶12.
- **House favorite:** **Conditional** — decisive when the target sits under a consent agreement or needs a facilities plan; filler otherwise. Pairs with ST-0038 (Wilmington) as the second "operator input changes the capital outcome" proof.

### ST-0004 — Westerly: biofilter media upgrade saves over $134K

- **Arc:** Aging biofilter running on organic media with short service life → Jacobs converted it to engineered media with a significantly longer life → fewer replacements, better reliability, and more than $134K in cost savings.
- **THE BEAT:** "...upgrading an aging biofilter system from organic media to engineered media with a significantly longer service life. This reduced replacement frequency, improved system reliability, and delivered over $134k in cost savings." An odor asset that paid for itself — the story ends on a hard dollar figure.
- **Proof-point claims:** PP-0151 >$134K cost savings (single-source; stated as "over $134k"). *(Unregistered: organic → engineered media; reduced replacement frequency — non-numeric.)*
- **Testimonial:** none.
- **Best for:** exec-summary, tech-approach (odor control, asset management), past-performance.
- **Pursuit fit:** wwtp-om, odor, collections (pump-station odor).
- **Blocks / verbatim:** `wiki/win-themes/proof-point-examples-coastal-complex-systems.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0007.md` ¶13.
- **House favorite:** **Yes** — the cleanest odor-plus-savings sentence in the library; drops into an executive summary unchanged. The figure is single-source — get the account team to confirm the year and the basis before it leads a section.

### ST-0005 — Waterbury: river overflows to $12.7 million in estimated savings

- **Arc:** Late-2017 sewer overflows fouled the Naugatuck River; the City ran a careful selection and chose Jacobs in November 2018 → a holistic operations + asset-management + CMOM + regional-support model, co-management of a ~$25 million phosphorus upgrade, and City-estimated savings of up to $12.7 million against the previous operating approach — and in 2023 the City handed Jacobs the water system too, previously operated by Veolia.
- **THE BEAT:** "The City estimated cost savings of up to $12.7 million compared to the previous operating approach." The client's number, not Jacobs' — and the Director of Finance is the one saying he "rest[s] easier."
- **Proof-point claims:** PP-0042 / PP-0830 up to $12.7M client-estimated savings · PP-0831 / PP-1391 99.57% NPDES permit compliance over the past 5 years · PP-0044 2017 overflows preceded procurement · PP-0043 November 2018 start · PP-0030 10-year agreement · PP-0035 ~$25M phosphorus upgrade · PP-0031 27 MGD design · PP-0045 <54 MGD wet weather *(conflict — 70 MGD appears in resume blocks)* · PP-0032 ~310 miles sewer *(conflict — 320 in Exhibit 3-3)* · PP-0033 20 pump stations · PP-0046 $6M annual project fee · PP-1656 water-system O&M contract awarded 2023 (previously Veolia) · PP-0648 Waterbury listed among the largest recent U.S. utility transitions Jacobs led.
- **Testimonial:** TM-0006 — Mike LeBlanc, Director of Finance, City of Waterbury: "I've seen a lot of improvements since our partnership began in 2018, and I rest easier knowing that Kevin Dahl and his team are taking excellent care of our wastewater system." (permission unknown; contact 203.574.6840 ext. 7059). **Attribution conflict:** the OCWUT source prints the same words over "Mayor Neil O'Leary, City of Waterbury, CT" (TM-0059, `ocwut-16-26/p0170 ¶1`). Resolve the speaker with the account team before the quote appears anywhere. Water-side witness: TM-0066 — Rob Langenauer, Superintendent of Water, City of Waterbury ("value-added services and savings to the city").
- **Best for:** past-performance, exec-summary, qualifications, cover-letter (one line).
- **Pursuit fit:** wwtp-om, collections, water-treatment (2023 expansion), regulatory-settlement (overflow-driven), incumbent-displacement, large or complex systems.
- **Blocks / verbatim:** `wiki/past-performance/project-waterbury-ct.md`; `wiki/past-performance/project-waterbury-ct-odor-control-and-results.md`; `wiki/win-themes/project-narrative-utility-partnership-cost-savings.md`; `wiki/past-performance/client-references.md`; `wiki/technical-approach/fulton-successful-experience-transition-asset-community.md` (2023 water award, TM-0066) — verbatim `verbatim/hull-wwtf-om-2026/pages/p0076.md` ¶3–¶4, ¶6, ¶17; `p0015.md` ¶2; `verbatim/ocwut-16-26/pages/p0170.md` ¶1, ¶7–¶8; `verbatim/fulton-county-2025/pages/p0026.md` ¶13, ¶25.
- **House favorite:** **Yes** — the biggest number in the library with a compliance-event origin and a finance-side witness; now the parent of four Waterbury sub-stories (ST-0028 odor, ST-0029 sludge backlog, ST-0030 CMOM, ST-0031 pipe collapse).

### ST-0006 — Traverse City: noncompliant plant with enforcement actions becomes a 35-year award winner

- **Arc:** In 1990 Jacobs took over a noncompliant facility under enforcement → a comprehensive operational strategy and maintenance management program restored compliance and resolved the enforcement actions → compliance held ever since, with awards in 2004, 2006, 2007, and 2019.
- **THE BEAT:** "We assumed operations when the facility was noncompliant and implemented a comprehensive operational strategy and maintenance management program that restored compliance and resolved enforcement actions." Then cite the award spread, not a single award — four award years across two decades prove it stuck. The Fulton wording adds the regulator: "introduced a sound operational plan and a CMMS that restored the plant's standing with the Michigan Department of Natural Resources."
- **Proof-point claims:** PP-0074 1990 start · PP-0081 2019 MWEA Large Facility Safety Award · PP-0082 2007 U.S. EPA Region 5 Best Operated and Maintained Facility · PP-0083 2006 ACEC Engineering Excellence Award (source reads "ACED") · PP-0084 2006 ACEC/SPE Eminent Conceptor Award · PP-0085 2004 MWEA Health and Safety Award · PP-0223 / PP-1883 $1.5M BNR upgrade (1999) · PP-0224 / PP-1883 $31M MBR upgrade (2004) · PP-0076 / PP-1880 8.5 MGD · PP-0078 / PP-1881 17 MGD peak · PP-0077 / PP-1880 ~50,000 residents · PP-1882 nine lift stations · PP-0075 13 staff · PP-0080 $3.5M annual project fee. *(Unregistered: "enforcement actions resolved" and "restored the plant's standing with the Michigan DNR" — non-numeric; verbatim at hull p0080 ¶3 and fulton p0174 ¶8.)*
- **Testimonial:** TM-0009 / TM-0064 — Richard Lewis, Traverse City Council Commissioner (see ST-0007 for the quote; permission unknown; page reference contact is Art Krueger, Director of Municipal Facilities).
- **Best for:** past-performance, qualifications, exec-summary, compliance.
- **Pursuit fit:** wwtp-om, regulatory-settlement, solids, mbr-membrane, multi-facility (satellite systems). Caution: lead with the turnaround, not the tenure, when the pursuit is driven by dissatisfaction with a long-tenured incumbent.
- **Blocks / verbatim:** `wiki/past-performance/project-traverse-city-mi.md`; `wiki/past-performance/fulton-traverse-city-dbo-overview.md`; `wiki/past-performance/fulton-traverse-city-dbo-accomplishments.md`; `wiki/win-themes/project-narrative-long-term-dbo-performance-excellence.md`; `wiki/past-performance/client-references.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0080.md` ¶3, ¶8–¶9, ¶18–¶22; `p0015.md` ¶2; `verbatim/fulton-county-2025/pages/p0174.md` ¶2–¶3, ¶8; `p0175.md` ¶2, ¶9.
- **House favorite:** **Yes** — the only enforcement-resolution story in the set, and the durability proof point.

### ST-0007 — Traverse City: MBR optimization cuts electricity more than 30%, membranes outlive their design life

- **Arc:** A $31 million MBR upgrade installed → optimization after installation reduced electrical consumption by more than 30% (about $120,000 a year) with additional chemical and natural-gas savings — enough that Jacobs lowered the fee to the City over a five-year period → proactive maintenance carried membrane performance beyond expected service life, and the Council Commissioner credits the maintenance program for it. Grand Traverse County's satellite plant posted a 40% cut (about $65,000 a year).
- **THE BEAT:** Pair the number with the quote: "Optimization efforts following MBR installation reduced electrical consumption by more than 30%" + "the Traverse City WWTP filter membrane operation has exceeded the life expectancy because of the maintenance program Jacobs put in place." Together they turn "proactive maintenance" into a measured result. The Fulton source adds the consequence: "These savings... allowed Jacobs to lower the fee to the city over a 5-year period."
- **Proof-point claims:** PP-0079 / PP-1885 >30% electrical consumption reduction post-MBR · PP-1654 ~$120,000/yr at the Regional WWTP and 40% (~$65,000/yr) at Grand Traverse County · PP-0224 $31M MBR upgrade · PP-0078 17 MGD peak · PP-0086 "29 plus years" (as quoted). *(Unregistered: additional chemical and natural gas savings; membrane life beyond expected lifespan; fee lowered over 5 years — the fee statement carries no figure and is narrative, not commercial data.)*
- **Testimonial:** TM-0009 — Richard Lewis, Traverse City Council Commissioner: "One of the value-added qualities of Jacobs is the maintenance program..." (permission unknown; the Fulton variant is TM-0064).
- **Best for:** tech-approach (energy, asset management), exec-summary, past-performance.
- **Pursuit fit:** wwtp-om, mbr-membrane, energy/asset-management-driven pursuits.
- **Blocks / verbatim:** `wiki/past-performance/project-traverse-city-mi.md`; `wiki/past-performance/fulton-traverse-city-dbo-accomplishments.md`; `wiki/technical-approach/fulton-successful-experience-multi-facility-mbr.md`; `wiki/win-themes/project-narrative-long-term-dbo-performance-excellence.md`; `wiki/past-performance/client-references.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0080.md` ¶7, ¶23; `p0015.md` ¶2; `verbatim/fulton-county-2025/pages/p0175.md` ¶4, ¶11; `p0025.md` ¶3.
- **House favorite:** **Yes** — quantified energy outcome plus a client witness; reusable wherever asset life or energy is scored.

### ST-0008 — Southbridge: odor complaints resolved without a capital project

- **Arc:** Persistent odor concerns under the previous operator → early-contract odor workshop with Town leadership and Jacobs process specialists → enhanced solids management, optimized aeration and process control, refined residuals handling → a measurable reduction in odor complaints and improved process stability, with no immediate capital investment.
- **THE BEAT:** "These changes addressed the root causes of odors without requiring immediate capital investment." States the before-condition as fact ("under the previous operator"), names the mechanism (a workshop that mirrors the proposed framework), and answers the evaluator's fear that odor fixes mean capital dollars.
- **Proof-point claims:** none registered — the outcome is qualitative in every source ("measurable reduction in odor complaints"; "reduced long-standing odor issues related to biosolids composting"). Do not invent a number. Supporting facts, also qualitative: odor control and dispersion study completed; composting improved by optimizing the wood amendment-to-biosolids ratio and adjusting blower operations by pile temperature (p0015 ¶2).
- **Testimonial:** TM-0008 — Rich Benoit, Director of Public Works, Town of Southbridge (see ST-0009; permission unknown).
- **Best for:** tech-approach (odor — as a sidebar beside the five-step framework), exec-summary, past-performance.
- **Pursuit fit:** odor, wwtp-om, collections, incumbent-displacement, solids (composting).
- **Blocks / verbatim:** `wiki/win-themes/embedded-differentiator-case-study-callout.md` (the callout); `wiki/technical-approach/site-specific-odor-control-program.md` (the methodology it sits beside); `wiki/win-themes/proof-point-examples-coastal-complex-systems.md` (one-paragraph exec-summary version); `wiki/past-performance/project-southbridge-ma.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0037.md` ¶1–¶3; `p0007.md` ¶10; `p0078.md` ¶7; `p0015.md` ¶2.
- **House favorite:** **Yes** — the capital-light odor story; when a number is needed, lead with ST-0028 (Waterbury, >55%) and use this as the "no capital" companion.

### ST-0009 — Southbridge: a unanimous "fresh start" that converted into an $85 million capital award

- **Arc:** Town needed a fresh start on wastewater operations and ran a competitive procurement → Jacobs unanimously selected; assumed full operating responsibility February 1, 2025 → immediate investment commitments (compost screening, odor dispersion study, Dragonfly AI CCTV, annual innovation workshops) → the Jacobs Design-Build group awarded the $85 million nitrogen reduction upgrade at the same plant.
- **THE BEAT:** "Jacobs was unanimously selected by the Town..." followed by the dated takeover — and then the $85 million design-build award, which shows a young O&M relationship converting to major capital work in under a year.
- **Proof-point claims:** PP-0006 February 1, 2025 takeover · PP-0002 5-year contract · PP-0003 3.77 MGD *(conflict — 3.7 in Exhibit 3-3)* · PP-0004 48 miles · PP-0005 11 lift stations · PP-0222 $85M nitrogen reduction upgrade (Exhibit 3-5 only) · PP-0064 2025 start · PP-0065 $1.7M annual project fee *(conflict)*. *(Unregistered: unanimous selection; Dragonfly AI enhanced CCTV — non-numeric.)*
- **Testimonial:** TM-0008 — Rich Benoit, Director of Public Works: "Southbridge was in need of a fresh start for our wastewater operations, and after undertaking a competitive procurement process, we were able to select the company that we feel is best suited for our needs." (permission unknown; page reference contact is John Jovan, Jr., Town Manager).
- **Best for:** past-performance, transition, exec-summary, qualifications (full-service / capital conversion).
- **Pursuit fit:** wwtp-om, collections, incumbent-displacement, solids; in-state proof for Massachusetts pursuits.
- **Blocks / verbatim:** `wiki/past-performance/project-southbridge-ma.md`; `wiki/win-themes/project-narrative-new-contract-mobilization-innovation.md`; `wiki/past-performance/client-references.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0078.md` ¶3, ¶5–¶9, ¶19; `p0015.md` ¶2.
- **House favorite:** **Conditional** — the template for a too-new-to-have-outcomes reference; use only for genuinely recent starts. Southbridge also sits on the MMSD transitions-from-the-incumbent map (ST-0059).

### ST-0010 — South Huron: the workforce came across and stayed

- **Arc:** Regional authority changes operators in 2019 with a 24-MGD plant and an existing workforce at stake → Jacobs led a successful staff transition, implemented targeted training, and kept a collaborative work environment → retention and operational continuity through the changeover, credited as outcomes.
- **THE BEAT:** "Since 2019, Jacobs has led a successful staff transition and implemented targeted training programs to strengthen workforce capability." The one reference that names people, not plant, as the result.
- **Proof-point claims:** PP-0069 2019 start · PP-0066 24 MGD design · PP-0008 9.99 MGD average *(conflict — 8 MGD in a resume)* · PP-0070 ~90,000 residents · PP-0067 36 miles interceptor *(conflict — 39 in Exhibit 3-3)* · PP-0068 two lift stations · PP-0071 1.3 MGD and PP-0072 39 MGD lift stations · PP-0073 $5.3M annual fee *(conflict — Appendix B page shows a literal "$xxM" placeholder)*. *(Unregistered: staff transition, training, retention — all qualitative.)*
- **Testimonial:** none usable — the testimonial printed on the Appendix B page is a copy/paste of the Southbridge quote (TM-0008, Rich Benoit) and must not be attributed to SHVUA. (TM-0002, Firooz Fath-Azam, former SHVUA System Manager, is a workshop quote — see ST-0012.)
- **Best for:** transition, staffing, past-performance.
- **Pursuit fit:** wwtp-om, collections, incumbent-displacement (transition-risk-driven evaluations, unionized or long-tenured incumbent staff).
- **Blocks / verbatim:** `wiki/past-performance/project-south-huron-mi.md`; `wiki/win-themes/project-narrative-workforce-transition-biosolids-modernization.md`; `wiki/past-performance/client-references.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0079.md` ¶3, ¶8; `p0015.md` ¶2.
- **House favorite:** **Conditional** — essential when the evaluator's fear is losing staff; carries two source-document errors that must be fixed first. For a quantified workforce-continuity proof use ST-0048 instead.

### ST-0011 — South Huron: biosolids modernized to Class A while the plant kept running

- **Arc:** Conventional thickening and stabilization with high residuals, chemical, and energy demand → alternatives evaluation, then thermal hydrolysis and supporting infrastructure for Class A biosolids, plus VFD and SCADA automation → reduced residuals volume, chemical use, and energy demand, a more sustainable disposal path, and continuous operations throughout.
- **THE BEAT:** "These improvements reduced residuals, improved efficiency, and provided a more sustainable disposal approach while maintaining continuous operations." Capital planning contribution beyond O&M, delivered without a shutdown.
- **Proof-point claims:** PP-0010 $5M Lystek thermal hydrolysis project, "the first biosolids handling process of its kind in Michigan" (from the Nathan Callison resume, p0069 ¶9). *(Unregistered: reduced solids volume, chemical usage, energy demand — qualitative.)*
- **Testimonial:** none usable (see ST-0010).
- **Best for:** tech-approach (biosolids, capital planning), past-performance, qualifications.
- **Pursuit fit:** wwtp-om, solids, biosolids-market-risk pursuits.
- **Blocks / verbatim:** `wiki/past-performance/project-south-huron-mi.md`; `wiki/win-themes/project-narrative-workforce-transition-biosolids-modernization.md`; `wiki/past-performance/client-references.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0079.md` ¶5–¶6; `p0015.md` ¶2; dollar figure at `p0069.md` ¶9.
- **House favorite:** **No** — good supporting evidence, but the outcomes are qualitative; the $5M figure describes the project size, not a saving.

### ST-0012 — Annual Innovation Workshop: "a WEFTEC workshop in your own backyard"

- **Arc:** Partnership claims are rhetorical until a mechanism proves them → a facilitated annual workshop of client staff and Jacobs SMEs reviews the year, sets targets, and avoids complacency → a former system manager describes eight hours that felt like a national conference built for his plant, and at Wilmington the workshop surfaced energy savings opportunities valued at more than $1 million.
- **THE BEAT:** "It was like attending a WEFTEC workshop in your own backyard with all the presentations that were custom made for your facility." Client validation that the workshop is substance, not a sales event — and the Santa Monica version adds the number: "energy savings opportunities valued at more than $1 million for the Wilmington WWTP."
- **Proof-point claims:** PP-0528 / PP-2276 >$1M energy savings opportunities identified for Wilmington WWTP ("opportunities identified," not savings realized — say so) · PP-0152 8-hour workshop · PP-0141 one per year · PP-0278 no cost to client · PP-0279 prior agendas from Traverse City, MI and Wilmington · PP-0158 $350,000 over 10 years (Hull bundle) · PP-0465 $300,000 over 5 years (Santa Monica bundle) · PP-0472 2–3 consulting SMEs · PP-0112 delivered June 5, 2024 agenda · PP-0113 agenda session count *(conflict — 9 vs. 10)*. Bundle values are pursuit-specific, not house numbers.
- **Testimonial:** TM-0002 — Firooz Fath-Azam, Former System Manager, South Huron Valley Utility Authority; TM-0010 — Vincent Carroccia, Deputy Commissioner of Public Works, City of Wilmington, DE. Both permission unknown. Use Wilmington, DE (not NC).
- **Best for:** exec-summary, tech-approach, cover-letter (one clause).
- **Pursuit fit:** wwtp-om, collections, reuse-dpr, multi-facility, incumbent-displacement (as the "more than routine O&M" device).
- **Blocks / verbatim:** `wiki/win-themes/exec-summary-annual-innovation-workshop-partnership-narrative.md`; `wiki/technical-approach/annual-innovation-workshop-program.md`; `wiki/technical-approach/swip-annual-innovation-workshop.md`; `wiki/technical-approach/innovation-workshop-appendix-agenda-and-examples.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0007.md` ¶15–¶19; `p0027.md` ¶5; `p0086.md` ¶7–¶21; `verbatim/santamonica-swip-om-2025/pages/p0062.md` ¶20, ¶24, ¶26, ¶30–¶31. (The Fulton, OCWUT and MMSD sources each offer the workshop again — `fulton-annual-innovation-workshop.md`, `mmsd-annual-innovation-workshop.md` — as a forward offer; the delivered-outcome evidence stays in the blocks above.)
- **House favorite:** **Yes** — the partnership beat every winning executive summary in the set uses; keep the quote attached, and lead with the $1M Wilmington line when energy is scored.

### ST-0013 — West Basin: the nation's largest reuse facility won from Veolia

- **Arc:** The 40-MGD Edward C. Little Water Recycling Facility — nine treatment trains, five product-water grades, four satellites, nearly 600 connections — operated by Veolia for more than 20 years → West Basin awards Jacobs a five-year O&M contract in 2025, Jacobs leads the transition and assumes full responsibility September 1, 2025, the Board President frames the award as an investment in long-term performance, the Manager of Engineering calls the transition "managed very effectively, with minimal challenges," staff satisfaction rises from 3.6 to 4.1, and the Assistant General Manager says the chemical-optimization tools "really made a difference in their selection."
- **THE BEAT:** "We are currently leading the transition from the District's previous contract operator, Veolia." Naming the displaced incumbent on the nation's most sophisticated reuse plant, then closing with the Board President: "We look forward to working with Jacobs to continue that high-quality production our customers have come to know and trust."
- **Proof-point claims:** PP-0022 40 MGD *(conflict — "30-40 MGD" in a resume)* · PP-0395 nine treatment trains · PP-0396 five water grades · PP-0413 drinking water conserved for up to 80,000 households/yr · PP-0414 four satellite facilities · PP-0415 nearly 600 connections · PP-0416 2025 start · PP-0412 five-year term · PP-0337 previous operator tenure >20 years · PP-0391 full responsibility September 1, 2025 · PP-0339 / PP-1412 employee satisfaction 3.6 → 4.1 · PP-2405 "largest reuse facility in North America" (MMSD wording). *(Unregistered: "$25M/year contract" in the Eric Owens quote — a contract value, treat as commercial and do not restate outside the quote.)*
- **Testimonial:** TM-0017 — Gloria Gray, Board President and Division II Director, West Basin Municipal Water District. TM-0004 / TM-0061 — Susanna Li, Manager of Engineering (310.660.6238): "...the transition was managed very effectively, with minimal challenges..." *(Not in inventory)*: Eric Owens, Assistant General Manager, West Basin — "Jacobs' ability to optimize our chemical budget using their digital tools really made a difference in their selection." (`mmsd-om-2028/p0068 ¶11`; graphic `297_007CAM_1`) — harvest before use. All permission unknown.
- **Best for:** past-performance, transition, exec-summary, qualifications.
- **Pursuit fit:** reuse-dpr, water-treatment, multi-facility, incumbent-displacement. Keep operating-history claims proportional to tenure; the story is the transition, not the record — the post-takeover chemical result is ST-0040.
- **Blocks / verbatim:** `wiki/past-performance/edward-c-little-water-recycling-facility-om.md`; `wiki/past-performance/references-section-overview.md`; `wiki/management-staffing/wastewater-om-transition-plan-mobilization.md`; `wiki/technical-approach/ocwut-transition-client-testimonials-proven-success.md`; `wiki/technical-approach/ocwut-workforce-transition-leadership-and-operational-readiness.md` (Exhibit 5-14 satisfaction table); `wiki/win-themes/mmsd-exec-summary-seamless-transition-and-workforce-continuity.md`; `wiki/technical-approach/mmsd-four-pillars-of-chemical-optimization.md` (Owens quote) — verbatim `verbatim/santamonica-swip-om-2025/pages/p0028.md` ¶2, ¶5–¶8; `p0029.md` ¶5–¶9; `p0021.md` ¶2; `p0020.md` ¶9; `verbatim/hull-wwtf-om-2026/pages/p0046.md` ¶15–¶16; `p0048.md` ¶6; `verbatim/ocwut-16-26/pages/p0145.md` ¶6; `p0148.md` ¶4; `verbatim/mmsd-om-2028/pages/p0011.md` ¶9; `p0068.md` ¶11.
- **House favorite:** **Yes** — the flagship incumbent-displacement reference with a Board-level quote, an engineering-side transition quote, an AGM selection quote, and a staff-satisfaction number; name Veolia only where the competitive posture warrants it.

### ST-0014 — Auburn: 32 years, and Plant of the Year every year since 2012

- **Arc:** A three-decade contract operations relationship for a California WWTP and collection system → strong technical personnel "improved our process tremendously, and reduced costs" → CWEA Plant of the Year and Collections of the Year every year since 2012, and the client calls the team "an extension of the City."
- **THE BEAT:** "The Jacobs team has won Plant of the Year and Collections of the Year every year since 2012 from the California Water Environment Association." Specific enough to be checked, which is what makes it credible — placed as a sidebar beside the collections methodology it validates.
- **Proof-point claims:** PP-0304 tenure *(conflict — 32 years in the Hull quote, 33 years on the Santa Monica footprint map; both are as-of dates, recompute)* · PP-0305 CWEA Plant of the Year and Collections of the Year every year since 2012. *(Unregistered: cost reduction — qualitative.)*
- **Testimonial:** TM-0003 — Mengil Dean, Public Works Manager, City of Auburn WWTP, CA (permission unknown; no contact on the page).
- **Best for:** tech-approach (collections — embedded sidebar), exec-summary, past-performance.
- **Pursuit fit:** collections, wwtp-om, incumbent-displacement (as a tenure-and-awards contrast).
- **Blocks / verbatim:** `wiki/technical-approach/collection-system-om-program.md` (carries the verbatim quote); `wiki/win-themes/embedded-client-testimonial-technical-narrative.md` (recipe for placement) — verbatim `verbatim/hull-wwtf-om-2026/pages/p0034.md` ¶10–¶11.
- **House favorite:** **Yes** — the best long-tenure quote in the library; the tenure → outcome → award → relationship sequence is a template.

### ST-0015 — Turlock ZLD: inherited design problems to $147K a year in chemical savings

- **Arc:** A new zero-liquid-discharge RO system at a 250 MW power plant arrives with operational challenges baked into the design → Jacobs re-plumbs, re-instruments, tunes loops, rewrites WAC rinse procedures to use one-fifth the water, and invents a bulk-chemical RO cleaning method → mixed-bed throughput up from 480,000 to 500,000 gallons (4%) with no quality loss, longer crystallizer runs, and $147,000 in chemical savings every year — over almost 20 years.
- **THE BEAT:** "The new method generates $147,000 in chemical savings for the client annually." An operator-invented fix with a recurring dollar figure, backed by a client who names "outstanding communication and transparency" as what he values most.
- **Proof-point claims:** PP-0411 $147,000/yr chemical savings · PP-0409 mixed-bed throughput 480,000 → 500,000 gallons · PP-0410 4% increase without loss of quality · PP-0408 WAC rinse using one-fifth the water · PP-0382 0.75 MGD *(conflict — 0.8 MGD on one page)* · PP-0397 250 MW plant · PP-0407 2005 start · PP-0369 ~20 years tenure.
- **Testimonial:** TM-0016 — Andrew Katen, Turlock Irrigation District (no title in source; permission unknown). Reference contact: Mike Tehada, Combustion Turbine Department Manager, 209.883.3455.
- **Best for:** past-performance, tech-approach (chemical efficiency, process optimization), exec-summary.
- **Pursuit fit:** water-treatment, industrial / power-adjacent; energy-chemical-efficiency themes in any pursuit.
- **Blocks / verbatim:** `wiki/past-performance/turlock-zero-liquid-discharge-facility-om.md`; `wiki/past-performance/references-section-overview.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0026.md` ¶8–¶12; `p0027.md` ¶2–¶8.
- **House favorite:** **Yes** — best-quantified continuous-improvement story in the reuse/industrial set.

### ST-0016 — Clovis: value engineering and MemPulse extend the life of a Title 22 MBR

- **Arc:** New Title 22 scalping plant delivered under a DBO with five industry awards → Jacobs saved the City more than $100,000 through value engineering, then improved MBR cleaning with MemPulse to extend fiber life, upgraded SCADA around operator input, tuned polymer and sludge parameters, and partnered with Palantir on DO control → all NPDES, reclamation, and odor guarantees met consistently since 2009, and no OSHA recordable injury in more than 15 years of operation.
- **THE BEAT:** "...saving the City more than $100,000 through value engineering" plus the operator-voice reality check: "Nobody wants to replace membranes early–they are expensive!" The Fulton source adds the safety close: "our staff has not had an OSHA recordable safety incident or injury since we began operating the facility in 2009."
- **Proof-point claims:** PP-0399 / PP-1890 >$100,000 value-engineering savings · PP-1890 $37M facility · PP-0381 2.8 MGD *(conflict — 3.1 MGD max-month in the Fulton reference panel)* · PP-0398 2009 start · PP-0368 16 years tenure · PP-1891 no recordable safety injuries for over 15 years · PP-0403 2009 DBIA Excellence Award · PP-0400 2009 WateReuse Award of Merit · PP-0401 2009 GWI Reuse Project of the Year Finalist · PP-0402 2009 AAEE Design Honor Award · PP-0404 2008 EBJ Merit Award. *(Unregistered: MemPulse adoption; Palantir DO control savings — qualitative.)* Caution: the same Santa Monica source self-discloses Clovis permit excursions (PP-0497–PP-0511) and the Fulton performance page admits electrical-guarantee shortfalls — reconcile "met consistently" with both before using it.
- **Testimonial:** TM-0014 — Tony Duffy, Jacobs Plant Manager (a Jacobs voice, not a client — do not present as a client testimonial).
- **Best for:** past-performance, tech-approach (MBR optimization), compliance (safety record).
- **Pursuit fit:** reuse-dpr, wwtp-om, mbr-membrane, water-treatment (Title 22).
- **Blocks / verbatim:** `wiki/past-performance/clovis-wwtp-wrf-om.md`; `wiki/past-performance/fulton-clovis-reuse-facility-overview.md`; `wiki/past-performance/fulton-clovis-reuse-facility-performance.md`; `wiki/past-performance/references-section-overview.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0022.md` ¶3–¶11; `p0023.md` ¶3–¶9; `verbatim/fulton-county-2025/pages/p0178.md` ¶2; `p0179.md` ¶3, ¶7, ¶12, ¶14.
- **House favorite:** **No** — solid reference, but the savings figure is modest and the only quote is internal; the 15-year zero-recordable line is the most usable new fact.

### ST-0017 — Soquel Creek: in the room at design, running the plant at startup

- **Arc:** A critically overdrafted groundwater basin needs an advanced purification plant → under an OMAR contract Jacobs reviews operability through design, supports construction and acceptance testing, then takes a 15-year O&M term → the General Manager credits the design-through-operations continuity and calls Jacobs "an extension of our team."
- **THE BEAT:** "From design through start-up and now operations, Jacobs has provided valuable support and service..." — the client narrating the lifecycle arc herself. (Outcome is relational rather than quantified; pair with ST-0018 for the number.)
- **Proof-point claims:** PP-0358 1.3 MGD *(conflict — 1.7 and 2 MGD appear elsewhere in the same proposal)* · PP-0405 15-year initial O&M term · PP-0406 2020 start · PP-0365 4 years tenure.
- **Testimonial:** TM-0015 — Melanie Mow Schumacher, General Manager, Soquel Creek Water District (permission unknown).
- **Best for:** past-performance, qualifications (full-service lifecycle), transition (startup).
- **Pursuit fit:** reuse-dpr, water-treatment; any pursuit with early O&M-provider engagement (OMAR/DBO).
- **Blocks / verbatim:** `wiki/past-performance/soquel-creek-advanced-water-purification-om.md`; `wiki/past-performance/references-section-overview.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0024.md` ¶2–¶8; `p0025.md` ¶3–¶5.
- **House favorite:** **Conditional** — decisive for OMAR/at-risk or startup-heavy pursuits; otherwise a supporting reference.

### ST-0018 — Soquel Creek: more than 10% energy reduction from membrane recovery and blower reprogramming

- **Arc:** An advanced treatment train running at design energy intensity → SCADA-integrated energy dashboards, VFD tuning, membrane recovery optimization, and blower reprogramming → more than 10% energy reduction.
- **THE BEAT:** "At Soquel Creek, the Jacobs team achieved more than 10% energy reduction through membrane recovery optimization and blower reprogramming." A named plant, a named mechanism, a percentage.
- **Proof-point claims:** PP-0476 >10% energy reduction at Soquel Creek (single-source).
- **Testimonial:** none in this block (see ST-0017).
- **Best for:** tech-approach (energy optimization), exec-summary.
- **Pursuit fit:** reuse-dpr, water-treatment, wwtp-om (membrane facilities).
- **Blocks / verbatim:** `wiki/technical-approach/swip-energy-chemical-efficiency-fleet-program.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0047.md` ¶10.
- **House favorite:** **Conditional** — use wherever energy is scored at a membrane plant; never reattribute to another facility.

### ST-0019 — Pure Water Monterey: RO clean-in-place frequency cut 35%

- **Arc:** RO trains cleaning on a fixed, frequent cycle → membrane monitoring and refined pre-treatment → 35% fewer CIP events, with the approach offered for replication via performance-normalization tools and vendor-integrated service contracts.
- **THE BEAT:** "...Jacobs reduced RO clean-in-place (CIP) frequency by 35% through membrane monitoring and refined pre-treatment practices." Fewer cleans means less chemical, less downtime, longer membranes.
- **Proof-point claims:** PP-0478 35% RO CIP frequency reduction at Pure Water Monterey (single-source).
- **Testimonial:** none.
- **Best for:** tech-approach (chemical efficiency, membrane optimization), exec-summary.
- **Pursuit fit:** reuse-dpr, water-treatment (RO facilities).
- **Blocks / verbatim:** `wiki/technical-approach/swip-energy-chemical-efficiency-fleet-program.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0048.md` ¶4.
- **House favorite:** **Conditional** — RO-specific; strong where it applies, irrelevant elsewhere.

### ST-0020 — NJAW Bound Brook (SmartCover vendor case): 12 SSOs a year to zero

- **Arc:** A newly acquired collection system with unknown I&I and a smoke-and-dye timeline of 18–24 months → 40 satellite SmartCover level monitors with NOAA/USGS integration and Hazen analytics → I&I isolated up to 12 months sooner, 16 SSOs prevented in the first four months, annual SSOs cut from 12 to 0, and the fleet grown to 196 units in under two years.
- **THE BEAT:** "Reduced annual SSOs from 12 to 0." Then the adoption signal: from 40 units to 196 across the utility's systems in less than two years — the client kept buying.
- **Proof-point claims:** PP-0125 12 → 0 annual SSOs · PP-0130 16 SSOs prevented in four months · PP-0129 40 units · PP-0131 196 units in under two years · PP-0127 18–24-month traditional methods · PP-0128 up to 12 months sooner · PP-0126 August 2022 acquisition · PP-0118 2.8M people · PP-0119 190 communities · PP-0120 31 systems · PP-0121 21 WWTPs · PP-0122 85 lift stations · PP-0123 500+ miles · PP-0124 >$105M invested over five years. Related vendor-wide claims: PP-0114 >40,000 overflows prevented; PP-0116 75–95% cleaning reduction.
- **Testimonial:** TM-0013 — unattributed NJAW customer statement in vendor literature (no named speaker; permission unknown). Related vendor testimonials TM-0011 (Arlington, TX) and TM-0012 (South Coast Water District).
- **Best for:** tech-approach (collections / I&I), past-performance appendix (as a technology case study).
- **Pursuit fit:** collections, stormwater (wet-weather I&I), wwtp-om.
- **Blocks / verbatim:** `wiki/technical-approach/smartcover-njaw-bound-brook-case-study.md`; the "up to 12 months sooner" claim is repeated in `wiki/technical-approach/collection-system-om-program.md` and `wiki/win-themes/value-added-no-cost-enhancements-framing.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0092.md` ¶3, ¶6, ¶10–¶11, ¶14; `p0093.md` ¶6, ¶11; `p0090.md` ¶11.
- **House favorite:** **Conditional** — the hardest before/after numbers on collections in the library, but it is SmartCover/Hazen/NJAW's story, not Jacobs'. Label it a technology case study every time.

### ST-0021 — Rio Rancho (AquaDNA DeRagger): eight pumps, no new panels, chronic SSOs reduced

- **Arc:** Chronic ragging-driven SSOs at a Jacobs-operated New Mexico project → eight sewage pumps fitted with the AquaDNA deragging system with no change to pumps, starters, or VFDs → SSO events reduced, with a dashboard tracking cleans, cycles, first-flush events, and time-to-spill; the Fulton source adds a newer installation at Wilmington, DE.
- **THE BEAT:** "...eight sewage pumps have been fitted with the system (no change in pumps or starters/VFDs is required) to reduce previously chronic sanitary sewer overflow (SSO) events." The no-retrofit clause is the sale.
- **Proof-point claims:** PP-0475 eight pumps at Rio Rancho, NM · PP-0473 ~100 US installations · PP-0474 decade of operating experience · PP-0468 $75,000 value over 5 years (Santa Monica bundle — pursuit-specific). *(Unregistered: SSO reduction — qualitative; Wilmington, DE installation; the Fulton $1,663,000 AquaDNA investment figure is a pursuit-specific value-add, not an outcome.)*
- **Testimonial:** none.
- **Best for:** tech-approach (lift stations / collections), exec-summary value-add line.
- **Pursuit fit:** collections, wwtp-om (critical upstream lift station), reuse-dpr, jv-delivery.
- **Blocks / verbatim:** `wiki/technical-approach/swip-aquadna-deragger-technology.md`; `wiki/win-themes/fulton-aquadna-smart-system-optimization.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0047.md` ¶2–¶3; `verbatim/fulton-county-2025/pages/p0039.md` ¶6–¶8.
- **House favorite:** **Conditional** — good for any ragging-prone station; outcome needs a number before it can lead.

### ST-0022 — PWSC Demonstration Plant: MBR snail infestation and the four-measure response

- **Arc:** Persistent Physa snail proliferation during MBR testing at the Pure Water Southern California Demonstration Plant; frequent cleaning managed but did not eliminate it and threatened membrane life → Jacobs and Hazen engaged → ultra-fine influent screening, chlorinated reactor feed, anoxic zone incorporation, and free ammonia membrane soaks now under evaluation to inform full-scale design.
- **THE BEAT:** The four named measures — that list is what makes an abstract "SME support" promise concrete. (Outcome not closed: measures were "under evaluation" in the source; confirm status before restating as proven.)
- **Proof-point claims:** none registered; four mitigation measures; operators Metropolitan and LACSD; partner Hazen — all non-numeric.
- **Testimonial:** none.
- **Best for:** exec-summary sidebar beside a discounted-engineering / SME offer; tech-approach (MBR).
- **Pursuit fit:** reuse-dpr, water-treatment (MBR biofouling).
- **Blocks / verbatim:** `wiki/technical-approach/swip-mbr-fouling-mitigation-case-study.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0104.md` ¶15–¶16.
- **House favorite:** **No** — third-party plant, open-ended outcome; useful only as bench-depth evidence.

### ST-0023 — Tillman AWPF (Replica digital twin): flow balance and membrane sizing solved before construction

- **Arc:** An existing WWTP and a new AWPF competing for the same flows → Replica digital twin optimized the flow balance to maximize capture to the AWPF and modeled hydraulics and controls to size membranes → tool carried forward for troubleshooting, optimization, and operator training after startup.
- **THE BEAT:** "For the Tillman AWPF, Replica optimized the flow balance between the original WWTP and the new AWPF, maximizing the capture of available flows to the AWPF." A named plant where the model changed a design decision.
- **Proof-point claims:** none registered; nothing quantified in the source. (The Fulton block prints "$430,000,000 worth of investment by JC Solutions" for the Replica offer — almost certainly a source typo for $430,000; verify before any reuse.)
- **Testimonial:** none.
- **Best for:** tech-approach (digital tools / process optimization).
- **Pursuit fit:** reuse-dpr, water-treatment, wwtp-om, mbr-membrane.
- **Blocks / verbatim:** `wiki/technical-approach/swip-replica-digital-twin-plant-digital-tools.md`; `wiki/win-themes/fulton-replica-digital-twin-optimization-training.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0046.md` ¶8; `verbatim/fulton-county-2025/pages/p0037.md` ¶7.
- **House favorite:** **No** — credible capability example without a measured outcome.

### ST-0024 — Key West: obsolete UV system replaced with treatment never interrupted

- **Arc:** An obsolete UV disinfection unit at Key West → phased two-channel replacement keeping one channel live, mechanical and electrical upgrades, full reprogramming of lost automation, vendor-coordinated warranty → completed without violations, with "very positive operational results."
- **THE BEAT:** "...phased replacement of two channels — keeping one operational at all times... completed without violations." Maintenance execution as a compliance story.
- **Proof-point claims:** PP-0571 two UV channels replaced in phases, zero violations. Context: PP-0089 10 MGD; PP-0090 37-year relationship (as of Hull proposal).
- **Testimonial:** none.
- **Best for:** tech-approach (asset management / maintenance), staffing (regional maintenance team).
- **Pursuit fit:** wwtp-om, reuse-dpr (disinfection-heavy), water-treatment.
- **Blocks / verbatim:** `wiki/technical-approach/swip-regional-maintenance-team-capability-proof-points.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0078.md` ¶2–¶3.
- **House favorite:** **Conditional** — the best of the four regional-maintenance vignettes; lead with it for disinfection or UV pursuits.

### ST-0025 — North Hudson: failed ATS, temporary power same day, permanent fix planned

- **Arc:** The primary automatic transfer switch at the 18th Street Pump Station fails → Jacobs plans and installs a temporary generator and ATS with site staff to keep the station running → a permanent full ATS replacement follows.
- **THE BEAT:** A pump-station power failure that never became an overflow — the before/after photo page (`141_008A26`) does the talking.
- **Proof-point claims:** none registered for the event itself. Context: PP-0093 30.8 MGD combined; PP-0094 28-year relationship; PP-0532 $36M CSO program managed.
- **Testimonial:** none (the North Hudson Sandy quote is ST-0049).
- **Best for:** tech-approach (emergency response / maintenance), staffing (regional maintenance team), compliance (power resilience).
- **Pursuit fit:** collections (pump stations), wwtp-om, stormwater (pump stations).
- **Blocks / verbatim:** `wiki/technical-approach/swip-regional-maintenance-team-capability-proof-points.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0078.md` ¶4–¶5.
- **House favorite:** **No** — a good vignette for power-resilience worries; too thin to carry a section. ST-0049 is the North Hudson story that carries one.

### ST-0026 — Waterbury WTF: deteriorated instrument panels replaced, before-and-after documented

- **Arc:** Deteriorated instrumentation panels compromising monitoring and control at the Waterbury facility → regional maintenance team removes and replaces them → reliability and integrity of the control system restored, documented in before/after images.
- **THE BEAT:** The photos. Text alone is a maintenance work order; the before/after pair is the proof.
- **Proof-point claims:** none registered.
- **Testimonial:** none (pairs with ST-0005 and TM-0006 if Waterbury is already in the proposal).
- **Best for:** tech-approach (I&C / asset management), staffing (regional maintenance).
- **Pursuit fit:** wwtp-om, collections (SCADA/I&C).
- **Blocks / verbatim:** `wiki/technical-approach/swip-regional-maintenance-team-capability-proof-points.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0078.md` ¶9–¶10.
- **House favorite:** **No** — supporting visual only.

### ST-0027 — Reading the incumbent's data room: from negative chemical values to a 70-component model

- **Arc:** Two years of the incumbent's operating records and two site tours reveal primary clarifier data gaps, negative chemical-usage entries, intermittent 600–900 lb/day wasting with low SVI, and no DO data → Jacobs builds a whole-plant mass-balance model of more than 70 components → the model shows the plant can perform strongly once wasting, DO control, and chemical feed are stabilized, tabulated as four improvement opportunities with expected benefits.
- **THE BEAT:** "Historical chemical consumption records contain numerous negative values..." — a finding the incumbent could not dispute and the client had never been told. (A pursuit-specific diagnostic narrative: the "after" is modeled, not delivered. Its value is as a device, not as past performance.)
- **Proof-point claims:** PP-0285 2024–2025 dataset · PP-0286 two site tours · PP-0287 600–900 lb/day normalized wasting · PP-0288 >70-component whole-plant model. All are the Hull facility's actual conditions — replace with the target's own findings.
- **Testimonial:** none.
- **Best for:** tech-approach, transition.
- **Pursuit fit:** wwtp-om, incumbent-displacement, solids.
- **Blocks / verbatim:** `wiki/technical-approach/phased-baseline-to-optimization-approach.md` — verbatim `verbatim/hull-wwtf-om-2026/pages/p0029.md` ¶2–¶18; `p0030.md` ¶2.
- **House favorite:** **Yes (as a device)** — the strongest technical-credibility passage in the Hull win; rebuild every finding from the new pursuit's data room. Its OCWUT, Fulton and MMSD siblings are ST-0054, ST-0055 and ST-0056.

### ST-0028 — Waterbury: four scrubbers in disrepair to 55% fewer odor complaints

- **Arc:** At contract start the four chemical wet scrubbers serving headworks, solids handling and the incinerator building were in disrepair and the incinerator itself was an odor source → an odor study identified and prioritized nine key sources → a short-term operational control plan cut public complaints by more than 55% between contract years one and two → a $2M capital upgrade (carbon absorber polishing stage, new air piping and dosing pumps) with Walsh Engineers made it permanent.
- **THE BEAT:** "...implemented a short-term operational control plan that reduced public complaints by more than 55% between contract years one and two, and helped develop a $2M capital upgrade." Source identification → short-term stabilization → permanent improvement, each step named — the three-phase pattern the OCWUT and Fulton proposals reuse as their odor method proof.
- **Proof-point claims:** PP-1390 >55% reduction between contract years one and two · PP-0805 / PP-0807 >55% "within the first year" *(conflict — time window)* · PP-1279 >55% "in the first 2 years" *(conflict — time window)* · PP-1294 >55% between Year 1 and Year 2 · PP-1295 $2M odor control upgrade · PP-1280 nine key odor sources identified and prioritized. **The source states the >55% figure with three different time windows; retain whichever wording the cited page uses and never harmonize them.** *(Unregistered: four wet scrubbers in disrepair; Walsh Engineers as design partner; carbon absorber polishing stage.)*
- **Testimonial:** TM-0006 / TM-0059 (Waterbury partnership quote — see the attribution conflict under ST-0005).
- **Best for:** tech-approach (odor — the method proof beside source sampling and dispersion modeling), exec-summary, past-performance, compliance.
- **Pursuit fit:** odor, wwtp-om, solids (incineration), incumbent-displacement (the before-state is the prior operator's), multi-facility.
- **Blocks / verbatim:** `wiki/past-performance/project-waterbury-ct-odor-control-and-results.md`; `wiki/technical-approach/ocwut-wwtf-odor-control-dispersion-modeling-and-equipment-restoration.md` (Exhibit 1-21 framing); `wiki/win-themes/exec-summary-technical-approach-pillars.md` ("55%+" form) — verbatim `verbatim/ocwut-16-26/pages/p0169.md` ¶10; `p0170.md` ¶9; `p0042.md` ¶1; `p0044.md` ¶9; `p0009.md` ¶10.
- **House favorite:** **Yes** — the odor story with a number; it is the analogue every later odor section reached for. Pair with ST-0008 (Southbridge) when the client fears odor fixes mean capital.

### ST-0029 — Waterbury WFP: a 35-year sludge backlog cleared in the first contract quarter

- **Arc:** When Jacobs assumed the water filtration plant contract in 2023, the previous operator had filled both sludge lagoons and all four GeoTubes to capacity → within 90 days Jacobs cleared and graded a 2-acre City parcel, built a new GeoTube laydown area, dredged the lower lagoon, and removed 1,100 dry tons of solids for beneficial reuse at less than half the cost of conventional disposal.
- **THE BEAT:** "...removed 1,100 dry tons of solids for beneficial reuse at less than half the cost of conventional disposal, solving a 35-year problem in the first contract quarter." Inherited deficiency, dated response, countable outcome, cost consequence, and the age of the problem — in one sentence.
- **Proof-point claims:** PP-1392 1,100 dry tons removed within 90 days · PP-1656 water-system contract awarded 2023, previously Veolia. *(Unregistered: 35-year problem; less than half the cost of conventional disposal; 2-acre parcel; both lagoons and four GeoTubes at capacity.)*
- **Testimonial:** TM-0066 — Rob Langenauer, Superintendent of Water, City of Waterbury (permission unknown).
- **Best for:** transition (early wins), past-performance, tech-approach (biosolids / residuals), exec-summary.
- **Pursuit fit:** water-treatment, solids, incumbent-displacement, wwtp-om (as the "inherited deficiencies don't have to define recovery" proof).
- **Blocks / verbatim:** `wiki/past-performance/project-waterbury-ct-odor-control-and-results.md`; `wiki/technical-approach/fulton-successful-experience-transition-asset-community.md` (the "innovative sludge-management project" the Fulton source previewed a year earlier) — verbatim `verbatim/ocwut-16-26/pages/p0170.md` ¶11, ¶15–¶16; `verbatim/fulton-county-2025/pages/p0026.md` ¶13.
- **House favorite:** **Yes** — the best single early-win sentence in the library; travels to any takeover where the incumbent left a backlog.

### ST-0030 — Waterbury collection system: inspections doubled, problem areas down 15%, and a nitrogen credit earned

- **Arc:** A 310-mile collection system with 20 pump stations and no structured CMOM under the previous approach → Jacobs stood up sewer cleaning, CCTV, FOG management and CIPP repairs, integrated 26 City employees into the team, and found an opening in Connecticut's Nitrogen Credit Exchange → monthly inspection rates up 100%, problem areas down nearly 15%, more than 1.5 million linear feet cleaned and inspected, and a $57,151 nitrogen credit earned for the City in 2022.
- **THE BEAT:** "Monthly sewer inspection rates increased 100%; sewer problem areas were reduced by nearly 15%" — then the unexpected revenue line: "in 2022, the WWTP earned a $57,151 nitrogen credit for the City."
- **Proof-point claims:** PP-0032 ~310 miles *(conflict — 320 in Exhibit 3-3)* · PP-0033 20 pump stations. *(Unregistered — harvest before use: +100% monthly inspection rate; ~15% reduction in problem areas; >1.5 million LF cleaned and inspected; $57,151 nitrogen credit (2022); 26 City employees integrated; 32-person on-site team.)*
- **Testimonial:** TM-0006 / TM-0059 (see ST-0005).
- **Best for:** tech-approach (collections / CMOM), past-performance, staffing (workforce integration), compliance.
- **Pursuit fit:** collections, wwtp-om, regulatory-settlement (nutrient trading), incumbent-displacement.
- **Blocks / verbatim:** `wiki/past-performance/project-waterbury-ct-odor-control-and-results.md` — verbatim `verbatim/ocwut-16-26/pages/p0170.md` ¶4, ¶12–¶13.
- **House favorite:** **Conditional** — the numbers are good but none is registered yet; strong for a collections-scored pursuit once harvested.

### ST-0031 — Waterbury, August 27, 2020: a collapsed 15-inch pipe never became a spill

- **Arc:** A sewer backup during a high-rain event, traced to an illicit floor drain → the team partially cleared the blockage, televised the line and found a collapsed 15-inch pipe → a temporary bypass with an outside contractor held service until the rain stopped → two days later 90 feet of pipe were replaced.
- **THE BEAT:** The dates and dimensions: August 27, 2020; a collapsed 15-inch pipe; a bypass for two days; 90 feet replaced. An emergency-response promise proven by a dated event rather than a procedure.
- **Proof-point claims:** PP-0318 August 27, 2020 event · PP-0319 collapsed 15-inch pipe · PP-0320 two-day bypass · PP-0321 90 feet replaced. Context: PP-0273 24-hour emergency line; PP-0277 response within 20 minutes (Hull commitments, pursuit-specific).
- **Testimonial:** none.
- **Best for:** compliance (emergency response), tech-approach (collections), transition.
- **Pursuit fit:** collections, stormwater, wwtp-om (coastal or flood-exposed systems).
- **Blocks / verbatim:** `wiki/compliance-plans/emergency-response-storm-preparedness-coastal-wwtf.md` (Exhibit 5-11) — verbatim `verbatim/hull-wwtf-om-2026/pages/p0041.md` ¶15–¶16.
- **House favorite:** **Conditional** — the only dated collection-system emergency in the set; use it wherever a wet-weather or emergency-response plan needs one proof.

### ST-0032 — Jackson: "only Jacobs was willing to answer our calls" — from crisis interim to a 9-year wastewater award

- **Arc:** The 2022 Jackson water crisis leaves nearly 150,000 residents without reliable safe water; EPA installs an interim third-party manager → Jacobs answers the call in November 2022 with two maintenance specialists and an advisor, mobilizes a 50-plus-person team within days of the interim contract, and runs interim O&M from December 2022 to August 2023 under DOJ direction → sole-source selection for a long-term water contract in fall 2023 → in 2025, on the strength of that record, JXN Water awards a 9-year wastewater contract for three WWTPs and 99 pump stations → City and prior-operator staff transitioned to Jacobs, lift-station functionality rises from about 30% operational to 90% fully operational, and staff satisfaction climbs from 2.8 to 4.3.
- **THE BEAT:** "In the throes of the water crisis, only Jacobs was willing to answer our calls for assistance." Then the operating number: "Lift station functionality improved from ~30% operational at takeover to 90% fully operational." Then the client six months later: "we are seeing a tremendous improvement in all wastewater operations compared with the previous contract operator."
- **Proof-point claims:** PP-1389 65 MGD WWTPs / 99 pump stations · PP-0704 / PP-0796 three WWTPs · PP-0705 99 pump stations *(conflict — PP-0797 says 98)* · PP-0710 / PP-0727 145 MGD combined water and wastewater · PP-0338 / PP-2732 partnership since the 2022 crisis · PP-0636 water takeover year · PP-2733 9-year wastewater contract awarded 2025 *(conflict — TM-0058 says "10-year engagement")* · PP-0340 / PP-1413 staff satisfaction 2.8 → 4.3 · PP-0648 Jackson among the largest recent U.S. utility transitions · PP-0760 among the largest and most complex O&M projects Jacobs supports. *(Unregistered — harvest before use: ~30% → 90% lift stations operational; ~70% of lift stations with one pump and/or no communications at takeover; 50+ person team within days; interim O&M December 2022–August 2023; sole-source selection; Lead and Copper Rule program manager role.)*
- **Testimonial:** TM-0005 — Ted Henifin, Interim Third Party Manager, JXN Water (757.274.7904): "only Jacobs was willing to answer our calls." TM-0058 — Ted Henifin: "They made the transition smooth and painless. Six months into this 10-year engagement we are seeing a tremendous improvement..." TM-0057 — Ted Henifin: "we restored treatment capacity, hired and trained new staff, performed triage on critical assets..." (two `[illegible]` spans — do not fill them). TM-0037 — Tim Durham (Jacobs voice, not a client). All permission unknown.
- **Best for:** past-performance, transition, exec-summary, qualifications, staffing.
- **Pursuit fit:** wwtp-om, water-treatment, collections (pump stations), multi-facility, incumbent-displacement, regulatory-settlement (federal oversight), solids.
- **Blocks / verbatim:** `wiki/past-performance/project-jackson-jxn-water-om.md`; `wiki/past-performance/project-jackson-jxn-water-turnaround-results.md`; `wiki/technical-approach/ocwut-transition-client-testimonials-proven-success.md`; `wiki/management-staffing/wastewater-om-transition-plan-mobilization.md`; `wiki/technical-approach/ocwut-workforce-transition-leadership-and-operational-readiness.md` (satisfaction table); `wiki/win-themes/mmsd-regional-partnership-engaged-partner-jxn-water-jackson.md`; `wiki/compliance-plans/ocwut-staffing-resilience-regional-emergency-support.md` (TM-0057) — verbatim `verbatim/ocwut-16-26/pages/p0167.md` ¶4, ¶6–¶9; `p0168.md` ¶1, ¶4–¶5, ¶9–¶10, ¶13; `p0145.md` ¶11; `p0148.md` ¶4; `p0052.md` ¶26; `verbatim/hull-wwtf-om-2026/pages/p0046.md` ¶17; `p0048.md` ¶6; `verbatim/mmsd-om-2028/pages/p0143.md` ¶11.
- **House favorite:** **Yes** — the most complete turnaround in the library: crisis entry, performance-based re-award, an operating before/after, a workforce number, and the same client witness three times. Reconcile the 9-year/10-year and 99/98 pump-station discrepancies in the spec sheet before use.

### ST-0033 — Jackson: six interns hired, three now full-time, and a scholarship the university matched

- **Arc:** A city whose workforce pipeline collapsed with its water system → Water and Maintenance 101 at Hinds Community College, a free custom college course for entry-level staff, a JXN Water Scholarship Fund covering full tuition for two students, a $25K Jackson State engineering endowment matched by JSU → six local interns hired across operations, maintenance and engineering, three of whom graduated and joined Jacobs full-time — plus SipSafe lead sampling for schools and childcare facilities, outside the contract scope.
- **THE BEAT:** "Hired six local interns across operations, maintenance, and engineering — three interns graduated and joined Jacobs as full-time staff." A conversion count, not a program description — and the university match proves the endowment was real.
- **Proof-point claims:** PP-2735 six interns · PP-2736 three hired full-time · PP-2734 two full-tuition scholarships · PP-2737 $25K JSU endowment · PP-2738 $25K JSU match · PP-2733 9-year contract.
- **Testimonial:** none in this block (TM-0005 / TM-0058 available via ST-0032).
- **Best for:** exec-summary (community / regional partnership), qualifications, staffing (workforce development).
- **Pursuit fit:** wwtp-om, water-treatment, multi-facility; any pursuit scoring community benefit, equity, or local workforce.
- **Blocks / verbatim:** `wiki/win-themes/mmsd-regional-partnership-engaged-partner-jxn-water-jackson.md` — verbatim `verbatim/mmsd-om-2028/pages/p0143.md` ¶11–¶16.
- **House favorite:** **Conditional** — the strongest community-benefit proof in the set because the stakes were highest; drop the takeover framing in a rebid.

### ST-0034 — Vancouver: unseating a 37-year incumbent, 90% of the transition in 90 days, then Utility of the Future

- **Arc:** In January 2016 Jacobs replaced Veolia after 37 years at two activated-sludge plants (28.26 and 16.1 MGD), an industrial lagoon and eight lift stations → a locally anchored management trio, interviews and offers to existing staff, a joint milestone schedule executed transparently → 90% of transition activities done in 90 days, all startup activities in 180 days, a six-month survey showing higher satisfaction than under the prior operator (3.3 → 4.7) → then a $25M multi-year SCADA and PLC modernization with no service interruption, 20 energy projects and $900,000 in utility rebates, zero lost-time incidents since start, NACWA Peak Performance awards every year 2017–2025 including Platinum, more than 20 Ecology Outstanding Performance awards, and WEF "Utility of the Future Today."
- **THE BEAT:** "In 2016, Jacobs replaced a 38-year incumbent operator in one of the most significant Pacific Northwest O&M transitions" → "90% of all transition activities were completed within 90 days, and all start-up activities wrapped within 180 days." Then let the client say it: "Jacobs put together a comprehensive transition plan which made the process very positive, smooth and seamless for not only the City but also the existing staff that became Jacobs employees. There was a high degree of transparency which continues to this day."
- **Proof-point claims:** PP-1655 / PP-0834 37-year incumbent (Veolia), 2016 · **(conflict — `ocwut-16-26/p0171` says 38-year; PP-0837 says "since contract start in 2015" while the same page says January 2016)** · PP-0621 / PP-0832 operated since 2016 · PP-1393 28.26 / 16.1 / 3.2 MGD / eight lift stations *(conflict — 1.7-MGD lagoon in `fulton-county-2025/p0026`)* · PP-0787 / PP-0833 two plants totaling 44 MGD · PP-1394 90% in 90 days, startup in 180 days · PP-0628 / PP-0629 satisfaction 3.3 → 4.7 · PP-1395 / PP-0835 $25M SCADA modernization, zero interruptions *(conflict — $24M in `fulton-county-2025/p0026`)* · PP-1396 / PP-0836 $900,000 utility rebates · PP-0837 zero lost-time incidents · PP-0838 nine-year transparent partnership · PP-1397 additional awards 2020–2024. *(Unregistered: 20 energy projects; NACWA awards 2017–2025 incl. Platinum; >20 Ecology Outstanding Performance awards; WEF Utility of the Future Today; glove recycling program adopted at 50+ sites.)*
- **Testimonial:** TM-0020 / TM-0065 / TM-0069 — Frank Dick, PE, Sewer and Wastewater Engineering Supervisor, City of Vancouver (360.487.7179) — the transition quote in three variants; use the Fulton full version (TM-0065) when the whole testimonial is wanted. TM-0019 / TM-0067 — Frank Dick on integrated engineering-construction-operations delivery. All permission unknown.
- **Best for:** transition, past-performance, exec-summary, qualifications, staffing.
- **Pursuit fit:** wwtp-om, multi-facility, solids (incineration), incumbent-displacement (long-tenured national incumbent), collections (lift stations).
- **Blocks / verbatim:** `wiki/past-performance/project-vancouver-wa-westside-marine-park.md`; `wiki/technical-approach/fulton-successful-experience-transition-asset-community.md`; `wiki/management-staffing/swip-transition-plan-overview-and-track-record.md`; `wiki/technical-approach/fulton-transition-continuity-and-staff-transfer.md` (TM-0069) — verbatim `verbatim/ocwut-16-26/pages/p0171.md` ¶4, ¶6, ¶9; `p0172.md` ¶5–¶10, ¶16; `verbatim/fulton-county-2025/pages/p0026.md` ¶2, ¶5, ¶9; `p0115.md` ¶10; `verbatim/santamonica-swip-om-2025/pages/p0096.md` ¶6–¶7.
- **House favorite:** **Yes** — the full incumbent-displacement arc with a dated schedule, a survey, and annual third-party awards. Fix the 37/38-year, 2015/2016, $24M/$25M and lagoon-capacity conflicts in the spec sheet first.

### ST-0035 — Vancouver incinerator: a $500,000 heat exchanger that deferred an unplanned shutdown

- **Arc:** An aging biosolids incinerator, one of the most odor-sensitive and emissions-regulated processes in wastewater → a $500,000 heat exchanger investment inside the integrated capital program → incinerator life extended, an unplanned shutdown deferred, confined-space entries for maintenance staff reduced, and $275,000–$400,000 in near-term capital avoided — while processing 100% of the biosolids the plant produced through the incinerator year over year.
- **THE BEAT:** "...extended the life of the aging incinerator, deferred an unplanned shutdown, reduced confined-space entry risks for maintenance staff, and avoided an estimated $275,000–$400,000 in near-term capital costs." Four consequences from one investment, one of them a safety consequence.
- **Proof-point claims:** PP-0809 heat exchanger extended incinerator life and deferred an unplanned shutdown · PP-0788 100% of biosolids processed through the incinerator year over year · PP-0795 incinerator O&M program saves the City $1M annually compared to the previous operator (registry-only; confirm the carrying block before use). *(Unregistered: $500,000 investment; $275,000–$400,000 avoided; reduced confined-space entries.)*
- **Testimonial:** none specific (Frank Dick quotes via ST-0034).
- **Best for:** tech-approach (asset management, solids / incineration, odor), past-performance.
- **Pursuit fit:** solids, wwtp-om, odor (incineration emissions), multi-facility.
- **Blocks / verbatim:** `wiki/past-performance/project-vancouver-wa-westside-marine-park.md` — verbatim `verbatim/ocwut-16-26/pages/p0172.md` ¶9 (as carried in `p0171.md` ¶10 context).
- **House favorite:** **Conditional** — strong for any incineration or aging-solids-asset pursuit; the avoided-cost range needs registering.

### ST-0036 — Vancouver polymer: 20% less polymer, $600,000 a year

- **Arc:** Solids dewatering at two plants (44 MGD combined) dosing polymer on habit → Intelligent O&M optimized polymer dosing → polymer use down 20% and $600,000 a year saved; separately the team cut polymer cost 20% by bypassing the Mannich system for emulsion totes.
- **THE BEAT:** "At the City of Vancouver, Washington... Intelligent O&M optimized polymer dosing for solids dewatering, reducing polymer use by 20% and saving $600,000 annually." A named plant, a named chemical, a percentage and a dollar figure.
- **Proof-point claims:** PP-0746 / PP-1531 20% polymer reduction · PP-0747 $600,000/yr · PP-0789 20% reduction in polymer costs by bypassing the Mannich system (a different mechanism — do not conflate with the Intelligent O&M result) · PP-0787 / PP-0833 44 MGD.
- **Testimonial:** none specific.
- **Best for:** tech-approach (chemical optimization, digital tools), exec-summary (innovation table row).
- **Pursuit fit:** wwtp-om, solids, multi-facility; any pursuit scoring energy-chemical efficiency.
- **Blocks / verbatim:** `wiki/win-themes/intelligent-om-chemical-energy-savings.md`; `wiki/win-themes/exec-summary-innovation-benefit-table.md`; `wiki/past-performance/project-vancouver-wa-westside-marine-park.md` (context) — verbatim `verbatim/ocwut-16-26/pages/p0180.md` ¶5; `p0010.md` ¶11.
- **House favorite:** **Yes** — the largest single chemical-savings figure attributable to a digital tool in the set; keep it attached to Vancouver.

### ST-0037 — Wilmington: 20% less chlorine, $200,000 a year, and "a lot of higher-level engineering support than our previous operator"

- **Arc:** A 168-MGD facility with an energy-recovery plant, CSO system and pump stations, taken over from Veolia → Intelligent O&M predictive dosing cut chlorine use 20%, saving $200,000 a year with perfect compliance; chemical consumption overall down 23% → Jacobs delivers a $134M capital program with an onsite engineering team that puts each project through due diligence, and the Deputy Commissioner says the difference from the previous operator out loud.
- **THE BEAT:** "With Jacobs, we have had a lot of higher-level engineering support than our previous operator which has helped the City." Then the number: "predictive tools reduced chlorine use by 20%, saving the City $200,000 annually while maintaining compliance."
- **Proof-point claims:** PP-0744 / PP-1530 20% chlorine reduction · PP-0745 / PP-1652 $200,000/yr · PP-2404 23% chemical consumption reduction (MMSD wording — a broader scope than the chlorine figure; state each with its own source) · PP-1652 168 MGD / $134M CIP *(conflict — 134 MGD in `ocwut-16-26/p0164` and `p0008`)* · PP-1653 ten-year capital backlog.
- **Testimonial:** TM-0063 — Vince Carroccia, Deputy Commissioner, Department of Public Works, City of Wilmington (permission unknown). TM-0010 — Vincent Carroccia on the Innovation Workshop (ST-0012).
- **Best for:** tech-approach (chemical optimization, capital support), exec-summary, past-performance, qualifications (more-than-an-operator).
- **Pursuit fit:** wwtp-om, multi-facility, collections (CSO), solids (renewable-energy biosolids), incumbent-displacement.
- **Blocks / verbatim:** `wiki/win-themes/intelligent-om-chemical-energy-savings.md`; `wiki/win-themes/exec-summary-innovation-benefit-table.md`; `wiki/technical-approach/fulton-successful-experience-multi-facility-mbr.md` (TM-0063); `wiki/win-themes/mmsd-exec-summary-wet-weather-and-optimization-savings.md` (23%) — verbatim `verbatim/ocwut-16-26/pages/p0180.md` ¶5; `p0010.md` ¶11; `verbatim/fulton-county-2025/pages/p0025.md` ¶3; `verbatim/mmsd-om-2028/pages/p0010.md` ¶5.
- **House favorite:** **Yes** — quantified chemical outcome plus the rare client quote that names the previous operator unfavorably. Resolve the 134/168 MGD conflict before the capacity appears.

### ST-0038 — Wilmington: operators' suggestion cuts a capital schedule 40% and its cost 20%

- **Arc:** A four-phase secondary treatment upgrade planned to start with blower replacement → operators argued diffusers first so the blowers could deliver, then at 90% design proposed working two aeration basins at a time instead of one → process engineers verified compliance could be held at max-month flows, a temporary polymer feed was set up as contingency → construction schedule cut 40% and cost cut 20%.
- **THE BEAT:** "Our operators' suggestion reduced the construction schedule by 40% and reduced costs by 20%." The whole "operator input changes capital outcomes" argument in one sentence, with the contingency plan showing the risk was managed rather than ignored.
- **Proof-point claims:** PP-2249 40% schedule reduction · PP-2250 20% cost reduction · PP-2247 four-phase project · PP-2248 two basins at a time · PP-2246 $91M aeration upgrade (the MMSD comparison anchor — pursuit-specific, replace).
- **Testimonial:** none (TM-0063 from ST-0037 is the natural pairing).
- **Best for:** tech-approach (CIP integration / MOPO / capital planning), exec-summary callout, qualifications.
- **Pursuit fit:** wwtp-om, multi-facility; any pursuit with an aeration or secondary upgrade in the CIP.
- **Blocks / verbatim:** `wiki/technical-approach/mmsd-wilmington-capital-upgrade-om-informed-savings.md` — verbatim `verbatim/mmsd-om-2028/pages/p0101.md` ¶14–¶15. Graphic `326_007CAM_3`.
- **House favorite:** **Yes** — compact, two hard percentages, a named contingency; confirm both figures with the Wilmington team, then use it as a callout beside any capital-support narrative.

### ST-0039 — Wilmington: a transition from Veolia executed through the COVID-19 outbreak without interruption

- **Arc:** A large-plant handover from the previous operator lands in the middle of the COVID-19 outbreak → a transition team of HR, operational and technical professionals; constant owner communication; a safe, private, remote onboarding process for employees; a technical team holding operations → operations continued without interruption and the Deputy Commissioner looks forward "to a continued partnership for many years to come."
- **THE BEAT:** "Despite the many challenges presented by the COVID-19 outbreak, Jacobs implemented a smooth and successful transition from our previous operator... a safe, private, and remote process for employees onboarding to Jacobs." The mechanics of what happens to the client's employees, in the client's words.
- **Proof-point claims:** PP-0621 / PP-0622 Wilmington and Vancouver cited as comparable Veolia transitions · PP-2525 four 2025 transitions from Veolia in which "an overwhelming number of staff" chose to join Jacobs (aggregate). *(Unregistered: COVID-era timing.)*
- **Testimonial:** TM-0021 / TM-0062 — Vincent R. Carroccia, Deputy Commissioner, Department of Public Works, City of Wilmington, DE (302.576.3081; permission unknown).
- **Best for:** transition, staffing, exec-summary.
- **Pursuit fit:** wwtp-om, multi-facility, incumbent-displacement (especially where the evaluator's fear is employee handling).
- **Blocks / verbatim:** `wiki/management-staffing/swip-transition-plan-overview-and-track-record.md`; `wiki/technical-approach/ocwut-transition-client-testimonials-proven-success.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0096.md` ¶6, ¶8; `verbatim/ocwut-16-26/pages/p0150.md` ¶3–¶4.
- **House favorite:** **Yes** — of the three transition testimonials the OCWUT block carries, this is the one that answers "what actually happens to my employees."

### ST-0040 — West Basin after the takeover: more than 40% hypochlorite savings, 15–40% less chemical

- **Arc:** The incumbent's "set it and forget it" dosing at the largest reuse facility in North America → after Jacobs assumed operations, predictive dosing built on the plant's own historical best practice → more than 40% sodium hypochlorite savings (against a 20–30% norm across 5- to 340-MGD plants), 15–40% reduction in chemical consumption overall, operator acceptance of push recommendations above 80% — and the Assistant General Manager says the chemical tools "really made a difference in their selection."
- **THE BEAT:** "After Jacobs assumed operations from another provider, we achieved more than 40% in savings—demonstrating the value of shifting away from the 'set it and forget it' approach." The savings exist because the incumbent left them there — the sharpest displacement-plus-optimization proof in the library.
- **Proof-point claims:** PP-2188 >40% chemical (hypochlorite) savings after takeover · PP-2403 15–40% chemical consumption reduction · PP-2402 20–30% savings at Wilmington and West Basin (aggregate) · PP-2187 typical 20–30% range · PP-2186 5 to 340+ MGD track record · PP-2191 >80% operator acceptance · PP-2405 largest reuse facility in North America. **Scope note:** ">40%" is the hypochlorite use case; "15–40%" is chemical consumption overall — cite each with its own source and never blend them.
- **Testimonial:** *(Not in inventory)* Eric Owens, Assistant General Manager, West Basin Municipal Water District (`mmsd-om-2028/p0068 ¶11`) — harvest into `testimonials/inventory.md` before use; the quote contains a "$25M/year" contract value that should stay inside the quote. TM-0004 / TM-0061 (Susanna Li) and TM-0017 (Gloria Gray) via ST-0013.
- **Best for:** tech-approach (chemical optimization), exec-summary, past-performance.
- **Pursuit fit:** reuse-dpr, water-treatment, wwtp-om, incumbent-displacement (the proof that a takeover unlocks savings), multi-facility.
- **Blocks / verbatim:** `wiki/technical-approach/mmsd-sodium-hypochlorite-disinfection-dosage-optimization.md`; `wiki/win-themes/mmsd-exec-summary-wet-weather-and-optimization-savings.md`; `wiki/technical-approach/mmsd-four-pillars-of-chemical-optimization.md` — verbatim `verbatim/mmsd-om-2028/pages/p0069.md` ¶16; `p0070.md` ¶12; `p0010.md` ¶5; `p0068.md` ¶11.
- **House favorite:** **Yes** — pairs with ST-0013 as the "and then the savings came" second act.

### ST-0041 — Agua Nueva DBO: $77M under budget, eight months early, $2M a year cheaper to run

- **Arc:** Pima County faces an Arizona nitrogen deadline for the Santa Cruz River that design-bid-build cannot meet, inside a $750M Water Campus program → Jacobs takes full DBO responsibility for a 32-MGD facility with five-stage Bardenpho, tertiary filtration and chloramine disinfection, with operators embedded in design → delivered $77M under budget and 8 months ahead of schedule (more than a year before the regulatory deadline), $2M a year lower operating cost, 25 MGD of Class A+ reclaimed water, North America's first ammonia-control step-feed aeration strategy, an odor system that removes virtually all odors without chemicals and no odor-related regulatory action since opening in 2013, about 80% of County staff joining the project, ADEQ inspections drawing only explanatory remarks, 3+ years without a recordable incident, and a Palantir Intelligent O&M platform cutting energy costs 20% plant-wide.
- **THE BEAT:** "Their DB best practices achieved all project objectives – under budget and ahead of schedule." — Jackson Jenkins, Director. Then the numbers: "$77M under budget; 8 months ahead of schedule" and "$2M reduction in annual operating costs."
- **Proof-point claims:** PP-1399 $77M under budget / 8 months ahead · PP-1400 20% plant-wide energy cost reduction · PP-1398 / PP-0359 / PP-0097 32 MGD / 25 MGD Class A+ · PP-1246 ~$300,000/yr from demand-responsive aeration control "at a comparable facility in Pima County" (OCWUT energy block — treat as the same facility, but the 20% and $300K framings come from different pages; cite each to its page). *(Unregistered — harvest before use: $2M annual opex reduction; $750M program; 80% of County personnel joined; no odor-related regulatory actions since 2013; zero recordables 3+ years / Target Zero Gold 2017; 2018 AZ Water Plant of the Year; 2018 NACWA Gold Peak Performance; 2014 AAEES Grand Prize; LEED Silver; North America's first ammonia control strategy.)*
- **Testimonial:** TM-0060 — Jackson Jenkins, Director of Pima Regional Wastewater Reclamation Department (permission unknown). Reference contact on the page: Jeff Prevatt, Deputy Director, 520.724.6060.
- **Best for:** past-performance, qualifications (DBO / integrated delivery), tech-approach (CIP integration, odor, energy, transition), exec-summary.
- **Pursuit fit:** wwtp-om, reuse-dpr, multi-facility, odor, regulatory-settlement (regulator-imposed deadline), solids; any DBO or capital-heavy pursuit.
- **Blocks / verbatim:** `wiki/past-performance/project-agua-nueva-dbo-pima-county-az.md`; `wiki/technical-approach/energy-optimization-proven-results-comparable-facilities.md` — verbatim `verbatim/ocwut-16-26/pages/p0173.md` ¶6, ¶10–¶16; `p0174.md` ¶1–¶14; `p0054.md` ¶10.
- **House favorite:** **Yes** — the hardest capital-delivery numbers in the library and a director-level quote; label it a DBO reference, not a pure O&M takeover.

### ST-0042 — San Marcos: ferric down 65%, 174,000 kWh a year, polymer down 40%, hauling down 50% — no capital required

- **Arc:** A 9-MGD plant discharging to one of Texas's most ecologically sensitive rivers, with rising chemical cost and biosolids hauling prices → enhanced biological phosphorus removal and process-control changes, operational-only electricity changes, restructured dewatering, lubrication-analysis predictive maintenance → ferric chloride use down 65%, electricity down more than 174,000 kWh a year ($22,000), polymer down 40%, hauling cost down about 50%, 323 million gallons of reclaimed water reused a year, $10M+ of capital support since 2017, and 20 years of compliance on a sensitive permit with 17 named awards.
- **THE BEAT:** "...our team reduced ferric chloride use by 65%. We also cut electricity consumption by more than 174,000 kWh annually through operational changes alone, with no capital investment required." Four chemical-and-energy percentages on one plant, each with its mechanism, none of them needing a capital project.
- **Proof-point claims:** PP-1402 65% ferric reduction · PP-1403 174,000 kWh/yr · PP-1404 323 million gallons/yr reclaimed · PP-1401 / PP-0099 / PP-0896 / PP-0961 9 MGD / 5.4 MGD avg / 18 MGD peak · PP-0096 relationship since October 2005 · PP-1405 award years and named personnel. *(Unregistered — harvest before use: $22,000/yr electricity savings; 40% polymer reduction; ~50% hauling-cost reduction; $10M+ capital support since 2017; three biotrickling filters; intern-to-project-manager progression.)*
- **Testimonial:** none on the page (reference contact Paul Kite, Assistant Director, 512.393.8003).
- **Best for:** tech-approach (chemical and energy optimization, biosolids, odor — biological scrubbers), past-performance, exec-summary.
- **Pursuit fit:** wwtp-om, reuse-dpr, solids, odor, regulatory-settlement (sensitive receiving water); any pursuit scoring energy-chemical efficiency.
- **Blocks / verbatim:** `wiki/past-performance/project-san-marcos-tx.md` — verbatim `verbatim/ocwut-16-26/pages/p0175.md` ¶4–¶9; `p0176.md` ¶1–¶9, ¶27.
- **House favorite:** **Yes** — the best "optimization without capital" number stack in the library; register the unregistered figures before it leads a section.

### ST-0043 — San Marcos: 70% of interns hired, a 900-million-gallon reuse pilot, and an intern who became the project manager

- **Arc:** A 19-year partnership used as the community-partnership proof rather than a service claim → a non-traditional O&M internship with Texas State University's Water Resources and Geology Departments; financial and in-kind support for a potable-reuse pilot deployed onsite; staff in the Great Texas River Cleanup → 70% of interns hired as full-time employees, more than 900 million gallons of reclaimed water produced by the pilot, 700 volunteers at the cleanup — and one intern recruited from a local university progressed into the project manager role.
- **THE BEAT:** "...hired 70% of interns as full-time employees." The conversion rate that makes any internship offer credible — and the OCWUT page's closer: "an intern recruited from a local university progressed into the project manager role."
- **Proof-point claims:** PP-2739 19 years · PP-2740 70% of interns hired · PP-2741 >900M gallons reclaimed by the pilot · PP-2742 700 volunteers. *(Unregistered: intern-to-PM progression; Friend of the River Award 2021.)*
- **Testimonial:** none.
- **Best for:** exec-summary (regional partnership), qualifications, staffing (workforce development), past-performance.
- **Pursuit fit:** wwtp-om, reuse-dpr; any pursuit scoring community engagement, university partnership or local workforce.
- **Blocks / verbatim:** `wiki/win-themes/mmsd-regional-partnership-engaged-partner-san-marcos.md`; `wiki/past-performance/project-san-marcos-tx.md` — verbatim `verbatim/mmsd-om-2028/pages/p0143.md` ¶20–¶24; `verbatim/ocwut-16-26/pages/p0176.md` ¶2.
- **House favorite:** **Conditional** — pick it when the pursuit client has its own pilot or research program; otherwise ST-0033 (Jackson) carries more weight.

### ST-0044 — Bixby: a brand-new SBR started up mid-construction, an under-design discovered, a holding-pond odor problem retired

- **Arc:** A 10-year contract for a 2.8-MGD SBR beginning before final acceptance, with no maintenance history, baselines or schedules → construction inspection, then startup with telemetry on seven lift stations, then full O&M with seven staff; a centrifuge down for over a week, pump damage from aging lift stations, utility power surges, a bar screen reprogrammed → CMMS loaded from field-verified as-builts rather than design drawings; when post-commissioning showed the plant under-designed for actual loading, One Jacobs resources developed alternative compliance strategies with the City → chronic odor and capacity problems at the old north transfer station holding pond resolved, a FOG program limiting odor at the source, and telemetry across all 18 lift stations.
- **THE BEAT:** "Taking over a brand-new facility midconstruction meant there were no historical maintenance records, equipment baselines, or schedules to rely on. We built the maintenance program from the ground up." Then the candor: "When post-commissioning operations revealed that the facility was under-designed for actual loading conditions, we mobilized our broader technical resources... to develop alternative compliance strategies with the City."
- **Proof-point claims:** PP-1388 2.8 MGD / 5.0 MGD ultimate / 18 lift stations · PP-0775 currently operates Bixby's WRF and 18 lift stations · PP-0857 pump stations (Exhibit 3-5) · PP-1003 contract operations coverage. *(Unregistered: 10-year contract from June 2021; ~28,609 residents; three contract phases; seven FTE; centrifuge outage >1 week; holding-pond odor resolved — qualitative.)*
- **Testimonial:** none (reference contact Dylan Warner, Public Works Director, 918.366.4430).
- **Best for:** transition (startup / operating during construction), past-performance, tech-approach (CMMS from as-builts, odor at the source).
- **Pursuit fit:** wwtp-om, collections (lift-station telemetry), odor, regulatory-settlement (in-state ODEQ proof); any pursuit taking over a plant still under construction.
- **Blocks / verbatim:** `wiki/past-performance/project-bixby-wrf-lift-stations-om.md`; `wiki/past-performance/project-bixby-wrf-lift-stations-results-and-partnership.md` — verbatim `verbatim/ocwut-16-26/pages/p0165.md` ¶4–¶11; `p0166.md` ¶1–¶13.
- **House favorite:** **Conditional** — decisive when the target is commissioning a new plant or wants an in-state Oklahoma reference; the outcomes are qualitative otherwise.

### ST-0045 — Spokane County DBO: seven months early, 50 ppb phosphorus, and the County's largest public works project

- **Arc:** Phosphorus depleting oxygen in the Spokane River and Lake Spokane; the County plans its own facility from 1999 → Jacobs selected in 2008 to design, build and operate an 8.5-MGD (expandable to 24) MBR with chemically enhanced primary treatment, cogeneration and LEED Silver buildings → started up about seven months ahead of schedule, discharging December 1, 2011; effluent held at 50 ppb phosphorus and 0.25 mg/L ammonia — some of the most stringent limits in the nation — through capital construction; leanly staffed with regional backfill; national DBIA awards in 2014 and 2016; the Maintenance AI Assistant first deployed here; and the Utilities Director calling it "the largest public works project ever completed by the County."
- **THE BEAT:** "Jacobs started up the facility approximately seven months ahead of schedule." Then the client: "This was the first Design-Build-Operate project for Spokane County, and the largest public works project ever completed by the County, and we are very satisfied with the results."
- **Proof-point claims:** PP-1889 ~7 months ahead; NPDES permit November 30, 2011; discharge December 1, 2011 · PP-1886 / PP-1888 8.5 MGD → 24 MGD; 50 ppb P; 0.25 mg/L NH3 · PP-1887 20-acre site; 2008 selection; 1999 planning start. *(Unregistered: DBIA 2014 national award and 2016 first place; 2023 WEF Burke Safety Award; cogeneration; LEED Silver; first deployment of the Maintenance AI Assistant.)*
- **Testimonial:** TM-0031 — Bruce Rawls, PE, Spokane County Utilities Director (permission unknown). Reference contact: Ben Brattebo, Water Programs Manager, 509.477.7521.
- **Best for:** past-performance, qualifications (DBO), compliance (stringent nutrient limits), tech-approach (MBR, digital tools).
- **Pursuit fit:** wwtp-om, mbr-membrane, reuse-dpr (Class A), solids (cogeneration), regulatory-settlement (nutrient-driven); DBO pursuits.
- **Blocks / verbatim:** `wiki/past-performance/fulton-spokane-county-dbo-overview.md`; `wiki/past-performance/fulton-spokane-county-dbo-performance.md`; `wiki/win-themes/fulton-maintenance-ai-assistant-palantir.md` — verbatim `verbatim/fulton-county-2025/pages/p0176.md` ¶2–¶14; `p0177.md` ¶2–¶14; `p0035.md` ¶4.
- **House favorite:** **Conditional** — the best nutrient-limit compliance reference; lead with it wherever a stringent phosphorus or ammonia limit is the client's fear.

### ST-0046 — Carol Stream: 36 energy projects in five years at a 3-MGD plant

- **Arc:** A small Illinois plant with an ordinary energy bill → 36 energy-efficiency projects over five years → electricity costs down $52,000 a year, $33,000 in utility incentives earned, and 466 metric tons of CO2-equivalent avoided.
- **THE BEAT:** "36 energy efficiency projects over 5 years reduced electricity costs by $52,000 annually and earned $33,000 in utility incentives." The small-plant, sustained-program proof that pairs with a large-plant aeration result (ST-0041).
- **Proof-point claims:** PP-1248 36 projects over 5 years · PP-1249 $52,000/yr · PP-1250 $33,000 incentives · PP-1251 466 t CO2e · PP-1247 3 MGD · PP-0091 / PP-0092 Carol Stream capacity and relationship since 9/1/1997.
- **Testimonial:** none.
- **Best for:** tech-approach (energy management), exec-summary (small-plant analogue).
- **Pursuit fit:** wwtp-om (small plants especially), collections; any pursuit scoring sustainability or energy.
- **Blocks / verbatim:** `wiki/technical-approach/energy-optimization-proven-results-comparable-facilities.md` — verbatim `verbatim/ocwut-16-26/pages/p0054.md` ¶11.
- **House favorite:** **Conditional** — use as the small-plant half of a two-proof-point energy paragraph.

### ST-0047 — Traverse City: a $1.6 million grant Jacobs wrote for the City, now building rooftop solar

- **Arc:** A city wanting energy resilience without a capital line → in 2022 Jacobs prepared a Michigan Public Service Commission grant application on the City's behalf → over $1.6 million awarded in 2023 for rooftop solar and battery storage producing 10% of the plant's annual energy, now under construction.
- **THE BEAT:** "The City was awarded over $1.6 million in 2023 to construct rooftop solar and a battery energy storage system, producing 10% of annual energy usage." A grant-funding promise with a dollar result attached.
- **Proof-point claims:** PP-1884 >$1.6M awarded 2023; 10% of annual energy.
- **Testimonial:** TM-0009 / TM-0064 (Richard Lewis, via ST-0007).
- **Best for:** tech-approach (grant and funding support, energy), exec-summary, past-performance.
- **Pursuit fit:** wwtp-om, mbr-membrane; any pursuit where grant/loan support is offered.
- **Blocks / verbatim:** `wiki/past-performance/fulton-traverse-city-dbo-accomplishments.md` — verbatim `verbatim/fulton-county-2025/pages/p0175.md` ¶3.
- **House favorite:** **Conditional** — the only grant-secured outcome on an O&M contract in the set (ST-0057 covers biosolids capital grants); pair it with the grant-support methodology block.

### ST-0048 — Transitioned staff are happier after Jacobs: five before/after survey pairs

- **Arc:** The evaluator's — and the incumbent workforce's — fear that a new operator means worse conditions → post-transition employee-satisfaction surveys at five takeovers → Pembroke Pines, FL 3.4 → 4.6; Vancouver, WA 3.3 → 4.7; Ontario, OR 2.7 → 4.5; West Basin, CA 3.6 → 4.1; Jackson, MS 2.8 → 4.3 — backed by a 90% job-offer conversion rate for qualified employees across more than a dozen transitions in three years.
- **THE BEAT:** "Staff members that have joined our firm after a transition are uniformly more satisfied with their work environment at Jacobs" — and then the five pairs. Numbers over transitions, not adjectives; the table (Exhibit 5-14 in OCWUT) does the work.
- **Proof-point claims:** PP-1650 3.4→4.6 / 3.3→4.7 / 2.7→4.5 (Fulton) · PP-0626 / PP-0627 Pembroke Pines · PP-0628 / PP-0629 Vancouver · PP-0630 / PP-0631 Ontario · PP-0339 / PP-1412 West Basin 3.6→4.1 · PP-0340 / PP-1413 Jackson 2.8→4.3 · PP-0623 / PP-1772 90% conversion rate · PP-0624 / PP-1771 over a dozen projects in three years · PP-1774 40+ years of transition experience, 10,000+ employees welcomed · PP-2525 four 2025 Veolia transitions with "an overwhelming number of staff" joining. Context: PP-0100 Pembroke Pines since 5/26/2015; PP-0822 Ontario since 2014.
- **Testimonial:** none required — TM-0020/0065/0069 (Frank Dick, Vancouver) and TM-0004 (Susanna Li, West Basin) corroborate two of the five.
- **Best for:** transition, staffing, exec-summary (one line), cover-letter (one clause).
- **Pursuit fit:** incumbent-displacement above all; wwtp-om, water-treatment, reuse-dpr, multi-facility.
- **Blocks / verbatim:** `wiki/technical-approach/fulton-workforce-satisfaction-and-industry-recognition.md`; `wiki/technical-approach/ocwut-workforce-transition-leadership-and-operational-readiness.md` (Exhibit 5-14); `wiki/management-staffing/wastewater-om-transition-plan-mobilization.md`; `wiki/management-staffing/swip-staff-retention-and-six-step-transition-process.md` (90% conversion); `wiki/technical-approach/fulton-transition-continuity-and-staff-transfer.md` (90% conversion, JV wording) — verbatim `verbatim/fulton-county-2025/pages/p0023.md` ¶5–¶6; `p0116.md` ¶6; `verbatim/ocwut-16-26/pages/p0148.md` ¶4; `verbatim/hull-wwtf-om-2026/pages/p0048.md` ¶6; `verbatim/santamonica-swip-om-2025/pages/p0097.md` ¶2.
- **House favorite:** **Yes** — the incumbent-workforce reassurance device; every displacement proposal since Santa Monica has used some version of it. Survey scales and dates are not stated in any source — confirm with HR before external use.

### ST-0049 — North Hudson after Superstorm Sandy: an expert team in 24 hours, primary treatment back in 48

- **Arc:** Storm surge floods the Hoboken plant of a 22-year client → the Authority's engineer calls Jacobs first; a team arrives within 24 hours → the plant pumped out, some 24 pumps removed, rebuilt and replaced, temporary electrical controls built → primary treatment restored 48 hours later and full secondary treatment within five days of the failure.
- **THE BEAT:** "...you were the first person that I reached out to for help... Our main Sewage Treatment Plant in Hoboken was pumped out, some 24 pumps were removed, rebuilt and replaced and temporary electrical control systems constructed to enable primary treatment 48 hours later with full secondary treatment restored within 5 days of the system failure. It was teamwork at its best." The client narrates the whole timeline himself.
- **Proof-point claims:** PP-1755 team in 24 hours; 24 pumps rebuilt; primary in 48 hours; secondary in 5 days; 22-year partnership · PP-2669 / PP-2670 partnership length and response time · PP-0093 / PP-0094 North Hudson combined capacity and 28-year relationship (Hull as-of).
- **Testimonial:** TM-0068 — Fredric J. Pocci, PE, North Hudson Sewerage Authority Engineer (permission unknown).
- **Best for:** compliance (emergency response / disaster recovery), qualifications (regional bench), exec-summary.
- **Pursuit fit:** wwtp-om, collections, stormwater, coastal or flood-exposed systems; any pursuit scoring resilience.
- **Blocks / verbatim:** `wiki/compliance-plans/fulton-emergency-response-regional-disaster-support.md` — verbatim `verbatim/fulton-county-2025/pages/p0099.md` ¶9–¶10.
- **House favorite:** **Yes** — the best disaster-response proof in the library, entirely in a client's voice with a checkable timeline.

### ST-0050 — Oakland County: a temporary ferric dosing system installed in two weeks to stop collection-system complaints

- **Arc:** Sulfide-driven odor complaints in a Detroit-area collection system during a critical operating period → local Jacobs staff recommended and deployed a temporary ferric chloride dosing system → installed in two weeks, complaints mitigated — offered as proof that WATS-predicted risk is answered with deployed equipment, not memos.
- **THE BEAT:** "Temporary Ferric Chloride Odor Control System for Oakland County Michigan was installed in 2 weeks to mitigate collection system complaints." The response time is the story.
- **Proof-point claims:** PP-2571 installed in 2 weeks · PP-2570 10-year Aalborg University WATS collaboration · PP-1276 SCORe program participation.
- **Testimonial:** none.
- **Best for:** tech-approach (collection-system odor, WATS), compliance (rapid response).
- **Pursuit fit:** collections, odor, wwtp-om, multi-facility.
- **Blocks / verbatim:** `wiki/technical-approach/mmsd-wats-model-systemwide-sulfide-and-corrosion-prediction.md` (preferred); `wiki/technical-approach/mmsd-wats-collection-system-sulfide-model-predictive-odor-management.md` (fallback twin, same passage) — verbatim `verbatim/mmsd-om-2028/pages/p0073.md` ¶5–¶7.
- **House favorite:** **No** — a good caption beside the WATS model; too thin to carry more.

### ST-0051 — Thames Tideway (Jacobs capital program, UK): social value with a price tag on every line

- **Arc:** The UK's largest water infrastructure program wants a skills-and-employment legacy → Jacobs designs the apprenticeship scheme, incentivized contractor schemes, and an education program → 1,000 previously unemployed people employed ($4.17M predicted social value), 150+ apprentices ($542K), 25% local employment ($2M), 37 people with convictions employed ($2M), 80,000 young people reached through STEM ($6.95M) — and the client CTO calls Jacobs' contribution "exemplary."
- **THE BEAT:** "Employed 1,000 previously unemployed people, with a predicted additional value to society of $4.17M by the end of the project." Every community commitment monetized — say the method (Simetrica-Jacobs) so the evaluator sees it was calculated, not asserted.
- **Proof-point claims:** PP-2748 / PP-2749 1,000 people / $4.17M · PP-2750 / PP-2751 / PP-2752 150+ apprentices, 1-in-50 target, $542K · PP-2753 / PP-2754 25% local, $2M · PP-2755 / PP-2756 37 people with convictions, $2M · PP-2757 / PP-2758 80,000 young people, $6.95M.
- **Testimonial:** *(Not in inventory)* Roger Bailey, Tideway Chief Technical Officer (`mmsd-om-2028/p0144 ¶26`) — harvest before use.
- **Best for:** exec-summary (regional partnership / social value), qualifications.
- **Pursuit fit:** any pursuit scoring community benefit or equity — but it is a UK capital program, not a US O&M contract; say so plainly.
- **Blocks / verbatim:** `wiki/win-themes/mmsd-regional-partnership-engaged-partner-thames-tideway.md` — verbatim `verbatim/mmsd-om-2028/pages/p0144.md` ¶13–¶26.
- **House favorite:** **Conditional** — the only monetized social-value example in the set; label it as evidence of method, never of comparable scope.

### ST-0052 — The Villages: 250 residents through the plants, four operators licensed from within in a year

- **Arc:** A 55-plus-community portfolio (13 water systems, four WWTFs, collection, distribution, meter reading, solid waste) whose ratepayers want to know what their fees buy → a Resident Academy of briefings, classes and tours; a Wastewater Operator Development Program; a college-level operations course with Lake-Sumter College → about 250 residents toured public works and treatment facilities, and four newly licensed operators were produced in one year by promoting from within.
- **THE BEAT:** "Created a Wastewater Operator Development Program that produced four newly licensed operators in one year, promoted from within the local workforce." Internal promotion is the sentence an incumbent workforce wants to read.
- **Proof-point claims:** PP-2746 ~250 residents · PP-2747 four licensed operators in one year · PP-2743 / PP-2744 / PP-2745 13 water systems / four WWTFs / 55+ communities.
- **Testimonial:** none.
- **Best for:** exec-summary (community), staffing (workforce development), qualifications (multi-system portfolio).
- **Pursuit fit:** multi-facility, water-treatment, wwtp-om, collections; any pursuit where the ratepayer base or the incumbent workforce is the audience.
- **Blocks / verbatim:** `wiki/win-themes/mmsd-regional-partnership-engaged-partner-the-villages.md` — verbatim `verbatim/mmsd-om-2028/pages/p0144.md` ¶12–¶15.
- **House favorite:** **Conditional** — the resident academy is the transferable idea.

### ST-0053 — Back River, Baltimore: a biosolids backlog cleared under an active consent decree

- **Arc:** One of the country's largest outsourced wastewater programs (180 MGD) with a massive biosolids backlog and a consent decree in force → Jacobs stepped in, cleared the backlog, and restored operational performance under the decree.
- **THE BEAT:** "At Baltimore's Back River WWTP (180 MGD)... we stepped in, cleared a massive biosolids backlog, and restored operational performance under an active consent decree." A regulatory-settlement story at the largest scale in the portfolio — told in one sentence, with no number behind the backlog.
- **Proof-point claims:** PP-0648 Baltimore among the largest recent U.S. utility transitions Jacobs led. *(Unregistered: 180 MGD; consent decree; backlog cleared — all from the Section 7 opener.)*
- **Testimonial:** none.
- **Best for:** qualifications (portfolio scale), past-performance (opener), exec-summary (one clause).
- **Pursuit fit:** regulatory-settlement, solids, multi-facility, wwtp-om (large systems).
- **Blocks / verbatim:** `wiki/past-performance/ocwut-om-portfolio-and-oklahoma-track-record.md` — verbatim `verbatim/ocwut-16-26/pages/p0164.md` ¶3.
- **House favorite:** **Conditional** — the sentence is strong; the story needs a project description and a number before it can carry a section. Source one from the Baltimore account team.

### ST-0054 — OCWUT: the case for change built from 200 ppm H2S, 3 of 30 scrubbers, and two failed WET tests

- **Arc:** Multi-day site visits at all five facilities and SME strategy sessions before a page was written → verified findings: headworks inaccessible at H2S readings up to 200 ppm; only 3 of 30 odor scrubbers operational system-wide (30 installed / 3 running at one plant, 7 / 3 at another); both major plants failing WET tests in Q4 2025; a reactive maintenance program with cascading monthly failures → reframed as latent capability: "These aren't design-limited facilities."
- **THE BEAT:** "What we found confirmed the urgency. North Canadian's headworks are inaccessible for routine maintenance due to H2S readings up to 200 ppm. Only 3 of 30 odor scrubbers system-wide are operational." Then the pivot: "Operators are working in conditions that exceed safe exposure thresholds because the systems designed to protect them aren't running." (A pursuit-specific diagnostic device, like ST-0027 — the "after" is proposed, not delivered.)
- **Proof-point claims:** PP-0719 200 ppm H2S · PP-0720 3 of 30 scrubbers · PP-0721 two plants failing WET tests Q4 2025 · PP-1281–PP-1284 30/3 and 7/3 scrubber counts · PP-0718 five facilities visited · PP-0715 ~$200M capital program · PP-0722 300+ prior projects. All are the OCWUT facilities' actual conditions — never carry them to another pursuit.
- **Testimonial:** none.
- **Best for:** exec-summary (opening), tech-approach (odor, maintenance), transition.
- **Pursuit fit:** incumbent-displacement, odor, wwtp-om, multi-facility.
- **Blocks / verbatim:** `wiki/win-themes/exec-summary-site-verified-understanding-and-case-for-change.md`; `wiki/technical-approach/ocwut-wwtf-odor-control-dispersion-modeling-and-equipment-restoration.md` — verbatim `verbatim/ocwut-16-26/pages/p0008.md` ¶2, ¶6–¶7, ¶9, ¶14; `p0042.md` ¶4.
- **House favorite:** **Yes (as a device)** — the strongest incumbent-displacement opening in the library: prove the homework, state the verified failures, reframe them as opportunity. Rebuild every finding from the new pursuit's site visits.

### ST-0055 — Fulton County: the scrubber that wasn't being fed caustic, and $500 a day

- **Arc:** Monthly reports from the incumbent's operation show sodium hydroxide not being used at one plant's chemical scrubbers, so H2S removal is low and the GAC polishing stage is doing the scrubber's job → JC Solutions models the setpoints and projects the correct chemical feed → about $500 a day less in combined chemical and GAC cost, and GAC restored to its intended role as backup.
- **THE BEAT:** "Monthly reports show that sodium hydroxide is not being used at [FACILITY B]. As a result, hydrogen sulfide removal by the scrubbers is low, leaving considerable hydrogen sulfide to be removed by GAC." A finding pulled from the client's own reports — the incumbent could not dispute it. (Device: the saving is projected, not delivered.)
- **Proof-point claims:** PP-1647 / PP-1728 ~$500/day.
- **Testimonial:** none.
- **Best for:** tech-approach (odor, chemical optimization), exec-summary (site-verified understanding).
- **Pursuit fit:** odor, incumbent-displacement, mbr-membrane, multi-facility, jv-delivery.
- **Blocks / verbatim:** `wiki/technical-approach/fulton-odor-control-scrubber-optimization.md` (sanitization-loss high — read the page) — verbatim `verbatim/fulton-county-2025/pages/p0067.md` ¶8–¶16; `p0068.md` ¶1.
- **House favorite:** **Yes (as a device)** — the odor-side twin of ST-0027; rebuild from the target's monthly reports.

### ST-0056 — MMSD: two years of the client's lab and SCADA records turned into $1M+ a year of predictive chemical savings

- **Arc:** Two years of laboratory and SCADA Historian records from the incumbent's operation → predictive dosing analysis finds >30% hypochlorite savings at one plant and ~20% at the other ($525K/yr), a second ferric injection point worth 20% ($600K/yr), predictive bisulfite matching ($100K/yr), RAS chlorination timed to filament drivers (~14%, $60K/yr) — conservatively over $1M a year, "almost double... a distinct possibility" — with an installed Phosphax analyzer found idle and operator acceptance above 80% elsewhere.
- **THE BEAT:** "While these savings values may appear unrealistic, these are typical savings for this particular use case." Pre-empting disbelief, then proving it with the 5- to 340-MGD track record and the West Basin >40% result (ST-0040). (Device: modeled on the client's data, not delivered.)
- **Proof-point claims:** PP-2180 $525K/yr hypochlorite · PP-2183 / PP-2184 >30% / ~20% · PP-2182 two-year window · PP-2193 20% / $600K ferric · PP-2181 $100K bisulfite · PP-2190 ~14% / $60K filament control · PP-2194 >$1M/yr conservative total · PP-2189 3–8 notifications/day · PP-2191 >80% acceptance · PP-2192 48-inch lines · PP-2176–PP-2179 four-pillars block ids. All are MMSD-data outputs — never carry the figures to another pursuit.
- **Testimonial:** Eric Owens (West Basin) via ST-0040 *(not in inventory)*.
- **Best for:** tech-approach (chemical optimization), exec-summary (optimization that delivers budget value).
- **Pursuit fit:** wwtp-om, multi-facility, water-treatment, incumbent-displacement.
- **Blocks / verbatim:** `wiki/technical-approach/mmsd-sodium-hypochlorite-disinfection-dosage-optimization.md`; `wiki/technical-approach/mmsd-ferric-chloride-phosphorus-optimization-and-future-use-cases.md`; `wiki/technical-approach/mmsd-dechlorination-and-ras-filament-control-optimization.md`; `wiki/technical-approach/mmsd-four-pillars-of-chemical-optimization.md` — verbatim `verbatim/mmsd-om-2028/pages/p0068.md` ¶7–¶14; `p0069.md` ¶5–¶16; `p0070.md` ¶8–¶12; `p0071.md` ¶7–¶9.
- **House favorite:** **Yes (as a device)** — the most complete data-room-to-savings diagnostic in the library; the structure travels, the numbers do not.

### ST-0057 — Biosolids capital funded by grants: $9.8M for Tulsa, $14.5M for Hendersonville

- **Arc:** Two utilities facing landfill dependence and the capital cost of drying → Jacobs' funding team secures a $9.8 million USDA grant toward Tulsa's $45 million biosolids fertilizer manufacturing center and a $14.5 million Clean Water SRF principal-forgiveness grant that pays the entire cost of Hendersonville's new drying facility.
- **THE BEAT:** "...a $14.5 million principal forgiveness grant... to pay the entire cost of building a new drying facility to eliminate the need for landfilling." A funding promise with two named, dollar-denominated precedents.
- **Proof-point claims:** PP-1528 / PP-1764 $9.8M USDA grant, $45M Tulsa facility · PP-1529 / PP-1765 $14.5M NC CWSRF principal forgiveness, Hendersonville.
- **Testimonial:** none.
- **Best for:** tech-approach (biosolids, grant / funding support), exec-summary (innovation), qualifications.
- **Pursuit fit:** solids, wwtp-om, multi-facility; any pursuit with a biosolids strategy change or thermal drying in view.
- **Blocks / verbatim:** `wiki/win-themes/innovative-financing-for-biosolids-management.md` — verbatim `verbatim/ocwut-16-26/pages/p0179.md` ¶14–¶15.
- **House favorite:** **Conditional** — decisive where biosolids disposal cost is the client's pain; note these are engineering/funding engagements, not O&M outcomes.

### ST-0058 — Coos Bay 2021: the handback the client thanked us for

- **Arc:** An O&M contract ending in Coos Bay, OR in 2021 → a professional transfer to the successor → the City Engineer records that the professionalism and dedication to a successful transfer "was greatly appreciated and acknowledged by the City."
- **THE BEAT:** "The professionalism and dedication to a successful transfer that the Jacobs team displayed in Coos Bay in 2021 was greatly appreciated and acknowledged by the City." The only exit-transition witness in the library — proof that the exit plan is not theoretical.
- **Proof-point claims:** none registered. *(Unregistered: Coos Bay, 2021 handback.)*
- **Testimonial:** TM-0070 — Jennifer Wirsing PE, CFM, City Engineer/Deputy, City of Coos Bay (permission unknown).
- **Best for:** transition (exit transition plan), compliance.
- **Pursuit fit:** any pursuit whose RFP requires an exit or handback plan.
- **Blocks / verbatim:** `wiki/technical-approach/fulton-transition-schedule-and-exit-plan.md` — verbatim `verbatim/fulton-county-2025/pages/p0125.md` ¶22–¶24.
- **House favorite:** **Conditional** — small, but it answers a question no other story does.

### ST-0059 — The transitions-from-Veolia map: fourteen handovers, four in 2025 alone, 100+ FTE

- **Arc:** A challenger bid against a long-tenured national incumbent → a map of prior Jacobs transitions from that same incumbent — Southbridge, Woonsocket, Goderich, Waterbury, Westerly, South Huron Valley, Wilmington, Vancouver, Gresham, Farmington, West Melbourne, Jackson (1 WWTP), and in 2025 West Basin (four reuse plants) and Jackson (three WWTPs) → the Fulton wording: transitions of Veolia-operated sites in MA, MS and CA "this past year" involving over 100 FTEs, led by a transition manager who has worked for both firms.
- **THE BEAT:** The map itself (asset `319_007CAM_3`) and the sentence: "Our recent transitions of Veolia-operated sites this past year in MA, MS, and CA involving over 100 FTEs illustrate our ability to deliver rapid, successful handovers without compromising service quality." Volume is the argument.
- **Proof-point claims:** PP-1848 100+ FTEs in MA, MS, CA · PP-2525 four 2025 transitions from Veolia · PP-0622 Wilmington and Vancouver as comparable Veolia transitions · PP-0648 largest recent transitions (Baton Rouge, Jackson, Baltimore, Waterbury, Lincoln). *(Unregistered: the fourteen-site map list.)*
- **Testimonial:** TM-0004 (Susanna Li) is placed beside the map in the MMSD source.
- **Best for:** transition, exec-summary, cover-letter (one clause).
- **Pursuit fit:** incumbent-displacement (Veolia or any national incumbent); wwtp-om, reuse-dpr, multi-facility.
- **Blocks / verbatim:** `wiki/win-themes/mmsd-exec-summary-seamless-transition-and-workforce-continuity.md`; `wiki/win-themes/exec-summary-comprehensive-jv-solution-benefits.md` — verbatim `verbatim/mmsd-om-2028/pages/p0011.md` ¶3, ¶8–¶9; `verbatim/fulton-county-2025/pages/p0010.md` ¶8.
- **House favorite:** **Conditional** — a device, not a single plant's story; name the incumbent only where the competitive posture warrants it, and verify every site on the map with the account teams.

### ST-0060 — Duncan, OK: thirty years inside the same regulator, and Plant of the Year

- **Arc:** A challenger needing in-state credibility → the City of Duncan's wastewater facility operated continuously since 1995 under ODEQ, its industrial pretreatment program administered by Jacobs for seven significant industrial users → multiple renewals across 30 years and an Oklahoma Water Environment Association Municipal Plant of the Year award.
- **THE BEAT:** "We have operated the City of Duncan's wastewater facilities since 1995... That's 30 years of working within the same state regulatory environment [CLIENT] operates every day." Tenure converted into regulator familiarity — the geography-specific paragraph that made the OCWUT opener land.
- **Proof-point claims:** PP-0770 since 1995 · PP-0771 30 years, multiple renewals · PP-0772 OWEA Municipal Plant of the Year · PP-0773 IPP for seven significant industrial users · PP-0778 44 years serving Oklahoma clients.
- **Testimonial:** none.
- **Best for:** qualifications (regional presence), past-performance (opener), cover-letter.
- **Pursuit fit:** wwtp-om; Oklahoma or ODEQ-regulated pursuits only — rebuild the equivalent in-state paragraph elsewhere.
- **Blocks / verbatim:** `wiki/past-performance/ocwut-om-portfolio-and-oklahoma-track-record.md` — verbatim `verbatim/ocwut-16-26/pages/p0164.md` ¶5.
- **House favorite:** **Conditional** — the template for an in-state tenure paragraph; the story is only as good as the state match.

### ST-0061 — Waterbury 2019: a water-supply emergency answered at no cost

- **Arc:** A water supply emergency in Waterbury in 2019, on a system Jacobs did not yet operate → at the City's request Jacobs staff, including the Regional Director, mobilized and engaged at no cost to troubleshoot supply restrictions and offer solutions → four years later the City awarded Jacobs the water system O&M (ST-0005 / ST-0029).
- **THE BEAT:** "...Jacobs staff (including Regional Director Kevin Dahl) mobilized and engaged with the City at no cost to help troubleshoot water supply restrictions and offer solutions." Showing up before the contract exists — and the 2023 award is the payoff.
- **Proof-point claims:** PP-0545 2019 Waterbury water-supply emergency mobilization at no cost · PP-1656 2023 water-system award.
- **Testimonial:** TM-0066 — Rob Langenauer, Superintendent of Water, City of Waterbury (via ST-0029; permission unknown).
- **Best for:** compliance (emergency response / regional resources), qualifications, exec-summary (one line).
- **Pursuit fit:** water-treatment, wwtp-om, multi-facility; any pursuit scoring regional bench or partnership.
- **Blocks / verbatim:** `wiki/compliance-plans/swip-emergency-response-regional-resources.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0067.md` ¶6.
- **House favorite:** **Conditional** — short, but it links directly to the 2023 water award and makes the "regional resources" claim concrete.

### ST-0062 — Prescott Valley: operators diverted flows so firefighters could fight a multi-alarm blaze

- **Arc:** A multi-alarm fire at an apartment complex under construction in the heart of Prescott Valley, AZ → the Jacobs water and wastewater team manned the stations in the early hours, diverted flows so first responders could attack the fire, and held pressure for residences and businesses → the Town Manager wrote to the project team to recognize "leadership and attention to detail."
- **THE BEAT:** "They diverted flows so first responders could tackle the huge blaze, while also maintaining adequate pressure for residences and businesses." Then the Town Manager's letter: "Your contributions have not gone unnoticed."
- **Proof-point claims:** none registered. *(Unregistered: multi-alarm fire; early-hours response — non-numeric.)*
- **Testimonial:** TM-0018 — Gilbert Davidson, Town Manager, Town of Prescott Valley, AZ (permission unknown).
- **Best for:** compliance (emergency response), exec-summary (community), qualifications.
- **Pursuit fit:** water-treatment, wwtp-om, multi-facility; any pursuit where community service or emergency coordination is scored.
- **Blocks / verbatim:** `wiki/compliance-plans/swip-emergency-response-regional-resources.md` — verbatim `verbatim/santamonica-swip-om-2025/pages/p0067.md` ¶14. Graphics `129_008A26`, `127_008A26`.
- **House favorite:** **No** — a warm vignette with a client letter; supporting texture, not an argument.

---

## Conflicts and flags surfaced in this pass

Resolve each in the pursuit spec sheet before the affected story appears in a draft.

| Item | Sources | Action |
|---|---|---|
| Waterbury partnership quote attributed to two speakers | Mike LeBlanc, Director of Finance (TM-0006, `hull p0076 ¶17`) vs. Mayor Neil O'Leary (TM-0059, `ocwut p0170 ¶1`) — identical words | Confirm the speaker with the Waterbury account team; use one attribution only (ST-0005, ST-0028, ST-0030) |
| Waterbury >55% odor-complaint reduction — three time windows | "between contract years one and two" (PP-1390, PP-1294); "within the first year" (PP-0805, PP-0807); "in the first 2 years" (PP-1279) | Quote the wording of the page cited; never harmonize (ST-0028) |
| Vancouver incumbent tenure | 37-year (`fulton p0026 ¶2`, PP-1655, PP-0834) vs. 38-year (`ocwut p0171 ¶6, ¶9`) | Resolve; also 2015 (PP-0837) vs. January 2016 contract start on the same OCWUT page (ST-0034) |
| Vancouver SCADA program value | $25M (`ocwut p0172`, PP-1395) vs. $24M (`fulton p0026`) | Resolve (ST-0034) |
| Vancouver industrial lagoon | 3.2 MGD (`ocwut p0171`) vs. 1.7 MGD (`fulton p0026`) | Resolve (ST-0034) |
| Wilmington capacity | 134 MGD (`ocwut p0164`, `p0008`) vs. 168 MGD (`fulton p0025`, `ocwut p0180`, PP-1652) | Resolve (ST-0037) |
| Wilmington chemical result | 20% chlorine / $200K (PP-0744/0745/1530/1652) vs. 23% chemical consumption (PP-2404) | Different scopes — cite each to its source (ST-0037) |
| West Basin chemical result | >40% hypochlorite (PP-2188) vs. 15–40% chemical consumption (PP-2403) | Different scopes — cite each to its source (ST-0040) |
| Jackson wastewater contract term | 9-year (`ocwut p0167`, `mmsd p0143 ¶11`, PP-2733) vs. "10-year engagement" inside TM-0058 | Confirm; do not edit the quote (ST-0032) |
| Jackson pump stations | 99 (PP-0705, PP-1389) vs. 98 (PP-0797) | Resolve (ST-0032) |
| Clovis capacity | 2.8 MGD (PP-0381, ops table) vs. 3.1 MGD max-month (PP-1890 reference panel) | State the basis (ST-0016) |
| Fulton Replica investment figure | "$430,000,000 worth of investment" (`fulton p0037`) | Almost certainly $430,000; verify before any reuse (ST-0023) |
| Unregistered testimonials | Eric Owens, AGM, West Basin (`mmsd p0068 ¶11`); Roger Bailey, CTO, Tideway (`mmsd p0144 ¶26`) | Add to `testimonials/inventory.md` before use (ST-0013, ST-0040, ST-0051) |
| Unregistered outcome numbers in OCWUT past-performance blocks | Jackson lift stations ~30% → 90%, 50+ team; Waterbury +100% inspections, ~15% problem areas, 1.5M LF, $57,151 credit, 26 staff; San Marcos $22K, 40% polymer, ~50% hauling, $10M+ capital; Agua Nueva $2M/yr opex, $750M program, 80% staff, awards; Vancouver $500K / $275–400K, 20 projects, NACWA 2017–2025 | Harvest into `proof-points/registry.md` (ST-0029, ST-0030, ST-0032, ST-0034, ST-0035, ST-0041, ST-0042) |

## Not cataloged — checked and excluded

- Value bundles and priced offers: `win-themes/value-added-no-cost-enhancements-framing.md` (carries ST-0020 only for the SmartCover claim), `swip-value-added-offerings-package.md`, `technical-approach/value-added-innovations-menu-om-contracts.md`, `mmsd-exec-summary-above-and-beyond-investments-and-savings.md` ($107M / $21–53M / $160M), `mmsd-value-added-investments-and-future-savings.md`, `mmsd-base-fee-value-added-investments-and-future-savings.md`, both `mmsd-exhibit-value-added-savings-*` tables, `mmsd-exhibit-value-added-innovations-pilots-optimization-table.md`, `mmsd-future-improvements-and-innovations-for-additional-savings.md`, `exec-summary-comprehensive-jv-solution-benefits.md` ($6.7M — patched only for the Veolia-transitions line, ST-0059), `alternative-escalation-index-methodology.md` ($620K), `discounted-engineering-services-offer.md`, `discounted-engineering-savings-example-table.md`, `fulton-energy-management-*` (projected $235–365K/yr), `fulton-additional-digital-tools.md`, `fulton-maintenance-planner-scheduler-palantir.md`, `fulton-value-added-innovation-program.md`, `fulton-workforce-digital-twin-collections-benefits.md`, `exec-summary-innovation-benefit-table.md` (patched only for its two reference-site rows, ST-0036 / ST-0037) — offers and projections, not delivered outcomes.
- Methodology and framing blocks with no delivered outcome: every `cover-letter-*`, `exec-summary-*` (other than those named above), `mmsd-regional-partnership-*` strategy, opening, partnering-plan, leadership, fishing-pier, research-portfolio and client-vision blocks, `mmsd-regional-partnership-local-community-involvement-record.md` (a list of activities plus a mayoral proclamation — texture, not a before/after), `fulton-community-*` and `fulton-school-*` / `fulton-public-information-*` / `fulton-proactive-media-*` blocks, `fulton-process-security-asset-management-benefits.md`, `fulton-regional-training-maintenance-intelligence.md`, `rfp-wayfinding-crosswalk-pattern.md`, `innovation-more-than-an-operator-framing.md`, `replica-hydraulic-model-system-optimization.md`, `nexgen-phase-2-asset-data-support.md`, `odor-study-gap-analysis-and-updated-report.md`, `exhibit-trusted-partnership-relationship-timeline.md`, `swip-*` win-theme blocks listed in the first pass, `differentiator-traditional-vs-enhanced-om-comparison.md`, `community-stewardship-public-engagement-program.md`, `value-proposition-table-approach-impact-value.md`, `leadership-team-and-coordinated-operations-narrative.md`.
- Technical-approach methodology in the title-filter set: `mmsd-aeration-energy-and-process-optimization.md` (opportunity, not result), `mmsd-dewatering-drying-cake-solids-optimization.md` ($350K per 1% cake solids is an estimate), `mmsd-odor-challenge-*`, `mmsd-odor-early-warning-*`, `mmsd-odor-complaint-protocol-*`, `mmsd-odor-continuous-improvement-*`, `mmsd-disciplined-plant-operations-*`, `mmsd-liquid-treatment-*`, `mmsd-settleability-*`, `mmsd-monitoring-control-practices-*`, `mmsd-pm-optimization-*`, `mmsd-level3-pdm-phased-rollout.md`, `mmsd-digital-one-water-*`, `mmsd-energy-optimization-focus-area-*`, `mmsd-chemical-usage-monitoring-and-control.md` (10–30% is a commitment), `fulton-odor-*` (other than the scrubber diagnostic, ST-0055), `fulton-mbr-maintenance-odor-biosolids-innovation.md` (names Wilmington / Pima / PRASA without figures — the figures live in ST-0037 / ST-0041), `fulton-biosolids-transfer-*`, `fulton-process-optimization-*`, `fulton-swing-zones-*`, `fulton-comprehensive-om-approach-and-transition.md`, `fulton-deliverables-commitment-*`, `ocwut-*` odor framework, monitoring, WATS, maintenance-as-driver, fence-line (commitments), `ocwut-oshg-conversion-transition-experience.md`, all `ocwut-transition-*` schedule, checklist, org-chart and work-plan exhibits, `ocwut-exhibit-1-1-*`, `ocwut-risk-based-transition-management.md`, `phased-no-cost-low-cost-energy-optimization-opportunities.md`, `major-pump-station-operations-*`, `site-specific-odor-control-program.md` (hosts ST-0008 only), `sensor-dispersion-model-*`, `wats-collection-system-odor-corrosion-modeling.md`, `swip-process-optimization-digital-modeling.md`.
- Checked 2026-09-13 and excluded (framing or methodology, no delivered before/after): `mmsd-exec-summary-trusted-partner-opening-and-six-core-attributes.md`, `mmsd-exec-summary-comprehensive-om-with-consulting-bench.md`, `mmsd-exec-summary-elevated-operations-technical-bench-and-no-surprises-compliance.md`, `mmsd-exec-summary-programmatic-framework-and-auditable-cost-transparency.md`, `mmsd-exec-summary-iso-55001-asset-management-and-reliability.md`, `mmsd-exec-summary-high-caliber-leadership-and-people-first-culture.md`, `mmsd-exec-summary-biosolids-continuity-and-odor-control.md`, `mmsd-exec-summary-regional-partnership-and-community-benefits.md`, `mmsd-exec-summary-why-jacobs-close.md` (CEO statement TM-0056 is a Jacobs voice, not a client outcome), `fulton-interactive-community-education-and-wellness-partnerships.md` (proposed partnerships, none delivered), `technical-approach/mmsd-odor-control-focus-area-and-program-commitment.md` and `mmsd-odor-complaint-response-protocol-and-odor-technologist-bench.md` (protocol and bench, superseded fallbacks), `technical-approach/phased-process-control-strategy-stabilize-optimize-sustain.md` (a forward roadmap — its OCWUT site findings are ST-0054).
- Past-performance tables and rosters: `similar-facilities-table.md`, `santamonica-swip-advanced-water-treatment-team-experience.md`, `fulton-mbr-experience-highlights-*` (two Exhibit 4-1 tables), `fulton-mbr-design-and-commissioning-portfolio.md`, `fulton-mbr-operations-engineering-and-sme-experience.md`, `fulton-pump-station-operations-experience.md`, `fulton-us-treatment-facilities-portfolio.md` — capability statements and tables, no narrative arc.

## Counts

- Stories cataloged: 62 (ST-0001 through ST-0062); 35 added 2026-09-11 (ST-0028–ST-0062); none added 2026-09-13. House favorite Yes 27 (incl. four "as a device": ST-0027, ST-0054, ST-0055, ST-0056) · Conditional 27 · No 8.
- Blocks scanned (2026-09-13 scope): 34 past-performance, 115 win-themes, 70 technical-approach by title filter, plus 7 management-staffing / compliance-plans blocks carrying a cataloged quote or event — 226 in all; 14 first checked in this pass.
- Blocks patched via `work/fragments/st_patches.json`: 91 (87 with at least one story id; 4 old-schema blocks kept at `story-ids: []` so the sweep is recorded). Applied and verified 2026-09-13 — every path in the map now carries its ids. Patch is written with `set`, so re-running is idempotent.
- Registry ids cited: 320 distinct PP ids; conflicts flagged inline and in the table above.
- Testimonial ids cited: 30 (TM-0002–0010, 0013–0021, 0031, 0037, 0057–0070) plus two quotes not yet in the inventory (Eric Owens, Roger Bailey); permission `unknown` for every one.
