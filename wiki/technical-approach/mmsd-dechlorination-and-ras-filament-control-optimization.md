---
title: Dechlorination and RAS Chlorination Optimization — Matching Dose to Lagging Data
category: technical-approach
block-type: prose
tags: [chemical-management, process-optimization, data-analytics, digital-tools, process-control, wastewater-treatment, technical-approach, cost-savings, continuous-improvement]
source: mmsd-om-2028
source-section: "IV.A.2. Approach to Operations of Facilities"
source-pages: [69, 70]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0069.md#¶8", "verbatim/mmsd-om-2028/pages/p0070.md#¶9"]
pursuit-type: [wwtp-om, water-treatment, multi-facility]
client-type: authority
client-size: "Two large water reclamation facilities + biosolids production / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [energy-chemical-efficiency, digital-tools, innovation-value-add, compliance-leadership]
proof-point-ids: [PP-2181, PP-2190]
testimonial-ids: []
story-ids: [ST-0056]
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; WDNR
quality: Two compact use cases that show the method generalizes — dechlorination dose follows the upstream chlorine dose, and filament control can be predicted from SRT, flow, and season when microscopy lags. Each carries its own quantified savings and its own delivery mechanism (the same operator push notification).
reuse-notes: Savings values are client-data-derived; re-run the analysis per pursuit. The transferable argument is the treatment of lagging indicators (residual as an after-the-fact surrogate, microscopy as delayed filament data) as a reason to predict from historical conditions instead.
---

# Dechlorination and RAS Chlorination Optimization — Matching Dose to Lagging Data

**Sodium bisulfite for disinfection.** Dechlorination of residual chlorine is applied before final effluent discharge to achieve essentially a 0 mg/L concentration. The dosage rate is almost entirely dependent on the excess sodium hypochlorite applied for bacteria kill, so too much chlorine results in too much bisulfite consumption. Using the same methods discussed above, **we can match the sodium bisulfite dosages very accurately, and predictively, resulting in an additional $100K per year versus baseline savings, at current chemical prices**. This is another very common use case, and "push" advisory notices to operators are done through the same message as the sodium hypochlorite dosage notices.

**Sodium hypochlorite for filament control.** The second water reclamation facility uses RAS chlorination to control filamentous bacterial growth because filaments tend to reduce settling efficiency in the secondary clarifiers, which may ultimately impact effluent water quality and regulatory compliance. Because real time information about filament populations is not available, we can use data science methods to look at what has historically driven high filament populations at the facility—SRT, flows, time of year, etc. to guide when and at what dose RAS chlorination would be most cost effective and yield the best settling performance. Then we watch in real time for those conditions and make the matching dosage recommendations. Plus, we can continue to refine the analysis with ongoing microscopy as it becomes available to build even more accuracy into the predictions. The concept is very much like for disinfection, where real time bacteria data is not available, and residual levels are at best an after-the-fact surrogate for bacteria kill. Here, we have lagging filament data but have tremendous historical records of what is known to work best instead. **Our pricing includes savings of about 14%, or $60K per year at current chemical prices, for this use case.**

## Reuse guidance

Universal: the dependency argument for dechlorination — bisulfite demand is created upstream, so optimizing hypochlorite pays twice — and the explanation of predicting from drivers when the measurement itself lags (filaments, bacteria). Both paragraphs also model the discipline of delivering multiple use cases through one operator notification rather than adding screens.

Pursuit-specific: the dollar and percentage savings, and the statement that savings are included in pricing, which must be confirmed with the cost lead. Pairs with the four pillars block and the sodium hypochlorite disinfection block, which carries the method and the adoption evidence. Read `verbatim/mmsd-om-2028/pages/p0069.md#¶8` and `p0070.md#¶9`–`#¶10`.
