---
title: "Level 3 PdM Integration with SCADA and the CMMS, and Critical Scope Considerations"
category: technical-approach
block-type: prose
tags: [predictive-maintenance, scada, cmms, cybersecurity, data-analytics, asset-management, scope-assumptions, technical-approach]
source: mmsd-om-2028
source-section: "IV.D. Potential Additive Work – Level 3 PdM — 8. Integration with SCADA and NexGen CMMS; 9. Critical Considerations in Developing Jacobs' Level 3 PdM Approach"
source-pages: [137]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0137.md#¶4", "verbatim/mmsd-om-2028/pages/p0137.md#¶5", "verbatim/mmsd-om-2028/pages/p0137.md#¶9", "verbatim/mmsd-om-2028/pages/p0137.md#¶10"]
pursuit-type: [wwtp-om, multi-facility, solids, collections]
client-type: authority
client-size: "Two large water reclamation facilities + regional conveyance system + biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [digital-tools, asset-management, partner-transparency, compliance-leadership]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:32.8-integration-with-scada-and-nexgen-cmms
section-order: 9
section-path: IV. Approach Summary › IV.D. Potential Additive Work – Level 3 PdM › 8. INTEGRATION WITH SCADA AND NEXGEN CMMS
doc-order: 232
context: "Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production and regional conveyance, 2028 challenger bid against an incumbent operator; WDNR. Advanced PdM was priced as a separate additive line item with its own pricing worksheet item."
quality: "Closes a technical offer the way an evaluator wants it closed — the data path drawn end to end (PdM tools → SCADA → historian → CMMS → work orders → asset health scores), then an explicit statement that base scope and additive scope do not overlap and that pricing, documentation, and cybersecurity follow the RFP's own exhibits."
reuse-notes: "Re-point the exhibit references (Exhibit B documentation, Exhibit Q cybersecurity, Pricing Worksheet Item J here) at the target RFP's equivalents. The no-double-counting statement is the reusable move on any bid that splits base and additive scope; keep it explicit."
---

# Level 3 PdM Integration with SCADA and the CMMS

## 8. Integration with SCADA and the CMMS

Successful Level 3 PdM depends on tight integration between predictive technologies, SCADA, the SCADA historian, and the CMMS. Jacobs will configure SCADA points and data flows for PdM inputs, ensuring alignment with [CLIENT]'s OT architecture and cybersecurity requirements. [CLIENT] is a regional sewerage district operating two large water reclamation facilities and a regional conveyance system. PdM tools will route their analytics to the historian or directly into the CMMS via open APIs, where automated work orders will be generated based on agreed thresholds.

The CMMS will be configured to accept condition levels, alerts, and asset health scores and to associate them with specific assets. This will improve work planning, enhance prioritization, and eliminate the manual interpretation of PdM reports that currently burdens [CLIENT].

**Callout — seamlessly integrated PdM, SCADA, historian, and CMMS automatically generate the right work at the right time to protect [CLIENT]'s assets.** The data path runs PdM tools → SCADA → historian → CMMS → work orders and asset health scores. Graphic reference: `334_007CAM_2`.

## 9. Critical considerations in developing Jacobs' Level 3 PdM approach

Jacobs' Level 3 PdM plan clearly differentiates between Level 2 (base scope) and Level 3 (additive) activities, avoiding any risk of double counting. All PdM procedures, thresholds, and condition ratings will be documented in the CMMS as required in Exhibit B. Data routing, access control, and API integrations will comply with Exhibit Q cybersecurity requirements. Pricing for Level 3 PdM will follow the RFP requirements, including an itemized breakdown for PdM as required in Pricing Worksheet Item J.

## Reuse guidance

Universal: the five-step data path stated as one line, the promise to eliminate manual interpretation of vendor PdM reports, and the four-part closing on scope separation, documentation, cybersecurity, and pricing compliance. Pursuit-specific: every RFP exhibit and worksheet citation, and the client's OT architecture constraints. Pairs with [PdM Program Approach — Integrating Levels 1, 2, and 3 Data](mmsd-pdm-program-approach-integrating-levels-1-3.md), [Levels 1–3 PdM Framework](mmsd-pdm-levels-1-3-framework.md), and [Exhibit — Process and Benefits of CMMS Integrations with Jacobs' Technology Systems](mmsd-cmms-nexgen-integrations-table.md). Read `verbatim/mmsd-om-2028/pages/p0137.md` for the full passage.
