---
title: OT and SCADA Modernization Roadmap for Wastewater O&M
category: technical-approach
block-type: prose
tags: [digital-tools, scada, cybersecurity, instrumentation-controls, asset-management, predictive-maintenance, energy-management]
source: hull-wwtf-om-2026
source-section: "Section 5, Operational Technology (OT)/SCADA/Intelligent O&M (Exhibit 5-9)"
source-pages: [38, 39]
verbatim-ref: ["verbatim/hull-wwtf-om-2026/pages/p0038.md#¶7", "verbatim/hull-wwtf-om-2026/pages/p0038.md#¶9", "verbatim/hull-wwtf-om-2026/pages/p0039.md#¶2", "verbatim/hull-wwtf-om-2026/pages/p0039.md#¶8"]
pursuit-type: [wwtp-om, collections, multi-facility]
client-type: municipal
client-size: "3.07 MGD / 42 mi / ~10k pop"
geography: "Northeast / MA / MassDEP"
rfp-section-type: [tech-approach]
win-theme-map: [digital-tools, asset-management, innovation-value-add, partner-transparency, compliance-leadership]
proof-point-ids: [PP-0137]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
context: Coastal New England municipal WWTF (3.07 MGD) + 42-mile collection system O&M, 2026, incumbent displacement
quality: Clear three-phase maturity model with paired objectives/benefits framing that scales to any OT/SCADA modernization pitch, anchored by the "automation performs only as well as the instruments, controls, and data that support it" argument
reuse-notes: Swap phase timelines and specific platform names (the client's existing SCADA/analytics tools) per pursuit; pair with the safety/cybersecurity block for a combined resiliency narrative.
---

# OT and SCADA Modernization Roadmap for Wastewater O&M

We view [CLIENT]'s OT/SCADA as **mission-critical operational infrastructure** that must be **reliable, recoverable, and easy for operators to use**, particularly given a coastal and flood-exposed setting and a stated expectation for stronger communication, leadership, and transparency. The OT/SCADA platform will serve as the **shared source of truth** for real-time status, alarms, and performance trends, allowing [CLIENT] and the on-site Jacobs team to **identify emerging risks early** through timely, consistent, and defensible reporting.

## Three-Phase Roadmap to Strengthen Visibility, Resilience, and Asset Performance

OT and SCADA improvements will be implemented through a **deliberate three-phase roadmap** (Exhibit 5-9) designed to strengthen **permit compliance, operational resiliency, and long-term asset performance** across the WWTF and collection system. The roadmap begins with core fundamentals, recognizing that automation performs only as well as the instruments, controls, and data that support it. Improvements will be implemented deliberately so they remain **transparent, maintainable, and sustainable** over the full contract term.

**Phase 1 — Foundation (Inventory and Modeling).** Jacobs will establish the OT foundation through:

- Inventorying PLCs, HMIs, SCADA, telemetry, instrumentation, and network assets across the WWTF and collection system
- Identifying critical spares, lifecycle gaps, cybersecurity risks, and documentation needs, and verifying key instrumentation
- Updating control narratives, architecture drawings, preventive maintenance strategies, and OT inputs to the O&M manuals, SOPs, and 5-year CIP

Understanding existing assets, validating data quality, and documenting system behavior to reduce risk and support future improvements will provide a clear understanding of existing automation and technology assets, reduced compliance and operational risk, alignment with asset management and documentation requirements, and an actionable roadmap for OT capital investments.

**Phase 2 — Operational Visibility (Monitoring, Planning, and Refinement).** Jacobs will strengthen systemwide visibility and readiness through:

- Expanded and standardized monitoring across WWTF and collection systems
- Secure remote access to SCADA and asset management systems with redundant WAN connectivity
- Scenario-based operational planning for storms, high-flow, and emergency events
- Implementation of OT governance, change control, and privileged access management

Refining operating strategies and enabling proactive planning to support consistent performance during normal and adverse conditions will provide reliable, real-time visibility across all facilities; better preparedness for storms and emergencies, with a more consistent response during severe weather and high-flow events; and less unplanned downtime and more reliable operations through secure remote support.

**Phase 3 — Optimization (Process Automation and Intelligence Integration).** Jacobs will deploy advanced automation and intelligence capabilities built on validated data and operating practices, including:

- Evaluating closed-loop control opportunities for key processes and coordinating pump station and conveyance controls to reduce variability
- Deploying operator advisory tools that turn data into actionable guidance
- Expanding predictive maintenance and lifecycle planning to reduce downtime, improve capital planning, and retire obsolete OT equipment

Deploying advanced automation and intelligence capabilities built on the validated data and operating practices established in Phases 1 and 2 will provide transparency, maintainability, and long-term sustainability; improved permit compliance consistency; lower chemical and energy costs; enhanced system resilience and accessibility during severe weather; and removal of any reliance on obsolete OT equipment.

## Key Outcomes Enabled by OT and SCADA

- Updated O&M manuals and SOPs
- Secure remote monitoring and process control access
- OT-informed 5-year CIP
- Stronger cybersecurity and governed change management
- More resilient storm and emergency response

We will also build on [CLIENT]'s demonstrated interest in digital tools for optimization and transparency, including its current use of Aquasight/APOLLO, by ensuring OT data are **trustworthy and actionable**, which supports better process insight, faster troubleshooting, and clearer reporting to stakeholders.

## Reuse guidance

The roadmap structure (Foundation → Operational Visibility → Optimization) is client- and technology-agnostic and reusable for any O&M pursuit involving SCADA/OT assets, regardless of facility size. Tailor per pursuit by (1) confirming the client's actual OT inventory and any existing digital tools already in use — name them specifically, as the Aquasight/APOLLO reference does here, because it signals attentiveness during evaluation; (2) adjusting the phase timeline to match the contract's mobilization schedule; and (3) right-sizing Phase 3 automation ambitions to the facility's process complexity and capital appetite. Pairs with `../compliance-plans/integrated-safety-security-cybersecurity-program.md` for a combined resiliency narrative and with [CMMS-Driven Asset Management and Maintenance Program](cmms-driven-asset-management-maintenance-program.md), since OT inputs feed the same 5-year CIP. Related graphic: Exhibit 5-9 three-phase OT and SCADA roadmap table.
