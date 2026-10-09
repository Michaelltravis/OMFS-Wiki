---
title: "PM Optimization, Operator-Driven Requests, and Work Planning"
category: technical-approach
block-type: prose
tags: [preventive-maintenance, maintenance-program, cmms, reliability-engineering, asset-management, inventory-management, digital-tools, technical-approach]
source: mmsd-om-2028
source-section: "IV.A.3. Approach to PM and CM — 3.4 PM Approach"
source-pages: [97]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0097.md#¶6", "verbatim/mmsd-om-2028/pages/p0097.md#¶9", "verbatim/mmsd-om-2028/pages/p0097.md#¶13", "verbatim/mmsd-om-2028/pages/p0097.md#¶15", "verbatim/mmsd-om-2028/pages/p0097.md#¶16"]
pursuit-type: [wwtp-om, multi-facility, solids]
client-type: authority
client-size: "Two large water reclamation facilities + regional conveyance system + biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [asset-management, digital-tools, incumbent-displacement]
proof-point-ids: [PP-2219]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:26.3-5-cm-and-work-order-management
section-order: 10
section-path: IV. Approach Summary › IV.A. Approach to Management, Operations, PM, and CM › IV.A.3. Approach to PM and CM › 3.5. CM and Work Order Management
doc-order: 173
volatility: evergreen
review-due: 2029-01-29
freshness-flags: []
context: "Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; WDNR."
quality: "Concrete, auditable PM optimization mechanics — PMO cycle, job-plan content, operator-driven requests, kitting, QR tagging, and a PM-Plus approval flow — rather than generic PM boilerplate."
reuse-notes: "Swap the CMMS platform name (NEXGEN here) for the client's system, confirm the governance committee names exist in the target contract, and tailor the PM-Plus/non-routine work approval flow to the client's task-order language."
---

# PM Optimization, Operator-Driven Requests, and Work Planning

We won't just schedule PMs—we'll optimize them with data and field feedback to maximize uptime and value:

**PMO.** We'll run a **formal PMO cycle on critical assets at least annually**. The PMO reviews MTBF/MTTR, PM compliance, failure modes, criticality, and cost, and it examines the task language with frontline staff to remove ambiguity. Each job plan will clearly state the scope, lockout points, steps, tools, acceptance criteria, evidence required (e.g., photo of replaced part), and the trigger for escalation to CM or PdM. PM frequencies will be adjusted by asset class and performance. Changes are vetted through the Maintenance/CMMS Governance Committees to ensure traceability.

**Operator-driven work requests.** We'll equip operators with NEXGEN's mobile platform and simple inspection checklists to detect abnormal conditions (smell, sound, temperature, vibration) before failure.

**Kitting and parts readiness.** The Planner/Scheduler will coordinate with the warehouse to kit common PMs and align lead-time parts with the look-ahead schedule so crews are never waiting on materials. Inventory staff will be trained in AM principles and participate in the weekly planning meeting.

**Asset identification and mobile enablement.** During mobilization, we'll complete barcode/QR tagging with a NEXGEN-aligned data dictionary. NEXGEN creates a new QR code for each asset that you can use to pull up the asset in the field. Crews will scan for history in the field, attach evidence, and close out work on mobile devices, creating a durable audit trail.

**PM-Plus workflow.** [CLIENT]'s PM-Plus (non-routine cleaning/maintenance) will be primarily self-performed. When a PM-Plus task requires a task order, we'll use a simple approval flow: request → scope → estimate (hours/materials) → [CLIENT] approval → execute → closeout + evidence, which was adapted from Jacobs' Maintenance Excellence playbook.

## Reuse guidance

Universal: the PMO cycle content (MTBF/MTTR, PM compliance, failure modes, criticality, cost), the job-plan element list, operator-driven work requests, kitting/parts readiness, and QR/barcode tagging at mobilization. These are platform-agnostic once the CMMS name is swapped.

Pursuit-specific: the CMMS product (NEXGEN), the governance committee structure, and the PM-Plus terminology, which is this client's contract vocabulary for non-routine cleaning and maintenance — rename it to whatever the target RFP calls non-routine work.

Pairs with [Corrective Maintenance, Work Order Closeout, and In-House Failure Analysis](mmsd-corrective-maintenance-and-failure-analysis.md) and [Maintenance Transparency, Reporting, and Governance](mmsd-maintenance-transparency-reporting-governance.md). Read `verbatim/mmsd-om-2028/pages/p0097.md` for the full passage, including the graphic-embedded PM-Plus and tagging text.
