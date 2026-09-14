---
title: Monitoring and Control Practices Table — Conveyance, Wet Weather, and Liquid Processes
category: technical-approach
block-type: table
tags: [process-control, wet-weather, collection-systems, lift-stations, scada, sampling-monitoring, wastewater-treatment, cybersecurity, technical-approach, table-layout]
source: mmsd-om-2028
source-section: "IV.A.2.2. Effective Process Monitoring and Control — Exhibit IV-15"
source-pages: [56]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0056.md#¶8"]
pursuit-type: [wwtp-om, multi-facility, collections]
client-type: authority
client-size: "Two large WRFs / 4,800-mi collection network / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [collection-system, compliance-leadership, digital-tools, energy-chemical-efficiency]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:24.odor-control
section-order: 1
context: Midwest US regional sewerage district, two large water reclamation facilities (Jones Island and South Shore) plus biosolids production, RFP P-3216, 2028 challenger bid vs. incumbent operator; WDNR
quality: A two-column "what we monitor / what we do with it" table that proves operating depth without narrative bulk. Names specific instruments, models, alarm classes, and control strategies — including CSO/SSO trade-off logic for storage tunnel operation — which is exactly the specificity evaluators score.
reuse-notes: Keep the column structure (Focus Area / Monitoring and Control Practices / Example Control Strategies and Their Benefits) and replace the rows with the pursuit's assets; hydraulic model names and permit program acronyms must match the pursuit's state and tools.
---

# Monitoring and Control Practices Table — Conveyance, Wet Weather, and Liquid Processes

**EXHIBIT IV-15. SUMMARY OF JACOBS' PROCESS MONITORING AND CONTROL PRACTICES FOR THE KEY OPERATIONAL FOCUS AREAS OF [CLIENT]'S FACILITIES** (part 1 of 2)

|**Focus Areas**|**Monitoring and Control Practices**|**Example Control Strategies and Their Benefits**|
|---|---|---|
|**Collection System, Tunnels and Wet Weather Flow Management**|▪ Real-time monitoring of metropolitan interceptor system (MIS)/ISS levels, flows, velocities, pump station performance, gate positions, and force main pressures.<br>▪ Integration of rainfall radar, forecast models, WATS/PCSWMM hydraulic tools.<br>▪ SCADA alarming for high-level events, pump fails, infiltration anomalies, power quality, and communication loss.<br>▪ Routine MIS/ISS readiness verification, pump availability checks, and forecast-based operating protocols. Managing the ISS system is critical to knowing when to activate combined sewer overflows (CSOs) and reserve tunnel capacity to avoid sanitary sewer overflows (SSOs).<br>▪ Drop shaft event monitoring and sampling compliant with Wisconsin Pollutant Discharge Elimination System (WPDES).<br>▪ Cybersecurity network segmentation and monitoring.|▪ Predictive inflow and infiltration (I/I) identification using long-term trends and anomaly detection.<br>▪ Optimize ISS pre-storm drawdown and pump sequencing to maximize storage and reduce CSOs.<br>▪ Deragging logic, variable frequency drive (VFD) control, and condition-based maintenance of pumps.<br>▪ Dynamic control of flow routing between the two WRFs based on available capacity.<br>▪ Wet-weather operating playbook, including tunnel pump triggers, clarifier/hydraulic protection steps, and post-storm dewatering coordination.<br>▪ Automated dropshaft sampling and event logging supporting WPDES requirements.|
|**WRF Wet Processes**|▪ Continuous monitoring of influent flow, screening differentials, grit removal efficiency, clarifier blankets.<br>▪ Online analyzers.<br>▪ Automated chlorine/chloramine and dechlorination dosing tied to flow/residual sensors.<br>▪ Once UV disinfection is operational, monitor and control by continuously measuring UV intensity, UV transmittance, and flow, then automatically adjusting lamp output and bank operation through SCADA to maintain the required dose while tracking lamp status, cleaning systems, and safety interlocks.<br>▪ Shared dashboards across both WRFs for hydraulic and biological load balancing.<br>▪ Process alarms for nutrient stress, solids washout risks, aeration failures, polymer feed issues.<br>▪ Compliance sampling per WPDES.|▪ Advanced dissolved oxygen (DO) control to reduce energy consumption.<br>▪ Selector zone optimization (e.g., intermittent mixing, RAS nitrate control, carbon management) to improve settleability and enhanced biological phosphorus removal (EBPR) reliability.<br>▪ Solids retention time (SRT), wasting, and return flows adjusted to stabilize clarifiers during wet weather.<br>▪ Automated disinfection and dechlorination control to ensure permit residual compliance.<br>▪ Use intelligent analytics to adjust aeration, wasting, and energy use.|

## Reuse guidance

Universal: the monitoring/strategy column pairing, the CSO-versus-SSO trade-off statement, the UV control description (usable wherever a UV system is being commissioned), and the shared-dashboard row for any multi-plant pursuit. Pursuit-specific: asset names, hydraulic model names, and the state permit program. Continues in [Monitoring and control practices — solids, energy, chemical, and odor](mmsd-monitoring-control-practices-solids-energy-chemical-odor-table.md); introduced by [Process monitoring and control for system-wide insight](mmsd-process-monitoring-control-system-wide-insight.md).
