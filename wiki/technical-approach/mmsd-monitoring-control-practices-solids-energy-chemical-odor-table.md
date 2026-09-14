---
title: Monitoring and Control Practices Table — Solids, Energy, Chemical, and Odor
category: technical-approach
block-type: table
tags: [biosolids, energy-management, chemical-management, odor-control, process-control, predictive-maintenance, scada, technical-approach, table-layout, cost-savings]
source: mmsd-om-2028
source-section: "IV.A.2.2. Effective Process Monitoring and Control — Exhibit IV-15"
source-pages: [57]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0057.md#¶6"]
pursuit-type: [wwtp-om, solids, multi-facility]
client-type: authority
client-size: "Two large WRFs / 4,800-mi collection network / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [energy-chemical-efficiency, odor-control, asset-management, digital-tools]
proof-point-ids: [PP-2148, PP-2969]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
context: Midwest US regional sewerage district, two large water reclamation facilities (Jones Island and South Shore) plus biosolids production, RFP P-3216, 2028 challenger bid vs. incumbent operator; WDNR
quality: 'Concrete, operator-level control strategies for the four cost-and-complaint drivers: solids/pellet production, energy, chemicals, and odor. Carries a hard operating target (blended sludge total solids above 3.25%) and a demand-charge and energy-purchasing angle that most competitors do not address.'
reuse-notes: Retain rows only for processes the pursuit actually has (thermal drying, turbines, digester gas, carbon scrubbers); the 3.25% blended sludge total solids target is specific to this facility's dewatering and drying train and must be re-derived for another plant.
---

# Monitoring and Control Practices Table — Solids, Energy, Chemical, and Odor

**EXHIBIT IV-15** (part 2 of 2)

|**Focus Areas**|**Monitoring and Control Practices**|**Example Control Strategies and Their Benefits**|
|---|---|---|
|**Solids Processing & Biosolids Product Production**|▪ Continuous tracking of thickening and dewatering performance, polymer dosing, filtrate quality.<br>▪ Maintain blended sludge total solids (TS) concentration above 3.25% which will lead to higher TS in dewatered cake.<br>▪ Dryer feed solids, temperatures, oxygen, exhaust parameters, and pellet quality indicators.<br>▪ Interplant pumping system (IPS) solids transfer monitoring, valve position feedback, and routing control logic.<br>▪ Condition monitoring of pumps, conveyors, mixers, dryers, turbines.|▪ Optimize thickening and dewatering using mass-based polymer pacing to increase cake solids and reduce chemical use.<br>▪ Adjust digester feed and temperature profiles to maximize biogas while maintaining downstream pellet specifications.<br>▪ Coordinate IPS transfers based on digester loading, dryer capacity, and energy availability.<br>▪ Regulate dryer feed rate, %TS, and recycle ratios to ensure product quality and minimize energy use.<br>▪ Maximize turbine heat recovery to reduce natural gas consumption.|
|**Energy Optimization**|▪ Monitoring digester gas flow/quality, mixing, temperature, pressure; flare and turbine usage.<br>▪ Real-time monitoring of energy use across aeration, pumping, future UV disinfection, heating, drying, and digester systems.<br>▪ Load profiling and demand-charge monitoring.<br>▪ Power quality tracking at motor control centers, blowers, and high-HP pumps.<br>▪ Integration of Intelligent O&M analytics for optimization.|▪ Optimize aeration through blower VFD control, valve balancing, and basin-level airflow distribution.<br>▪ Manage peak demand by staging pumping and other high-energy processes.<br>▪ Optimize dryer heat recovery and turbine utilization based on gas availability and energy pricing.<br>▪ Operate pumps near best efficiency point using VFDs and level-based sequencing.<br>▪ Use Energy Purchasing Subcommittee protocols to reduce exposure to price volatility.|
|**Chemical Optimization**|▪ Monitoring chemical storage levels.<br>▪ Online analyzers for chlorine, ammonia, phosphorus, and dechlorination residuals.<br>▪ Monitoring ferric/ferrous chemicals for total phosphorus removal and odor mitigation.<br>▪ SCADA integration for dose-flow pacing and cost tracking.|▪ Automated disinfection and dechlorination pacing to minimize overdosing and maintain permit compliance.<br>▪ Polymer dose optimization using mass-basis pacing and filtrate quality feedback.<br>▪ Chemically enhanced primary treatment (CEPT) adjustments during wet weather to enhance solids capture and protect secondary systems.<br>▪ Use Intelligent O&M algorithms to reduce chemical consumption and stabilize biological processes.|
|**Odor Control**|▪ Carbon monitoring for breakthrough; differential pressure and runtime tracking.<br>▪ Influent sulfide monitoring combined with atmospheric monitoring and dispersion modeling for odor-risk prediction.<br>▪ Tracking odor complaints, investigations, and mitigation protocols.|▪ Trigger granular activated carbon changeouts based on breakthrough trends.<br>▪ Increase ventilation or adjust airflow patterns during peak odor periods.<br>▪ Implement seasonal odor profiles and rapid response protocols.<br>▪ Use upstream process data to identify and correct root odor drivers (e.g., industrial loads, long detention times).|

## Reuse guidance

Universal: mass-based polymer pacing, demand-charge management by staging high-energy processes, carbon changeout on breakthrough trend rather than calendar, and the odor row's "correct root odor drivers upstream" logic — all travel to any wastewater pursuit. Pursuit-specific: the 3.25% blended sludge TS target, thermal-drying and turbine content, the Energy Purchasing Subcommittee, and the pending UV system. Continues [Monitoring and control practices — conveyance, wet weather, and liquid processes](mmsd-monitoring-control-practices-conveyance-liquid-table.md).
