---
title: Energy Demand Management — Predictive Advisories Without Capital Investment
category: technical-approach
block-type: prose
tags: [energy-management, data-analytics, digital-tools, process-control, operations-management, technical-approach, cost-savings, no-cost-value-add, continuous-improvement]
source: mmsd-om-2028
source-section: "IV.A.2. Approach to Operations of Facilities"
source-pages: [67]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0067.md#¶15"]
pursuit-type: [wwtp-om, solids, multi-facility]
client-type: authority
client-size: "Two large water reclamation facilities + biosolids production / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [energy-chemical-efficiency, digital-tools, innovation-value-add, partner-transparency, compliance-leadership]
proof-point-ids: [PP-2173, PP-2174, PP-2175]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: true
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:24.sswrf-digester-gas-may-meet-all-facility-s-power-needs
section-order: 23
section-path: IV. Approach Summary › IV.A. Approach to Management, Operations, PM, and CM › IV.A.2. Approach to Operations of Facilities › 03 STRATEGIC AND CONTINUOUS IMPROVEMENT › 2.2.2. JIWRF and SSWRF Wet Processes - Focus Area › SSWRF digester gas may meet all facility’s power needs
doc-order: 123
volatility: evergreen
review-due: 2029-01-29
freshness-flags: []
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; WDNR
quality: The single best demand-charge passage in the bank — it separates kWh from kW, names the actual peak driver, quantifies the opportunity (10% of demand charges, up to $600K/year), states that implementation needs no capital, and answers the autonomy objection head-on with "driving directions to licensed operators."
reuse-notes: Re-derive the 10% and $600K figures from the target client's own billing and SCADA history before use; they are analysis outputs, not standard claims. Keep the key-person-risk argument and the operator-authority language verbatim — both defuse predictable evaluator objections.
---

# Energy Demand Management — Predictive Advisories Without Capital Investment

**Energy Demand Management.** Power bills contain two dominant cost components: energy usage measured in kWhrs, and energy demand measured in kW. Both are worth investigating to conserve power, but as noted earlier, the biggest energy usage at both sites (aeration blowers) must be carefully managed to ensure the contractual effluent performance targets are met. The highest peak demands at the primary water reclamation facility are due to the inline tunnel pumps. **Jacobs' analysis shows that energy demand can be managed more efficiently, with up to a 10% improvement in demand-related charges at both plants, valued at up to $600K per year in savings.** These savings can be achieved by providing predictive guidance to operations staff on the optimal times to operate major energy-intensive equipment such as the inline tunnel pumps.

[CLIENT], a regional sewerage district operating two large water reclamation facilities, already manages this with good results, but **our analysis of historical records shows opportunities for further improvement.** Implementation is simple and requires no capital investment. Operators and managers would receive advisory push-notifications that indicate when adjusting major equipment would reduce demand charges, while staying within regulatory and operational limits. Recommendations account for rainfall, tunnel storage volumes, current and projected loading, and other plant conditions. Because these decisions rely on large amounts of data and many system variables, they are well-suited to Jacobs' data-science tools. **This approach reduces operational risk by supporting a complex decision process currently handled by only a few individuals** and **could save hundreds of thousands of dollars each year**.

Like all our Intelligent O&M tools, this approach is grounded in actual [CLIENT] historical performance and established best practices—not theoretical models. All recommendations preserve operator authority and ensure no direct SCADA logic control. In essence, the system provides "driving directions" to licensed operators rather than attempting to operate equipment autonomously.

Through disciplined operations, digital insight, predictive analytics, and strong alignment with [CLIENT]'s capital planning, **Jacobs will transform energy management from a facility-by-facility operation into a systemwide optimization platform**. This approach supports [CLIENT]'s 2035 Vision, reduces costs, increases renewable utilization, improves reliability of critical assets, and ensures that process stability and compliance remain at the forefront of every operating decision.

## Reuse guidance

Universal and high-value: (1) the kWh-versus-kW distinction stated plainly, which most proposals skip; (2) crediting the client's current results before claiming improvement; (3) "requires no capital investment," which removes the owner's main objection to a digital claim; (4) the key-person-risk reframe — the tool protects the utility from depending on a few experienced individuals; and (5) the operator-authority paragraph, including the "driving directions" metaphor and the explicit statement that there is no direct SCADA logic control. Reuse (5) verbatim in any section that proposes AI or analytics to an operations audience.

Pursuit-specific: the inline tunnel pumps as the peak driver, the percentage and dollar figures, and the rainfall/tunnel-storage inputs. Pairs with the energy monitoring block and with the chemical optimization use-case blocks, which use the same advisory push-notification mechanism. Read `verbatim/mmsd-om-2028/pages/p0067.md#¶15`–`#¶18`.
