---
title: SCADA/OT/Cybersecurity Responsibility Split — Owner-Managed, Shared, Contractor-Managed
category: technical-approach
block-type: table
tags: [scada, cybersecurity, instrumentation-controls, partnership, asset-management]
source: ocwut-16-26
source-section: "Operations Plan, Exhibit 1-23, Summary of Jacobs' Understanding of SCADA/OT/Cybersecurity Responsibilities"
source-pages: [46]
verbatim-ref: ["verbatim/ocwut-16-26/pages/p0046.md#¶1", "verbatim/ocwut-16-26/pages/p0046.md#¶7", "verbatim/ocwut-16-26/pages/p0046.md#¶8"]
pursuit-type: [wwtp-om, multi-facility, collections]
client-type: trust
client-size: ">110 MGD combined / 4 WWTPs + 1 major pump station / 109 FTE"
geography: "Southcentral / OK / ODEQ"
rfp-section-type: [tech-approach]
win-theme-map: [partner-transparency, compliance-leadership, digital-tools]
proof-point-ids: [PP-1386]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: true
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: ocwut-16-26:05.phase-1-establishing-a-shared-baseline-for-process-control-p
section-order: 33
section-path: Section 1 | Technical Approach › Operations Plan › SCADA/OPERATIONAL TECHNOLOGY (OT)/ CYBERSECURITY › Process Control System Phased Performance Improvement Plan › Phase 1 – Establishing a Shared Baseline for Process Control Performance
doc-order: 68
context: Southcentral US municipal water utility trust wastewater O&M competitive procurement, 2026 award for Jan 1 2027 start; four WWTPs plus one major pump station, >110 MGD combined design capacity, Class B biosolids land application, 109 FTE proposed; challenger bid against an underperforming incumbent operator, backed by a 20-year engineering relationship; ODEQ regulatory regime.
quality: A one-graphic answer to the question every utility asks about an O&M operator and its SCADA — who touches what. Naming the owner-retained items first, before claiming any scope, is what makes the transparency claim land.
reuse-notes: The line items are this client's systems; rebuild the asset list from the pursuit's actual architecture and confirm each assignment with the client before publishing. The three-column device (owner-managed / shared / contractor-managed) is the reusable pattern. Source is a Venn-style graphic (asset ID 119_009385); the row assignments below are reconstructed from the exhibit's text layer, so verify against the render before reuse.
---

# SCADA/OT/Cybersecurity Responsibility Split — Owner-Managed, Shared, Contractor-Managed

**EXHIBIT 1-23.** *Summary of Jacobs' Understanding of SCADA/OT/Cybersecurity Responsibilities*

| Responsibility | [CLIENT]-managed | Shared | Contractor-managed (Jacobs) |
|---|---|---|---|
| Wonderware/AVEVA software | ● | | |
| Firewalls and access controls | ● | | |
| Communications network and backbone radios | ● | | |
| Telog telemetry hardware | ● | | |
| SCADA/PC server hardware | ● | | |
| CMMS (NexGen EAM) and LIMS | ● | | |
| Email alert/notification systems | ● | | |
| Cybersecurity policies and standards | ● | | |
| Telemetry/SCADA contract management | ● | | |
| SCADA access and security configuration | | ● | |
| Plant radio support | | ● | |
| PLC programming and coding | | | ● |
| Field instrumentation, I/O, and calibration | | | ● |
| Operator interface terminals (OITs) | | | ● |
| VFDs and motor controls | | | ● |
| Chemical pumps and controls | | | ● |
| Valve actuators and controls | | | ● |
| Plant UPS systems | | | ● |
| Lift station controls | | | ● |
| Sampling instruments | | | ● |

Graphic asset ID: 119_009385 (client-specific — rebuild for reuse).

The exhibit supports the section's governing statement: SCADA, OT, and cybersecurity remain firmly under [CLIENT]'s governance, with the operator maintaining field-level assets at the owner's direction, and a small set of items — SCADA access and security configuration, plant radio support — managed jointly so that access decisions stay visible to the owner while the field team keeps the equipment running.

## Reuse guidance

Universal: the three-column responsibility device and the ordering that puts the owner's retained systems first. Use it early in any OT or SCADA response where the client owns the control system and fears an operator taking over the network — it defuses the objection in one page. Pursuit-specific: every line item, and the shared-column entries in particular, which should be negotiated rather than asserted. Pairs with `ocwut-owner-governed-scada-ot-support-approach.md` and `ocwut-operational-technology-cybersecurity-its-plan.md`. Read `verbatim/ocwut-16-26/pages/p0046.md#¶7` and `#¶8` plus the page render for the original layout.
