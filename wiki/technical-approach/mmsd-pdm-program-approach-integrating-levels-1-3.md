---
title: "PdM Program Approach — Integrating Levels 1, 2, and 3 Data for Asset Protection and PM Results"
category: technical-approach
block-type: prose
tags: [predictive-maintenance, data-analytics, reliability-engineering, asset-management, cmms, scada, cybersecurity, preventive-maintenance, technical-approach]
source: mmsd-om-2028
source-section: "IV.D. Potential Additive Work – Level 3 PdM — 6. PdM Program Approach for Using Technologies for Asset Protection and PM Results"
source-pages: [135, 136]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0135.md#¶9", "verbatim/mmsd-om-2028/pages/p0136.md#¶2", "verbatim/mmsd-om-2028/pages/p0136.md#¶3"]
pursuit-type: [wwtp-om, multi-facility, solids, collections]
client-type: authority
client-size: "Two large water reclamation facilities + regional conveyance system + biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [asset-management, digital-tools, partner-transparency, innovation-value-add]
proof-point-ids: [PP-2272]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
context: "Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production and regional conveyance, 2028 challenger bid against an incumbent operator; WDNR. The client already collected substantial condition data that sat unused across vendor reports."
quality: "The strongest 'we will use the data you already own' argument in the bank — it reframes an additive-scope sell as unlocking a sunk investment, names the highest-consequence assets it starts with, and commits the resulting insights to three standing client committees rather than to a report."
reuse-notes: "Re-name the highest-consequence asset list for the target facility and confirm the client's committee names and cybersecurity exhibit reference. The assumption that existing PLCs and control systems can route PdM data to SCADA, the historian, and the CMMS must be re-verified per pursuit — it is a scope assumption, not a given."
---

# PdM Program Approach — Integrating Levels 1, 2, and 3 Data

Jacobs' Level 3 PdM program approach integrates Level 1, Level 2, and Level 3 data into a cohesive predictive framework grounded in [CLIENT]'s asset criticality rankings. [CLIENT] is a regional sewerage district operating two large water reclamation facilities, a regional conveyance system, and a biosolids production operation. We recognize that [CLIENT] already collects a substantial amount of Level 1 and Level 2 data—SCADA trends, historian data, vibration analyses, and oil testing—but that these datasets may be underutilized because they are dispersed across vendor reports, independent systems, or high-level CMMS entries. The core objective of our Level 3 program is to unite these data streams into a comprehensive, structured, and repeatable maintenance intelligence system.

By combining previously underused [CLIENT] data with high-frequency PdM analytics, Jacobs creates a complete picture of asset condition that supports earlier fault detection, clearer prioritization of maintenance actions, and more accurate alignment of maintenance resources with asset risk. The program focuses initially on [CLIENT]'s most critical assets, including the dryers that produce [CLIENT]'s biosolids product, cogeneration/Solar Turbine systems, aeration blowers, deep tunnel pumps, and high-consequence conveyance stations, where predictive insights generate the highest operational and financial impact.

This program is designed to **build on [CLIENT]'s existing systems**. Any required sensors are included as part of the PdM technologies themselves, and Jacobs assumes [CLIENT]'s PLCs and control systems can support the necessary routing of PdM data to SCADA, the historian, and the CMMS. Jacobs' SCADA/OT specialists will configure tag structures, historian routing, and alarm strategies in accordance with Exhibit Q cybersecurity protocols.

Working with [CLIENT], Jacobs will establish automated rulesets that interpret patterns in vibration signatures, electrical anomalies, hydraulic performance changes, temperature trends, and operational behavior. These rulesets will generate alerts, create automated CMMS work orders, update asset condition ratings, and drive PM optimization. We'll routinely review PdM insights with [CLIENT] through the Operations Committee, Maintenance Committee, and CMMS Governance Committee to ensure transparency, alignment, and continuous improvement.

Graphic reference: `332_007CAM_3`.

## Reuse guidance

Universal: the "your data is already good, it is just dispersed" diagnosis; the commitment that sensors come bundled with the technology rather than as a separate hardware ask; the automated-ruleset chain (alert → work order → condition rating → PM optimization); and routing insights through standing joint committees. Pursuit-specific: the critical-asset list, the client's committee names, and the cybersecurity exhibit citation. Pairs with [Roles and Responsibilities for a Disciplined PdM Program](mmsd-pdm-roles-and-responsibilities.md), [Levels 1–3 PdM Framework](mmsd-pdm-levels-1-3-framework.md), and [Level 3 PdM Integration with SCADA and the CMMS](mmsd-level3-pdm-integration-scada-cmms-and-considerations.md).
