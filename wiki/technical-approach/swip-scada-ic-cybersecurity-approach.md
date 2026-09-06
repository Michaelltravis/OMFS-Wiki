---
title: SCADA, Instrumentation & Controls, and Cybersecurity Approach
category: technical-approach
tags: [scada, instrumentation-and-controls, cybersecurity, ot-it, dedicated-ic-technician, nist, awia, ignition-scada, allen-bradley]
source: santamonica-swip-om-2025
source-section: "2.4 Firm Approach — SCADA, I&C, and Cybersecurity (pp. 68-69)"
context: Southern California sustainable water infrastructure O&M, 2025
sanitized: true
quality: A candid site-assessment-based gap analysis (single-point-of-failure server, no redundancy) paired with a concrete cybersecurity survey value-add and a firm-wide SCADA/OT capability statement — demonstrates technical credibility through specificity rather than generic claims.
reuse-notes: The specific findings (Dell R340 server, Allen Bradley PLCs, Ignition SCADA, Wonderware-to-Ignition conversion) are pursuit-specific site-visit observations — replace with the target facility's actual platform/vendor findings; the firm-wide capability statistics (2,600+ IT professionals, 350 SCADA practitioners) are reusable as-is. The closing testimonial (Frank Dick, PE, City of Vancouver) is a real, attributable reference-client quote — keep the name and city verbatim per wiki policy on reference testimonials; confirm continued permission to publish before reuse.
---

# SCADA, Instrumentation & Controls, and Cybersecurity Approach

## Site Visit Findings

During our recent site visits, Jacobs observed that the client's SCADA and instrumentation systems are relatively modern and well maintained. Across all sites, systems are built on Allen Bradley PLCs and touchscreen HMIs, with Ignition SCADA software serving as the primary interface. At one facility, a recent conversion from Wonderware to Ignition demonstrates the client's commitment to modernization and system standardization.

However, we noted critical gaps in system resilience. Most notably, the SCADA system currently lacks redundancy—a single server failure would disrupt all monitoring and control capabilities. The server in use is a minimal model without built-in failover protection. Additionally, we were unable to verify licensing, remote access configurations, and spare part inventories—underscoring the need for a comprehensive assessment early in the contract term to fully map the system architecture and risks.

## Cybersecurity Survey

Cybersecurity is a foundational element of Jacobs' approach to operational resilience. We recognize that water and wastewater control systems are increasingly targeted by cyber threats, and that safeguarding these systems is critical to protecting public health, compliance, and reliability of service.

For [CLIENT], Jacobs will work with the client during the transition phase to confirm the appropriate cybersecurity frameworks are in place. This structured survey includes reviewing existing systems, clarifying roles and responsibilities, and ensuring right-sized safeguards are established. Our focus is on practical, cost-effective protections that align with the client's risk tolerance and regulatory requirements, without over-engineering or introducing unnecessary complexity.

**Above and Beyond — Cybersecurity Survey:** Jacobs will collaborate with the client during the transition to assess cybersecurity readiness—at no additional cost (a $34,000 value). This includes reviewing systems, clarifying responsibilities, and implementing right-sized safeguards that align with the client's risk profile and regulatory needs—avoiding unnecessary complexity or cost. ($34,000 embedded value.)

## Dedicated I&C Technician with Regional Support

To directly address these vulnerabilities and support long-term system reliability, Jacobs will allocate a dedicated Instrumentation & Controls (I&C) Technician to our regional maintenance team. This technician will be based in the region and will prioritize serving the client's facilities and a nearby sister project, while spending remaining time helping other regional projects. This position is in addition to the onsite I&C Technician also included on the project team.

This cross-support model ensures high availability and responsiveness while leveraging regional expertise and cost efficiency. For the client, this approach provides the following key benefits:

