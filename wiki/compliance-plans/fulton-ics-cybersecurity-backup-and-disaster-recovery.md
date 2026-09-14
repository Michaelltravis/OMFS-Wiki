---
title: ICS Cybersecurity, 3-2-1-1 Backups, and Disaster Recovery
category: compliance-plans
block-type: prose
tags: [cybersecurity, scada, resilience-planning, emergency-response, regulatory-compliance, digital-tools, jv-structure]
source: fulton-county-2025
source-section: "2.8 Cybersecurity"
source-pages: [96, 97]
verbatim-ref: ["verbatim/fulton-county-2025/pages/p0096.md#¶22", "verbatim/fulton-county-2025/pages/p0096.md#¶23", "verbatim/fulton-county-2025/pages/p0096.md#¶25", "verbatim/fulton-county-2025/pages/p0096.md#¶26", "verbatim/fulton-county-2025/pages/p0096.md#¶27", "verbatim/fulton-county-2025/pages/p0097.md#¶1", "verbatim/fulton-county-2025/pages/p0097.md#¶2", "verbatim/fulton-county-2025/pages/p0097.md#¶3", "verbatim/fulton-county-2025/pages/p0097.md#¶4", "verbatim/fulton-county-2025/pages/p0097.md#¶5", "verbatim/fulton-county-2025/pages/p0097.md#¶6", "verbatim/fulton-county-2025/pages/p0097.md#¶7"]
pursuit-type: [wwtp-om, multi-facility, jv-delivery]
client-type: county
client-size: "Three MBR water-reclamation facilities plus pump stations"
geography: "Southeast / GA / GA EPD"
rfp-section-type: [compliance]
win-theme-map: [resilience-planning, compliance-leadership, innovation-value-add]
proof-point-ids: [PP-1750]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: low
extracted: 2026-09-07
last-verified: 2026-09-07
context: Southeast US county wastewater O&M pursuit, bid as JC Solutions, a Jacobs/CERM JV.
quality: Near-verbatim OT/ICS security strategy coupled to a specific backup and recovery sequence.
reuse-notes: Validate standards, contract references, backup maturity, and the 90-day priority before use; do not claim an assessment finding without a target-system review.
---

# ICS Cybersecurity, 3-2-1-1 Backups, and Disaster Recovery

JC Solutions understands that cybersecurity is critical to the reliability and resilience of wastewater-treatment operations. As cyber threats targeting water and wastewater utilities increase, our team will apply a proven and comprehensive strategy to safeguard Industrial Control Systems (ICS), SCADA, and business systems across the [CLIENT] service area. Jacobs brings deep expertise in ICS cybersecurity, shaped by years of work with federal, municipal, and confidential clients—including the EPA. Our approach is aligned with NIST SP 800-series guidance and includes both proactive defense strategies and rapid-response protocols to protect infrastructure, data, and public health.

Using the Purdue model, assets are divided based on their criticality, and separate process areas are isolated to prevent lateral movement between systems. Security controls and network inspection are added between areas to monitor and manage access. Real-time monitoring is used to ensure that security controls are operable, and issues are detected before operations are impacted. Systems are kept patched and updated to ensure mitigation against the latest vulnerabilities.

Our cybersecurity program will include a risk and resilience assessment; a site-specific cybersecurity and SCADA Security Plan; ICS-focused cybersecurity policies and procedures including logical and physical network-architecture reviews, remote-access controls, endpoint protection, and penetration testing of WAN systems; cybersecurity awareness in staff onboarding and regular training; ongoing threat monitoring with real-time alerts; backup and disaster-recovery planning; and compliance with applicable regulations and [CLIENT] IT standards.

Many facilities and utilities do not have adequate backup systems in place. During our brief review of the core control systems for [CLIENT] wastewater facilities, it is unclear if the utility has an offsite backup system. We will implement an improved backup strategy following the 3-2-1-1 rule, including offsite and immutable cloud-storage backups. This approach minimizes downtime and data loss in the unfortunate event of server failure or malicious attack. Establishing a baseline backup of all systems will be the Operational Technology team’s highest priority in the first 90 Days. These backups will primarily be stored onsite, and immutable encrypted copies will be made offsite to ensure availability during a disaster.

We will also provide secure integration of SCADA, LIMS, CMMS, GIS, and other critical systems. Data will be stored and shared via encrypted, access-controlled systems that are fully auditable and aligned with [CLIENT] IT protocols.

## Reuse guidance

The architecture, backup, and recovery sequence is reusable; the claimed lack of offsite backups is source-specific and must be independently verified.
