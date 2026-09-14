---
title: Sensor-to-Dispersion-Model Early Warning System for Proactive Odor Mitigation
category: technical-approach
tags: [odor-control, data-analytics, process-modeling, operations-management]
source: hull-wwtf-om-2026
source-section: "Appendix F - WATS Modeling (p. F-2)"
story-ids: []
status: preferred
house-favorite: false
proof-point-ids: []
extracted: '2026-09-05'
last-verified: '2026-09-05'
block-type: prose
source-pages: [96]
verbatim-ref: [verbatim/hull-wwtf-om-2026/pages/p0096.md#¶1]
pursuit-type: [wwtp-om, collections]
client-type: municipal
client-size: 3.07 MGD / 42 mi / 10k pop
geography: Northeast / MA / MassDEP
rfp-section-type: [tech-approach]
win-theme-map: [odor-control, innovation-value-add]
sanitization-loss: high
section-id: hull-wwtf-om-2026:17.wastewater-aerobic-anaerobic-transformations-in-sewers-wats
section-order: 2
section-path: Section 7 - Appendix F - WATS Modeling › WASTEWATER AEROBIC/ANAEROBIC TRANSFORMATIONS IN SEWERS (WATS) MODELING
doc-order: 87
context: Coastal New England municipal WWTF (3.07 MGD) + collection system O&M, ~10,000 residents
sanitized: true
quality: Compact, visual, easily-understood differentiator chaining real-time sensing to predictive dispersion modeling; strong for win-theme and technical-approach sections addressing community odor complaints near sensitive receptors.
reuse-notes: 'SYNTHESIS, NOT SOURCE PROSE: this body restructures the source rather than reproducing its sentences (measured verbatim overlap ~0%). Read the passage at the cited verbatim-ref before reusing, and prefer the source wording. The four-step chain (sensor -> process model -> dispersion model -> complaint warning) is a generic Jacobs capability pattern; confirm current instrumentation/software brand names (Sulfilogger, Sumo, AERMOD) are still the approved toolset before reuse, and tailor to whichever tools the pursuit team intends to actually deploy.'
---

# Sensor-to-Dispersion-Model Odor Early Warning System

Jacobs pairs continuous field sensing with predictive air dispersion modeling to give operations staff advance notice of conditions likely to generate an odor complaint, rather than reacting after a complaint is received.

The workflow chains four elements:

1. **Continuous H2S sensor (e.g., "Sulfilogger"-type instrumentation)** — captures real-time hydrogen sulfide concentrations at key collection-system or treatment locations.
2. **Sewer/treatment process model (e.g., Sumo Model)** — converts sensor readings into predicted odor-causing compound generation and release rates.
3. **Atmospheric dispersion model (e.g., AERMOD)** — projects how released compounds will disperse under current/forecast wind and weather conditions, producing a concentration contour map (e.g., 1-hour average concentration by receptor location).
4. **Potential complaint warning** — flags when dispersion output indicates concentrations likely to reach sensitive receptors (residences, businesses) at levels that could trigger complaints, enabling proactive mitigation (e.g., adjusting chemical dosing, ventilation, or operations) before an odor event occurs.

This early-warning approach shifts odor management from reactive (respond after a complaint) to proactive (anticipate and mitigate before an off-site impact occurs), which is particularly valuable for facilities and collection systems located near residential neighborhoods or other sensitive receptors.

Related graphic: `337_007CAM_1` (early-warning workflow diagram with AERMOD dispersion output) — see `wiki/graphics/hull-wwtf-om-2026.md`.

## Reuse guidance

Universal: the four-stage logic (sense → model process → model dispersion → warn) is transferable to any wastewater treatment or collection-system pursuit with an odor-sensitivity concern, regardless of specific software brands.

Pursuit-specific: confirm which specific instrumentation and modeling software (sensor hardware, process model, dispersion model) the responsible technical team actually intends to propose — brand names shown here are illustrative of the source proposal and must be verified current before reuse. Tailor the description of "sensitive receptors" to the pursuit's actual surrounding land use (residential density, schools, businesses). Pairs well with `wats-collection-system-odor-corrosion-modeling.md` for pursuits emphasizing a full odor-management program.
