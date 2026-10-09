---
title: Tunnel and Inline Storage System Operations Monitoring and Wet Weather Coordination
category: technical-approach
block-type: prose
tags: [wet-weather, process-modeling, data-analytics, scada, energy-management, performance-reporting, technical-approach, process-optimization, collection-systems, digital-tools]
source: mmsd-om-2028
source-section: "Section IV, 2.6.3. Tunnel System Operations; 2.7.6. Wet Weather Coordination and System Modeling"
source-pages: [84, 89]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0084.md#¶9", "verbatim/mmsd-om-2028/pages/p0089.md#¶4"]
pursuit-type: [wwtp-om, collections, multi-facility, stormwater]
client-type: authority
client-size: "2 large WRFs / deep tunnel ISS / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [collection-system, digital-tools, compliance-leadership, energy-chemical-efficiency, innovation-value-add]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:25.2-6-3-tunnel-system-operations
section-order: 28
section-path: IV. Approach Summary › IV.A. Approach to Management, Operations, PM, and CM › IV.A.6. Responding to Public Odor Complaints › 2.6. Monitoring, Tracking, and Reporting Operational Parameters › 2.6.3. Tunnel System Operations
doc-order: 155
volatility: evergreen
review-due: 2029-01-29
freshness-flags: []
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; state DNR regulatory regime
quality: The best available treatment of deep-tunnel/inline-storage operations as a monitored, modeled, and post-event-reported process rather than a reactive one. Ties CSO capture, energy cost, and digital twin evaluation into one loop, and names the specific post-event report contents (captured volume, pump-out rate, overflow prevention, energy utilization).
reuse-notes: Only for clients with storage tunnels, deep tunnels, equalization basins, or a CSO/SSO storage asset. For systems without storage, keep the post-event reporting structure and the weather-forecast-driven optimization but recast around wet-weather flow routing and peak-flow treatment. Dewatering pump energy is called out as a top shared-cost driver here; verify that framing applies before repeating it.
---

# Tunnel and Inline Storage System Operations Monitoring

[CLIENT]'s inline storage system (ISS) plays a vital role in controlling combined sewer overflows (CSOs) and maintaining system reliability. **Jacobs will integrate ISS performance parameters into the broader operational monitoring framework.** The system will continuously monitor tunnel water levels, pump station flows, and gate positions through **SCADA integration**. Predictive modeling will assess **hydraulic performance and storage utilization**, using weather forecast data to optimize system operations during wet-weather events. Real-time tracking of energy use and runtime for tunnel dewatering pumps will provide visibility into one of the largest contributors to shared power costs. After each event, Jacobs will prepare post-event reports summarizing captured volume, pump-out rate, overflow prevention, and energy utilization. Tunnel operations data will also feed into the **digital twin model** to evaluate alternative control strategies and support long-term optimization. This integrated approach will enable coordinated decision-making across treatment plants, conveyance, and storage, maximizing CSO capture efficiency while minimizing cost and energy use.

## Wet weather coordination and system modeling

Jacobs will use real-time hydraulic and treatment-performance data to coordinate wet-weather operations across the ISS, conveyance system, and both water reclamation facilities. Monitoring tunnel capacity, pump back timing, and plant loading will allow operators to manage flows effectively, reduce the risk of combined sewer overflows, and maintain high treatment efficiency during storm events.

## Reuse guidance

Universal: the closed loop — monitor in SCADA, model ahead using forecast data, operate, then report the event against four fixed metrics and feed the result back into the twin. Committing in advance to a post-event report with named contents is a strong transparency device and travels to any wet-weather pursuit.

Pursuit-specific: the storage asset itself, the regulatory driver (CSO here; an SSO consent decree, a stormwater permit, or a peak-flow limit elsewhere), and whether a digital twin actually exists or is being proposed. Do not imply an existing model where one would have to be built — say which, and put the build in the transition or value-add section.

Read `verbatim/mmsd-om-2028/pages/p0084.md` and `verbatim/mmsd-om-2028/pages/p0089.md` for the full passages. Pairs with [Integrated performance management framework](mmsd-integrated-performance-monitoring-framework.md) and [Holistic, systems-based One Water One Team approach](mmsd-holistic-systems-based-one-water-one-team.md).
