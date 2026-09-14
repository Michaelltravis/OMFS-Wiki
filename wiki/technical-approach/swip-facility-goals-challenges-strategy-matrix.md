---
title: Facility-by-Facility Goals, Challenges, and Strategy Matrix (Multi-Facility Water Reuse O&M)
category: technical-approach
block-type: table
tags: [project-understanding, exhibit, section-opener, water-reuse, scada, cmms, stormwater, groundwater-recharge, multi-facility-operations]
source: santamonica-swip-om-2025
source-section: "2.4 Firm Approach — Jacobs Understands [CLIENT]'s Challenges and Goals for its Facilities, Exhibit 2-6"
source-pages: [30, 31]
verbatim-ref: ["verbatim/santamonica-swip-om-2025/pages/p0030.md#¶9", "verbatim/santamonica-swip-om-2025/pages/p0030.md#¶2", "verbatim/santamonica-swip-om-2025/pages/p0031.md#¶1"]
pursuit-type: [reuse-dpr, water-treatment, wwtp-om, stormwater, multi-facility]
client-type: municipal
client-size: "1.0 MGD advanced water treatment facility + stormwater diversion/pump assets, urban runoff recycling facility, and GRRP injection wells"
geography: "Southern California / CA / SWRCB Division of Drinking Water + LA RWQCB (Title 22 GRRP, WDRs; State Board Orders R4-2021-0044 and R4-2023-0366)"
rfp-section-type: [tech-approach]
win-theme-map: [incumbent-displacement, partner-transparency, compliance-leadership, asset-management, stormwater, digital-tools, innovation-value-add]
proof-point-ids: [PP-0026, PP-0417, PP-0418, PP-0419, PP-0420, PP-0421, PP-0422, PP-0423, PP-0424, PP-0425, PP-0426, PP-0427, PP-0428, PP-0429, PP-0430, PP-2796, PP-2797, PP-2798]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
context: Southern California advanced water treatment / potable reuse facility O&M, 2025, incumbent (Veolia) displacement — multi-facility potable reuse program including an advanced water treatment facility, stormwater diversion/pump assets, an urban runoff recycling facility, groundwater replenishment reuse project (GRRP) injection wells, and an interface with an adjacent municipal water treatment plant
quality: A section-opening device that grounds the technical approach in the client's own facility-by-facility conditions rather than generic O&M language — the 3-column table format (Understanding of Goals | Key Current/Future Challenges | Jacobs' Strategies) scales cleanly across a multi-facility, multi-technology reuse portfolio (MBR, RO, UV-AOP, SCADA/OT, stormwater assets, injection wells) and reads as evidence the team did real due-diligence fieldwork before writing.
reuse-notes: The specific facility list, equipment (PLC models, server hardware, SCADA platform), and named challenges are drawn from this pursuit's actual site visits and RFP/scope documents — do not reuse the specific challenge language for a different pursuit's facilities. The narrative opener (decades of comparable-scale experience, due-diligence site visits, talking with client staff) and the 3-column per-facility matrix structure are fully reusable for any multi-facility O&M pursuit.
---

# Facility-by-Facility Goals, Challenges, and Strategy Matrix (Multi-Facility Water Reuse O&M)

## Section-opening narrative

Jacobs will deliver an integrated, transparent, and results-driven project management approach that ensures 24/7 compliance, reliable production of advanced treated water, and seamless coordination across [CLIENT]'s facilities. With decades of experience operating facilities comparable in scale and technology — including membrane bioreactor (MBR), reverse osmosis (RO), UV-advanced oxidation process (UV-AOP) systems, and large pump stations — Jacobs is uniquely equipped to manage the full scope of operations in accordance with the client's applicable regulatory orders (in this pursuit, State Board Orders R4-2021-0044 and R4-2023-0366). As one of the largest O&M services providers in North America, Jacobs will leverage the depth of its operations, engineering, asset management, maintenance, and compliance capabilities to meet the client's performance standards while driving long-term value and sustainability. The Jacobs team will integrate with client staff to uphold a community-first culture rooted in accountability, safety, and regulatory excellence.

## Jacobs understands [CLIENT]'s challenges and goals for its facilities

