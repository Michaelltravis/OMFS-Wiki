---
title: OT Asset Management Software Platform Modules Table (Exhibit IV-31)
category: technical-approach
block-type: table
tags: [instrumentation-controls, scada, cybersecurity, asset-management, cmms, digital-tools, technical-approach, table-layout, resilience-planning, quality-assurance]
source: mmsd-om-2028
source-section: "IV. Approach — Exhibit IV-31. Summary of Function and Benefits of Jacobs OT Modules Asset Management Software Platform"
source-pages: [79]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0079.md#¶7"]
pursuit-type: [wwtp-om, multi-facility, collections]
client-type: authority
client-size: "2 large water reclamation facilities / regional metro service area / biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [digital-tools, asset-management, innovation-value-add, compliance-leadership]
proof-point-ids: [PP-3023]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid vs. incumbent operator; WDNR
quality: Seven OT asset management modules stated as commitments ("what Jacobs will do"), not features — inventory down to connectors and SFP modules, network mapping with Layer 2/Layer 3 tracking, lifecycle profiles integrated to the client's CMMS, architecture dependency mapping, downtime impact tracing, configuration comparison against standards, and governed change workflows. Concrete enough to survive a technical evaluator's scrutiny.
reuse-notes: Replace the CMMS integration reference with the pursuit's platform. Where a client has an existing OT inventory or network documentation, reframe the inventory rows as verification and gap-closure rather than establishment.
---

# OT Asset Management Software Platform Modules Table (Exhibit IV-31)

| **OT Asset Management Modules** | **What Jacobs Will Do for [CLIENT]** |
|---|---|
| **Asset Inventory** | Establish a complete inventory of all OT components, including devices, connectors, cables, and SFP modules.<br>Strengthen cybersecurity by ensuring full visibility of all assets and interconnections.<br>Improve spare-parts planning to reduce downtime and enhance system resilience. |
| **Asset Network Inventory** | Map [CLIENT]'s segmented OT networks to verify each device resides on the correct network.<br>Track Layer 2/Layer 3 addressing across IP and serial systems for deeper SCADA insight.<br>Identify unauthorized or misconfigured components to improve security and compliance. |
| **Asset Life-Cycle Management** | Develop standardized OT asset profiles incorporating manufacturer specs and Jacobs' operational experience.<br>Enable optimized lifecycle planning and targeted condition assessments.<br>Integrate with [CLIENT]'s CMMS to align PM strategies with OT asset needs. |
| **Architecture Inventory and Management** | Visualize logical and physical links between OT devices to reveal dependencies.<br>Support resiliency planning by identifying redundancy gaps.<br>Reduce risk of cascading failures through informed architecture management. |
| **Downtime Management** | Track dependencies for communications, power, and data pathways.<br>Quickly assess how device failures impact treatment and conveyance operations.<br>Strengthen incident response and continuity-of-operations planning. |
| **Configuration Management** | Continuously compare configuration files against standards and peer assets.<br>Maintain synchronized configuration data through dynamic linking to asset records.<br>Ensure accurate labeling and documentation consistent with field installation context. |
| **OT Change Management** | Manage change through guided workflows that consider logical, physical, and environmental dependence.<br>Enforce governance using approval pathways and pre-deployment validation checks.<br>Reduce risk and protect system integrity by controlling and auditing all configuration changes. |

## Reuse guidance

Drop-in for any pursuit offering OT asset management; every module is firm capability. Tailor only the CMMS integration row and the network-segmentation language to the client's architecture. Pairs with [world-class operational technology](mmsd-operational-technology-tools-expertise-and-ot-asset-management-platform.md). Read `verbatim/mmsd-om-2028/pages/p0079.md#¶7` for the source table.
