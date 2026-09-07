# Richmond 2026 — Pursuit Spec Sheet (proof-first)

**Pursuit:** City of Richmond, CA — WPCP, Wastewater Collection and Stormwater Collection O&M
**Angle:** proof-first. Built from the proof-point registry, the testimonial inventory, the story catalog, and the four verbatim proposal layers *first*; requirements and win themes were then matched to the evidence that already exists. Where the evidence does not exist, this sheet says so and assigns a decision instead of a placeholder.
**Built:** 2026-09-06 · **Proposal due:** 2026-09-29 14:00 PT · **Contract start:** 2027-05-15
**Author's rule for every row below:** no value is invented. Every figure is copied from `proof-points/registry.md`, a `verbatim/<slug>/pages/pXXXX.md` page, or a pursuit document (RFP requirement id, Scope Register id, or the trip-report digest), and carries its source. Where sources disagree, all values are listed and a lock is recommended with a reason.

## How to read the ids

| Prefix | Means | Authority |
|---|---|---|
| `PP-####` | Registered proof point | `proof-points/registry.md` / `.json` |
| `PPN-##` | **Proposed** proof point — real fact, sourced to a verbatim page, **not yet registered** | this sheet; register before any live draft |
| `TM-####` | Testimonial | `testimonials/inventory.md` |
| `ST-####` | House story | `stories/catalog.md` |
| `STN-##` | **Proposed** story — not yet catalogued | this sheet; catalogue before assignment is final |
| `C-###` / `S-###` | RFP requirement / Scope Register item | `reqs/*.md` |
| `TR` | Due-diligence trip-report digest | `trip-report-digest.md` |

## What changed against the pilot's diagnosis

The pilot fact pack (`fp_03_qualifications.md` §K) recorded three gaps that are **no longer gaps**, because the verbatim layer now covers two proposals the pilot could not see (`ocwut-16-26`, `fulton-county-2025`):

1. **The Waterbury "55%+ odor complaint reduction" figure exists.** Six placements in `verbatim/ocwut-16-26`, with the mechanism and a $2M capital upgrade attached. See PPN-01 to PPN-04.
2. **NexGen EAM / Oklahoma City experience exists.** Jacobs is stated to be OCWUT's NexGen EAM implementation consultant, with two named SMEs. See PPN-20 to PPN-22.
3. **Waterbury's compliance and collections outcomes are quantified** (99.57% NPDES over five years; sewer inspection rate +100%; problem areas −15%; 1.5 million linear feet). See PPN-05 to PPN-08.

It also surfaces one thing the pilot did not catch: **the Waterbury client quote is attributed to two different people in two Jacobs proposals.** See Section 5, Q-01.

---

# 1. Locked number sheet

One row per figure the proposal may state. **LOCKED** = write this value, exactly this way. **needs-owner** = do not print until the named owner confirms. Nothing in this table may appear in body text with a bracket, a hedge, or a second value beside it (voice guide Rule 35).

## 1A. Corporate scale and finance

| id | Claim | LOCKED value | Competing values seen (with source) | Owner to confirm | Status |
|---|---|---|---|---|---|
| L-01 | Contracting-entity years in contract O&M | **45 years** ("OMI has been engaged in providing contract operations, maintenance, and management services for 45 years") | 45 / 45+ / >45 (hull p10 ¶2, ¶6; p11 ¶3; p5 ¶8) · 40 years, "four decades" (santamonica p15 ¶3, p63 ¶3, p64 ¶5, p99 ¶15, p7 ¶2) — PP-0149 conflict. "Full-service O&M since 1980" (ocwut p0074 ¶39) | Corporate Secretary | **locked** — 45 is the only value derivable from the incorporation date (L-03); the 40-year figures are the parent's O&M history, a different claim |
| L-02 | Contracting entity | **Operations Management International, Inc. (OMI), a wholly-owned subsidiary of Jacobs Solutions, Inc.** | Single pattern (hull p0010 "Company at a Glance"); Richmond entity is undecided per `pursuit.md` | Legal + Roy Aristizabal | needs-owner |
| L-03 | Entity incorporation | **10/25/1980, State of California** (PP-0165) | Single-source (hull p0010) | Corporate Secretary / CA SOS | needs-owner (verify current good standing) |
| L-04 | Federal tax ID | **93-0784940** (PP-0164) | Single-source (hull p0010) | Tax | needs-owner |
| L-05 | O&M-specific annual revenue | **more than $1.6 billion** (PP-0534) | $1.6B (santamonica p0063 ¶56) and "over $1.6 billion O&M annual revenue" (fulton p0168 ¶26) — two independent placements, no competing value | Finance | **locked** (answers C-001.6 with a 32× margin over the $50M threshold) |
| L-06 | OMFS revenue series | **2021 $376M · 2022 $390M · 2023 $435M · 2024 $485M · 2025 $495M; five-year average $429M** (PP-0216, PP-0215, PP-0214, PP-0213, PP-0212, PP-0217) | Single-source (hull Exhibit 3-4) | Finance | needs-owner — **preferred answer to C-001.6/C-051**: a five-year series from the operating group beats one corporate number |
| L-07 | O&M backlog | **more than $2.4 billion** (PP-0168) | $2.4B in hull, santamonica and fulton p0192 ¶23 — consistent | Finance | **locked** |
| L-08 | Parent annual revenue | **approximately $12 billion (FY24)** | ~$12B (hull p10 ¶5, p14 ¶10; santamonica p15 ¶3) · ~$16B (hull p14 ¶2) · $15B (santamonica p63 ¶3, p64 ¶4) — PP-0167 conflict | Finance | needs-owner — **recommend omitting**: the RFP asks for O&M revenue, not corporate revenue; L-05 and L-06 answer it without touching the conflict |
| L-09 | Contract renewal / client retention | **98% since 2013** (PP-0177) | 98% (hull p12 ¶5; santamonica p15 ¶6, p7 ¶2) · 99% (santamonica p63 ¶24) | OMFS Operations | **locked** — three placements support 98%, one supports 99%; the lower figure is also the safer one under reference-check verification (C-075) |
| L-10 | Credit rating | **5A3, "Stable Condition", "Low-Moderate Business Risk" (Dun & Bradstreet)** (PP-0536) | Single-source | Finance | needs-owner (currency) |
| L-11 | Contracts terminated for compliance or performance failure | **zero** (PP-0537) | "Not a single contract has ever been canceled due to compliance issues"; "Zero contract terminations due to performance failures" | Legal | needs-owner — the sourced statement is bounded at **five years** (PP-0221); C-056 asks ten. See G-07 |
| L-12 | Operating entities | *do not print* | ~370 operating companies and affiliates (hull p14 ¶10) · 300 entities (santamonica p64 ¶4) — PP-0219 conflict; ~100 in North America (PP-0220, consistent) | — | **needs-owner** — recommend printing only PP-0220 ("approximately 100 operating entities in the U.S. and Canada"), the value both cycles agree on |

## 1B. Portfolio counts

| id | Claim | LOCKED value | Competing values seen (with source) | Owner to confirm | Status |
|---|---|---|---|---|---|
| L-13 | Wastewater facilities operated | **106 wastewater facilities across 69 clients** (PP-0179, PP-0180) | Single-source each (hull) | OMFS Operations | needs-owner (point-in-time; recompute to Sept 2026) |
| L-14 | Facilities above 3 MGD | **50 facilities with capacities exceeding 3 MGD** (PP-0181) | Single-source | OMFS Operations | needs-owner |
| L-15 | Plants at least 3 MGD in the representative table | **20 wastewater treatment plants of at least 3 MGD** (PP-0188) | Single-source (Exhibit 3-3) | OMFS Operations | needs-owner |
| L-16 | Collection systems operated | **more than 6,700 miles** (PP-0183); **12 collection systems exceeding 40 miles** (PP-0189) | Single-source each | OMFS Operations | needs-owner — see G-03 for the ≥50-mile count C-001.4 actually asks for |
| L-17 | Distribution systems | **5,400 miles** (PP-0184) | Single-source | OMFS Operations | needs-owner (omit unless water scope is discussed) |
| L-18 | O&M portfolio | **more than 300 O&M projects** (PP-0150) | Consistent across hull, santamonica, ocwut p0074 ¶39 and p0164 ¶23 | — | **locked** |
| L-19 | US O&M staff | **4,000+ O&M professionals in the United States** (PP-0356) | 4,000+ (santamonica; fulton p0168 ¶36) · "over 2,300 employees" (fulton p0192 ¶23) | OMFS Operations | needs-owner — the 2,300 figure is a different denominator (operations teams generating backlog). Print 4,000+ only |
| L-20 | Global workforce | *do not print* | 42,000+ (hull p10 ¶5, p14 ¶10) · 45,000 (santamonica p64 ¶4) — PP-0171 conflict | — | needs-owner — irrelevant to this RFP; drop |
| L-21 | Industry ranking | **№1 in Sewer & Waste, Wastewater Treatment, and Sanitary & Storm Sewers — 2024 ENR Rankings** (PP-0361) | Single-source (santamonica p7); corroborated in fulton p0168 ¶36 | Marketing | needs-owner (confirm the 2026 ENR position before printing a year) |

## 1C. Compliance and safety

| id | Claim | LOCKED value | Competing values seen (with source) | Owner to confirm | Status |
|---|---|---|---|---|---|
| L-22 | NPDES permit compliance | **a 20-year compliance record of 99.8% with NPDES permit requirements across the wastewater treatment plants we operate nationwide** (PP-0232, PP-0233; hull p0017 ¶71) | 99.98% "environmental compliance record" (hull p0031 ¶20; santamonica p15 ¶6, p52 ¶8, p63 ¶20, p7 ¶2, p11 ¶14; fulton p0010 ¶29, p0168 ¶39) | OMFS Compliance | **locked, with a split** — these are two different claims. Use 99.8%/NPDES/20-year wherever the sentence is about permits (C-049.4). **Never print both figures in the same document** |
| L-23 | Environmental compliance record (firm-wide) | **99.98%** — *reserve; use only if a non-NPDES environmental claim is needed* | see L-22 | OMFS Compliance | needs-owner |
| L-24 | Current TRIR | **0.89** (PP-0225) | 2024 1.38 (PP-0226) · 2023 1.89 (PP-0227) · 2022 1.17 (PP-0484) · 2021 1.59 (PP-0485) · 2020 1.34 (PP-0486) | Corporate HSE | needs-owner — figure is the Hull 2026 cycle; C-049.3 asks for the *current* rate |
| L-25 | Current EMR | **0.45 (NCCI, 7/1/2025–7/1/2026)** (PP-0228) | 0.42 (7/1/2024–7/1/2025, PP-0230) · 0.45 (7/1/2023–7/1/2024, PP-0231) · 0.52 / 0.51 / 0.47 (2022/2021/2020) | Corporate HSE / Risk | needs-owner |
| L-26 | RIR against industry | **five-year average RIR 0.19 against an industry average of 0.62 — 60% better** (PP-0311, PP-0312, PP-0313; BLS 2018–2022) | Consistent across hull, santamonica, ocwut p0048 ¶13 | Corporate HSE | **locked** — but see the caution: 0.19 (five-year average) and 0.89 (current TRIR) are different bases. If both appear, the sentence must say so, or drop L-24 |
| L-27 | DART / LTIR against industry | **five-year average 0.056 against an industry average of 0.20 — 72% better** (PP-0314, PP-0315, PP-0316) | Consistent across three proposals | Corporate HSE | **locked** |
| L-28 | EMR against a contract threshold | **0.45, against a 1.0 requirement** (PP-0228, PP-0229) | Consistent | Risk | **locked** (satisfies voice Rule 12 — comparator in the same sentence) |
| L-29 | Environmental fines, last five years | **City of Ontario, OR — 5/26/2022 — $660 — herbicide applicator licences expired, renewed** (PP-0235); **City of Roseburg, OR — 5/26/2022 — $1,628 — same issue, same resolution** (hull Exhibit 3-9 adjacent row) | Single-source (hull) | Legal + OMFS Compliance | needs-owner — **regenerate current to Sept 2026** (C-049.3, five-year window) |
| L-30 | Self-disclosed permit incidents | **do not print** — 13 incidents across Clovis, Crescent City, Gilroy and Red Bluff (PP-0511) | santamonica Exhibit 2-24 | — | **locked as a suppression** — see Section 10. C-049.3 asks for *violations*, not for a voluntary excursion log; printing it is a volunteered negative (voice Rule 30) |

