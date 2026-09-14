---
title: Managed OT Privileged Access Management (PAM) Service
category: technical-approach
block-type: prose
tags: [cybersecurity, scada, instrumentation-controls, digital-tools, quality-assurance, technical-approach, value-added-services, differentiator, innovation]
source: mmsd-om-2028
source-section: "Section IV, 2.4.3. Jacobs Managed OT Privileged Access Management (PAM) Service"
source-pages: [81]
verbatim-ref: ["verbatim/mmsd-om-2028/pages/p0081.md#¶7", "verbatim/mmsd-om-2028/pages/p0081.md#¶8", "verbatim/mmsd-om-2028/pages/p0081.md#¶9", "verbatim/mmsd-om-2028/pages/p0081.md#¶10", "verbatim/mmsd-om-2028/pages/p0081.md#¶14", "verbatim/mmsd-om-2028/pages/p0081.md#¶18"]
pursuit-type: [wwtp-om, multi-facility, collections, solids]
client-type: authority
client-size: "2 large WRFs / deep tunnel ISS / regional sewerage district"
geography: "Midwest / WI / WDNR"
rfp-section-type: [tech-approach]
win-theme-map: [innovation-value-add, digital-tools, partner-transparency, compliance-leadership]
proof-point-ids: []
testimonial-ids: []
story-ids: []
status: preferred
house-favorite: false
sanitized: true
sanitization-loss: none
extracted: 2026-09-05
last-verified: 2026-09-05
section-id: mmsd-om-2028:25.2-4-3-jacobs-managed-ot-privileged-access-management-pam-ser
section-order: 1
context: Midwest US regional sewerage district, two large water reclamation facilities plus biosolids production, 2028 challenger bid against an incumbent operator; state DNR regulatory regime
quality: A concrete, offerable OT cybersecurity enhancement written as an optional value-add, with four named capabilities each paired with a plain-language "what this means for you" example drawn from real plant work (PLC programming, SCADA passwords, wet-weather pump logic, remote conveyance troubleshooting). Useful in any pursuit where the client raises SCADA/OT security.
reuse-notes: Confirm the client actually wants PAM offered as an option before including; the block is written as "should [CLIENT] desire." Swap the four example scenarios for assets the client actually owns (PLC, SCADA server, network switch, remote conveyance site all generalize easily). Exhibit asset ID 303_007CAM_3 is a Jacobs-standard graphic and is not client-specific. Pairs with the corporate-resources block for the OT/automation/cybersecurity pillar.
---

# Managed OT Privileged Access Management (PAM) Service

To further strengthen cybersecurity and operational integrity, we can implement a PAM solution purpose-built for OT, as summarized in **Exhibit IV-33** (asset `303_007CAM_3`), should [CLIENT] — a regional sewerage district operating two large water reclamation facilities and a deep-tunnel conveyance and storage system — desire. Unlike traditional VPN and jump host access, where users may gain broad network entry and passwords often remain static, PAM provides **tight, role-based access** to specific devices and applications without exposing the underlying network.

Our PAM solution stores privileged credentials in a secure vault and automatically rotates them, eliminating the risk of password reuse and reducing the number of ways an attacker could gain access. It also manages and logs privileged sessions so activity can be monitored and recorded, creating a complete audit trail to support compliance and incident response.

For [CLIENT], this would mean that a contractor who needs to update a PLC program can be granted time-limited access to that single PLC, but not to unrelated systems. With this kind of "just-in-time" access, elevated privileges exist only for the duration of approved tasks and then expire automatically.

Integrated with our OT asset management and change control processes, PAM can provide a secure, streamlined way to manage remote and onsite privileged access, improving accountability, reducing cybersecurity risk, and eliminating the complexity and vulnerabilities of legacy remote access technologies.

## Exhibit IV-33. Managed OT Privileged Access Management

**Granular, Role-Based Access** — System enforces precise, role-based permissions reducing cybersecurity risk. For [CLIENT], this means a contractor performing maintenance on a single PLC at one water reclamation facility can be granted access only to that controller — without exposing the rest of the process networks, significantly reducing cybersecurity risk.

**Credential Vaulting and Rotation** — System stores credentials in a secure vault and rotates them automatically, reducing the likelihood of unauthorized access. Static passwords are a common vulnerability in legacy remote access solutions. For [CLIENT], our approach ensures that passwords for critical assets like SCADA servers or network switches are never reused or exposed, reducing the risk of credential compromise.

**Session Monitoring and Audit Trails** — Complete audit trail for compliance and incident response, ensuring transparency and accountability for operational changes. Every privileged session is recorded and monitored in real time. If a technician modifies pump control logic during a wet weather event, [CLIENT] can review the exact steps taken, ensuring transparency and accountability for operational changes.

**Just-in-Time Access** — Solution provides permissions only for the duration of an approved task, reducing persistent risk. For [CLIENT], this means that when an engineer needs to troubleshoot a remote conveyance site, access is automatically revoked once the work is complete, reducing persistent risk. Traditional VPNs often leave elevated privileges active indefinitely, increasing exposure.

## Reuse guidance

Universal: the four-capability structure (granular role-based access, credential vaulting and rotation, session monitoring and audit trails, just-in-time access), each followed by a one-sentence client-specific consequence. That pairing — capability, then "for [CLIENT], this means" — is the reusable device and should survive rewriting.

Pursuit-specific: whether PAM is offered at all, and the four example scenarios. Substitute assets the client names in its RFP (membrane skid PLCs, lift station RTUs, a SCADA historian) so each example lands. If the client has an existing IT/OT security standard, add a sentence stating alignment with it.

Read `verbatim/mmsd-om-2028/pages/p0081.md` for the full passage. Pairs with [Leveraging corporate resources for operational excellence](mmsd-leveraging-corporate-resources-operational-excellence.md), whose OT/automation/cybersecurity pillar this block supports.
