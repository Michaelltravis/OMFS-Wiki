---
title: "Exhibit — Prioritized Asset Types for Continuous PdM Monitoring"
category: technical-approach
block-type: table
tags: [predictive-maintenance, reliability-engineering, asset-management, instrumentation-controls, technical-approach, exhibit, table-layout]
source: mmsd-om-2028
source-section: "IV.D. Potential Additive Work – Level 3 PdM — Exhibit IV-61. Summary of Prioritized Asset Types for Continuous PdM Monitoring"
source-pages: [133]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0133.md#¶8", "verbatim/mmsd-om-2028/pages/p0133.md#¶7"]
pursuit-type: [wwtp-om, multi-facility, solids, collections]
client-type: authority
client-size: "Two large water reclamation facilities + regional conveyance system + biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [asset-management, innovation-value-add, digital-tools]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:32.4-1-proposed-pdm-technologies-for-mmsd-s-treatment-facilitie
section-order: 4
section-path: IV. Approach Summary › IV.D. Potential Additive Work – Level 3 PdM › 4. JACOBS’ RECOMMENDED LEVEL 3 PdM PLAN › 4.1. Proposed PdM Technologies for MMSD’s Treatment Facilities
doc-order: 227
volatility: evergreen
review-due: 2029-01-29
freshness-flags: []
context: "Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production and regional conveyance, 2028 challenger bid against an incumbent operator; WDNR."
quality: "A criticality-tiered monitoring plan that names the equipment, the parameter to be trended, and the specific sensor or analysis for each — the artifact that proves a PdM offer was engineered against the client's asset base rather than sold from a catalog."
reuse-notes: "Re-tier the equipment list against the target facility's own criticality rankings; the three-tier structure and the four-column format carry over unchanged. Confirm sensor types against what the target plant's PLCs and historian can actually route."
---

# Exhibit IV-61 — Summary of Prioritized Asset Types for Continuous PdM Monitoring

Based on our analysis of the water reclamation facilities' assets, we've identified and prioritized the types of assets where continuous monitoring is most beneficial based on asset criticality. We'll work with [CLIENT], a regional sewerage district operating two large water reclamation facilities and a regional conveyance system, to confirm the final selection of assets for Level 3 PdM deployment.

|**Tier**|**Equipment**|**Key Parameters**|**Recommended Sensors & Analysis**|
|---|---|---|---|
|**1**|Gas Compressors|Vibration; temperature; pressure; motor current|Vibration sensors; Resistance temperature detectors (RTDs)/thermocouples; pressure transducers; current sensors; oil analysis; infrared analysis|
|**1**|Blowers|Vibration; airflow; motor current|Vibration sensors; airflow meters; current sensors; oil analysis; motor current signature analysis; IR analysis|
|**1**|RAS Pumps|Flow; torque; motor health|Flow meters; torque sensors; motor current sensors; motor current signature analysis|
|**1**|WAS Pumps|Flow; pressure; motor load|Flow meters; pressure sensors; current sensors; motor current signature analysis|
|**1**|Lift / Influent Pumps|Vibration; flow; seal integrity|Vibration sensors; flow meters; seal leakage sensors; IR analysis|
|**2**|Aeration Blowers|Vibration; airflow; motor current|Vibration sensors; airflow meters; current sensors; oil analysis; motor current signature analysis|
|**2**|Chemical Feed Pumps|Flow accuracy; pump health|Flow meters; pressure sensors; motor current sensors|
|**2**|Mixers & Agitators|Torque; vibration|Torque sensors; vibration sensors; infrared analysis|
|**3**|HVAC Compressors & Chillers|Temperature; vibration|RTDs/thermocouples; vibration sensors; IR analysis|
|**3**|Backup Generators|Load; fuel level; vibration|Load sensors; fuel level sensors; vibration sensors; oil analysis; IR analysis|
|**3**|Conveyors & Dewatering Equipment|Motor current; alignment|Current sensors; alignment sensors; motor current signature analysis|

## Reuse guidance

Universal: the table itself as a device — tier, equipment, parameters, sensors — and the tiering logic that puts gas compressors, blowers, RAS/WAS pumps, and influent pumps in Tier 1. Pursuit-specific: which equipment exists at the target facility and where each falls in the client's own criticality ranking. Pairs with [Recommended Level 3 PdM Technologies for the Treatment Facilities](mmsd-level3-pdm-technologies-treatment-facilities.md) and [Level 3 PdM Integration with SCADA and the CMMS](mmsd-level3-pdm-integration-scada-cmms-and-considerations.md). Read `verbatim/mmsd-om-2028/pages/p0133.md#¶8` for the source table.
