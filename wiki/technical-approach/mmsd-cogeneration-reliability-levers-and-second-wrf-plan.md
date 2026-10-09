---
title: Cogeneration Reliability Levers and the Second WRF Enhancement Plan
category: technical-approach
block-type: prose
tags: [reliability-engineering, energy-management, biosolids, predictive-maintenance, preventive-maintenance, instrumentation-controls, scada, maintenance-program, process-control, technical-approach]
source: mmsd-om-2028
source-section: "Section IV.A.3, Approach to PM and CM — 3.3.1 Cogeneration Reliability and O&M Enhancement Plan (continued); 3.3.2 Second WRF Cogeneration Reliability and O&M Enhancement Plan"
source-pages: [96]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0096.md#¶3"]
pursuit-type: [wwtp-om, multi-facility, solids]
client-type: authority
client-size: "Two large water reclamation facilities with digester gas cogeneration"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [innovation-value-add, energy-chemical-efficiency, asset-management, incumbent-displacement]
proof-point-ids: [PP-2215, PP-2216, PP-2217, PP-2218]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:26.3-3-reliability-enhancement-plans-improving-equipment-uptime
section-order: 9
section-path: 'IV. Approach Summary › IV.A. Approach to Management, Operations, PM, and CM › IV.A.3. Approach to PM and CM › 3.3. Reliability Enhancement Plans: Improving Equipment Uptime at JIWRF and SSWRF'
doc-order: 172
volatility: evergreen
review-due: 2029-01-29
freshness-flags: []
context: Midwest US regional sewerage district, two large water reclamation facilities with digester gas cogeneration, 2028 challenger bid against an incumbent contract operator; WDNR
quality: The deepest equipment-level reliability content in the section — adaptive alarm thresholds, safe operating ranges, predictive siloxane management, seasonal cooling and valve discipline, hot water loop balancing, and a unified health dashboard, each tied back to a shutdown mechanism it prevents. Names the engine fleet (Caterpillar units, White Superior) and the four reliability constraints.
reuse-notes: Every lever here is digester-gas cogeneration specific; carry it to pursuits with gas-fueled engines or turbines and rebuild the constraint list from the client's own shutdown history. The closing paragraph — converting reliability triggers into standard work order processes in the CMMS — is the general pattern and transfers to any reliability plan.
---

# Cogeneration Reliability Levers and the Second WRF Enhancement Plan

**Adaptive thresholds to reduce nuisance alarms.** We'll adjust select alarm upper and lower limits based on operating mode, ambient conditions, and fuel blend to reduce avoidable alarms, while protecting assets.

**Condition-based maintenance focus.** We'll prioritize converting appropriate PM tasks to condition-based maintenance by using leading indicators such as differential pressure trends, fuel quality trends, flow compared to target, and heat exchanger fouling indicators.

**Automatic shutdown event capture and standardized root cause analysis.** When an unplanned shutdown occurs, we'll automatically capture a defined operating snapshot to support rapid diagnosis, then execute a standardized root cause analysis process and close corrective and preventive actions quickly to prevent recurrence.

**Reliability governance that drives closure.** We'll use weekly reliability huddles and monthly leadership reviews to remove barriers, approve parameter and logic changes, and ensure corrective actions are reviewed by the governance board before they become durable standards.

**Operating ranges that prevent unplanned shutdowns.** We'll define clear safe operating ranges for critical parameters (for example, fuel pressure stability, discharge temperature stability, and dewpoint margin) and use dashboards to manage any drift toward shutdown conditions, so they're easily visible and actionable.

**Predictive siloxane management.** We'll strengthen periodic sampling of the media by using trends such as differential pressure and methane flow behavior to identify breakthrough risk early and reduce forced outages and engine impacts.

**Seasonal cooling strategy and valve discipline.** We'll implement seasonal setpoints and routine valve PM inspections to reduce temperature instability that can drive alarms, derates, and shutdowns.

**Hot water loop balancing.** We'll correct hydraulic conflicts through targeted loop balancing and three-way valve maintenance to stabilize jacket water temperature difference and reduce temperature-driven shutdowns.

**Unified health dashboard operators can act on.** We'll provide clear indices for gas compression, fuel quality, cooling water, and hot water, so operators and maintenance teams can quickly identify degrading conditions, required actions, and needed work.

**Cogeneration reliability and O&M enhancement plan (WRF-2).** We'll increase uptime and stabilize performance across the Caterpillar units and the White Superior engine by controlling the upstream conditions that drive unplanned shutdowns, and by improving alarm management, dashboards, and operator discipline. Our plan targets the most common reliability constraints:

- Digester gas variability and siloxane breakthrough
- Compressor fuel pressure instability
- Seasonal cooling water imbalances
- Hot water loop interactions that affect jacket water temperature stability

**Condition-based maintenance conversion and shutdown learning.** We'll apply PdM health scoring to prioritize work and convert suitable tasks for filters, exchangers, and carbon beds to condition-based maintenance. We'll also use automatic shutdown event capture and standardized root cause analysis to understand, prevent, and predict conditions that cause failures.

We'll integrate these plans directly into our AMS by converting reliability triggers (for example, defined condition indicators, event capture, and alarm priorities) into **standard work order processes** in the CMMS, tying actions to clearly defined KPIs and dashboards, and using a disciplined root cause and corrective-action process to ensure fixes are permanent and measurable.

## Reuse guidance

Universal: the closing integration paragraph — reliability triggers become standard work orders, tied to KPIs and dashboards, closed through RCA — is the sentence that connects any equipment-level reliability plan back to the asset management system, and it transfers to any pursuit. The weekly huddle / monthly leadership review cadence is also portable.

Pursuit-specific: the engine fleet and manufacturer names; the four reliability constraints, which come from the client's shutdown history; siloxane and digester-gas content, which applies only where biogas fuels the engines; the WRF-1 / WRF-2 designations, which stand for the client's two named facilities and should be replaced with the pursuit's own facility names.

Continues from [cogeneration data flow and alarm strategy](mmsd-cogeneration-reliability-enhancement-plan-data-and-alarms.md). Pairs with [10-Box AMS elements 6–10](mmsd-10-box-ams-elements-6-10-people-through-outcomes.md) for the KPI set these plans report into. Full passage, as a two-column layout: verbatim/mmsd-om-2028/pages/p0096.md#¶3.
