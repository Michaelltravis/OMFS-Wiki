---
title: Swing-Zone Aeration Decisions and Nitrate Probe Placement
category: technical-approach
block-type: prose
tags: [process-optimization, process-control, instrumentation-controls, energy-management, permit-compliance, membrane-treatment]
source: fulton-county-2025
source-section: "OPERATION & MAINTENANCE PLANS"
source-pages: [62]
verbatim-ref: ["verbatim/fulton-county-2025/pages/p0062.md#¶3", "verbatim/fulton-county-2025/pages/p0062.md#¶6", "verbatim/fulton-county-2025/pages/p0062.md#¶7"]
pursuit-type: [wwtp-om, multi-facility, mbr-membrane, jv-delivery]
client-type: county
client-size: "Three MBR water reclamation facilities / 33 pump stations"
geography: "Southeast / GA / GA EPD"
rfp-section-type: [tech-approach, compliance]
win-theme-map: [asset-management, innovation-value-add, energy-chemical-efficiency, compliance-leadership]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-14
last-verified: 2026-09-14
section-id: fulton-county-2025:12.swing-zones
section-path: Section 2 | Operations & Maintenance Plan › 2.8 | Approach and Understanding of the Scope of Work and Required Facilities Plans › OPERATION & MAINTENANCE PLANS › Swing Zones
section-order: 17
doc-order: 60
volatility: evergreen
review-due: 2028-04-17
freshness-flags: []
context: Southeast US county, three MBR WRFs + 33 pump stations, 2025, bid as JC Solutions (Jacobs/CERM JV); GA EPD
quality: Shows the operating logic behind a swing-zone aeration decision — the ammonia-limit override, the nitrate-delivery alternatives when IMLR pumping is short, and the instrument-placement consequence — in the plant-specific detail that demonstrates real process command.
reuse-notes: Confirm which bioreactor zones at the target facility are true swing zones, whether IMLR exists and at what capacity, whether RAS flow can be increased to deliver nitrate, and where the nitrate probe is physically installed before repeating any of these conclusions. Exhibit reference must be renumbered to the new proposal's exhibit sequence.
---

# Swing-Zone Aeration Decisions and Nitrate Probe Placement

Several considerations affect the decision of whether to aerate a swing zone, and this is best evaluated using process simulation.

When a swing zone is aerated, it operates as an aerobic zone. When aeration is needed to meet effluent ammonia limits (for example, during the winter), it overrides all other considerations.

At [FACILITY B], a wastewater reclamation facility, secondary phosphorus release can be prevented by providing sufficient internal mixed liquor recycle (IMLR) pumping. If insufficient pumping capacity exists, it would be necessary to aerate the swing zone. [FACILITY A], a wastewater reclamation facility, does not have IMLR, but RAS flow can be increased to deliver more nitrate to the anoxic zone.

At [FACILITY A], there is a nitrate probe in the anoxic zone just upstream of the swing zone (**Exhibit 2-25**). When the swing zone is unaerated (making it anoxic), it would be ideal to make the nitrate measurement in the swing zone.

## Reuse guidance

Universal: the decision hierarchy itself — ammonia permit compliance overrides energy and alkalinity benefits; an unaerated swing zone only works for EBPR if nitrate keeps arriving; and where nitrate is measured has to follow where the anoxic zone actually ends. That logic transfers to any BNR plant with switchable zones.

Pursuit-specific: which facilities have swing zones, whether IMLR is installed, whether RAS flow is an available nitrate-delivery path, and the current probe location. All of it must be re-verified against current drawings and a site walk.

Pairs with [Swing Zones and Internal Mixed Liquor Recycle Optimization](fulton-swing-zones-and-internal-mixed-liquor-recycle.md) (the anoxic-zone benefits and EBPR constraint, plus the value-added probe-relocation evaluation), [Fermentation Zone Operating Variables](fulton-fermentation-zone-operating-variables.md), [IMLR Piping and Membrane Commissioning](fulton-imlr-piping-and-membrane-commissioning.md), and [Energy, Uptime, and Ammonia Aeration Control](fulton-energy-uptime-and-ammonia-aeration-control.md). Read `verbatim/fulton-county-2025/pages/p0062.md` for the full swing-zone passage in order.
