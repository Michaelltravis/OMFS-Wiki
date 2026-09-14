---
title: MBR Process Optimization Approach with Calibrated Digital Process Modeling (BioWin/Pro2D/Replica)
category: technical-approach
block-type: prose
tags: [process-optimization, membrane-treatment, process-modeling, digital-tools, wastewater-treatment, lift-stations]
source: santamonica-swip-om-2025
source-section: "2.4 Firm Approach A - Process Optimization; Addressing Other Potential Process Impacts"
source-pages: [36, 37]
verbatim-ref: ["verbatim/santamonica-swip-om-2025/pages/p0036.md#¶4", "verbatim/santamonica-swip-om-2025/pages/p0036.md#¶8", "verbatim/santamonica-swip-om-2025/pages/p0036.md#¶9", "verbatim/santamonica-swip-om-2025/pages/p0037.md#¶3", "verbatim/santamonica-swip-om-2025/pages/p0037.md#¶7"]
pursuit-type: [reuse-dpr, water-treatment, wwtp-om]
client-type: municipal
client-size: "Advanced water treatment facility (MBR/RO/UV-AOP) + urban-runoff water recycling facility + lift stations + stormwater diversion/storage; coastal municipal potable-reuse program"
geography: "Southern California / CA / SWRCB Division of Drinking Water (Title 22) + Cal/OSHA"
rfp-section-type: [tech-approach]
win-theme-map: [innovation-value-add, digital-tools, asset-management, energy-chemical-efficiency]
proof-point-ids: [PP-0439, PP-0440, PP-0441]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: true
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: santamonica-swip-om-2025:08.observations-and-understanding-of-the-city-s-operations
section-order: 6
section-path: 'Section 2: Qualifications › 2.4 FIRM APPROACH › PROCESS CONTROL › Observations and Understanding of the City’s Operations'
doc-order: 34
context: Southern California advanced water treatment / potable reuse facility O&M, 2025, incumbent (Veolia) displacement
quality: Combines a technically credible MBR optimization methodology (weekly bug counts; SRT, MLSS, DO, ORP, ammonia, nitrate, pH, and suspended-solids monitoring; KPI development) with named proprietary modeling tools and direct access to national subject matter experts - operator-level discipline plus enterprise-level depth.
reuse-notes: The MBR parameters apply directly to any MBR facility; substitute the relevant process-control parameters for other treatment trains. The lift-station monitoring language suits any pursuit with a critical upstream pump station. The page-46 digital-tools and Replica(TM) Digital Twin passage that used to close this block now lives in swip-replica-digital-twin-plant-digital-tools.md.
---

# MBR Process Optimization Approach with Calibrated Digital Process Modeling (BioWin/Pro2D/Replica)

## Observations and understanding of current operations

The facility's advanced water treatment facility (AWTF) is currently operating as designed, with treatment processes performing effectively. Jacobs has observed that the MBR system in particular offers continued opportunities for optimization, especially as biological conditions evolve and influent characteristics vary. Weekly microscopic evaluations (bug counts), continuous instrumentation readings, and in-house laboratory analyses provide a strong foundation for performance-based decision-making. These tools enable Jacobs to proactively adjust operational parameters, ensuring the MBR consistently produces a high-quality effluent while operating at maximum efficiency.

## Jacobs' approach to process optimization at the AWTF

Jacobs will apply a comprehensive, data-driven strategy to continuously evaluate and optimize the performance of all treatment processes at the AWTF. This approach includes the development of KPIs for process units, allowing operators to assess system performance and identify when operational adjustments are warranted.

In the MBR system, Jacobs will focus on controlling solids retention time (SRT), mixed liquor suspended solids (MLSS), and sludge age to maintain optimal biological activity. Weekly bug counts, SRT calculations, and continuous monitoring of parameters such as dissolved oxygen (DO), oxidation-reduction potential (ORP), ammonia (NH3), nitrate (NO3), pH, and suspended solids (SS) will inform operational strategies. This holistic monitoring program will enable Jacobs to maintain a highly filterable mixed liquor, ensuring membrane longevity and reducing cleaning frequencies.

