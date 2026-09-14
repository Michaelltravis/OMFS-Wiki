---
title: Metal Salt Optimization for Phosphorus Control — Injection Point Change Plus Machine Learning
category: technical-approach
block-type: prose
tags: [chemical-management, process-optimization, process-modeling, data-analytics, digital-tools, wastewater-treatment, permit-compliance, technical-approach, cost-savings, instrumentation-controls]
source: mmsd-om-2028
source-section: "IV.A.2. Approach to Operations of Facilities"
source-pages: [71]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0071.md#¶7"]
pursuit-type: [wwtp-om, multi-facility]
client-type: authority
client-size: "Two large water reclamation facilities + biosolids production / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [energy-chemical-efficiency, compliance-leadership, digital-tools, innovation-value-add]
proof-point-ids: [PP-2192, PP-2193, PP-2194]
testimonial-ids: []
story-ids: [ST-0056]
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:24.sswrf-digester-gas-may-meet-all-facility-s-power-needs
section-order: 27
section-path: IV. Approach Summary › IV.A. Approach to Management, Operations, PM, and CM › IV.A.2. Approach to Operations of Facilities › 03 STRATEGIC AND CONTINUOUS IMPROVEMENT › 2.2.2. JIWRF and SSWRF Wet Processes - Focus Area › SSWRF digester gas may meet all facility’s power needs
doc-order: 127
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; WDNR
quality: The clearest passive-plus-active optimization example in the section — a physical second injection point for molar-ratio, mixing, and residence-time efficiency, plus a machine-learning layer trained on the client's own data — with a stated savings figure, a redundancy benefit, and an observant detail (an installed analyzer sitting idle) that proves site-level attention.
reuse-notes: Injection-point geometry, dosage savings, and the idle instrument observation are pursuit-specific and only credible where a site visit confirmed them. Keep the passive/active structure and the closing "future opportunities" paragraph, which sets expectations without over-promising unpriced savings.
---

# Metal Salt Optimization for Phosphorus Control — Injection Point Change Plus Machine Learning

**Ferric chloride (oxidized pickle liquor) for total phosphorus control.** Another efficiency opportunity at the second water reclamation facility focuses on ferric (or ferrous) chloride injection ahead of the primary clarifiers. Jacobs is aware that chemicals are currently added primarily to reduce organic loading to the secondary treatment process. As CEPT is improved at the primaries via well-mixed polymer addition (a process that Jacobs has significant experience operating) and primary BOD capture increases and stabilizes, phosphorus removal will become more of a driver for metal salt addition. Jacobs' process simulation analysis shows that metal salt dosage is required to achieve the contractual performance standards and total phosphorus permit limits. There are two optimization methods planned: a passive change to the injection points for greater mixing and dosage efficiency, and an active management step based on data science and machine learning methods. Currently, ferric chloride is injected at each of the 48" diameter lines to each bank of primary clarifiers. We recommend the addition of a second dosage point at the effluent mixed liquor channel feeding the secondary clarifiers before a new mechanical mixer. **The benefit of this is more efficient chemical phosphorus removal (20% savings, $600K / year).** This is due to more efficient metal salt to phosphorus molar ratio, improved mixing intensity, and longer residence time. Secondary dosage will provide a backup system should the facility implement EBPR and may improve settleability. This improvement will be supported by our data science tools, as illustrated in **Exhibit IV-23**, to monitor against baseline performance and relevant water quality targets. Some additional optimization may be possible once an operating history with the multiple injection points has been established.

We noted that a Hach Phosphax instrument to measure phosphorus content was installed but was curiously not running. We plan on using this instrument and others to further refine our machine learning approach, which may also yield more savings.

**Future chemical optimization opportunities.** While the use cases above **conservatively total over $1M per year in savings (almost double this amount is a distinct possibility)**, there are other use cases that we'll evaluate in the future. While insufficient data is available currently to price in the savings, things like odor control chemicals and dewatering polymer are potential targets that we have successfully optimized elsewhere.

*Existing ferric injection ahead of the primary clarifier. Jacobs recommends adding an injection point downstream.*

**EXHIBIT IV-23. EFFLUENT PHOSPHORUS MODEL TRAINING AND TESTING** — Given the ample data we had from [CLIENT], a regional sewerage district operating two large water reclamation facilities, the model training and testing aligned extremely well, which gives us high confidence in their predictability.

## Reuse guidance

Universal: the passive-plus-active pairing (move the chemistry, then manage the dose), the reasons a second injection point works (molar ratio, mixing intensity, residence time), the redundancy argument for a future EBPR conversion, and the closing paragraph that totals the priced use cases, hints at upside honestly, and names the unpriced candidates (odor control chemicals, dewatering polymer) without claiming them.

Pursuit-specific: pipe sizes, the recommended dosage location, the savings figures, the CEPT context, and the idle Phosphax instrument. The model training exhibit caption is only usable where the client actually supplied enough data to train on. Pairs with the four pillars block and the other chemical use-case blocks from this source. Read `verbatim/mmsd-om-2028/pages/p0071.md` for the full passage.