[CLIENT]'s sustainable water infrastructure program represents a significant advancement in water treatment and establishes [CLIENT] as a pioneer in water reuse. The 1.0-MGD advanced water treatment facility (AWTF) is the first of its kind to successfully treat both wastewater and stormwater, the first ever to receive log removal credits for pathogen reduction using MBR, and the first to do all of this in an underground facility.

The program plays a critical role in reducing [CLIENT]'s reliance on imported water supplies and promotes sustainability through the injection of recycled water into the local aquifer as a barrier to seawater intrusion and for aquifer replenishment. In addition, [CLIENT] is in a great position to be the first direct potable reuse (DPR) facility in the country — an amazing aspiration and one the full Jacobs team would love to help [CLIENT] achieve.

In preparation for this proposal, our team talked with your staff, thoroughly reviewed the RFP, scope of work, draft agreement and exhibits, and spent several days in the field visiting the facilities conducting due diligence, which has provided a deep understanding of the challenges and opportunities to innovate and improve the O&M of the facilities.

The matrix below provides a concise, facility-by-facility summary of our understanding of your goals, challenges, and the resources and strategies Jacobs can bring to ensure we meet and exceed your expectations for exceptional O&M services. Across all sites, Jacobs recognizes the need to operate to [CLIENT]'s permits and KPI framework to reliably produce Product Water for non-potable and groundwater replenishment reuse project (GRRP) uses, implement CMMS-based asset management, and integrate alarms via the SCADA/HMI platform (in this pursuit, Ignition), per the Scope of Services.

## Facility-by-facility understanding, challenges, and strategies

### Advanced Water Treatment Facility (AWTF)

| O&M Element | Understanding of [Client]'s Goals | Key Current/Future Challenges | Jacobs' Strategies to Deliver Results |
|---|---|---|---|
| SCADA, Controls & Instrumentation | Maintain reliable, permit-compliant Product Water with centralized alarming in the SCADA/HMI platform (in this pursuit, Ignition) and clear Critical Control Point (CCP)/Log Removal Value (LRV) tracking. | SCADA/HMI clients on an aging OS (Ignition clients on Windows 10); programmable logic controllers (PLCs) (in this pursuit, CompactLogix 5069-L340ER models) and software versions/licensing and VPN details may not be fully documented. | Verify and document SCADA/PLC versions and license ownership; finalize point lists and CCPs/LRVs; implement secure, auditable remote access and alarm callout integration in the SCADA/HMI platform. |
| OT Network & Remote Access | Ensure resilient 24/7 operations with a hardened operational-technology (OT) network and reliable remote alarming/response. | Single server with no redundancy (in this pursuit, a single Dell R340 server); disorganized network cabinet; fiber/remote topology unclear; remote access governance not verified. | Add server redundancy (failover/virtualization); re-rack/label and document network paths; implement role-based remote access aligned with the client's security standards. |
| Operations & Regulatory Compliance | Continuously meet Waste Discharge Requirements (WDRs)/Title 22 GRRP requirements; complete sampling, QA/QC, and reporting. | New facility; need consistent CCP/LRV trending and accessible performance dashboards for client stakeholders. | Operate the full treatment train (screening/MBR→carbon filtration (CF)→RO→UV-AOP); run the performance monitoring program (CCPs, LRVs, KPIs); deliver monthly compliance/KPI reports and remote alarm verification. |
| Maintenance, CMMS & Spares | Protect assets and warranties; execute preventive maintenance (PMs) on schedule; maintain critical spares and timely repair recommendations. | Mentor asset performance management (APM) CMMS in use; critical PLC/HMI spares not confirmed. | Stand up a PM library in the CMMS; verify and maintain critical spares; provide 72-hour large/emergency repair recommendations; track PM compliance monthly. |
| Staffing & Response | Staff a cross-trained team (including a designated Chief Plant Operator (CPO) holding an advanced water treatment grade-5 certification) with on-call coverage and rapid instrumentation & controls (I&C) support. | The client utilizes the facility to cross-train staff/interns; frequent analyzer/I&C callouts across sites. | Provide certified operators and a CPO; place dedicated onsite I&C staff with regional support backup; maintain remote SCADA monitoring and defined response times. |

### Stormwater diversion/lift/pump-station facilities