## 1D. California

| id | Claim | LOCKED value | Competing values seen (with source) | Owner to confirm | Status |
|---|---|---|---|---|---|
| L-31 | California O&M since | **1984** (PP-0371) | Single-source | Howard Brewen (CA O&M Director) | needs-owner |
| L-32 | California facilities | **contract O&M experience at 26 facilities statewide** (PP-0372), **including 11 municipal water and wastewater treatment plants** (PP-0373) | Single-source each | Howard Brewen | needs-owner |
| L-33 | California offices | *do not print a count* | 15 offices (santamonica p17 ¶6) · 11 offices (santamonica p65 ¶5) — PP-0375 conflict | Paul Rheault (VP Ops, West) | needs-owner — C-040.5 asks only for the office nearest Richmond and the office managing the project. Answer that; skip the count |
| L-34 | California emergency reach | **12 O&M projects in California whose personnel can respond within hours** (PP-0539); **2,400 associates in the region available for rapid deployment** (PP-0538) | Single-source each | Howard Brewen | needs-owner |
| L-35 | California tenures (footprint map) | **Gilroy 41 · Fort Irwin 20 · Turlock 20 · Twin Oaks 19 · Clovis 16 · Davis-Woodland 11 · Crescent City 6 · Red Bluff 5 · Soquel Creek 4 · Lincoln 1** (PP-0367, PP-0366, PP-0369, PP-0370, PP-0368, PP-0364, PP-0362, PP-0363, PP-0365, PP-0663) | All are as-of the 2025 Santa Monica cycle | Howard Brewen | needs-owner — **recompute every tenure to 2026-09-29 before printing** |
| L-36 | Auburn tenure | **recompute** | 32 years (hull p34 ¶10) · 33 years (santamonica p15 ¶9, p7 ¶2) — PP-0304 conflict | Howard Brewen | needs-owner — both are as-of dates a year apart; the recomputed 2026 value resolves it |
| L-37 | California AWT operators | **12 California AWTO-certified employees** (PP-0449); **the largest bench of AWT-certified operators in California** (PP-0450) | Consistent | Howard Brewen | needs-owner (reuse-specific; low relevance to Richmond — hold in reserve) |

## 1E. Reference plants — size, system, tenure, fee

| id | Reference | LOCKED values | Competing values seen | Owner | Status |
|---|---|---|---|---|---|
| L-38 | **Waterbury, CT** | 27 MGD activated sludge (PP-0031) · **approximately 310 miles** of sanitary sewer (PP-0032) · 20 pump stations (PP-0033) · 10-year agreement (PP-0030) · **November 2018** start (PP-0043) · **$6M** annual fee (PP-0046) | 320 miles in Exhibit 3-3 (hull p13 ¶3) vs 310 in four other placements — PP-0032 conflict | Kevin Dahl / account team | **locked** — 310 carries four placements including the reference sheet in two separate proposals |
| L-39 | Waterbury wet-weather flow | **wet-weather capacity above 54 MGD** (ocwut p0169 ¶5) | "<54 MGD" (hull p76 ¶7, PP-0045) · ">70 MGD" at the pump stations (hull p73/p74 resume blocks, PP-0034) | Kevin Dahl | needs-owner — the hull "<54" reads as a transcription of "≥/>"; two of three sources say *above*. If the owner cannot confirm, **write around it**: "wet-weather flows well above design" |
| L-40 | **San Marcos, TX** | 9 MGD WWTP · screening, grit, **primary clarification, biological nutrient removal, secondary clarification**, tertiary sand filtration, UV, post-aeration, biosolids dewatering, **three odor biotrickling filters**, Type I reclaimed water (ocwut p0175 ¶8) · **20 years** of service (ocwut p0175 ¶14) | none | Account team | needs-owner (contact, fee, exact contract dates are not in the bank — see G-11) |
| L-41 | **Vancouver, WA** | Westside **28.26 MGD** and Marine Park **16.1 MGD** activated sludge, a 3.2-MGD industrial waste lagoon, **eight major lift stations**, accredited laboratory, IPP, NPDES and Title V permits (ocwut p0171 ¶6) | Marine Park 16 MGD (hull Appendix C, PP-0101) vs 16.1 (Exhibit 3-3, PP-0207) | Account team | **locked at 16.1** — the two most recent placements agree |
| L-42 | Vancouver transition year | **2016** (PP-0621; ocwut p0171 ¶10 "In 2016, Jacobs replaced a 38-year incumbent operator") | "since 8/1/2015" (`past-performance/similar-facilities-table.md`) · "since contract start in 2015" (ocwut p0172 ¶5) · "January 2016 – Ongoing" (ocwut p0171 ¶18) | Account team | needs-owner — **print 2016 for the transition**; do not print a 2015 date beside it |
| L-43 | **West Basin / Edward C. Little, CA** | **40 MGD** (PP-0022) · nine treatment trains (PP-0395) · five grades of recycled water (PP-0396) · four satellite facilities (PP-0414) · nearly 600 connections (PP-0415) · **five-year** term (PP-0412) · **2025** start (PP-0416) · full responsibility **September 1, 2025** (PP-0391) | "30-40 MGD" in one resume (hull p72 ¶7) — PP-0022 conflict | Account team | **locked at 40 MGD** — four placements to one |
| L-44 | West Basin previous operator tenure | **more than 20 years** (PP-0337) | none | Account team | **locked** — and per voice Rule 28 the previous operator is **never named in body text** |
| L-45 | **Clovis, CA** | **2.8 MGD** MBR / Title 22 scalping plant (PP-0381) · **2009** start (PP-0398) · **16 years** (PP-0368) · more than **$100,000** in value-engineering savings (PP-0399) | none | Account team | needs-owner (annual fee not in the bank — G-11) |
| L-46 | Southbridge, MA | 3.77 MGD (PP-0003) · 48 miles (PP-0004) · 11 lift stations (PP-0005) · **February 1, 2025** takeover (PP-0006) · 5-year term (PP-0002) · $1.7M annual fee (PP-0065) | 3.7 MGD in Exhibit 3-3 (PP-0191) · fee unresolved on one source (PP-0065) | Account team | **locked at 3.77** — six placements to one |
| L-47 | Traverse City, MI | 8.5 MGD (PP-0076) · **1990** start (PP-0074) · $3.5M annual fee (PP-0080) · $31M MBR upgrade (PP-0224) · $1.5M BNR upgrade (PP-0223) | 17 MGD peak (PP-0078) is a peak, not a design value | Account team | **locked** |
| L-48 | Westerly, RI | 3.3 MGD (PP-0047) · nine pump stations (PP-0048) · **July 2017** start (PP-0057) · $2.4M annual fee (PP-0058) | none | Account team | **locked** |
| L-49 | South Huron, MI | 24 MGD (PP-0066) · 2019 start (PP-0069) · two lift stations (PP-0068) | interceptor **36 miles** (PP-0067, three placements) vs **39 miles** (Exhibit 3-3, PP-0192) · fee $5.3M (Exh 3-5) vs a literal "$xxM" placeholder on the Appendix B page (PP-0073) | Account team | needs-owner — **do not use as a listed reference until the fee and mileage are fixed** |
| L-50 | Turlock, CA | 2005 start (PP-0407) · ~20 years (PP-0369) · **$147,000/yr** chemical savings (PP-0411) · mixed-bed throughput 480,000 → 500,000 gallons, a 4% gain (PP-0409, PP-0410) | capacity 0.75 vs 0.8 MGD — PP-0382 conflict | Account team | needs-owner — **write around the capacity**; the savings figure is the usable part |
| L-51 | Soquel Creek, CA | 15-year O&M term (PP-0405) · 2020 start (PP-0406) · more than 10% energy reduction (PP-0476) | capacity 1.7 / 1.3 / 2 MGD — PP-0358 conflict | Account team | needs-owner — **do not print a capacity** until resolved |
| L-52 | Key West, FL | 10 MGD, 57 miles, 24 pump stations (PP-0194) | 37-year relationship (PP-0090), as of the Hull cycle | Account team | needs-owner (recompute duration) |

## 1F. Richmond's own numbers (the City's, not ours)

These are the figures the proposal will quote back to the City. Every one is a pursuit-document value, not a Jacobs claim.

| id | Claim | LOCKED value | Source | Owner | Status |
|---|---|---|---|---|---|
| L-53 | Fee basis flow and loading | **6.50 MGD influent · BOD 375 mg/L · TSS 450 mg/L** | C-078 / S-030 (RFP Attachment A p.40) | — | **locked** |
| L-54 | Plant capacity and storm storage | **20 MGD full treatment; flow above that goes to the 4.6 MG storm storage tank; about four blending events a year; incoming flow averages about 5 MGD** | TR (site visit 2026-08-18) | Roy Aristizabal | **locked** — trip-report fact; not a Jacobs claim |
| L-55 | Collection system | **approximately 190 miles of sanitary sewer; 20 remote lift stations, all submersible; a 5-mile sludge force main to West County; roughly one mile of the Keller Beach interceptor underwater in the bay** | TR | Roy Aristizabal | **locked** |
| L-56 | Stormwater system | **catch basins cleaned 100% twice a year; five hydrodynamic-separator trash-capture units; open channels and V-ditches; the Lake; outfalls and detention facilities; no debris baseline exists** | TR; C-004.6, C-004.7 | Roy Aristizabal | **locked** — note "no baseline" is a City-side fact, stated neutrally (voice Rule 29) |
| L-57 | Regulatory drivers | **2025 stormwater Cease and Desist Order requiring 100% trash reduction by 2030-06-30; Baykeeper Settlement Agreement obligations** | TR; C-002.11, C-003 | Roy Aristizabal | **locked** |
| L-58 | Performance standards and liquidated damages | **collection cleaning 25%/yr by Dec 31 ($250/day) · CCTV 10%/yr by Jun 1 ($250/day) · stormwater cleaning and CCTV 10%/yr by Jun 30 ($250/day) · monthly O&M report by the 10th ($500/day after the 15th) · Baykeeper compliance ($1,000/day, no grace period) · on-site emergency response 1 hour business hours / 2 hours after hours, $1,000 per occurrence after two misses in a month · specific deliverables $500** | C-005.1–C-005.7 (RFP §3.2, Attachment B) | — | **locked** |
| L-59 | M&R fund | **$2,000,000 first-year fund, inside the base fee, covering WWTP, sanitary and stormwater; work orders under $5,000 charged without pre-approval; over $5,000 need Public Works Director approval; unused funds returned to the City** | C-062, C-065, C-066, C-068, C-069 | — | **locked** |
| L-60 | Energy | **baseline 2,050 kWh/MG, 50/50 gain-share both ways, annual averages; the City pays gas and water** | C-061, C-063 / S-019 | — | **locked** |
| L-61 | Term and fee validity | **initial term 2027-05-15 to 2037-05-14; one mutually agreeable 5-year renewal on 180 days' notice; fee valid at least 180 days** | C-021, C-028, C-040.6 / C-045 | — | **locked** |
| L-62 | Escalation and adjustment | **CPI, U.S. city average, Water and Sewerage Maintenance, NSA, Series ID CUSR0000SEHG01; adjustment trigger at more than 10% change in flow, load, or system size** | C-067, C-071 | — | **locked** |
| L-63 | Staffing scale (City side) | **the incumbent's collections crew is one supervisor and seven crew, and the same crew maintains stormwater; the laboratory has three analysts; Jacobs' own estimate is 29–32 FTEs; prevailing wage applies to about 30% of operations and about 90% of maintenance labor** | TR; C-025 (prevailing wage) | Roy Aristizabal | needs-owner — the 29–32 FTE estimate is a pursuit estimate, not a commitment; it must not appear in body text until Staffing locks the org chart |
| L-64 | Richmond WPCP as it appears in Jacobs records | **"a facility designed for 16-MGD treatment of the City's sewage"; 27 employees across five departments** (`wiki/resumes/mack-mckenzie.md`; verbatim santamonica p0086 ¶3) | resume block | Mack Mckenzie | **locked as historical** — this is the plant *as it was during Mack's tenure*. It conflicts with L-54 (20 MGD today). Any sentence using it must be past tense and must not describe today's plant |

