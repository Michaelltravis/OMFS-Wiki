---
title: SCADA, Instrumentation & Controls, and Cybersecurity Approach
category: technical-approach
block-type: prose
tags: [scada, instrumentation-and-controls, cybersecurity, ot-it, dedicated-ic-technician, nist, awia, ignition-scada, allen-bradley, value-added-extras]
source: santamonica-swip-om-2025
source-section: "2.4 Firm Approach — SCADA, I&C, and Cybersecurity"
source-pages: [68, 69]
verbatim-ref: ["verbatim/santamonica-swip-om-2025/pages/p0068.md#¶3", "verbatim/santamonica-swip-om-2025/pages/p0068.md#¶4", "verbatim/santamonica-swip-om-2025/pages/p0068.md#¶6", "verbatim/santamonica-swip-om-2025/pages/p0068.md#¶7", "verbatim/santamonica-swip-om-2025/pages/p0068.md#¶10", "verbatim/santamonica-swip-om-2025/pages/p0068.md#¶12", "verbatim/santamonica-swip-om-2025/pages/p0068.md#¶21", "verbatim/santamonica-swip-om-2025/pages/p0069.md#¶2", "verbatim/santamonica-swip-om-2025/pages/p0069.md#¶10", "verbatim/santamonica-swip-om-2025/pages/p0069.md#¶11"]
pursuit-type: [reuse-dpr, water-treatment, multi-facility]
client-type: municipal
client-size: "Advanced water treatment / potable reuse facility plus a water treatment plant and remote injection wells and lift stations"
geography: "Southern California / CA / SWRCB Division of Drinking Water"
rfp-section-type: [tech-approach, compliance]
win-theme-map: [innovation-value-add, digital-tools, regional-bench, incumbent-displacement, compliance-leadership]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: true
sanitized: true
sanitization-loss: low
extracted: 2026-09-05
last-verified: 2026-09-05
context: Southern California advanced water treatment / potable reuse facility O&M, 2025, incumbent (Veolia) displacement
quality: A candid site-assessment-based gap analysis (single-point-of-failure server, no redundancy) paired with two priced no-cost value-adds and a firm-wide SCADA/OT capability statement plus a named client testimonial — technical credibility through specificity rather than generic claims.
reuse-notes: The specific findings (minimal-model server with no failover, Allen Bradley PLCs, Ignition SCADA, Wonderware-to-Ignition conversion) are pursuit-specific site-visit observations — replace with the target facility's actual platform and vendor findings. The firm-wide capability statistics (2,600+ IT professionals, 350 SCADA practitioners) and the embedded-value figures for the cybersecurity survey and dedicated I&C technician are reusable as-is. The closing testimonial (Frank Dick, PE, City of Vancouver) is a real, attributable reference-client quote — keep name and city verbatim; confirm permission before reuse.
---

# SCADA, Instrumentation & Controls, and Cybersecurity Approach

## Site Visit Findings

During our recent visits to [CLIENT]'s advanced water treatment facility, water treatment plant, and the supporting remote facilities, Jacobs observed that [CLIENT]'s SCADA and instrumentation systems are relatively modern and well maintained. Across all sites, systems are built on Allen Bradley PLCs and touchscreen HMIs, with Ignition SCADA software serving as the primary interface. At the water treatment plant, the recent conversion from Wonderware to Ignition demonstrates [CLIENT]'s commitment to modernization and system standardization.

However, we noted critical gaps in system resilience. Most notably, the SCADA system at the advanced treatment facility currently lacks redundancy—a single server failure would disrupt all monitoring and control capabilities. The server in use is a minimal model without built-in failover protection. Additionally, we were unable to verify licensing, remote access configurations, and spare part inventories—underscoring the need for a comprehensive assessment early in the contract term to fully map the system architecture and risks.

## Cybersecurity Survey

Cybersecurity is a foundational element of Jacobs' approach to operational resilience. We recognize that water and wastewater control systems are increasingly targeted by cyber threats, and that safeguarding these systems is critical to protecting public health, compliance, and reliability of service.

For [CLIENT], Jacobs will work with the utility during the **transition phase** to confirm the appropriate cybersecurity frameworks are in place. This structured survey includes reviewing existing systems, clarifying roles and responsibilities, and ensuring right-sized safeguards are established. Our focus is on **practical, cost-effective protections** that align with [CLIENT]'s risk tolerance and regulatory requirements, without over-engineering or introducing unnecessary complexity.

**Above and beyond — value-added extra: cybersecurity survey.** Jacobs will collaborate with [CLIENT] during the transition to assess cybersecurity readiness—at no additional cost (a $34,000 value). This includes reviewing systems, clarifying responsibilities, and implementing right-sized safeguards that align with [CLIENT]'s risk profile and regulatory needs—avoiding unnecessary complexity or cost. *$34,000 embedded value by Jacobs.*

## Dedicated I&C Technician with Regional Support

