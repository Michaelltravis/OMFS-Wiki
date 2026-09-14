---
title: AMS Drives Maintenance Delivery — Weekly Planning, Daily Execution, and the Work Order Life Cycle
category: technical-approach
block-type: prose
tags: [maintenance-program, cmms, nexgen-eam, asset-management, preventive-maintenance, scada, quality-assurance, technical-approach, exhibit, structure-pattern]
source: mmsd-om-2028
source-section: "Section IV.A.3, Approach to PM and CM — 3.2.2 AMS Drives Maintenance Delivery; 3.2.3 How our SAMP looks day-to-day"
source-pages: [93, 94]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0093.md#¶18", "verbatim/mmsd-om-2028/pages/p0094.md#¶6"]
pursuit-type: [wwtp-om, multi-facility, collections]
client-type: authority
client-size: "Two large water reclamation facilities + deep tunnel conveyance + biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [asset-management, partner-transparency, digital-tools]
proof-point-ids: [PP-2207, PP-2208, PP-2209]
testimonial-ids: []
story-ids: []
status: fallback
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
superseded-by: wiki/technical-approach/work-order-lifecycle-process.md
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent contract operator; WDNR
quality: Bridges the framework to the field — names the accountable leader, the system of record and its integrations, then walks the five-stage work order life cycle with the Planner/Scheduler's specific duties and the chronic-issue loop back to RCA/PMO.
reuse-notes: Substitute the named Director of Maintenance and Asset Management and the client's EAM. The work order life cycle is drawn from Jacobs' Maintenance Resource Guide and transfers unchanged; only the dashboard recipient and the asset classes in the coverage sentence need editing. A duplicate exists at work-order-lifecycle-process.md from an earlier source — check which is preferred for the pursuit.
---

# AMS Drives Maintenance Delivery — Weekly Planning, Daily Execution, and the Work Order Life Cycle

Director of Maintenance and Asset Management John Loucks-Powell develops the AMS and associated maintenance delivery based on the framework illustrated in **Exhibit IV-44** (graphic 322_007CAM_2). The AMS will span WRF process units, conveyance/tunnels and structures, facilities, and fleet, with NEXGEN EAM as the system of record, which integrates to SCADA/Historian and GIS so that vertical and linear assets live in a single view. The AMS — aligned to ISO 55001 and governed by the Maintenance Committee with its CMMS and SCADA subcommittees — carries the SAMP's policy, roles and decision rights, standard work, and KPIs into **weekly planning, daily execution, and transparent results**.

The SAMP will set the policy, process, and standards, and **Exhibit IV-45** (graphic 324_007CAM_3) illustrates how this translates to daily maintenance activities. We'll document these processes in detail to ensure understanding and compliance with expectations. For example, our standard work order life cycle process, drawn from our decades of lessons learned and best practice — and documented in our Maintenance Resource Guide — serves as the standard for all projects. Jacobs' Work Order Life Cycle runs from need identification through planning, execution, verification, and closeout, ensuring consistent, well-documented maintenance and clear accountability:

**Work order creation.** Whether triggered by a cycled PM task, a SCADA alarm, or an operator check, a mobile work order is generated. A Planner assigns a priority to the work order, determined by asset risk and criticality.

**Planning and preparation.** The Planner verifies and defines the job plan scope; coordinates kitting of required parts and materials; ensures lockout/tagout and confined space requirements are addressed; and schedules the work based on priority and craft availability, building a two-week schedule through work list review.

**Execution.** The assigned crew performs the work according to the job plan, meeting acceptance criteria and providing photo evidence of completion.

**Verification and closure.** Supervisors verify job completion and notify the Planning Group. The Planner reviews and closes requests, triggering automatic updates to the dashboards provided to [CLIENT], a regional sewerage district operating two large water reclamation facilities.

**Chronic issue management.** Any recurring or chronic issues are identified by the Planning Group and reviewed by RCA/PMO reliability engineering for further analysis. They may result in adjustments to PM or PdM strategies and, if justified, implementation of additional PdM measures.

## Reuse guidance

Universal: the five-stage life cycle with the Planner/Scheduler's four planning duties and the chronic-issue feedback loop. The three-beat close of the AMS exhibit — weekly planning, daily execution, transparent results — is a reusable summary line for any maintenance approach.

Pursuit-specific: the named director; the EAM and its integrations; which asset classes the AMS spans (fleet and facilities are often out of scope); the review cadence if the client's contract sets a different schedule interval.

Pairs with [10-Box AMS elements 1–5](mmsd-10-box-ams-elements-1-5-governance-through-information.md) and [integrated reliability program outcomes](mmsd-integrated-reliability-maintenance-program-outcomes.md). Full passage and the exhibit's swimlane labels: verbatim/mmsd-om-2028/pages/p0093.md#¶18–¶21 and p0094.md#¶5–¶9.