**Locked-number count: 64 rows — 27 locked, 37 needs-owner.**

---

# 2. Approved proof points

Outcome proofs — savings, complaint reductions, enforcement resolved, energy cuts, callouts eliminated, awards. Wording is verbatim from the source; a writer may compress but may not add. **External-use status** is the honest state today: `approved` = the fact has been published in a submitted Jacobs proposal and needs only a currency refresh; `client-permission-needed` = it names a client we intend to list as a reference, so C-048/C-052 permission is required anyway; `internal-only` = do not print in this form.

## 2A. Odor — the theme with the thinnest prior evidence, now the best sourced

| id | Exact wording | Source | External use | Assigned to |
|---|---|---|---|---|
| **PPN-01** | "reduced public complaints by more than 55%" — Waterbury, CT, following a formal odor source-characterization study | `verbatim/ocwut-16-26/pages/p0170.md` ¶9; `p0169.md` ¶12; `p0044.md` ¶41; `p0077.md` ¶26, ¶38; `p0042.md` ¶17; `p0009.md` ¶47 | client-permission-needed | 8.4.2 Executive Summary (stat callout) · 8.4.5 Technical Approach — odor · 8.4.3 Qualifications (reference narrative) |
| **PPN-02** | Window for PPN-01: **"between contract years one and two"** | `p0170.md` ¶9; `p0169.md` ¶12; `p0044.md` ¶41 | client-permission-needed | same as PPN-01 |
| **PPN-03** | "Four chemical wet scrubbers serving the headworks, solids handling areas, and incineration building were in disrepair at contract start, and the on-site incinerator was also contributing to odor source." | `p0169.md` ¶12; `p0077.md` ¶26 | client-permission-needed | 8.4.5 — odor (the before-condition) |
| **PPN-04** | "$2M odor control upgrade completed" — "a carbon absorber polishing stage added downstream of the primary scrubbers, replacement of aging air piping and chemical dosing pumps on scrubber system #1, and new dosing pumps on scrubber system #2" | `p0170.md` ¶2, ¶10 | client-permission-needed | 8.4.5 — odor · 8.4.3 |
| ST-0008 / no number | "These changes addressed the root causes of odors without requiring immediate capital investment." — Southbridge, MA | `verbatim/hull-wwtf-om-2026/pages/p0037.md` ¶1–¶3 | client-permission-needed | 8.4.5 — odor (sidebar). **Qualitative — do not attach a number** |
| PP-0151 | "delivered over $134k in cost savings" — Westerly biofilter converted from organic to engineered media | hull p0007 ¶13 | client-permission-needed | 8.4.5 — odor / asset management · 8.4.2 |
| **PPN-05** | "We operate and maintain three biological scrubbers that control odors across the headworks, solids handling, and treatment areas… This preventive approach eliminates odors without the chemical costs and handling concerns associated with chemical scrubbing systems." — San Marcos, TX | `verbatim/ocwut-16-26/pages/p0175.md` ¶12; `p0176.md` ¶1 | client-permission-needed | 8.4.5 — odor (answers the chemical-cost transfer, TR) |
| PP-0309 | Commitment to respond to all odor complaints within **1 hour** of notification | hull; `wiki/technical-approach/site-specific-odor-control-program.md` | approved | 8.4.5 — odor (commitment callout) |

## 2B. Compliance, enforcement, and permit performance

| id | Exact wording | Source | External use | Assigned to |
|---|---|---|---|---|
| **PPN-06** | "The facility has maintained a 99.57% permit compliance rate over the past 5 years." — Waterbury | `verbatim/ocwut-16-26/pages/p0169.md` ¶5; `p0170.md` ¶7 | client-permission-needed | 8.4.3 Qualifications (C-049.4) · 8.4.2 |
| ST-0006 | "We assumed operations when the facility was noncompliant and implemented a comprehensive operational strategy and maintenance management program that restored compliance and resolved enforcement actions." — Traverse City, 1990 | hull p0080 ¶3; p0015 ¶2 | client-permission-needed | 8.4.3 · 8.4.5 — compliance (the enforcement-resolution proof) |
| PP-0056 | 2021 RIDEM consent agreement: Jacobs modelled, assessed and recommended, then was selected as the progressive design-build designer "due to our operational knowledge" — Westerly | hull p0077 ¶12 | client-permission-needed | 8.4.3 · 8.4.5 — capital planning |
| PP-0053 / PP-0054 | DEM-mandated corrective action items inherited from a 2016 inspection, closed; approximately **32 disinfection callouts a year eliminated** — Westerly | hull p0077 ¶5–¶12 | client-permission-needed | 8.4.5 — transition/maintenance · 8.4.2 |
| PP-0059 / PP-0060 / PP-0061 | RICWA Consistent Permit Compliance Award 2019–2023; RICWA Three-or-More-Years Complete Permit Compliance Award 2022; USEPA New England Regional O&M Excellence Award 2018 — Westerly | hull p0077 | client-permission-needed | 8.4.3 (awards) |
| PP-0305 | "The Jacobs team has won Plant of the Year and Collections of the Year every year since 2012 from the California Water Environment Association." — Auburn, CA | hull p0034 ¶10 | client-permission-needed | 8.4.5 — collections (sidebar) · 8.4.3 (California) |
| **PPN-07** | "NACWA Performance Awards from 2017-2025, including Platinum Peak Performance Awards"; "WA Department of Ecology Outstanding Performance Award more than 20 times"; WEF "Utility of the Future Today" — Vancouver | `verbatim/ocwut-16-26/pages/p0172.md` ¶6, ¶11, ¶16 | client-permission-needed | 8.4.3 (awards) |
| PP-0235 + Exh 3-9 | Ontario, OR $660 and Roseburg, OR $1,628, both 5/26/2022, expired herbicide applicator licences, both renewed: "These matters were administrative in nature, promptly addressed, and resolved in coordination with regulators, with no impact to our ability to deliver services." | hull p0014 area, Exhibit 3-9 | approved (this is the *required* C-049.3 disclosure) | 8.4.3 — must carry the four-move close (Section 10) |

## 2C. Money returned to the client

| id | Exact wording | Source | External use | Assigned to |
|---|---|---|---|---|
| PP-0042 | "The City estimated cost savings of up to $12.7 million compared to the previous operating approach." — Waterbury | hull p0076 ¶6; corroborated `ocwut p0169.md` ¶9, `p0170.md` ¶8 | client-permission-needed | 8.4.2 (closer) · 8.4.3 · 8.4.1 (one clause) |
| **PPN-08** | "our team reduced ferric chloride use by 65%" — San Marcos, through enhanced biological phosphorus removal and process control | `verbatim/ocwut-16-26/pages/p0176.md` ¶3, ¶5 | client-permission-needed | 8.4.5 — process/chemical optimization. **Directly answers the transfer of chemical cost to the operator and the ferric-chloride H₂S/struvite dosing on the 5-mile sludge line (TR)** |
| **PPN-09** | "cut electricity consumption by more than 174,000 kWh annually through operational changes alone, with no capital investment required" — "174,000+ kWh in annual electricity savings — $22,000 per year" — San Marcos | `p0176.md` ¶3, ¶6 | client-permission-needed | 8.4.5 — energy · 8.4.7 (gain-share rationale). **The proof behind the 2,050 kWh/MG gain-share offer** |
| **PPN-10** | "40% reduction in polymer use; ~50% reduction in biosolids hauling costs" — San Marcos | `p0176.md` ¶3, ¶7 | client-permission-needed | 8.4.5 — solids |
| **PPN-11** | "$900,000 in utility rebates from energy efficiency initiatives"; "The team completed 20 energy projects" — Vancouver | `verbatim/ocwut-16-26/pages/p0172.md` ¶10, ¶16 | client-permission-needed | 8.4.5 — energy · 8.4.2 |
| **PPN-12** | "A $500,000 heat exchanger investment extended the life of the aging incinerator, deferred an unplanned shutdown, reduced confined-space entry risks for maintenance staff, and avoided an estimated $275,000–$400,000 in near-term capital costs." — Vancouver | `p0171.md` ¶11; `p0172.md` ¶9 | client-permission-needed | 8.4.5 — asset management / capital planning |
| **PPN-13** | "earned a $57,151 nitrogen credit for the City" through Connecticut's Nitrogen Credit Exchange Program, 2022 — Waterbury | `p0170.md` ¶4, ¶13 | client-permission-needed | 8.4.5 — **Innovation to improve revenue** (C-036). The only non-ratepayer-revenue proof in the bank |
| PP-0411 | "The new method generates $147,000 in chemical savings for the client annually." — Turlock ZLD, CA | santamonica p0026–p0027 | client-permission-needed | 8.4.5 — chemical optimization (California) |
| PP-0049 / PP-0050 | More than $500,000 saved against the original six-year forecast; approximately $250,000 against the adjusted forecast over three years — Westerly | hull p0077 ¶5 | client-permission-needed | 8.4.2 · 8.4.3 |
| PP-0399 | "saving the City more than $100,000 through value engineering" — Clovis, CA | santamonica p0022 | client-permission-needed | 8.4.3 (California reference narrative) |
| PP-0528 | "energy savings opportunities valued at more than $1 million for the Wilmington WWTP", identified at an Annual Innovation Workshop | santamonica p0062 | approved | 8.4.5 — innovation. **Say "opportunities identified", not "savings realized"** |
| PP-0476 | "more than 10% energy reduction through membrane recovery optimization and blower reprogramming" — Soquel Creek, CA | santamonica p0047 ¶10 | client-permission-needed | 8.4.5 — energy (California) |
| PP-0079 | "Optimization efforts following MBR installation reduced electrical consumption by more than 30%" — Traverse City | hull p0080 ¶7 | client-permission-needed | 8.4.5 — energy |

## 2D. Transition and workforce

| id | Exact wording | Source | External use | Assigned to |
|---|---|---|---|---|
| **PPN-14** | "In 2016, Jacobs replaced a 38-year incumbent operator in one of the most significant Pacific Northwest O&M transitions." — Vancouver | `verbatim/ocwut-16-26/pages/p0171.md` ¶10 | client-permission-needed | 8.4.4 Staffing/transition · 8.4.2. **Rewrite without the word "incumbent operator" attached to a name; the firm is never named (voice Rule 28)** |
| **PPN-15** | "90% of all transition activities were completed within 90 days, and all start-up activities wrapped within 180 days." — Vancouver | `p0171.md` ¶16 | client-permission-needed | 8.4.4 — transition plan (C-053.7) |
| **PPN-16** | "100% of represented staff were offered employment, and they enjoyed equal or better compensation packages"; "integrating 26 City employees into our operations team" — Waterbury | `p0169.md` ¶7; `p0170.md` ¶4 | client-permission-needed | 8.4.4 — the answer to the incumbent-staff question |
| PP-0628 / PP-0629 | Employee satisfaction 3.3 before, 4.7 after — Vancouver | santamonica; `swip-staff-retention-and-six-step-transition-process.md` | approved | 8.4.4 |
| PP-0339 | Employee satisfaction 3.6 → 4.1 after Jacobs assumed contract operations — West Basin, CA | hull p0048 ¶6 | approved | 8.4.4 · 8.4.3 |
| PP-0626 / PP-0627 · PP-0630 / PP-0631 | Pembroke Pines 3.4 → 4.6; Ontario, OR 2.7 → 4.5 | santamonica | approved | 8.4.4 (use two of the four swings, not all four) |
| PP-0624 | "90% conversion rate" for qualified employees offered positions during Jacobs transitions | santamonica | approved | 8.4.4 |
| PP-0623 | "over a dozen projects in three years" seamlessly transitioned | santamonica | approved | 8.4.4 |
| PP-0621 / PP-0622 | Two prior transitions from the same previous operator — Wilmington, DE and Vancouver, WA | santamonica; `management-staffing/swip-transition-plan-overview-and-track-record.md` | approved | 8.4.2 · 8.4.4. **Name neither firm** |
| PP-0055 | "Removing six 30-yard containers of trash and debris from throughout the facility and pump stations, including scrap metal that was recycled with the money refunded to the client." — Westerly | hull p0077 | client-permission-needed | 8.4.5 — housekeeping. **The single closest analogue to Richmond's unanimous housekeeping finding (TR)** |
| **PPN-17** | "Within 90 days, we cleared and graded a 2-acre City-owned parcel, built a new GeoTube laydown area, dredged the lower lagoon, and removed 1,100 dry tons of solids for beneficial reuse at less than half the cost of conventional disposal, solving a 35-year problem in the first contract quarter." — Waterbury WFP | `verbatim/ocwut-16-26/pages/p0170.md` ¶15, ¶11 | client-permission-needed | 8.4.5 — transition/first-90-days · 8.4.2 |

