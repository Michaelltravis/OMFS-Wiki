---
title: Sodium Hypochlorite Disinfection Dosage Optimization — Predictive Dosing Use Case
category: technical-approach
block-type: prose
tags: [chemical-management, process-optimization, data-analytics, digital-tools, process-control, sampling-monitoring, technical-approach, cost-savings, proof-point, case-study]
source: mmsd-om-2028
source-section: "IV.A.2. Approach to Operations of Facilities"
source-pages: [69, 70]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0069.md#¶13"]
pursuit-type: [wwtp-om, water-treatment, water-reuse, multi-facility]
client-type: authority
client-size: "Two large water reclamation facilities + biosolids production / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [energy-chemical-efficiency, digital-tools, innovation-value-add, incumbent-displacement, partner-transparency]
proof-point-ids: [PP-2180, PP-2182, PP-2183, PP-2184, PP-2185, PP-2186, PP-2187, PP-2188, PP-2189, PP-2191]
testimonial-ids: []
story-ids: [ST-0040, ST-0056]
status: preferred
house-favorite: true
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; WDNR
quality: The flagship digital use case — it explains why the savings exist (lab lag time drives "set it and forget it" dosing), pre-empts disbelief in the percentage, backs it with a 5-MGD-to-340+-MGD track record and a 40% result after taking over from another provider, and closes the loop with operator adoption rates.
reuse-notes: Percentages and dollar values are outputs of a client-specific data analysis over two years of lab and SCADA records; never carry them to another pursuit. Everything explaining the mechanism, the track record range, and the adoption evidence is reusable.
---

# Sodium Hypochlorite Disinfection Dosage Optimization — Predictive Dosing Use Case

**Specific chemical optimizations for the [CLIENT] facilities include:**

**Sodium hypochlorite for disinfection.** Both water reclamation facilities use a significant amount of this chemical to ensure bacteria deactivation of the final effluent. We understand that UV upgrades are being planned and the usage profile for hypo will be changing. However, **our analysis of 2 years of laboratory and SCADA Historian records reveals substantial savings opportunities for the current configuration, including over 30% at the primary facility, and about 20% for the second facility.** While these savings values may appear unrealistic, these are *typical* savings for this particular use case. Until now, operators have lacked predictive insights into optimal dosage rates and have relied on overly conservative dosage rates to ensure bacterial kill. This is especially true where bacteria testing involves days of lag time before laboratory results are available. In most instances, we see operators resorting to a "set it and forget it" chemical dosing approach. By contrast, we are leveraging the vast history of what dosage rates always achieved the needed fecal coliform deactivation under a wide range of operating conditions, and we can watch for those same conditions (flow, temperature, pH, time of year, etc.), as shown in **Exhibit IV-20**, to recommend the right dosage rate to apply ahead of time for operators. **Exhibit IV-21** highlights significant sodium hypochlorite savings for [CLIENT], a regional sewerage district operating two large water reclamation facilities, that could have been achieved over the past 3 years while ensuring permit and contract compliance.

We have applied this use case for many plants, from small 5-MGD facilities up to major 340+ MGD capacity plants, and the results typically fall in this 20-30% range. A recent exception is the West Basin, CA, reuse facility. After Jacobs assumed operations from another provider, we achieved more than 40% in savings—demonstrating the value of shifting away from the "set it and forget it" approach. Much of the savings resulted from giving operators visibility into their historical best practices, highlighting the importance of disciplined monitoring, transparency, and continuous improvement.

**Total savings for these two use cases (one for each water reclamation facility) is $525K or more per year versus baseline, at current chemical prices**.

The frequency and timing of recommendations is up to the operations team but varies from three to eight notifications per day. **Exhibit IV-22** provides adoption rates of dosage recommendations. Operator acceptance rate exceeds 80% at other facilities we operate, after implementing optimization push notifications.

**EXHIBIT IV-20. SCATTER PLOT FOR RAS CHLORINATION VS. FILAMENTS** (graphic asset `300_007CAM_2`) — In our review of [CLIENT]'s data, we found clear instances when chlorination wasn't necessary.

**EXHIBIT IV-21. SODIUM HYPOCHLORITE SAVINGS** — Sodium hypochlorite saving opportunities that could have been achieved over the past 3 years with predictive insights from our digital tools (actual hypo flow, average, quant_25, savings, expense, plotted by date).

**EXHIBIT IV-22. ADOPTION RATES OF DOSAGE RECOMMENDATIONS** (graphic asset `299_007CAM_4`) — High utilization rate for adoption of optimization push notifications.

## Reuse guidance

Universal and strong: the causal explanation (lab lag time → conservative dosing → recoverable margin), the pre-emptive "these values may appear unrealistic" move, the scale range that proves the use case is not a small-plant trick, the West Basin takeover result as evidence the savings are specifically available when displacing another operator, and the adoption-rate evidence that answers "will operators actually use it?"

Pursuit-specific: the percentage and dollar figures, the two-year analysis window, and the planned UV upgrade caveat — note how the passage acknowledges the upgrade will change the picture rather than ignoring it. Pairs with the four pillars block (read it first), the dechlorination and filament control block, and the phosphorus block. Read `verbatim/mmsd-om-2028/pages/p0069.md` and `p0070.md` for the full passage and exhibit captions.
