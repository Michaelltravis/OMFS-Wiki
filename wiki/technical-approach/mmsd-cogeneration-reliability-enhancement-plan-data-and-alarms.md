---
title: Reliability Enhancement Plans for WRF Uptime — Cogeneration Data Flow and Alarm Strategy
category: technical-approach
block-type: prose
tags: [reliability-engineering, energy-management, maintenance-program, predictive-maintenance, scada, instrumentation-controls, data-analytics, process-control, technical-approach, differentiator]
source: mmsd-om-2028
source-section: "Section IV.A.3, Approach to PM and CM — 3.3 Reliability Enhancement Plans; 3.3.1 Cogeneration Reliability and O&M Enhancement Plan"
source-pages: [95]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0095.md#¶10", "verbatim/mmsd-om-2028/pages/p0095.md#¶13"]
pursuit-type: [wwtp-om, multi-facility, solids]
client-type: authority
client-size: "Two large water reclamation facilities with digester gas cogeneration"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [innovation-value-add, energy-chemical-efficiency, asset-management, incumbent-displacement]
proof-point-ids: [PP-2211, PP-2212, PP-2213, PP-2214]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:26.3-3-reliability-enhancement-plans-improving-equipment-uptime
section-order: 1
context: Midwest US regional sewerage district, two large water reclamation facilities with digester gas cogeneration, 2028 challenger bid against an incumbent contract operator; WDNR
quality: Shows work already done before award — facility-specific reliability plans developed from the O&M manuals and RFP alone. The three-lever structure (make data actionable, make alarms meaningful, prevent repeat shutdowns) is the reusable spine, and the alarm-tiering sentence protects safety shutdowns while cutting nuisance alarms.
reuse-notes: This only works where the team has actually read the client's O&M manuals and can name the systems that drive uptime — write the plan before claiming it. Replace the cogeneration asset list (fuel gas conditioning and compression, cooling water, fuel quality, turbine operating envelope, waste heat) with the pursuit's own uptime-critical systems.
---

# Reliability Enhancement Plans for WRF Uptime — Cogeneration Data Flow and Alarm Strategy

Based on our review of [CLIENT]'s O&M manuals and the RFP and scope requirements, Jacobs' maintenance team has already developed initial WRF-specific reliability enhancement plans focused on the equipment and systems that most directly drive uptime at both water reclamation facilities. [CLIENT] is a regional sewerage district operating two large water reclamation facilities and a deep tunnel conveyance system. These plans apply the same integrated maintenance backbone described above (standardized asset data, evidence-based work execution, and reliability analytics) to deliver measurable increases in availability, fewer repeat failures, and stronger operational stability. The result is enhanced reliability from more predictable performance and fewer unplanned disruptions caused by nuisance alarms and unexpected equipment shutdowns. At the same time, it will lead to better prioritization of maintenance labor and spares, and clearer performance visibility for [CLIENT].

**Cogeneration reliability and O&M enhancement plan (WRF-1).** We can increase equipment availability by reducing nuisance alarms, preventing unplanned equipment shutdowns, and converting priority PM work to condition-driven actions across the fuel gas conditioning and compression system, cooling water, fuel quality, turbine operating envelope, and waste heat systems. As illustrated in **Exhibit IV-46**, our plan focuses on three practical levers: (1) make data actionable, (2) make alarms meaningful, and (3) prevent repeat shutdowns through disciplined root cause analysis and closure.

**Actionable reliability data flow.** We'll connect process signals and equipment condition indicators into a consistent flow from the control system and historian into reliability analytics, then into the CMMS and dashboards, so abnormal conditions trigger the right response work order, and follow-through (not just alarms).

**Unified alarm strategy and alarm hygiene.** We'll tier alarms (information, warning, critical, and safety shutdown) with clear expectations for response and escalation. To do that, we'll evaluate and optimize the alarm system so operators only see alarms that matter, without weakening the safety and equipment-protection shutdowns that are there to prevent damage or unsafe conditions.

**Exhibit IV-46. Cogeneration reliability and O&M enhancement plan to increase equipment reliability and uptime by reducing nuisance alarms and unplanned shutdowns** (graphic 359_007CAM_1):

|**Responsible group**|**Assigned responsibility**|**Condition-based response**|
|---|---|---|
|Governance Group|Make Data Actionable|Adaptive thresholds to reduce nuisance alarms|
|Reliability Engineering|Make Alarms Meaningful||
|Operations and Maintenance|Escalate Maintenance Activity|Automatic shutdown event capture and standardized root cause analysis|
|Planning/Scheduling||Failure event response and standardized root cause analysis|

## Reuse guidance

Universal: the three levers, the four-tier alarm taxonomy with the safety-shutdown caveat, and the data path from control system and historian through reliability analytics into the CMMS. The responsibility table transfers to any pursuit with a governance group and a reliability engineering function.

Pursuit-specific: the facility designation (WRF-1 here stands for the client's first named water reclamation facility); the uptime-critical system list; the claim that plans are "already developed," which must be backed by the actual draft plan in the file.

Continues in [cogeneration reliability levers and the second WRF plan](mmsd-cogeneration-reliability-levers-and-second-wrf-plan.md). Full passage: verbatim/mmsd-om-2028/pages/p0095.md#¶9–¶16.