## 2E. Collections, maintenance, and OT/SCADA

| id | Exact wording | Source | External use | Assigned to |
|---|---|---|---|---|
| **PPN-18** | "Monthly sewer inspection rates increased 100%; sewer problem areas were reduced by nearly 15%, and the team cleaned and inspected more than 1.5 million linear feet of pipe." — Waterbury CMOM | `verbatim/ocwut-16-26/pages/p0170.md` ¶12 | client-permission-needed | 8.4.5 — collections. **The Baykeeper-analogue outcome** |
| **PPN-19** | "We led a $25M, multi-year modernization of the SCADA and control infrastructure, replacing PLCs, upgrading HMI systems, and improving network architecture without a single service interruption." — Vancouver | `verbatim/ocwut-16-26/pages/p0172.md` ¶8; `p0171.md` ¶10 | client-permission-needed | 8.4.5 — SCADA/OT · 8.4.2. **The answer to the end-of-life PLC and undocumented-firewall findings (TR)** |
| **PPN-20** | "OCWUT has selected NexGen EAM as the enterprise AMS, and our team is OCWUT's implementation consultant for the platform." | `verbatim/ocwut-16-26/pages/p0060.md` ¶23, ¶26 | **internal-only until verified** — see G-05 | 8.4.5 — asset management/CMMS (C-004.3) |
| **PPN-21** | Janeane Giarrusso, IAM — CMMS/NexGen SME, 25 years of experience (9 with Jacobs), "a key member of Jacobs' current NexGen implementation for OCWUT" | `p0060.md` ¶41, ¶44; `p0092.md` ¶23 | internal-only until verified | 8.4.4 — technical bench · 8.4.5 |
| **PPN-22** | Amy Dembinski, CRL — 18 years in enterprise asset management and CMMS implementation, based in Tulsa, "currently supporting the City of Oklahoma City's NexGen EAM implementation" | `p0085.md` ¶17; `p0115.md` ¶26 | internal-only until verified | 8.4.4 — technical bench |
| PP-0571 | Two UV channels replaced in phases, one channel operational at all times, "completed without violations" — Key West | santamonica p0078 ¶2–¶3 | client-permission-needed | 8.4.5 — maintenance |
| PP-0318–PP-0321 | August 27, 2020 sewer backup in a high-rain event; CCTV found a collapsed 15-inch pipe; a two-day temporary bypass held service; 90 feet of pipe replaced — Waterbury | hull; `compliance-plans/emergency-response-storm-preparedness-coastal-wwtf.md` | client-permission-needed | 8.4.5 — wet-weather and emergency response (C-005.6) |
| PP-0545 | Jacobs staff mobilized at the City's request during a 2019 water-supply emergency **at no cost to the City** — Waterbury | santamonica; `compliance-plans/swip-emergency-response-regional-resources.md` | client-permission-needed | 8.4.5 — emergency response |
| PP-0125 / PP-0130 / PP-0131 | SmartCover at NJAW Bound Brook: annual SSOs 12 → 0; 16 SSOs prevented in four months; fleet grew 40 → 196 units in under two years | hull p0092–p0093 | **internal-only as Jacobs performance** — label it a SmartCover/Hazen/NJAW technology case study every time (ST-0020) | 8.4.5 — collections technology, as a labelled vendor case only |
| PP-0520 | Jacobs field-trained maintenance specialists have completed condition assessments on **1,000,000** water and wastewater plant assets | santamonica | approved | 8.4.5 — condition assessment (C-004.2) |
| PP-0331 / PP-0342 | Baseline condition assessment with prioritized, data-driven renewal, reliability and capital-planning recommendations **within 90 days of commencement** | hull | approved | 8.4.5 — matches C-004.2's 90-day deliverable exactly |

## 2F. Firm-wide statistics cleared for use

| id | Value | External use | Assigned to |
|---|---|---|---|
| L-05 / PP-0534 | more than $1.6 billion in annual O&M revenue | approved (currency refresh) | 8.4.3 (C-001.6) · 8.4.1 |
| L-09 / PP-0177 | 98% contract renewal rate since 2013 | approved | 8.4.2 · 8.4.3 |
| L-22 / PP-0232 | 20-year record of 99.8% NPDES permit compliance | approved | 8.4.3 (C-049.4) · 8.4.5 |
| L-26 / L-27 | RIR 0.19 against 0.62 (60% better); DART 0.056 against 0.20 (72% better) | approved | 8.4.3 (C-049.3) · 8.4.4 |
| L-28 | EMR 0.45 against a 1.0 requirement | approved | 8.4.3 |
| PP-0374 | "over 100 O&M and technical specialists focused solely on supporting projects like [the City]'s" | approved | 8.4.4 (C-049.2, C-053.5) |
| PP-0553 | a committed annual technical and regional support allowance, stated in hours | approved as a *pattern*; the Santa Monica value (1,300 hours) is pursuit-specific and **must be re-priced for Richmond** | 8.4.4 · 8.4.7 |
| PP-0547 / PP-0548 | 2,600 IT professionals; 350 dedicated SCADA practitioners | approved | 8.4.5 — cybersecurity (a TR hot button) |
| PP-0027 | Santa Monica SWIP treats up to **0.5 MGD** of stormwater, urban runoff and brackish groundwater for beneficial reuse | approved | 8.4.3 (C-001.5) — **the only Jacobs-operated stormwater asset in the bank.** See G-04 |

**Approved proof-point count: 52 entries — 22 of them (PPN-01 to PPN-22) newly sourced from the verbatim layer and not yet in the registry.**

---

# 3. Preferred reference set

C-048 and C-052 require five references with all six fields: name and location, owner contact, description of services, processes and system attributes, years of service, and annual project fee. The set below is chosen so that the five together cover every desired qualification in C-001 and every hot button in the trip reports, and so that **no single permission failure collapses the set** (each bench reference substitutes for a named primary).

| # | Reference | One-line reason tied to Richmond | What this reference must prove | Permission / contact status |
|---|---|---|---|---|
| **1** | **City of Waterbury, CT — Waterbury Water and Wastewater System O&M** | The only reference that matches Richmond on all four legs at once: a 27-MGD activated-sludge plant, ~310 miles of sanitary sewer, 20 pump stations, and a procurement triggered by sewer overflows that reached a river — Richmond's Baykeeper situation with the names changed. | C-001.3 (≥10 MGD activated sludge) · C-001.4 (≥50-mile system) · odor outcome (PPN-01, PPN-04) · permit compliance rate (PPN-06) · client-stated savings (PP-0042) · CMOM against a cleaning/CCTV regime (PPN-18) | Contact on file: **Mike LeBlanc, Director of Finance, 203.574.6840 x7059, mleblanc@waterburyct.org**. **Written permission NOT on file. Contact currency NOT verified. The client quote has a live attribution conflict — see Q-01.** |
| **2** | **City of San Marcos, TX — San Marcos WWTP O&M** | Process-identical to Richmond and nothing else in the bank is: screening, grit, **primary clarification**, activated-sludge BNR, secondary clarification, tertiary filtration, UV, **three odor biotrickling filters**, discharging to an ecologically sensitive river — plus twenty years of it. | The chemical and energy commitments Richmond prices: ferric chloride −65% (PPN-08), 174,000+ kWh/yr = $22,000/yr (PPN-09), polymer −40% and hauling −50% (PPN-10), odor controlled biologically rather than chemically (PPN-05) | **No contact, no fee, no contract dates in the bank.** Account team must supply all three (G-11). Highest-value reference in the set and the least documented — start here. |
| **3** | **City of Vancouver, WA — Westside and Marine Park WWTPs O&M** | Displaced a 38-year incumbent at two activated-sludge plants (28.26 and 16.1 MGD) and then rebuilt the control system — the two things Richmond is most afraid of, in one project. | Incumbent displacement without service loss (PPN-14, PPN-15) · $25M SCADA/PLC modernization with no interruption (PPN-19) · $900K in utility rebates from 20 energy projects (PPN-11) · staff satisfaction 3.3 → 4.7 (PP-0628/PP-0629) · zero lost-time incidents since contract start | Contact on file: **Frank Dick, P.E., Sewer and Wastewater Engineering Supervisor, 360.487.7179, frank.dick@cityofvancouver.us**. **Permission NOT on file.** Two usable quotes (Q-05, Q-06) both unpermissioned. |
| **4** | **West Basin Municipal Water District — Edward C. Little Water Recycling Facility, El Segundo, CA** | California, 40 MGD, nine treatment trains, and Jacobs is displacing the same operator Richmond is replacing — right now, 400 miles down the same coast. | C-001.2 (California) · active displacement of a >20-year incumbent (PP-0337) · transition managed to the client's satisfaction (PP-0339, Q-03) | Contact on file: **Susanna Li, Manager of Engineering, 310.660.6238, susannal@westbasinca.gov**. **Permission NOT on file. Annual fee NOT in the bank (G-11).** Contract began 2025 — keep every operating-history claim proportional to that. |
| **5** | **City of Clovis, CA — Clovis WWTP/WRF** | Sixteen unbroken California years under Title 22 with contractual regulatory, environmental **and odor** performance guarantees met — the durability answer beside West Basin's recency. | C-001.2 · C-049.4 (guaranteeing permit compliance) · long-tenure California standing · $100K+ value engineering (PP-0399) | Contact on file: **Nicholas Torstensen, Assistant Public Utilities Director, 1033 Fifth Street, Clovis CA 93611, 559.324.2662, nicholast@clovisca.org**. **Permission NOT on file. Annual fee NOT in the bank (G-11).** Note the internal tension flagged in ST-0016: the same source proposal self-discloses Clovis permit excursions. Reconcile "met consistently" against that record before writing it (Section 10). |

## Bench

| # | Reference | Substitutes for | Why it is bench, not primary |
|---|---|---|---|
| **B1** | **Town of Southbridge, MA — Southbridge WWTP** — 3.77 MGD, 48 miles, 11 lift stations, unanimous selection over an incumbent, odor complaints resolved with no capital, and an $85M nitrogen upgrade awarded to Jacobs Design-Build within the year | San Marcos (if permission or contact fails) or Waterbury (if the quote conflict cannot be resolved) | Started February 2025 — too new to carry a compliance record, and its odor outcome is qualitative (ST-0008 has no registered number). It is the *procurement-shaped* analogue, not the performance analogue. Contact: **John Jovan, Jr., Town Manager, 508.764.5405, jjovan@southbridgemass.org**; permission not on file. |
| **B2** | **City of Traverse City, MI — Traverse City Regional WWTP DBO** — took over a noncompliant plant under enforcement in 1990, resolved the enforcement actions, and has held compliance for 35 years with awards in 2004, 2006, 2007 and 2019 | Clovis (if the excursion record makes the guarantee language unusable) | The only enforcement-resolution story in the library, and the strongest possible answer if the panel weights the Cease and Desist Order — but it is an MBR plant in Michigan with a 1990 start, so it argues durability rather than fit. Contact: **Art Krueger, Director of Municipal Facilities, 231.922.4923, akrueger@traversecitymi.gov**; permission not on file. |

