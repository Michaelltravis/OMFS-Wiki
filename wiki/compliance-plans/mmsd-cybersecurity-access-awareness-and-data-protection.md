---
title: Cybersecurity Access Control, Workforce Awareness, Data Protection, and Field Security
category: compliance-plans
block-type: prose
tags: [cybersecurity, scada, training-certification, collection-systems, lift-stations, cmms, quality-assurance, continuous-improvement]
source: mmsd-om-2028
source-section: "IV.A.4. Safety, Security Approach and Emergency Preparedness — 4.2.7 (continued): Access Control and Account Management; Workforce Awareness, Testing, and Threat Detection; Data Protection, Continuous Improvement, and Partnership; Field and Collection System Security"
source-pages: [109]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0109.md#¶5", "verbatim/mmsd-om-2028/pages/p0109.md#¶7", "verbatim/mmsd-om-2028/pages/p0109.md#¶9", "verbatim/mmsd-om-2028/pages/p0109.md#¶12"]
pursuit-type: [wwtp-om, multi-facility, collections]
client-type: authority
client-size: "Two large water reclamation facilities plus regional conveyance and biosolids production"
geography: "Midwest / WI / WDNR"
rfp-section-type: [compliance]
win-theme-map: [compliance-leadership, digital-tools, collection-system, partner-transparency]
proof-point-ids: [PP-2664, PP-2665, PP-2666]
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:27.access-control-and-account-management
section-order: 1
context: Midwest US regional sewerage district, two large water reclamation facilities (Jones Island and South Shore) plus biosolids production, RFP P-3216, 2028 challenger bid vs. incumbent operator; WDNR
quality: Specific where most cybersecurity narrative is vague — least privilege with just-in-time escalation, no shared accounts, enhanced credential monitoring on SCADA-adjacent systems, AES-256 encryption with change attribution, and an offer of joint penetration testing with the client. Closes by extending the same vigilance to remote conveyance sites and logging field findings in the CMMS.
reuse-notes: Confirm the encryption standard and monitoring toolset with corporate IT security before reuse. The joint penetration-testing offer is conditional ("as appropriate") and should stay conditional unless the capture team has agreed to it. Adjust the field security paragraph to the remote assets actually in scope.
---

# Access Control and Account Management

Jacobs enforces rigorous identity and access management controls based on role-based access, unique user accounts, and least-privilege principles. Account permissions are reviewed periodically and disabled promptly when no longer required. Privilege escalation is controlled through just-in-time access, shared accounts are prohibited, and enhanced credential monitoring is applied to critical and SCADA-adjacent systems.

# Workforce Awareness, Testing, and Threat Detection

Jacobs conducts mandatory annual cybersecurity and critical infrastructure protection training, supplemented by simulated phishing exercises and advanced email filtering. Continuous monitoring using SIEM platforms, behavioral analytics, and automated alerting supports real-time threat detection and proactive threat hunting. Jacobs performs routine penetration testing on its business networks and will coordinate joint testing of protected systems with [CLIENT], as appropriate.

# Data Protection, Continuous Improvement, and Partnership

Jacobs protects data confidentiality and integrity through AES-256 encryption, automated data classification, version control, and change attribution to support auditability and compliance. Cybersecurity performance will be reviewed quarterly with [CLIENT]'s risk and IT teams to assess metrics, track corrective actions, and incorporate lessons learned from drills, audits, and incidents.

Jacobs' 24/7 readiness is supported by Safety360, which analyzes safety and security data across our global portfolio to identify emerging risks and recurring vulnerabilities. Together, Jacobs and [CLIENT] will maintain a culture of vigilance, shared learning, and continuous improvement to protect [CLIENT]'s people, assets, and data.

# Field and Collection System Security

[CLIENT]'s conveyance and collection assets receive the same level of cybersecurity vigilance as treatment facilities. Jacobs will monitor alarms and intrusion alerts from remote sites, conduct access and lighting inspections, and document findings in the CMMS. Integration of CCTV, SCADA, and monitoring systems provides real-time visibility into systemwide security conditions and response actions.

## Reuse guidance

Universal: the identity and access management paragraph (role-based access, unique accounts, least privilege, periodic reviews, just-in-time escalation, no shared accounts, enhanced monitoring on SCADA-adjacent systems); the training-plus-simulated-phishing model; the SIEM and behavioral analytics monitoring stack; the data protection controls; the quarterly cybersecurity performance review with the client's risk and IT teams; and the field and collection system paragraph.

Pursuit-specific: the client team names in the review cadence, the remote assets listed in the field security paragraph, and the CMMS name. Where the client operates its own SIEM or SOC, describe the interface rather than presenting Jacobs' stack as the whole answer.

Pairs with [Enterprise Cybersecurity — Governance, Incident Response, and Network Protection](mmsd-cybersecurity-governance-and-incident-response.md), which this block continues. Read verbatim page p0109 for the full passage.
