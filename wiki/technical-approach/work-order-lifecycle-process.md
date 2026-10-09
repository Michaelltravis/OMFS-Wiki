---
title: Lifecycle Delivery and the Work Order Lifecycle Process (Exhibit 1-31)
category: technical-approach
block-type: prose
tags: [maintenance-program, cmms, preventive-maintenance, reliability-engineering, quality-assurance, diagram, exhibit]
source: ocwut-16-26
source-section: "Section 1, Maintenance Plan (Assets) — Lifecycle Delivery and How the SAMP Looks Day-to-Day (Exhibit 1-31)"
source-pages: [61]
verbatim-ref: ["verbatim/ocwut-16-26/pages/p0061.md#¶2", "verbatim/ocwut-16-26/pages/p0061.md#¶3"]
pursuit-type: [wwtp-om, multi-facility]
client-type: trust
client-size: ">110 MGD combined / 4 WWTPs + 1 major pump station / 109 FTE"
geography: "Southcentral / OK / ODEQ"
rfp-section-type: [tech-approach]
win-theme-map: [asset-management, partner-transparency, compliance-leadership, digital-tools]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
supersedes: wiki/technical-approach/mmsd-ams-drives-maintenance-delivery-and-work-order-lifecycle.md
section-id: ocwut-16-26:06.lifecycle-delivery-and-how-the-samp-looks-day-to-day
section-order: 6
section-path: Section 1 | Technical Approach › Maintenance Plan (Assets) › Asset Management Plans (AMPs) › Lifecycle Delivery and How the SAMP Looks Day-to-Day
doc-order: 92
volatility: evergreen
review-due: 2029-05-05
freshness-flags: []
context: Southcentral US municipal water utility trust wastewater O&M competitive procurement, 2026 award for Jan 1 2027 start; four WWTPs plus one major pump station, >110 MGD combined design capacity, Class B biosolids land application, 109 FTE proposed; challenger bid against an underperforming incumbent operator, backed by a 20-year engineering relationship; ODEQ regulatory regime.
quality: Shows how policy becomes practice — a five-stage work order lifecycle with named role swimlanes (requestor, planner/scheduler, operations/maintenance) and an explicit chronic-issue loop back into RCA and PM/PdM strategy, anchored to a corporate standard (the Maintenance and Reliability Resource Guide).
reuse-notes: The five-stage lifecycle, the swimlane structure, and the chronic-issue management loop are universal and reusable verbatim on any O&M pursuit. Note that the source graphic contains a leftover reference to dashboards "provided to MMSD" from a prior project's version of the exhibit — replace that with the target client before use. Confirm the current title of the corporate Maintenance and Reliability Resource Guide.
---

# Lifecycle Delivery and the Work Order Lifecycle Process (Exhibit 1-31)

## Lifecycle Delivery and How the SAMP Looks Day-to-Day

The SAMP sets the policy, process, and standards. The graphic below illustrates how this translates to daily maintenance activities from need identification through planning, execution, verification, and closeout. We'll document these processes in detail and draw on decades of lessons learned embedded in our Maintenance and Reliability Resource Guide, which serves as the standard for all Jacobs O&M projects. **All maintenance activities follow a structured lifecycle from identification through planning, scheduling, execution, verification, and feedback, ensuring consistency and repeatability across all facilities (Exhibit 1-31).**

**Exhibit 1-31.** *Jacobs' Work Order Lifecycle Process* (graphic asset ID 165_009385). Jacobs' work order lifecycle from need identification through planning, execution, verification, and closeout drives consistent, well-documented maintenance and clear accountability. Swimlanes run from the requestor (staff or public service request), through review and approval (emergency? urgent? parts or services required? review needed?), the planner/scheduler (PM-program-generated work orders, secure parts and contract services, two-week schedule, work list review), and operations/maintenance (manager and crew lead assign shift work, crew leader assigns the technician, technician receives and executes the work order, adds details, completes), with rework and edit loops back into review before the work order is closed.

- **Work order creation.** Whether triggered by a cycled PM task, a SCADA alarm, or an operator check, a mobile work order is generated. A Planner assigns a priority to the work order, determined by asset risk and criticality.
- **Planning and preparation.** The Planner verifies and defines the job plan scope; coordinates kitting of required parts and materials; ensures lockout/tagout and confined space requirements are addressed; and schedules the work based on priority and craft availability.
- **Execution.** The assigned crew performs the work according to the job plan, meeting acceptance criteria and providing photo evidence of completion.
- **Verification and closure.** Supervisors verify job completion and notify the Planning Group. The Planner reviews and closes requests, triggering automatic updates to dashboards provided to the client.
- **Chronic issue management.** Any recurring or chronic issues are identified by the Planning group and reviewed by RCA/PMO reliability engineering for further analysis. This may result in adjustments to PM or PdM strategies and, if justified, implementation of additional PdM measures.

## Reuse guidance

Universal: the whole passage. The five-stage lifecycle, role swimlanes, priority-by-risk-and-criticality rule, kitting and LOTO/confined-space checks in planning, photo evidence at execution, and the chronic-issue feedback loop into reliability engineering transfer to any wastewater or water O&M pursuit without change.

Pursuit-specific: the client name on the dashboard reference (the source graphic still names a prior client, MMSD — correct this), the CMMS platform used to generate mobile work orders, and the facility count.

Pairs with: [Asset Management System — ISO 55001 Framework, SAMP, and Governance](asset-management-system-iso-55001-samp-governance.md), which sets the policy this executes, and [NexGen EAM — CMMS Governance and Implementation-to-Operations Continuity](nexgen-eam-cmms-governance-and-implementation-continuity.md). Read `verbatim/ocwut-16-26/pages/p0061.md` for the raw exhibit text.