## Dropped from the pilot's five, and why

- **Westerly, RI** — kept as a *story* (ST-0001, housekeeping and callouts) but dropped as a listed reference: 3.3 MGD is an order of magnitude below Richmond and it adds no qualification the five already carry.
- **South Huron Valley Utility Authority, MI** — dropped: two unresolved source conflicts (36 vs 39 interceptor miles; a literal `$xxM` fee placeholder in one source, L-49) and **no usable client quote** — the testimonial printed on its page is a copy/paste of the Southbridge quote (TM-0008) and must never be attributed to SHVUA.

---

# 4. House stories, ranked

Top eight for Richmond, with the beat, the proof ids, and the section that gets it. `STN-` entries are real, sourced stories that are **not yet in `stories/catalog.md`** — catalogue them before a writer touches them.

| Rank | id | The beat | Proof ids | Assigned section |
|---|---|---|---|---|
| **1** | **ST-0005** — Waterbury: overflows in a river to a client-stated $12.7 million | "The City estimated cost savings of up to $12.7 million compared to the previous operating approach." The number is the client's, not ours — and it now travels with a compliance rate and an odor result. | PP-0042 · PP-0043 · PP-0030 · PP-0031 · PP-0032 · PP-0033 · PP-0046 · PP-0035 · **PPN-01 · PPN-02 · PPN-04 · PPN-06 · PPN-16 · PPN-18** · TM-0006 (blocked, Q-01) | **8.4.2 Executive Summary — the closer** · 8.4.3 · 8.4.5 |
| **2** | **STN-01** — Vancouver: a 38-year incumbent replaced, then the control system rebuilt underneath a running plant | "We led a $25M, multi-year modernization of the SCADA and control infrastructure… without a single service interruption." Two plants, no interruption, and the staff scored the change 3.3 → 4.7. | **PPN-14 · PPN-15 · PPN-19 · PPN-11 · PPN-12** · PP-0621 · PP-0628 · PP-0629 · PP-0207 · Q-05, Q-06 (blocked) | 8.4.4 Staffing and transition · 8.4.5 SCADA/OT · 8.4.2 |
| **3** | **STN-02** — San Marcos: twenty years of taking cost out of the same treatment train Richmond runs | "Our team reduced ferric chloride use by 65%… cut electricity consumption by more than 174,000 kWh annually through operational changes alone, with no capital investment required." | **PPN-05 · PPN-08 · PPN-09 · PPN-10** | 8.4.5 Technical Approach — process, chemical, energy, odor · 8.4.7 fee narrative |
| **4** | **ST-0013** — West Basin: the nation's largest reuse facility, taken over from a twenty-year operator, in California | The Board President and the Manager of Engineering both went on record about the transition, and staff satisfaction rose 3.6 → 4.1. | PP-0022 · PP-0337 · PP-0391 · PP-0412 · PP-0416 · PP-0339 · Q-03, Q-04 (blocked) | **8.4.3 Qualifications — the closer** · 8.4.4 |
| **5** | **ST-0001** — Westerly: the first eighteen months | "Removing six 30-yard containers of trash and debris from throughout the facility and pump stations, including scrap metal that was recycled with the money refunded to the client." | PP-0052 · PP-0053 · PP-0054 · PP-0055 · PP-0057 · PP-0059 · PP-0060 · PP-0061 | 8.4.5 — housekeeping and first-90-days (**the direct answer to the unanimous housekeeping finding, TR**) · 8.4.4 transition |
| **6** | **ST-0008** — Southbridge: odor complaints resolved without a capital project | "These changes addressed the root causes of odors without requiring immediate capital investment." | none registered — **qualitative only, do not attach a number** | 8.4.5 — odor, as the sidebar beside the four-layer framework |
| **7** | **ST-0006** — Traverse City: a noncompliant plant under enforcement becomes a 35-year record | "We assumed operations when the facility was noncompliant and implemented a comprehensive operational strategy and maintenance management program that restored compliance and resolved enforcement actions." | PP-0074 · PP-0081 · PP-0082 · PP-0083 · PP-0084 · PP-0085 · PP-0076 · PP-0080 | 8.4.3 · 8.4.5 — compliance leadership |
| **8** | **ST-0014** — Auburn: 32 years and Plant of the Year every year since 2012 | "The Jacobs team has won Plant of the Year and Collections of the Year every year since 2012 from the California Water Environment Association." | PP-0304 (conflict, L-36) · PP-0305 · Q-02 (blocked) | 8.4.5 — collections sidebar · 8.4.3 California |

**Honorable mention, and where each earns its space:** ST-0012 Annual Innovation Workshop (8.4.5 innovation; lead with PP-0528, the >$1M Wilmington energy opportunity, because Richmond scores energy) · ST-0027 reading the incumbent's data room (8.4.5 transition — use it as a **device**, rebuilt entirely from Richmond's own data room; every figure in it belongs to another plant) · ST-0020 SmartCover (8.4.5 collections technology, labelled a vendor case study every single time) · ST-0004 Westerly biofilter $134K (8.4.2 one-liner).

## The closers

- **Executive Summary closer — ST-0005 (Waterbury).** It is the only story in the library whose origin is a river-protection compliance failure, whose middle is a cleaning-and-CCTV program run to a schedule, and whose end is a number the *client* published. With PPN-01, PPN-06 and PPN-18 attached it now closes on odor, permit performance and collections in one paragraph — the three things Richmond told us it cares about.
- **Qualifications closer — ST-0013 (West Basin).** Qualifications is where the California corporation, the California good standing (C-050) and the California operating record (C-001.2) live. West Basin closes it because it is the one project that is California, at scale, and a live displacement of the same operator — the argument made as a fact rather than as a promise.

---

# 5. Quotable inventory

Every quote the proposal may print. **Permission is `unknown` for all 46 entries in `testimonials/inventory.md`** — no release, approval, or reuse authorization is recorded anywhere in the content bank. Therefore **every client quote below is NOT PRINTABLE until the account team confirms permission in writing.** Voice Rule 18 additionally bars any quote without name, title and organization.

## 5A. Client quotes — candidates for Richmond

| id | Quote (abridged where marked) | Attribution | Permission | Status |
|---|---|---|---|---|
| **Q-01** | "Protection of the Naugatuck River is a key priority for our city. We went through a careful process to select our O&M contractor, and I'm pleased that we chose Jacobs. I've seen a lot of improvements since our partnership began in 2018, and I rest easier knowing that Kevin Dahl and his team are taking excellent care of our wastewater system." | **CONFLICT.** `TM-0006` records **Mike LeBlanc, Director of Finance, City of Waterbury** (hull p0076 ¶17). The identical text is attributed to **Mayor Neil O'Leary, City of Waterbury** in `verbatim/ocwut-16-26/pages/p0170.md` ¶1 ("I'm *very* pleased"). | unknown | **NOT PRINTABLE — attribution unresolved.** Two Jacobs proposals put the same words in two different mouths. Do not print in any form until the account team says which is correct. Also confirm Kevin Dahl is still on the account before printing a named-staff quote. |
| **Q-02** | "For the past 32 years, Jacobs has been our contract operator… The Jacobs team has won Plant of the Year and Collections of the Year every year since 2012… we think of them as an extension of the City." | TM-0003 — Mengil Dean, Public Works Manager, City of Auburn WWTP, CA | unknown | **NOT PRINTABLE.** Best California tenure quote in the bank. No contact on file; needs fresh consent (catalog rule). Tenure figure carries the L-36 conflict. |
| **Q-03** | "…the transition was managed very effectively, with minimal challenges, and resulted in a smooth and successful onboarding for a system of this complexity." | TM-0004 — Susanna Li, Manager of Engineering, West Basin Municipal Water District | unknown | **NOT PRINTABLE.** Highest-value transition quote for this pursuit: California, and she is also the listed reference contact. |
| **Q-04** | "This O&M contract reflects our fervent commitment to investing in the long-term performance of our recycled water treatment facilities… We look forward to working with Jacobs to continue that high-quality production our customers have come to know and trust." | TM-0017 — Gloria Gray, Board President and Division II Director, West Basin MWD | unknown | **NOT PRINTABLE.** Board-level validation; pairs with Q-03. |
| **Q-05** | "Jacobs took responsibility of operating and maintaining Vancouver's wastewater treatment plants in 2016. As part of the transition process Jacobs put together a comprehensive transition plan which made the process very positive, smooth and seamless for not only the City but also the existing staff that became Jacobs employees. There was a high degree of transparency which continues to this day." | TM-0020 — Frank Dick, P.E., Sewer and Wastewater Engineering Supervisor, City of Vancouver – Public Works | unknown | **NOT PRINTABLE.** Longest usable transition quote; the full variant is in `fulton-county-2025/p0026`. Trim to ≤35 words for a pull quote (voice Rule 32). |
| **Q-06** | "Jacobs has seamlessly integrated engineering, construction, and contract operations to deliver several equipment and controls system in a cost-effective manner… maintain treatment plant level-of-service; and maintain or extend service life of assets." | TM-0019 — Frank Dick, P.E., City of Vancouver – Public Works | unknown | **NOT PRINTABLE.** The SCADA/controls quote — the exact voice for the Richmond OT hot button. Note it contains the banned word "seamlessly"; quoted client speech is exempt, but do not echo the word in our own prose. |
| **Q-07** | "Despite the many challenges presented by the COVID-19 outbreak, Jacobs implemented a smooth and successful transition from our previous operator… a technical team that applied their engineering and operational expertise to ensure that operations continued without interruption." | TM-0021 — Vincent R. Carroccia, Deputy Commissioner, DPW, City of Wilmington, DE | unknown | **NOT PRINTABLE.** Second displacement testimonial; use only if Vancouver's is unavailable, to avoid two transition quotes in one section. |
| **Q-08** | "The Town of Westerly was pleased to receive Jacobs' innovative proposal, which increased the annual O&M budget by $100,000 while saving the Town $100,000 annually in contract costs. Jacobs staff were on hand to take over hours before the contract inception and they hit the ground running." | TM-0007 — Sheila M. McGauvran, PE, Town Engineer, Town of Westerly, RI | unknown | **NOT PRINTABLE.** The most quotable paradox in the library and a natural fit for the M&R-fund transparency argument. |
| **Q-09** | "Southbridge was in need of a fresh start for our wastewater operations, and after undertaking a competitive procurement process, we were able to select the company that we feel is best suited for our needs." | TM-0008 — Rich Benoit, Director of Public Works, Town of Southbridge, MA | unknown | **NOT PRINTABLE.** Also carries a source-document hazard: the identical quote is reprinted on the South Huron page (hull p0079 ¶20) and **must never be attributed to SHVUA.** |
| **Q-10** | "One of the value-added qualities of Jacobs is the maintenance program. For example, the Traverse City WWTP filter membrane operation has exceeded the life expectancy because of the maintenance program Jacobs put in place." | TM-0009 — Richard Lewis, Traverse City Council Commissioner, MI | unknown | **NOT PRINTABLE.** Elected-official voice crediting maintenance for an asset-life outcome. |
| **Q-11** | "It was like attending a WEFTEC workshop in your own backyard with all the presentations that were custom made for your facility." | TM-0002 — Firooz Fath-Azam, **Former** System Manager, South Huron Valley Utility Authority, MI | unknown | **NOT PRINTABLE.** The "former" in the title weakens it; if permission comes through, the title must still be printed accurately. |
| **Q-12** | "…brainstorm ideas for the future direction of our utility that are of great value to the City and our ratepayers." | TM-0010 — Vincent Carroccia, Deputy Commissioner of Public Works, City of Wilmington, DE | unknown | **NOT PRINTABLE.** Pairs with PP-0528 for the innovation section. Do not use Q-07 and Q-12 in the same proposal. |
| **Q-13** | "What I appreciate most is the outstanding communication and transparency we have with their team, which is essential to having a positive and productive partnership." | TM-0016 — Andrew Katen, Turlock Irrigation District, CA | unknown | **NOT PRINTABLE — and doubly blocked:** the source records **no title**, and voice Rule 18 requires name, title and organization. Obtain both permission and title, or drop. |
| **Q-14** | "From design through start-up and now operations, Jacobs has provided valuable support and service to Soquel Creek Water District… We've welcomed Jacobs as an extension of our team." | TM-0015 — Melanie Mow Schumacher, General Manager, Soquel Creek Water District, CA | unknown | **NOT PRINTABLE.** Third California client voice; hold in reserve. |
| **Q-15** | "In the throes of the water crisis, only Jacobs was willing to answer our calls for assistance… they have proven to be outstanding partners, delivering on their commitments…" | TM-0005 — Ted Henifin, Interim Third Party Manager, JXN Water | unknown | **NOT PRINTABLE.** Powerful but off-theme for Richmond; reserve for the interview, not the book. |
| **Q-16** | "I want to recognize the water production and water distribution teams for their ongoing commitment to excellence…" | TM-0018 — Gilbert Davidson, Town Manager, Town of Prescott Valley, AZ | unknown | **NOT PRINTABLE.** Generic; recommend dropping. |
| **Q-17** | "…the true partnership between the County's project manager and the Jacobs management team that continued throughout the design-build phase… we are very satisfied with the results." | TM-0031 — Bruce Rawls, PE, Spokane County Utilities Director, WA | unknown | **NOT PRINTABLE.** Only found in the verbatim layer (fulton p0177); no content block. |

