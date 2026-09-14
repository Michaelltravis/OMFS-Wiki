---
title: Odor Early Warning System — Sulfiloggers, SUMO, and AERMOD Dispersion Modeling
category: technical-approach
block-type: prose
tags: [odor-control, data-analytics, process-modeling, sampling-monitoring, chemical-management, digital-tools, community-engagement, differentiator]
source: mmsd-om-2028
source-section: "IV. Approach — 2.2.6. Odor Control and Responding to Odor Complaints (Focus Area)"
source-pages: [73, 74]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0073.md#¶9", "verbatim/mmsd-om-2028/pages/p0073.md#¶12", "verbatim/mmsd-om-2028/pages/p0074.md#¶3", "verbatim/mmsd-om-2028/pages/p0074.md#¶4"]
pursuit-type: [wwtp-om, collections, multi-facility]
client-type: authority
client-size: "Two large water reclamation facilities plus regional conveyance and deep-tunnel inline storage"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [odor-control, innovation-value-add, digital-tools, community-engagement, partner-transparency]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
supersedes: wiki/technical-approach/mmsd-odor-early-warning-system-at-the-water-reclamation-facilities.md
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid vs. incumbent operator; WDNR.
quality: A concrete, named technology stack that converts odor control from reactive dosing to a forecast — liquid-phase sulfide monitoring feeding a dosing control loop, plus AERMOD plume prediction that triggers resident notification before complaints arrive.
reuse-notes: Confirm the current dosing practice being displaced, the availability of a meteorological station location, and the notification channels and community contacts for the target service area. Sulfilogger and AERMOD are vendor/regulatory tool names — verify current product naming before external use.
---

# Odor Early Warning System — Sulfiloggers, SUMO, and AERMOD Dispersion Modeling

**Installation of an "Odor Early Warning System" at the water reclamation facilities to minimize odors before they occur.** Sulfides generated in the collection system will reach the treatment plants and under certain operating and meteorological conditions result in offsite odors and complaints. In addition, plant conditions such as elevated primary clarifier blanket levels or extended sludge storage times can increase sulfide generation. Currently ferric chloride is added to influent wastewater to precipitate sulfide and mitigate odors after offsite impacts are detected. **Rather than reacting after odors occur, we propose an odor early warning system** (**Exhibit IV-25**) that **identifies odor potential in advance, allowing operators to take proactive actions to prevent or minimize emissions**. The proposed system includes the following components:

- **Sulfiloggers™ for influent sulfide monitoring.** Sulfiloggers are an emerging technology that measure dissolved sulfides in the liquid phase upstream of the plant rather than H₂S in the air as measured by traditional Odalogs. By measuring sulfides in liquid rather than the air, sulfide mass loading in the influent can be calculated and used in a control loop to automatically adjust chemical dosing. This approach accounts for highly dynamic, diurnal sulfide variations, reduces chemical costs, and avoids underdosing during peak sulfide conditions that can occur with constant-dose strategies.

- **Predictive odor modeling and community impact assessment.** While influent sulfide mass provides critical process insight, it does not indicate if odors will reach nearby receptors at concentrations that could cause complaints. To address this, we propose installing a system that will continuously estimate odor concentrations at locations surrounding the water reclamation facilities. These emissions will then be used in an AERMOD dispersion model along with real-time wind speed and direction data from a Jacobs-installed meteorological station. The model results will be displayed graphically to illustrate the shape and extent of odor plumes and identify potential offsite areas impacted.

- When modeling indicates a risk of offsite odor impacts, notifications can be sent to residents, elected representatives, and neighborhood associations using multiple communication channels, including social media, email, and opt-in text messages. While we recognize the inherent uncertainties associated with modeling, our experience shows that with proper design and calibration, this integrated system provides a reasonably reliable early warning that is often a strong indicator of conditions likely to result in odor complaints. **Exhibit IV-26** illustrates how we calibrated our model.

**Exhibit IV-25. Early Warning System Allows for Proactive Odor Mitigation Measures to Minimize Complaints** (asset ID `337_007CAM_1`) shows the chain from Sulfilogger to SUMO model to AERMOD dispersion model output and potential complaint warning.

## Reuse guidance

Universal: the liquid-phase-versus-air-phase sulfide monitoring argument, the dosing control-loop benefit (lower chemical cost, no underdosing at diurnal peaks), and the modeling-to-notification chain. Pursuit-specific: the plant conditions that drive sulfide generation locally and the notification audience. Pairs with the WATS model block (the upstream prediction layer) and the complaint protocol block (the response layer that consumes early warning data during investigations).