| O&M Element | Understanding of [Client]'s Goals | Key Current/Future Challenges | Jacobs' Strategies to Deliver Results |
|---|---|---|---|
| Operations Profile & Readiness | Keep wet-weather assets ready; remove debris promptly; coordinate with AWTF operations. | Assets run episodically during rain; all monitored from the AWTF; the stormwater separator requires vac-truck cleaning when active; the pump station requires routine vac-truck cleaning, and the current frequency has not been sufficient to prevent backflows. | Maintain wet-weather readiness; exercise valves; include readiness metrics in monthly reporting. Jacobs will increase the vac-truck cleaning frequency at the pump station, as well as install Jacobs' proprietary AquaDNA DeRagger technology, as a value-add to the client, to help ensure operational uptime. |
| SCADA & Alarms | Ensure remote visibility and reliable alarm callouts via the SCADA/HMI platform. | Stations are SCADA-visible from the AWTF; alarm/point lists need verification and periodic testing. | Validate and standardize point lists; test alarms monthly; document results in the Operations Report. |

### Urban runoff recycling facility

| O&M Element | Understanding of [Client]'s Goals | Key Current/Future Challenges | Jacobs' Strategies to Deliver Results |
|---|---|---|---|
| Role & Regulatory Alignment | Maintain the facility to support the broader reuse/GRRP program (including a potential diluent role) and keep systems safe/ready. | Facility has been offline roughly 2 years pending upgrades; PLC-based SCADA visibility (Allen-Bradley PLC in this pursuit); RO membranes preserved ("pickled") with periodic upkeep required. | Uphold preservation protocols; perform required O&M on active systems; coordinate OEM service contracts; integrate facility data into reporting when back in service. |

### Groundwater replenishment reuse project (GRRP) injection wells

| O&M Element | Understanding of [Client]'s Goals | Key Current/Future Challenges | Jacobs' Strategies to Deliver Results |
|---|---|---|---|
| Startup & Performance Protection | Achieve compliant indirect potable reuse and protect well capacity and aquifer conditions. | Wells nearing startup; backwashing and tracer testing underway; wells will be SCADA-monitored from the AWTF. | Implement well performance trending (head pressure, specific capacity, backwash intervals); integrate alarm/telemetry into AWTF dashboards; document data for regulatory confidence. |

### Interface / optional-support facility (adjacent municipal water treatment plant)

| O&M Element | Understanding of [Client]'s Goals | Key Current/Future Challenges | Jacobs' Strategies to Deliver Results |
|---|---|---|---|
| Controls & I&C Interface | Stabilize operations where the adjacent plant interfaces with the client's water supply; coordinate packaged systems; resolve controls issues. | Converted from a legacy SCADA platform to the current one (in this pursuit, from Wonderware to Ignition; one area pending); fresh/finished water RO system (FRO/FRRO); RO modulating valve control issues; third-party I&C currently engaged. | If authorized, provide routine I&C/maintenance coverage; tune RO control loops; coordinate with OEMs (in this pursuit, e.g., Trojan, Pall); align alarming and reporting with the client's standards. |

## Reuse guidance

Universal: opening the technical-approach section with (1) a short narrative naming the client's specific reuse/water program, its regulatory drivers, and the team's due-diligence process (site visits, staff conversations, RFP/scope review), followed by (2) a facility-by-facility crosswalk table (Understanding of Goals | Key Challenges | Jacobs' Strategies) — this structure works for any multi-facility O&M pursuit and demonstrates the proposal team actually walked the assets rather than writing generic boilerplate.

Pursuit-specific: every facility name, equipment make/model, SCADA platform, and challenge listed is drawn from this specific pursuit's site conditions — rewrite entirely from the target pursuit's actual facilities, equipment, and due-diligence findings before reuse. Do not carry forward the specific PLC models, server hardware, or SCADA platform names for a different pursuit unless independently verified. Pair with `swip-om-project-execution-framework.md` (the very next exhibit in the source proposal, functioning as the "how we run O&M day to day" complement to this "here's what you told us, here's how we respond" opener) and `swip-process-control-system-tools.md` for the deeper process-control methodology referenced here. Related graphic: Exhibit 2-6 (see graphics catalog, source `santamonica-swip-om-2025`; a data table with no separate DAM asset ID, flagged client-specific).