## 5B. Never printable as client testimony

| id | Why |
|---|---|
| TM-0011, TM-0012, TM-0013 (SmartCover — Arlington TX, South Coast Water District, New Jersey American Water) | Unattributed vendor-marketing testimonials with no named speaker. Blocked by voice Rule 18 regardless of permission. |
| TM-0014 (Tony Duffy, Clovis) | A **Jacobs** plant manager, not a client. Usable only as a clearly-labelled operator voice inside our own prose, never as a testimonial. |
| TM-0022–TM-0030, TM-0032–TM-0046 (Jacobs staff self-statements from the Fulton and OCWUT key-personnel callouts) | Self-statements by proposed staff. Usable **only** if the person is actually on the Richmond team and approves their own words for this pursuit. They are a device for the key-personnel callouts (C-053.2, C-053.4), not evidence. |
| TM-0001 (Paul Rheault attestation) | Cover-letter signatory boilerplate, not a testimonial. Reusable in 8.4.1 **only if** Paul Rheault is the confirmed Richmond signatory (D-03). |

**Quote count: 17 candidate client quotes, 0 printable today.**

---

# 6. The unmatchable fact

**Mack Mckenzie ran the Richmond Water Pollution Control Plant.** No competitor can write a sentence like it, and Veolia cannot write it either. It is the single highest-leverage fact in this pursuit and it is also the easiest one to over-reach on.

## Exact wording allowed

Verbatim source: `wiki/resumes/mack-mckenzie.md`; verbatim layer `verbatim/santamonica-swip-om-2025/pages/p0086.md` ¶2–¶3.

> **Chief Plant Operator (CPO)/Assistant General Manager | Richmond Water Pollution Control Plant | Richmond, CA.** Mack was responsible for the operation, maintenance, collections system, and laboratory at the Richmond Water Pollution Control Plant, a facility designed for 16-MGD treatment of the City's sewage. He supervised 27 employees within five departments: Operations, Maintenance, Collections, Laboratory, and Administration.

**Also available, verbatim:** duties included "fostering a safe work environment, meeting contract deliverables, maintaining client satisfaction, presenting at monthly board meetings, ensuring regulatory and lab compliance, addressing routine and emergency maintenance issues, capital planning, budget compliance, managing large capital projects, implementing efficiency programs, and developing long-term strategic plans"; and "Mack also trained operations staff in wastewater theory and practical application." Credentials: Wastewater Treatment Plant Operator Grade V, Water Treatment Operator T2, AWT3™, Distribution System Operator D2. Current standing: "Member, California State Water Resources Control Board – Wastewater Needs Assessment Advisory Group (2024 - 2027)."

## Rules for using it

1. **Past tense, always.** Mack ran that plant; he does not run it now. The 16-MGD design figure is the plant *as it was* (L-64) and conflicts with the 20 MGD in the trip reports (L-54). Never let the resume figure describe today's facility.
2. **Placement — first 100 words of Qualifications and of the Executive Summary, in a box.** In both sections the fact sits in a bordered fact box beside the opening paragraph, not buried in prose. The box carries three things and stops: the role, the plant, and the span of responsibility (operations, maintenance, collections, laboratory; 27 people; five departments). No adjectives. No claim about what it means.
3. **The prose beside the box says what it changes, once.** One sentence, in the main clause, naming a Richmond-specific consequence — the collections and laboratory scope, or the five-department span, or the monthly board reporting. Not "unique insight". Not "unmatched familiarity" (voice Rule 34 bars intensifiers without a number in the sentence).
4. **Never in the cover letter.** Three pages, eight mandated confirmations (C-040.1–C-040.8), and a disclosure requirement (C-043). The fact is wasted there and looks like a boast.
5. **Never as an implied promise of assignment.** Until D-01 is decided, no sentence may suggest Mack will hold a Richmond role. The pilot's editorial log already corrected this once ("no longer 'our proposed project manager'"); do not let it regress.
6. **Named key personnel are a separate question.** C-053.2 and C-054 require the Project Manager and the Collection System Manager to be named. Mack's Richmond history does not satisfy either requirement, and using it near the org chart will read as if it does.

## The decision this needs

**What role, if any, does Mack Mckenzie hold on the Richmond team, and is he available?** Three options, in order of value:

| Option | What the proposal can then say | Risk |
|---|---|---|
| **A — named on-site Project Manager** | Everything above, in the present tense, and C-054 is answered by the one person in the industry who has already done this job at this plant. | Highest value, highest exposure: the City may test the claim against its own institutional memory of his tenure. Requires availability, relocation, and his consent. |
| **B — named transition or start-up lead, or Operations Manager** | The fact stays past tense but attaches to a named Richmond role, which is enough to make the box mean something. | Moderate. Still requires availability. |
| **C — not on the team; the fact is stated as firm knowledge only** | The box stays, framed as Jacobs experience rather than as a person's assignment. | Lowest value. An evaluator who notices he is not proposed will read the box as decoration. If C is chosen, consider cutting the box from the Executive Summary and keeping it only in Qualifications. |

**Default recommendation: B.** It is achievable inside the schedule, it makes the fact load-bearing, and it does not stake the highest-scored section (Staffing, 30%) on one person's availability. Owner: Roy Aristizabal, with Howard Brewen. Needed by **2026-09-15** so the org chart and the two named-personnel requirements can be built around the answer.

---

# 7. Gap decisions

Every known gap, with a decision. **No placeholder reaches body text** (voice Rule 35; the pilot ran 52 tags and 14.9 brackets per 1,000 words — the winners ran zero).