- **Site-level familiarity** with facility SCADA infrastructure, enabling proactive diagnostics, routine calibration, and software/hardware troubleshooting.
- **Rapid on-site response** for SCADA failures or instrument alarms, reducing system downtime and operational risk.
- **Consistent I&C coverage across all remote facilities**, including injection wells and lift stations, helping to maintain regulatory compliance and permit-required data integrity.
- **Backup staffing and knowledge continuity**, reducing risks associated with vacation or turnover.

The technician will collaborate closely with the operations team and Jacobs' deep bench of SCADA engineers to ensure robust system performance across all facilities.

**Above and Beyond — Dedicated I&C Technician:** In addition to the onsite I&C Technician on the project team, Jacobs will assign a separate, dedicated I&C Technician based in the region to support both this project and a nearby sister project—ensuring rapid, expert response across all facilities. This shared-resource model provides local familiarity, operational continuity, and cost efficiency without compromising coverage. ($210,000 embedded value.)

## Firm-wide SCADA and Cybersecurity Capabilities

Jacobs brings extensive SCADA and IT/OT expertise, supporting O&M clients nationwide with modern, secure, and resilient control systems. Our in-house teams are certified integrators for Ignition and Rockwell Automation platforms, among others. Jacobs also brings national experience supporting utilities and agencies with cybersecurity reviews and frameworks. We apply industry best practices, including NIST standards, to our OT and IT environments, while tailoring controls to the unique needs of each facility. Our teams have supported water and wastewater clients across the state and nationwide, ensuring compliance with emerging requirements such as the American Water Infrastructure Act (AWIA). These resources will be available to the project as-needed, including our internal SCADA diagnostics team and cybersecurity specialists.

We routinely provide support for:
- SCADA architecture assessments and upgrades
- Network cybersecurity planning
- Remote access configuration and security hardening
- Data historian and dashboard development
- Compliance documentation and audit preparation

Jacobs' comprehensive SCADA capabilities ensure we can support any need the client may have, and allow us to develop a custom reporting tool for new membrane operations to make sure they work well and last. Our full-service expertise includes:

- **Integrated IT/OT:** We have 2,600+ IT professionals and 350 dedicated SCADA practitioners to support facilities with expert network management (Cisco-certified), applications and systems updates, comprehensive cybersecurity, and reliable distributed control systems.
- **Seamless Process Controls Systems:** We can deliver full-service implementations that seamlessly interface with existing ControlLogix PLCs, manage historian data, alarms, SQL database integration, and provide critical operational trends.
- **Customized Automation Tools:** Our proven capabilities include SCADA master planning, systems integration, software programming, and cybersecurity—ensuring custom-built monitoring solutions that maximize efficiency, compliance, and performance.

With Jacobs, the client gains a responsive partner uniquely qualified to leverage SCADA technology and enhance operational excellence.

*Client testimonial: "Jacobs has seamlessly integrated engineering, construction, and contract operations to deliver several equipment and controls system in a cost-effective manner. For Vancouver's major control system upgrade, each part of the organization is working hand-in-hand to provide smart state-of-the-art improvements that meet long-term needs for O&M while minimizing impacts to the current operation during construction; maintain treatment plant level-of-service; and maintain or extend service life of assets." — Frank Dick, PE, Sewer and Wastewater Engineering Supervisor, City of Vancouver*

## Reuse guidance

Universal: the firm-wide IT/OT capability statistics, the "practical, cost-effective, right-sized" cybersecurity philosophy, and the dedicated-I&C-technician shared-resource model are reusable across pursuits. Pursuit-specific: site-visit findings (specific server model, PLC/SCADA platform, redundancy gaps) must be regenerated from an actual site assessment of the target facility — do not reuse the Dell R340/single-point-of-failure finding unless verified for the new pursuit. Pair with `swip-asset-management-program-overview.md` (both use the shared dedicated-technician value-add pattern) and existing Hull-sourced `technical-approach/ot-scada-modernization-roadmap.md` for cross-comparison during merge, plus `compliance-plans/integrated-safety-security-cybersecurity-program.md`.