To support advanced decision-making, Jacobs will build and maintain a calibrated digital process model of the AWTF. Drawing from Jacobs' extensive suite of modeling tools — such as BioWin and Jacobs' proprietary Pro2D and Replica(TM) tools — Jacobs will select and tailor the most appropriate model to the facility's influent conditions and treatment processes. This model will be updated regularly with site-specific data and used to simulate operational changes before implementation. For example, the model can evaluate energy savings and nitrogen removal improvements associated with reducing the dissolved-oxygen setpoint in the aeration basin.

As a fully integrated engineering and operations firm, Jacobs also provides direct access to national subject matter experts in membrane bioreactors, process modeling, process control, and advanced analytics. Operations staff collaborate regularly with these experts to troubleshoot challenges, test innovations, and apply best practices — ensuring the facility benefits from the most current and effective approaches in the industry.

**Benefits:** Jacobs' process optimization strategy delivers measurable operational, environmental, and financial benefits. By maintaining biological stability and proactively adjusting process conditions, Jacobs helps extend membrane life, reduce chemical consumption, and lower energy costs. The use of a calibrated process model allows client staff to visualize operational trade-offs and make data-informed decisions. In addition, Jacobs' ability to engage in-house experts across engineering, operations, and data science ensures continuous advancement in process performance and technology application. This integrated approach ensures the AWTF remains flexible, resilient, and capable of achieving regulatory compliance while supporting the client's long-term sustainability goals.

## Addressing other potential process impacts (critical lift station monitoring)

Jacobs recognizes the critical role of the upstream lift station in delivering up to 100% of the flow to the AWTF. To ensure uninterrupted operation and protect system reliability and water quality, Jacobs will implement monthly contractor inspections and preventive maintenance routines. These inspections target mechanical integrity, pump efficiency, and system cleanliness to mitigate risk and avoid costly disruptions.

In addition, Jacobs will perform ongoing reviews and continuous monitoring of the station's alarm and control systems to maintain stable flow conditions and support rapid response to any deviations. These efforts enhance operational resilience at the AWTF and ensure compliance with permit and regulatory performance standards.

To further minimize impacts from lift-station operations, Jacobs will deploy its proprietary AquaDNA DeRagger tool at the lift station (see `swip-aquadna-deragger-technology.md` for full detail). This AI-based tool optimizes pump performance, reduces clogging events, and supports energy efficiency.

The digital-tools and Replica(TM) Digital Twin half of this story (page 46 of the source proposal) now lives in its own block: see [swip-replica-digital-twin-plant-digital-tools.md](swip-replica-digital-twin-plant-digital-tools.md).

## Reuse guidance

The MBR-specific monitoring parameters (bug counts, SRT, MLSS, DO, ORP, NH3, NO3, pH, SS) and the calibrated digital-process-model concept (BioWin/Pro2D/Replica(TM)) are broadly reusable for any MBR-based treatment facility; adapt the parameter list for other treatment technologies (e.g., activated sludge without membranes, fixed-film processes). The lift-station monitoring language is reusable for any pursuit with a critical upstream pump/lift station feeding the primary treatment facility. The "up to 100% of flow" framing for the upstream lift station is specific to this pursuit's hydraulic configuration — verify the equivalent dependency at the target facility before restating it. Pair with `swip-aquadna-deragger-technology.md` (the lift-station technology solution referenced here), `swip-process-control-system-tools.md` (the CPCS/UPCP framework this optimization program feeds into), and `swip-innovation-value-added-offerings-overview.md` (which catalogs this as one of several value-added tools). Related graphic: Exhibit 2-17, "Example of the Jacobs Replica(TM) Tool's Capabilities for Optimization" (asset ID `154_008A26`, labeled as a generic example facility, not client-specific, reusable as-is; see graphics catalog, source `santamonica-swip-om-2025`).