| id | Gap | Decision | Detail |
|---|---|---|---|
| **G-01** | Waterbury 55% odor complaint reduction — flagged unsourced in the Directive and in `fp_03_qualifications.md` §K.17 | **RESOLVED — SOURCE FOUND** | Six placements in `verbatim/ocwut-16-26` (PPN-01). Lock the magnitude at "more than 55%" and the window at "between contract years one and two" (PPN-02) — three sources support that window; two say "within the first contract year" and one says "in the first 2 years". Register PPN-01 to PPN-04 in the registry. **Owner: Roy Aristizabal, by 2026-09-12.** |
| **G-02** | NexGen EAM / Oklahoma City experience — "not present anywhere in the Wiki" per §K.18 | **SOURCE BY 2026-09-15, Roy Aristizabal + Amy Dembinski** | It *is* present, in the OCWUT verbatim layer: Jacobs is stated as OCWUT's NexGen EAM implementation consultant, with two named SMEs (PPN-20 to PPN-22). But it comes from a live pursuit, so confirm (a) the implementation engagement is real and current, (b) it is citable in another client's proposal, and (c) whether the OCWUT O&M award has been decided. Until then the claim is **internal-only**. |
| **G-03** | Validated list of five activated-sludge plants ≥10 MGD and five collection systems ≥50 miles (C-001.3, C-001.4) | **SOURCE BY 2026-09-18, OMFS Operations** | The evidence exists but has never been assembled as a validated list. ≥10 MGD activated sludge available now: Waterbury 27 (PP-0031), Vancouver Westside 28.26 and Marine Park 16.1 (L-41), South Huron 24 (PP-0066), Gresham 20, Twin Falls 18, Pima Agua Nueva 32 (PP-0359), West Basin 40 (PP-0022), Key West 10 (PP-0194), Wilmington 168 (PP-0206), Back River 180 (PP-0205). ≥50-mile systems available now: Pembroke Pines 445 (PP-0195), Farmington 350 (PP-0196), Prescott Valley 360 (PP-0200), Waterbury ~310 (PP-0032), Fort Campbell 162.5 (PP-0197), The Villages 127 (PP-0201), West Melbourne 125 (PP-0203), Pampa 120 (PP-0202), Ontario OR 78 (PP-0199), Wilsonville 70 (PP-0198), Key West 57 (PP-0194). **Eleven each — both requirements are met with margin; the gap is validation and currency, not existence.** |
| **G-04** | Stormwater collection-system reference (C-001.5) | **WRITE AROUND — and the approach is specified here** | There is no Jacobs municipal stormwater *collection* system O&M reference in the bank (no catch basins, open channels, or hydrodynamic separators). What exists: Santa Monica SWIP treats up to 0.5 MGD of stormwater and urban runoff for beneficial reuse (PP-0027) and operates stormwater diversion structures; Vancouver operates pump-assisted stormwater injection wells; stormwater permits sit inside the standard permit-ownership statement ("Jacobs assumes full responsibility for meeting all permit requirements, including NPDES, air quality, biosolids, and stormwater permits"); CSO/MS4/IDDE/CMOM consulting sits in the full-service capability set. **Write it as capability plus method, never as a reference:** name the SWIP stormwater assets as operated Jacobs stormwater infrastructure, name the permit ownership, then answer the City's real question — that no debris baseline exists (TR) — with the year-one assessment-and-baseline approach and a capped-hours or T&M structure. **Do not claim a stormwater collection reference.** Also: the MS4 program in the Fulton verbatim belongs to **CERM**, a joint-venture partner, and is not Jacobs past performance. |
| **G-05** | Bonding capacity, surety company, notarized surety statement (C-026, C-047, C-051) | **SOURCE BY 2026-09-15, Risk + Legal** | Nothing in the content bank: no capacity figure, no surety name, no notarized-statement language, no 30-day cancellation acknowledgment. The only adjacent facts are Jacobs' 10-K disclosure of approximately **$2.0 billion in surety bonds outstanding** (`verbatim/fulton-county-2025/pages/p0431.md` ¶38, as of 2023-09-29) and "we are often required to provide performance or payment bonds or letters of credit" (`p0342.md` ¶20). The 10-K figure may support a capacity sentence but **is not a substitute for the notarized surety statement C-047 demands.** Hard requirement; a miss risks non-responsiveness (C-072). |
| **G-06** | California principal office and telephone for the contracting entity (C-044, C-040.5) | **SOURCE BY 2026-09-12, Paul Rheault + Howard Brewen** | The bank carries only the Boston address used for Hull. C-040.5 needs two answers — the office nearest Richmond, and the office from which the project will be managed. Do not print an office count (L-33 conflict). |
| **G-07** | Ten-year litigation and termination-for-cause disclosure (C-056) | **SOURCE BY 2026-09-18, Legal (General Counsel)** | Every disclosure pattern in the bank is bounded at **five** years (PP-0221). The strongest available wording is entity-specific and still five-year: "Operations Management International, Inc. (OMI, a Jacobs subsidiary) has not been terminated for cause or default or replaced as a result of having been terminated for cause under any operations contract in the last five years." Legal must extend the window to ten or supply the ten-year answer. **Do not print the five-year sentence against a ten-year question.** |
| **G-08** | Current TRIR, EMR and DART as of the proposal date, plus any OSHA citations in the last five years (C-049.3) | **SOURCE BY 2026-09-15, Corporate HSE** | The bank's figures are the Hull/Santa Monica cycle (L-24, L-25, L-27). There is **no OSHA citation history in the bank at all** — the health-and-safety half of C-049.3 is unanswered. Also refresh the five-year environmental violations table (L-29). |
| **G-09** | Bay Area offices and staff counts within a radius of Richmond | **DROP the counts; SOURCE the single nearest office** | The regional-proximity block is a template with no California figures, and L-33 is in conflict. C-040.5 asks for one office, not a footprint. Answer C-040.5 exactly and drop the rest. The reachable substitutes that *are* sourced: 12 California O&M projects able to respond within hours (PP-0539) and 2,400 regional associates (PP-0538). |
| **G-10** | Contracting entity for Richmond, its California Secretary of State standing, and the tax ID (C-044, C-050) | **SOURCE BY 2026-09-12, Legal + Corporate Secretary** | OMI as a California corporation incorporated 10/25/1980 (L-03) is the strongest available answer and the entity's home state *is* California — rewrite the Hull good-standing sentence so California standing is a single statement rather than a home-state/foreign-state pair. Tax ID 93-0784940 is single-source (L-04). |
| **G-11** | Annual project fees and current contacts for the California references and San Marcos (C-052) | **SOURCE BY 2026-09-15, account teams** | Missing fees: Clovis, West Basin, Soquel Creek, Turlock, **San Marcos**. Missing contact and contract dates: San Marcos. C-052 makes the annual fee a mandatory field — a reference without it is an incomplete submittal. |
| **G-12** | Written reference permission and contact verification for all five references, plus permission for every printed quote (C-048, C-052, C-075) | **SOURCE BY 2026-09-19, account teams** | Zero permissions on file across 46 testimonials and 10 reference sheets. The City reserves the right to contact any client named (C-075), so an unverified contact is a live risk, not a formality. Sequence: permission first, then contact currency, then quote clearance. |
| **G-13** | Signatories authorized to negotiate and sign (C-050, C-016, C-042) | **SOURCE BY 2026-09-19, Legal + Corporate Secretary** | No names in the bank. The governance chain that would supply them: Bob Pragada → Patrick Hill → Greg Fischer → Paul Rheault (VP Operations, West) → Howard Brewen (California O&M Director). The cover letter must be signed by an authorized official (C-042). |
| **G-14** | Waterbury wet-weather flow figure | **WRITE AROUND unless the account team confirms** | Three values, two directions (L-39). If unconfirmed, write "wet-weather flows well above design capacity" and drop the number. |
| **G-15** | Soquel Creek and Turlock capacities | **WRITE AROUND** | PP-0358 (1.3 / 1.7 / 2 MGD) and PP-0382 (0.75 / 0.8 MGD) are unresolved and neither project is in the reference five. Use the outcome figures (PP-0476, PP-0411) and omit the capacities. |
| **G-16** | South Huron interceptor mileage and annual fee | **DROP the reference** | Two unresolved conflicts (L-49) and no usable quote. Its workforce-transition value is carried better by Vancouver (PPN-15, PPN-16). |
| **G-17** | "Communities of Practice" as a named Jacobs term | **DROP the term; use the sourced equivalents** | The phrase does not appear in the bank. What does: the four named reach-back groups (Regional Process Specialists, Regional Maintenance Specialists, Compliance & Reporting Group, Regional Management), the Annual Innovation Workshop, and the named SME benches. The trip reports also name individuals — Bill Desing, Bill McMillan, Jennifer Baldwin, Courtney Kennedy — who can be named directly. |
| **G-18** | Whether reach-back services sit in the base fee or are separately authorized under the Richmond fee structure (C-049.2) | **SOURCE BY 2026-09-19, Roy Aristizabal + pricing** | The bank's sentence — "at no additional cost to our clients" — is a strong differentiator and a commercial commitment. C-049.2 asks the question explicitly, and Richmond's $2M M&R fund and $5,000 approval threshold (L-59) make the boundary consequential. Answer it with a line, not a hedge. |
| **G-19** | Vancouver contract start year | **SOURCE BY 2026-09-15, account team** | Four values (L-42). Print 2016 for the transition; never print 2015 beside it. |

**Gap-decision count: 19 — 1 resolved, 12 source-by-date, 4 write-around, 2 drop.**

---

# 8. Page and device budget per section

**Cap: 40 narrative pages, 12-point type, PDF (C-037).** Bios, required forms, financials and supplemental material are excluded. The fee proposal is a separate submission. Format non-compliance is a disqualification risk (C-039), so this budget is a hard allocation, not a target.

| § | Section | Pages | Tables max | Stat rows | Fact boxes | Pull quotes | Figures | Callouts | Detail sent to appendix |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 8.4.1 | Cover Letter | **3** (RFP max) | 0 | 0 | 0 | 0 | 0 | 0 | Nothing. Eight mandated confirmations (C-040.1–.8), the C-043 communications disclosure, the C-076 draft-agreement statement, the 180-day validity (C-045), the single point of contact (C-040.7), and a signature (C-042). No devices. |
| 8.4.2 | Executive Summary | **4** | 2 | 4 | 2 | **1** | 2 | 3 | Value-add pricing detail. Carries the **one** value wheel and the **one** Traditional-vs-Jacobs table for the whole proposal. One Mack Mckenzie fact box in the first 100 words. Closer: ST-0005. |
| 8.4.3 | Qualifications | **8** | 6 | 3 | 3 | **1** | 2 | 2 | Extended reference write-ups, awards lists, financial statements, the notarized surety statement, the org chart's detail layers, 10-K excerpts. **The six mandated reference fields (C-052) stay in the body** — see the decision note below. One Mack fact box in the first 100 words. Closer: ST-0013. |
| 8.4.4 | Staffing and Management Plan | **10** | 5 | 3 | 4 | **1** | 3 | 4 | All resumes and bios (excluded from the count anyway), certification schedules, the subcontractor register detail, shift rosters. Carries the **one** org chart for the proposal (C-053.1). |
| 8.4.5 | Technical Approach | **14** | 8 | 6 | 6 | **1** | 6 | 6 | Deliverable templates, the CMMS configuration detail, sampling schedules, the transition schedule's task-level Gantt, the odor study protocol. Split as: Operational Approach 4 · Maintenance Plan 3 · Transition Plan 2.5 · Innovation and green 2 · Specific Deliverables 2.5. |
| 8.4.6 | Required Forms | **0** | — | — | — | — | — | — | Entirely in the Attachment D forms: Sanctuary City Compliance Statement (C-030), LLC Disclosure Affidavit (C-031). Excluded from the page count. |
| 8.4.7 | Fee Proposal | **0** narrative pages here | — | — | — | — | — | — | Separate submission. Allow **1 page** of fee-rationale narrative *inside* the fee submission for the stormwater standalone price (C-058), the energy gain-share position (C-061), and the M&R accounting commitment (C-060). |
| | **Total** | **39** | | | | | | | 1 page of float held for the Executive Summary or Technical Approach |

## Device rules that apply everywhere

- **Stat callout:** number + comparator + consequence, 8–20 words, and the figure must also appear in prose. **≤1 per page.**
- **Fact box:** verbless triad of outcomes, 15–30 words, no tool names, the City named. **1 per subsection, closing it.**
- **Pull quote:** ≤35 words with name, title and organization. **≤1 per major section — and 0 today**, because no quote has permission (Section 5).
- **Commitment callout:** "[named person or role] will [verb] [object] [cadence]" plus a number or dollar value. **≤2 per section.**
- **Table share ≤0.35 of words, aim ≤0.25.** The five mandated reference tables and the C-001 crosswalk raise this legitimately in 8.4.3; nothing else may.
- **Rightmost column of every multi-column proof exhibit names the City's outcome** ("Value to the City"), and every exhibit is pointed to from a prose sentence in bold.
- **One of each, proposal-wide:** org chart (8.4.4), Traditional-vs-Jacobs table (8.4.2), value wheel (8.4.2).

## The one open budget decision

**D-09 — do the five reference detail tables live in the body or the appendix?** C-048 and C-052 put them in §8.4.3; appendices are excluded from the 40-page count, so moving them buys roughly 1.5 pages. **Recommendation: keep the six mandated fields in the body as one compact five-row table (name/location, contact, services, processes and size, years, annual fee) and move the narrative write-ups, awards and photographs to the appendix, with a bold pointer sentence from the body.** Compliance beats page economy when C-039 allows disqualification for mis-organized content.

---

# 9. Win-theme evidence map

The Directive names seven themes. **Themes 1 and 6 are the same theme** (transparency / real partner), and the voice guide caps a proposal at three to five themes each repeated at least three times with at least one heading appearance (Rule 26). **Recommendation: merge 1 and 6, and carry five.** Marked below.

| # | Theme | 8.4.1 Cover Letter | 8.4.2 Executive Summary | 8.4.3 Qualifications | 8.4.4 Staffing | 8.4.5 Technical Approach |
|---|---|---|---|---|---|---|
| **1 + 6** | **Real partner, transparency** *(merged)* | One clause naming the monthly M&R reconciliation commitment. Device: **plain sentence** | PP-0042, PPN-06, ST-0005; the M&R and data-access commitments (L-59). Device: **Traditional-vs-Jacobs table** + **commitment callout** | PP-0177 (98% renewal), PP-0537 (zero terminations), SEC-filings transparency, single-entity guarantor. Device: **stat row** | PP-0623, PP-0624, PPN-16, PP-0339/PP-0628/PP-0629. Device: **fact box** | PPN-18, PP-0525–PP-0527 (report cadence), the compliance dashboard. Device: **commitment callout** ×2 |
| **2** | **Four-layer odor and H₂S control** | Not carried | PPN-01 + PPN-02 + PPN-04. Device: **stat callout** | Waterbury and Clovis odor guarantees in the reference narratives. Device: **table row** | Named odor SMEs from the trip reports (Bill Desing). Device: **bullet** | PPN-03 → PPN-01 → PPN-04 as the before/mechanism/after; PPN-05 (biotrickling, no chemical cost); ST-0008 sidebar; PP-0151; PP-0309 (1-hour response); WATS modelling and the sensor-to-dispersion early-warning system. Device: **case-study callout + figure** |
| **3** | **IPP expertise** | Not carried | One clause | Named IPP programs: Vancouver (`ocwut p0171` ¶6), Bixby (`p0165` ¶5), South Huron, Westerly, Traverse City — **five named programs**. Device: **table column** | The IPP role in the org chart. Device: **org-chart node** | Method plus the five named programs. Device: **bullet list** |
| **4** | **NexGen EAM depth** | Not carried | One clause, **conditional on G-02** | Not carried | PPN-21, PPN-22 (named SMEs). Device: **bench table row** — *conditional on G-02* | PPN-20 as the mechanism against C-004.3's 120-day CMMS deliverable; PP-0520 (1,000,000 assets assessed); PP-0331/PP-0342 (90-day baseline). Device: **commitment callout** — *conditional on G-02* |
| **5** | **Successful comparable projects** | Brief history (C-040.4). Device: **plain sentence** | ST-0005 closer. Device: **stat row** | The five references, the C-001 crosswalk, L-13 to L-18. Device: **crosswalk table** + **California footprint map** | STN-01 (Vancouver transition). Device: **fact box** | STN-02 (San Marcos), ST-0001 (Westerly), PP-0318–PP-0321 (Waterbury emergency). Device: **embedded case studies** |
| **7** | **Compliance leadership, belt-and-suspenders** | Statement of intent (C-040.2). Device: **plain sentence** | L-22 (99.8% NPDES, 20 years) with the comparator in-sentence. Device: **stat callout** | C-049.4 five-layer approach; ST-0006 (enforcement resolved); L-29 disclosure with the four-move close. Device: **layered figure** | Certifications and staffing to permit requirements (C-053.6, C-080). Device: **table** | The controlled obligation register; Baykeeper and CDO obligation tracking; PPN-06; PP-0531 (five compliance tools). Device: **register table** |