To directly address these vulnerabilities and support long-term system reliability, Jacobs will allocate a dedicated Instrumentation & Controls (I&C) Technician to our regional maintenance team in southern California. This technician will be based in the metropolitan area and will prioritize serving [CLIENT]'s facilities and our West Basin project in El Segundo, while spending their remaining time helping our other projects in California. This position is in addition to the onsite I&C Technician also included on our [CLIENT] team.

This cross-support model ensures high availability and responsiveness while leveraging regional expertise and cost efficiency. For [CLIENT], this approach provides the following key benefits:

- **Site-level familiarity with the water treatment plant and advanced treatment facility SCADA infrastructure**, enabling proactive diagnostics, routine calibration, and software/hardware troubleshooting.
- **Rapid on-site response** for SCADA failures or instrument alarms, reducing system downtime and operational risk.
- **Consistent I&C coverage across all remote facilities**, including injection wells and lift stations, helping to maintain regulatory compliance and permit-required data integrity.
- **Backup staffing and knowledge continuity**, reducing risks associated with vacation or turnover.

The technician will collaborate closely with our operations team and Jacobs' deep bench of SCADA engineers to ensure robust system performance across all facilities.

**Above and beyond — value-added extra: dedicated I&C technician.** In addition to the onsite I&C Technician on our [CLIENT] team, Jacobs will assign a separate, dedicated I&C Technician based in the metropolitan area to support both [CLIENT] and our West Basin project—ensuring rapid, expert response across all facilities. This shared-resource model provides local familiarity, operational continuity, and cost efficiency without compromising coverage. *$210,000 embedded value by Jacobs.*

## Firm-wide SCADA and Cybersecurity Capabilities

Jacobs brings extensive SCADA and IT/OT expertise, supporting O&M clients nationwide with modern, secure, and resilient control systems. Our in-house teams are certified integrators for Ignition and Rockwell Automation platforms, among others. Jacobs also brings national experience supporting utilities and agencies with cybersecurity reviews and frameworks. We apply industry best practices, including NIST standards, to our OT and IT environments, while tailoring controls to the unique needs of each facility. Our teams have supported water and wastewater clients across the state and nationwide, ensuring compliance with emerging requirements such as the American Water Infrastructure Act (AWIA). These resources will be available to the [CLIENT] project as needed, including our internal SCADA diagnostics team and cybersecurity specialists.

We routinely provide support for:

- SCADA architecture assessments and upgrades
- Network cybersecurity planning
- Remote access configuration and security hardening
- Data historian and dashboard development
- Compliance documentation and audit preparation

By leveraging Jacobs' broad O&M experience and our SCADA and cybersecurity expertise, [CLIENT] will benefit from a trusted partner who can strengthen resilience against evolving cyber threats, while maintaining transparency and operational continuity.

**Value-added offerings draw on Jacobs' advanced SCADA capabilities.** Jacobs' comprehensive SCADA capabilities ensure we can support any need [CLIENT] may have, and allow us to develop a custom reporting tool for your new membrane operations to make sure they work well and last. Our full-service expertise includes:

- **Integrated IT/OT:** We have 2,600+ IT professionals and 350 dedicated SCADA practitioners to support your facilities with expert network management (Cisco-certified), applications and systems updates, comprehensive cybersecurity, and reliable distributed control systems.
- **Seamless Process Controls Systems:** We can deliver full SCADA implementations that seamlessly interface with existing ControlLogix PLCs, manage historian data, alarms, SQL database integration, and provide critical operational trends.
- **Customized Automation Tools:** Our proven capabilities include SCADA master planning, systems integration, software programming, and cybersecurity—ensuring custom-built monitoring solutions.

With Jacobs, [CLIENT] gains a responsive partner uniquely qualified to leverage SCADA technology and enhance operational excellence.

> "Jacobs has seamlessly integrated engineering, construction, and contract operations to deliver several equipment and controls system in a cost-effective manner. For Vancouver's major control system upgrade, each part of the organization is working hand-in-hand to provide smart state-of-the-art improvements that meet long-term needs for O&M while minimizing impacts to the current operation during construction; maintain treatment plant level-of-service; and maintain or extend service life of assets."
> — **Frank Dick, PE**, Sewer and Wastewater Engineering Supervisor, City of Vancouver

Related graphic: `130_008A26` (SCADA and IT/OT services suite).

## Reuse guidance

Universal: the firm-wide IT/OT capability statistics, the "practical, cost-effective, right-sized" cybersecurity philosophy, the transition-phase cybersecurity survey as a priced no-cost value-add, the dedicated-I&C-technician shared-resource model, and the Frank Dick / City of Vancouver testimonial are reusable across pursuits. Pursuit-specific: site-visit findings (server model, PLC and SCADA platform, redundancy gaps, unverified licensing and spares) must be regenerated from an actual site assessment of the target facility — do not reuse the single-point-of-failure finding unless verified. The West Basin sister-project pairing only works where Jacobs has a genuinely nearby project to share the technician with; substitute the real neighboring project or drop the shared-resource framing. Full passage: verbatim pages p0068 and p0069.
