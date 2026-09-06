---
title: SCADA Control System Redundancy Upgrade Recommendation
category: technical-approach
block-type: prose
tags: [scada, ignition, hyperconverged-infrastructure, redundancy, control-system, resiliency, unpriced-recommendation]
source: santamonica-swip-om-2025
source-section: "Section 4: Suggested Modifications to the Scope of Work — Additional Items for Consideration, SCADA Control System Deployment"
source-pages: [106]
verbatim-ref: ["verbatim/santamonica-swip-om-2025/pages/p0106.md#¶19", "verbatim/santamonica-swip-om-2025/pages/p0106.md#¶17", "verbatim/santamonica-swip-om-2025/pages/p0106.md#¶20", "verbatim/santamonica-swip-om-2025/pages/p0106.md#¶21"]
pursuit-type: [wwtp-om, water-treatment, reuse-dpr]
client-type: municipal
client-size: "Underground AWTF (MBR/RO/UV-AOP) plus urban runoff recycling facility, stormwater assets, and 2 injection wells; five-year contract"
geography: "Southern California / CA / SWRCB Division of Drinking Water — Title 22 GRRP"
rfp-section-type: [exec-summary]
win-theme-map: [digital-tools, partner-transparency, innovation-value-add]
proof-point-ids: [PP-0695]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
context: Southern California advanced water treatment / potable reuse facility O&M, 2025, incumbent (Veolia) displacement
quality: A short pair of named-technology recommendations (Ignition virtualized redundancy, hyperconverged infrastructure) presented honestly as unpriced and needing further scoping — a useful pattern for suggesting high-value modifications without overcommitting on cost, plus the reusable framing sentence that opens an "Additional Items for Consideration" subsection.
reuse-notes: This was explicitly presented as an idea requiring further information from the client before it could be scoped and priced — preserve that framing if reused. Confirm the named SCADA platform and infrastructure approaches are still the current recommendation, as products and versions change.
---

# SCADA Control System Redundancy Upgrade Recommendation

## Additional Items for Consideration

Our team believes the following suggested modifications will bring significant value to [CLIENT]; however, we will require additional information for [Firm] to scope the work and provide a price.

### SCADA Control System Deployment

The two key enhancements should be considered for the current SCADA control system deployment. Introducing redundancy at both the SCADA/HMI layer and the server infrastructure would significantly improve system resiliency and operational continuity. These upgrades would help to safeguard against single points of failure and ensure consistent performance in critical environments:

- Implementing Ignition virtualized redundancy within SCADA system ensures continuous operation by automatically switching to a backup server during failures.
- Implementing hyperconverged infrastructure consolidates compute, storage, and networking into a unified platform, simplifying management and scaling. Compared to a single server setup, it offers higher availability, built-in redundancy, backup, and seamless expansion without major hardware overhauls.

## Reuse guidance

This block carries two reusable pieces. The first is the "Additional Items for Consideration" framing sentence, which opens a subsection of genuinely valuable modifications that the proposer will not price without more information. That posture reads as consultative rather than salesy, and it lets a proposal surface ideas that would otherwise be dropped for lack of data — reuse the sentence verbatim as the transition between the priced value-adds and the unpriced ones, and resist the temptation to attach a speculative number to items placed under it. The second is the SCADA recommendation itself, which works because it names the failure mode (single points of failure at the SCADA/HMI layer and in the server infrastructure), then names two specific remedies and what each one buys: automatic failover to a backup server, and a consolidated compute, storage, and networking platform that adds availability, built-in redundancy, backup, and room to expand without a hardware overhaul. Confirm that Ignition virtualized redundancy and hyperconverged infrastructure are still the current recommended approach before reuse, since control-system platforms and infrastructure products evolve quickly, and check whether the target client's existing SCADA vendor makes a different redundancy path more appropriate. Where a fuller control-system narrative is required, fold this recommendation into a phased OT/SCADA modernization roadmap rather than leaving it as a two-bullet aside. Pairs with [swip-mechanical-ic-regional-support-value-add.md](swip-mechanical-ic-regional-support-value-add.md), which offers the IT/OT bench that would execute the work, and with [swip-city-staff-training-program.md](swip-city-staff-training-program.md) and [swip-cmms-inventory-management-value-add.md](swip-cmms-inventory-management-value-add.md), the other two items under the same unpriced heading. Full passage: verbatim/santamonica-swip-om-2025/pages/p0106.md ¶16–¶21.