## Themes with thin or blocked evidence

| Theme | State | Action |
|---|---|---|
| **4 — NexGen EAM depth** | **Sourceable, not yet cleared.** PPN-20 to PPN-22 come from a live pursuit's verbatim layer. | **G-02.** If it does not clear by 2026-09-15, the theme must be rewritten as "CMMS and GIS integration discipline" carried by PP-0520, PP-0331 and the Vancouver/Waterbury CMMS records — and the City's NexGen mandate (C-004.3) answered as a commitment rather than as experience. |
| **3 — IPP expertise** | **Named programs exist; no IPP outcome exists.** Five programs are named across the bank; not one carries a measured result (a pretreatment enforcement resolved, a loading reduction, a surcharge recovered). | **needs source** — ask the account teams for one quantified IPP outcome by 2026-09-19. Without it the theme is a capability list, and capability lists do not score. |
| **2 — odor** | **Now the best-evidenced theme in the pursuit** — but every proof is client-named and unpermissioned. | G-12. |
| **stormwater** *(not a Directive theme, but the RFP's newest scope and the City's live enforcement exposure)* | **No reference, no outcome, no baseline.** | **needs source / write around per G-04.** Consider promoting it to a sixth theme framed as *"a stormwater baseline the City has never had"* — the honest position is stronger than a borrowed reference, and it converts the absence of a baseline (TR) into the first-year deliverable (C-004.6, C-004.7). |

---

# 10. Concession policy

Every required negative follows the four-move pattern in one paragraph: **(a) scale context, (b) bounding, (c) resolution, (d) no-impact close.** Nothing negative is volunteered beyond what the RFP asks (voice Rule 30).

## What may be admitted, and how

| Item | Required by | How it is written |
|---|---|---|
| **Environmental fines, last five years** — Ontario, OR $660 and Roseburg, OR $1,628, both expired herbicide applicator licences, both renewed | C-049.3 | Four moves in one paragraph: "Jacobs may, from time to time, have minor environmental violations, as customarily occurs in the ordinary course of business" → "administrative in nature" → the licences were renewed, in coordination with regulators → "with no impact to our ability to deliver services." Table with a **Resolution column beside every row.** |
| **West Basin tenure began in 2025** | Honesty; the reference is in the five | Voice Rule 31 — one sentence, weakness in the subordinate clause, answer in the main clause: *"While Jacobs assumed full responsibility for the Edward C. Little Water Recycling Facility in September 2025, the transition of a 40-MGD, nine-train facility from a contract operator of more than twenty years is the transition Richmond is asking us to describe."* One sentence. No dwelling. |
| **Litigation and terminations** | C-056 | Scale framing, materiality, and the SEC pointer, in the entity's own name. **Ten-year window required** — do not ship the five-year sentence (G-07). |
| **Reference projects outside California** | Implicit in C-001.2 | One sentence on the pattern of voice Rule 31: while three of the five references are outside California, they operate under comparable regulatory frameworks and at the plant and collection-system scale Richmond requires — followed immediately by the California record (L-31, L-32, L-35). |
| **No stormwater collection-system reference** | C-001.5 | **Never admitted as an absence.** Written forward per G-04: the stormwater assets Jacobs operates, the permit responsibility Jacobs assumes, and the year-one assessment that produces the baseline the City does not have. |

## What must never be volunteered

1. **The 13-row self-disclosed permit-excursion table** (PP-0511, Clovis / Crescent City / Gilroy / Red Bluff). C-049.3 asks for *violations*, not for a voluntary excursion log. Printing it is a volunteered negative exhibit — a hard gate failure — and it directly contradicts the Clovis "guarantees met consistently and reliably" line in the same proposal. **Suppress it, and reconcile the Clovis wording before using the guarantee sentence** (ST-0016 caution).
2. **Any self-disclaimer.** "We make no claim yet about long-run results", "it is too early", "contacts and fees are as last confirmed", "this section is here because". Zero occurrences. The pilot ran two.
3. **Any statement of a Jacobs internal conflict.** Competing figures are resolved in this sheet, never in a sentence. If a lock is unavailable, the prose states the precision both sources support ("more than 300 miles", "at least 98%") and the conflict is logged below the draft-notes rule, which is stripped before layout.
4. **The incumbent's name, and any swipe at ownership models.** Say "the previous contract operator", "the previous operating approach", "qualified incumbent employees". The pilot named the incumbent six times; both winning proposals named it zero. The private-equity contrast sentence in the bank is **barred** despite being available.
5. **Any sentence attributing a shortcoming to the City, its staff, or its program.** The trip reports catalogue housekeeping, deferred maintenance, unlabeled drums, inconsistent LOTO, an open pit secured by a single wire, and end-of-life PLCs. **Every one of those becomes an aspiration, not an accusation**: what the City is seeking, what the first ninety days deliver, what the condition assessment produces. Never "what the City has lacked".
6. **The 29–32 FTE estimate** (L-63) and any other internal pursuit estimate, until Staffing converts it into a committed org chart.
7. **A guarantee of no SSOs.** The trip reports set the position explicitly: Jacobs commits to cleaning and CCTV on a stated frequency (25%/yr, 10%/yr, 10%/yr — L-58) and to response times, not to an SSO-free system. Any sentence implying otherwise creates liquidated-damages exposure under C-005.2.
8. **Waterbury's "<54 MGD"**, Soquel's capacity, Turlock's capacity, Auburn's tenure, and any other unresolved figure — write around them (G-14, G-15, L-36).

---

# 11. Decisions table

One line per decision, with a default recommendation. Owners are as named in `pursuit.md` unless stated.

| id | Decision | Default recommendation | Owner | Needed by |
|---|---|---|---|---|
| **D-01** | Mack Mckenzie's role and availability | **Option B** — named transition or start-up lead, or Operations Manager. Keeps the unmatchable fact load-bearing without staking the 30%-weighted Staffing section on one person | Roy Aristizabal + Howard Brewen | 2026-09-15 |
| **D-02** | Named on-site Project Manager and Collection System Manager (C-054 — currently PLACEHOLDER by decision 2026-09-05) | Name both. C-054 is a hard requirement and C-087 gives the City approval rights over PM changes; an unnamed PM in a 30%-weighted section is a scoring loss, not a risk deferral. Pair with the relocation, stay-pay and key-personnel LD offers already identified in the trip reports | Roy Aristizabal | **2026-09-12** |
| **D-03** | Contracting entity and signatory | **OMI, a California corporation since 10/25/1980**, with Paul Rheault or Howard Brewen signing. It is the only structure that makes "a California corporation" a fact rather than a framing | Legal + Corporate Secretary | 2026-09-19 |
| **D-04** | Which reference occupies slot 2 | **San Marcos**, on the strength of process identity and four quantified chemical/energy outcomes — conditional on G-11 producing a contact, a fee and contract dates by 2026-09-15. Fallback: **Southbridge (B1)** | Roy Aristizabal | 2026-09-15 |
| **D-05** | The Waterbury quote attribution (Q-01) | **Ask the account team which is correct and print only that.** If it cannot be resolved by 2026-09-19, **drop the quote** and carry Waterbury on PPN-06, PP-0042 and PPN-01 alone — the numbers are stronger than the quote | Kevin Dahl / account team | 2026-09-19 |
| **D-06** | Merge win themes 1 and 6 | **Merge.** Carry five themes, each named once and repeated at least three times with one heading appearance | Roy Aristizabal | 2026-09-12 |
| **D-07** | Promote stormwater to a named theme | **Yes** — "a stormwater baseline the City has never had". It converts the pursuit's weakest evidence position into a first-year deliverable and answers the 2025 CDO directly | Roy Aristizabal | 2026-09-12 |
| **D-08** | Whether to cite the NexGen/OKC engagement (G-02) | **Cite it if it clears by 2026-09-15**; otherwise rewrite theme 4 as CMMS/GIS discipline and answer C-004.3 as a commitment | Roy Aristizabal + Amy Dembinski | 2026-09-15 |
| **D-09** | Reference detail: body or appendix | **Six mandated fields in the body as one compact table; narratives and awards to the appendix** | Proposal manager | 2026-09-19 |
| **D-10** | Stormwater commercial structure | **T&M or capped hours in year one, plus a funded assessment and baseline cleaning** — three trip reports independently concluded the City cannot scope the level of effort either. Also answers C-058's standalone stormwater price | Roy Aristizabal + pricing | 2026-09-22 |
| **D-11** | Transition and corrective-maintenance budget | **Propose a separate first-6-to-12-month corrective/backlog budget outside the $2M M&R fund**, with regional maintenance as reimbursable T&M. Multiple trip reports judge M&R exceedance likely in the early years | Pricing | 2026-09-22 |
| **D-12** | Reach-back cost boundary (C-049.2, G-18) | **State the boundary in one sentence**: named reach-back groups and technical support inside the base fee; capital design and construction separately authorized | Roy Aristizabal + pricing | 2026-09-19 |
| **D-13** | Print the 13-row self-disclosure table | **No.** Not required by C-049.3, contradicts the Clovis guarantee line, and fails the volunteered-negative gate | Proposal manager | 2026-09-12 |
| **D-14** | Which NPDES/compliance figure appears (L-22 vs L-23) | **99.8% NPDES over 20 years only.** Never both in one document | OMFS Compliance | 2026-09-15 |
| **D-15** | Whether to print corporate revenue at all (L-08) | **No.** The RFP asks for O&M revenue; L-05 and L-06 answer it and avoid a live three-way conflict | Finance | 2026-09-15 |
| **D-16** | Register PPN-01 to PPN-22 and catalogue STN-01, STN-02 | **Yes, before any writer opens a section.** Twenty-two facts and two stories are currently traceable only to this sheet | Content-bank owner | 2026-09-12 |
| **D-17** | Recompute every tenure and duration to 2026-09-29 | **Yes.** The California footprint tenures, Auburn, Key West, Waterbury, Traverse City and Clovis durations are all frozen at earlier cycles | Account teams | 2026-09-18 |
| **D-18** | Interview team composition (C-018 — key personnel and leadership expected to attend, 2026-10-28) | **Named PM, named Collection System Manager, Mack Mckenzie, Howard Brewen, Roy Aristizabal.** Decide with D-01 and D-02 so the book and the room match | Roy Aristizabal | 2026-09-15 |

---

## Draft notes — not for body text

- Twenty-two facts in this sheet (`PPN-01` to `PPN-22`) and two stories (`STN-01`, `STN-02`) are sourced to verbatim pages but are **not in the registry or the catalog**. D-16 fixes that.
- The registry records `approved_for_external_use: pending` and no owner for all 696 ids; the testimonial inventory records `permission: unknown` for all 46. Section 2's "approved" column reflects prior publication in a submitted proposal, not a recorded approval.
- `fulton-county-2025` content is voiced as **JC Solutions, a Jacobs/CERM joint venture.** Facts sourced there that belong to CERM — notably the Lithonia MS4 program — are **not Jacobs past performance** and must not be presented as such.
- `ocwut-16-26` is a submitted proposal whose outcome is not recorded in the bank. Facts about *other* Jacobs projects quoted inside it (Waterbury, Vancouver, San Marcos) are past-performance statements and are treated as such here; statements about OCWUT's own facilities are bid promises and are not used.
