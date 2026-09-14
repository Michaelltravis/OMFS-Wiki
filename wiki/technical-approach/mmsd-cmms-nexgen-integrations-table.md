---
title: "Exhibit — Process and Benefits of CMMS Integrations with Jacobs' Technology Systems"
category: technical-approach
block-type: table
tags: [cmms, nexgen-eam, digital-tools, scada, predictive-maintenance, asset-management, exhibit, technical-approach]
source: mmsd-om-2028
source-section: "IV.C. Computerized Maintenance Management System (CMMS) Approach — 3.4 Integrations Required by Jacobs (Exhibit IV-59)"
source-pages: [129]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0129.md#¶12", "verbatim/mmsd-om-2028/pages/p0129.md#¶14", "verbatim/mmsd-om-2028/pages/p0129.md#¶19"]
pursuit-type: [wwtp-om, multi-facility, collections, solids]
client-type: authority
client-size: "Two large water reclamation facilities + regional conveyance system + biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [digital-tools, asset-management, innovation-value-add]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
context: "Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production and regional conveyance, 2028 challenger bid against an incumbent operator; WDNR."
quality: "A concrete, named integration map — client systems on one side, Jacobs digital tools on the other, direction of data flow and the decision each integration supports. It answers the 'what will you actually connect?' question that generic digital-tools language never does."
reuse-notes: "Replace the client-side system names with the target utility's stack and confirm which Jacobs tools are contracted for that pursuit. Direction of flow (one-way vs. two-way) should be re-verified with the CMMS vendor. The source is a graphic (asset ID 329_007CAM_3) whose column pairings are partially reconstructed from the text layer — verify against the PDF render before external use."
---

# Exhibit IV-59 — Process and Benefits of CMMS Integrations with Jacobs' Technology Systems

Jacobs has identified candidate integrations shown in **Exhibit IV-59** to enhance the NexGen implementation with technology systems our O&M team use to inform decision making:

| Systems | Integration direction | Purpose and benefit |
|---|---|---|
| ArcGIS; work order data; advanced asset registry; PM data | Two-way integration to NexGen | Exchange work order scheduling details and labor, asset, parts/warehouse, PM, and cost data for use in scheduling, work order analysis, and PM optimization and to monitor work orders, safety, compliance, and sustainability |
| Oracle (purchase orders) | One-way interface from NexGen | For purchase orders, to obtain financial and work order data |
| Augury / Artesis (PdM) | One-way integration to NexGen | For PdM — upload vibration analysis results and motor current analysis data |
| Fleet / vehicle software | Two-way integration with NexGen | For vehicle data |
| Dragonfly / Argon (CCTV inspections) | One-way interface to NexGen | For CCTV inspection data analysis — upload CCTV inspection results into NexGen |

Client-side systems shown in the exhibit include ArcGIS, Bentley, Solar Online AI, Ion City, Hach (WIMS), iFIX SCADA, metering, OnBase, Trimble Unity (drawings/manuals), and Oracle. Jacobs-side systems shown include the advanced asset registry, PdM platforms (Augury / Artesis), fleet software, Dragonfly / Argon CCTV inspection, and Construct. The exhibit legend distinguishes [CLIENT] systems from Jacobs systems.

Graphic reference: `329_007CAM_3`.

## Reuse guidance

Universal: the integration-map device itself — name the systems, the direction, and the decision each feed supports. Pursuit-specific: every system name and every flow direction. Pairs with [Differentiating Strength in CMMS Implementation](mmsd-cmms-differentiating-strength-and-nexgen-experience.md) and [Level 3 PdM Integration with SCADA and CMMS](mmsd-level3-pdm-integration-scada-cmms-and-considerations.md). Read `verbatim/mmsd-om-2028/pages/p0129.md` and the PDF render before reproducing the exhibit.
