---
title: Phase 2 — "SCADA You Can Trust" Monitoring, Planning, and Process Refinement
category: technical-approach
block-type: prose
tags: [process-control, scada, instrumentation-controls, data-analytics, maintenance-program, wet-weather, compliance-leadership]
source: ocwut-16-26
source-section: "Operations Plan, SCADA/Operational Technology (OT)/Cybersecurity — Phase 2"
source-pages: [46]
verbatim-ref: ["verbatim/ocwut-16-26/pages/p0046.md#¶13", "verbatim/ocwut-16-26/pages/p0046.md#¶14", "verbatim/ocwut-16-26/pages/p0046.md#¶18"]
pursuit-type: [wwtp-om, multi-facility]
client-type: trust
client-size: ">110 MGD combined / 4 WWTPs + 1 major pump station / 109 FTE"
geography: "Southcentral / OK / ODEQ"
rfp-section-type: [tech-approach]
win-theme-map: [incumbent-displacement, compliance-leadership, digital-tools, asset-management, innovation-value-add]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: true
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
context: Southcentral US municipal water utility trust wastewater O&M competitive procurement, 2026 award for Jan 1 2027 start; four WWTPs plus one major pump station, >110 MGD combined design capacity, Class B biosolids land application, 109 FTE proposed; challenger bid against an underperforming incumbent operator, backed by a 20-year engineering relationship; ODEQ regulatory regime.
quality: The strongest incumbent-displacement device in this section — site-visit observations of inaccurate, disconnected, or invisible instrumentation are converted into an end-to-end control-path validation commitment and the memorable "SCADA you can trust" phrase, tied to wet-weather recovery and compliance.
reuse-notes: The site-visit observations are evidence gathered on this pursuit; substitute observations actually made during the new pursuit's site visits, or reframe as a first-90-days verification commitment if no site visit occurred. The sensor to I/O to PLC logic to communications/historian to HMI validation chain, the verification-based maintenance idea, and the equipment anomaly program are fully portable. "SCADA you can trust" is a reusable headline.
---

# Phase 2 — "SCADA You Can Trust" Monitoring, Planning, and Process Refinement

During our site visits, we observed instances where critical instrumentation (DO, flow, and device status) that was inaccurate, disconnected, or not visible in SCADA, directly limiting effective process control. Phase 2 will involve validating each control path end to end (sensor → I/O → PLC logic → communications/historian → HMI), correcting application issues, and implementing verification-based maintenance. The result will be **"SCADA you can trust" — reliable information for risk-informed decisions in routine operations and high-stress wet-weather events**, particularly at [FACILITY A], where post-event recovery and compliance have been challenging. Trusted data shortens recovery time, protects compliance, and lowers operational cost.

Phase 2 will translate the shared understanding established in Phase 1 into repeatable, dependable day-to-day performance. The objective is to reduce operational variability and risk by clearly:

- Defining how each facility should operate under all realistic conditions
- Ensuring assets and control systems are configured to support those operating modes
- Confirming operational decisions are based on trusted, qualified data

**Process planning, refinement, and monitoring.** Our team will formalize how each process area should operate across normal and non-normal conditions (equipment downtime, construction tie-ins, influent and IPP changes, wet-weather events, chemical adjustments) and align equipment configuration, control narratives, and interlocks with those plans. Where gaps exist, we'll refine control strategies or adjust monitoring elements so operating plans stay executable, resilient, and consistent with [CLIENT] standards. In parallel, we'll establish data integrity from field device through PLC, SCADA, and operator interface by validating instrument installation, tightening calibration and PM verification routines, and requesting SCADA interface modifications so critical information displays clearly. An equipment anomaly program that ties together operator rounds, PM, SCADA-based condition monitoring, and alarm management will cut nuisance alarms and flag drift earlier.

## Reuse guidance

Universal: the end-to-end control path validation chain, verification-based maintenance, the three-part Phase 2 objective (define operating modes, configure assets to support them, qualify the data behind decisions), and the equipment anomaly program combining rounds, PM, condition monitoring, and alarm management. Pursuit-specific: the site-visit findings and the named facility with wet-weather recovery problems. Sits between `ocwut-process-control-phased-improvement-plan-phase-1-baseline.md` and `ocwut-process-control-phase-3-automation-integration.md`. Read `verbatim/ocwut-16-26/pages/p0046.md#¶13` for the full passage.
