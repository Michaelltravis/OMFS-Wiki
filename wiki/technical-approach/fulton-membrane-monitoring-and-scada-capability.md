---
title: "Membrane Monitoring, SCADA Capability, and Peak-Flow Testing"
category: technical-approach
block-type: prose
tags: [membrane-treatment, scada, data-analytics, process-control, process-optimization, cybersecurity, asset-management, jv-structure]
source: fulton-county-2025
source-section: "Section 2.8, Membrane Performance and SCADA"
source-pages: [65, 66, 67]
verbatim-ref: ["verbatim/fulton-county-2025/pages/p0065.md#¶3", "verbatim/fulton-county-2025/pages/p0066.md#¶2", "verbatim/fulton-county-2025/pages/p0066.md#¶3", "verbatim/fulton-county-2025/pages/p0066.md#¶4", "verbatim/fulton-county-2025/pages/p0066.md#¶5", "verbatim/fulton-county-2025/pages/p0066.md#¶6", "verbatim/fulton-county-2025/pages/p0067.md#¶1", "verbatim/fulton-county-2025/pages/p0067.md#¶4", "verbatim/fulton-county-2025/pages/p0067.md#¶6"]
pursuit-type: [wwtp-om, multi-facility, mbr-membrane, jv-delivery]
client-type: county
client-size: "Three MBR water-reclamation facilities and associated pump stations"
geography: "Southeast / GA / GA EPD"
rfp-section-type: [tech-approach, compliance]
win-theme-map: [asset-management, digital-tools, compliance-leadership, regional-bench]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-07
last-verified: 2026-09-07
context: "Southeast US county wastewater O&M pursuit, bid as JC Solutions, a Jacobs/CERM JV, for multi-facility MBR operations."
quality: "Near-verbatim membrane-monitoring and SCADA capability narrative with a source-client testimonial and comparable MBR testing method."
reuse-notes: "Confirm platform availability, monitoring parameters, test protocols, technical staffing, and quote permission before reuse. The p66 peak-flow-test sentence continues on p67 and must be completed with that source page in the next range."
---

# Membrane Monitoring, SCADA Capability, and Peak-Flow Testing

Membranes are the heart of all three plants, and tracking membrane performance is critical to maintaining optimal operation, scheduling chemical cleaning, and planning for membrane replacement. [FACILITY B] and [FACILITY C] have Veolia (formerly Zenon, GE, and Suez) hollow fiber membranes, and Veolia offers a tool called InSight, which produces a bi-weekly report tracking performance of each membrane train. There also is an online component, which allows customization of the data view. We understand that the current operator has been inconsistent in maintaining InSight. However, JC Solutions understands its importance and will maintain InSight at [FACILITY B] and [FACILITY C].

Jacobs’ comprehensive SCADA capabilities ensure we can support any need [CLIENT] may have, and allow us to develop a custom reporting tool for [CLIENT]'s new Kubota membrane operations to make sure they work well and last. Our full-service expertise includes:

- **Integrated IT/OT:** We have 2,600+ IT professionals and 350 dedicated SCADA practitioners support your facilities with expert network management (Cisco-certified), applications and systems updates, comprehensive cybersecurity, and reliable distributed control systems.
- **Seamless Process Controls Systems:** We can deliver full SCADA implementations that seamlessly interface with existing ControlLogix PLCs, manage historian data, alarms, SQL database integration, and provide critical operational trends.
- **Customized Automation Tools:** Our proven capabilities include SCADA master planning, systems integration, software programming, and cybersecurity—ensuring custom-built monitoring solutions that maximize efficiency, compliance, and performance.

“Jacobs has seamlessly integrated engineering, construction, and contract operations to deliver several equipment and controls system in a cost-effective manner. For Vancouver’s major control system upgrade, each part of the organization is working hand-in-hand to provide smart state-of-the-art improvements that meet long-term needs for O&M while minimizing impacts to the current operation during construction; maintain treatment plant level-of-service; and maintain or extend service life of assets.” — Frank Dick, PE, Sewer and Wastewater Engineering Supervisor, City of Vancouver.

[FACILITY A] has Kubota flat plate membranes. Kubota does not offer a tool like InSight, so Jacobs system integrators will develop a similar one for this plant. The system will monitor permeate flow, temperature, and transmembrane pressure for each membrane train and calculate temperature-corrected permeability using these parameters. Permeability will be tracked at two points in the production cycle—immediately before and after the “relax” step in which permeate production stops for about one minute while air scour continues. The resulting data distinguish two types of membrane fouling: the part that accumulates quickly and can be removed by air scour, and the part that accumulates gradually and cannot be removed by air scour.

Mixed liquor filterability is a consequence of biological process operation, but it affects membrane performance. We will monitor mixed liquor filterability weekly at each plant. For [FACILITY B] and [FACILITY C], we will used Veolia’s “Time to Filter” procedure. For [FACILITY A], we will use Kubota’s “Paper Filtrate Test” procedure.

At the MBR plant Jacobs operates in Traverse City, MI, we have developed a peak flow test to monitor ability of each membrane train to operate at its design peak flow capacity. Each month, one train at a time is operated at design peak flow for one hour. If the train does not enter transmembrane pressure (TMP) control mode, the train has passed the test. If the train does enter TMP control mode, this indicates that the train cannot operate at peak flow. Typically, this suggests the need for recovery cleaning, but it also could signal the need to replace the membranes. Jacobs will perform monthly peak flow testing on active membrane trains at each of the three [CLIENT] plants.

We understand the importance of the existing InSight tool at [FACILITY B] and [FACILITY C], and Jacobs system integrators will develop a similar tool for [FACILITY A]. At each plant, we will monitor mixed liquor filterability weekly and perform monthly peak flow testing on active membrane trains. **How It Benefits [CLIENT]:** Supports and enhances the ability to proactively address performance issues, optimize membrane life, and enable better capital replacement planning.

The procedures described above relate to membrane production capacity. Permeate quality is also important. At the three [CLIENT] plants, turbidity is monitored for each membrane train, and low turbidity indicates membrane integrity is intact. [FACILITY A] and [FACILITY C] (the newer plants) have a degassing column upstream of each turbidimeter to reduce false positive readings due to air bubbles. [FACILITY B] does not have this feature, and we would like to discuss with [CLIENT] the possibility of adding them.

## Reuse guidance

Use only with verified membrane suppliers, data systems, SCADA staff, and site-specific test protocols. The source identifies related visuals as Exhibits 2-29 and 2-30. Do not use the Frank Dick quote until permission is confirmed.
