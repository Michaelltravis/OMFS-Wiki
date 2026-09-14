---
title: Intelligent Dry Weather Management of Interceptors and Pump Stations
category: technical-approach
block-type: prose
tags: [collection-systems, lift-stations, predictive-maintenance, data-analytics, digital-tools, inflow-infiltration, process-modeling, scada, technical-approach, key-personnel]
source: mmsd-om-2028
source-section: "IV.A.2.2.1. Collection System, Tunnels, and Wet Weather Flow Management - Focus Area"
source-pages: [58, 59]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0058.md#¶8", "verbatim/mmsd-om-2028/pages/p0059.md#¶4", "verbatim/mmsd-om-2028/pages/p0058.md#¶13"]
pursuit-type: [wwtp-om, collections, multi-facility]
client-type: authority
client-size: "Two large WRFs / 4,800-mi collection network / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [collection-system, digital-tools, asset-management, regional-bench, odor-control]
proof-point-ids: [PP-2149, PP-2970, PP-2974]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:24.intelligent-dry-weather-management
section-order: 1
context: Midwest US regional sewerage district, two large water reclamation facilities (Jones Island and South Shore) plus biosolids production, RFP P-3216, 2028 challenger bid vs. incumbent operator; WDNR
quality: The clearest AquaDNA write-up in the library — it explains the anomaly-detection use case, pairs it with a real proof exhibit from Wilmington, DE (a dry-weather CSO caught and cleared after an alert), and extends it to amp-draw-based deragging that keeps pumps online before a fault requires a crew. Also names the local modeling bench.
reuse-notes: Scale the sensor count to the pursuit's instrumentation; the Wilmington, DE exhibit and the Mead & Hunt study reference are real past performance and stay verbatim; substitute the named local experts and the hydraulic models (WATS, PCSWMM) with those the pursuit team will actually use.
---

# Intelligent Dry Weather Management of Interceptors and Pump Stations

*Intelligent Dry Weather Management.* We'll manage dry-weather operations with proactive maintenance, close monitoring, and predictive tools to keep the metropolitan interceptor system (MIS) and inline storage system (ISS) ready. Using SCADA data from 250+ real-time flow meters and level sensors, we'll find inflow and infiltration (I/I) trends and work with [CLIENT] to evaluate future use of AquaDNA (a digital tool for anomaly detection) and predictive maintenance (PdM). **Exhibit IV-16** shows an example of wet weather and dry weather alerts used at Wilmington with AquaDNA. Over time, integrating CMMS, SCADA, IoT sensors, and analytics will give operators a clearer, real-time picture of system capacity and asset health. We'll operate all pump stations for reliability and efficiency using structured preventative maintenance (PM), vibration and electrical testing, wet well maintenance, and targeted improvements such as deragger sensors at high-ragging sites. Our AquaDNA deragging technology can clear blockages based on monitoring amp draws and keep pumps online before a fault occurs that requires hands on repair.

If complex issues arise, our national pump station team will back up the local team. Our local technical experts, including **John Siczka** and our partners **Amy Post** and **Nick Tecca** from Mead & Hunt, will support dry weather operational analysis, leveraging their deep familiarity with [CLIENT]'s hydraulics and modeling tools. From Day 1, they'll apply process and hydraulic modeling tools like WATS and PCSWMM, incorporating insights from the August 2025 "Impact of Water Levels on District Conveyance System Assets" written by Mead & Hunt. During dry weather, system knowledge will be key to preventing odors by making sure stagnant flow and significant flow drops are minimized, as discussed further in *Section 2.2.6*.

**EXHIBIT IV-16. VIEW OF WET-WEATHER AND SUBSEQUENT DRY-WEATHER CSO THAT WAS CLEARED FOLLOWING ALERT FROM AQUA DNA IN WILMINGTON, DE.** Level sensor readings plot a wet weather event, an Aqua DNA dry overflow warning, a crew clearing the system blockage, and collection system flow returning to baseflow, annotated against CSO overflow level and baseflow level. *Aqua DNA alarm allowed for quick system blockage identification and clearance.*

## Reuse guidance

Universal: the dry-weather readiness argument (dry weather is when you earn wet-weather performance), the AquaDNA anomaly-detection and amp-draw deragging description, the Wilmington DE exhibit as third-party proof, and the link from dry-weather flow management to odor prevention — a connection most competitors miss. Pursuit-specific: sensor counts, local expert names and teaming partner, and the referenced client study. Pairs with [Collection system, tunnels, and wet weather flow management](mmsd-collection-system-tunnels-wet-weather-focus-area.md) and [Effective and efficient wet weather operations](mmsd-effective-efficient-wet-weather-operations.md).
