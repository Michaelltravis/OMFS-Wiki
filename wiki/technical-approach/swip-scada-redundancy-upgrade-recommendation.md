---
title: SCADA Control System Redundancy Upgrade Recommendation
category: technical-approach
tags: [scada, ignition, hyperconverged-infrastructure, redundancy, control-system, resiliency, unpriced-recommendation]
source: santamonica-swip-om-2025
source-section: "Section 4: Suggested Modifications to the Scope of Work, Additional Items for Consideration — SCADA Control System Deployment (p. 106)"
context: Southern California sustainable water infrastructure O&M, 2025
sanitized: true
quality: a short, concrete pair of named-technology recommendations (Ignition virtualized redundancy, hyperconverged infrastructure) presented honestly as unpriced/needing more scoping — a useful pattern for suggesting high-value modifications without overcommitting on cost
reuse-notes: this was explicitly presented as an unpriced idea requiring further scoping information from the client, not a firm commercial offer — preserve that framing if reused. Confirm current recommended SCADA platform/technology names before reuse, as products and versions change.
---

# SCADA Control System Redundancy Upgrade Recommendation

## Additional Items for Consideration

[Firm] believes the following suggested modification will bring significant value to [CLIENT]; however, additional information is required to scope the work and provide a price.

### SCADA Control System Deployment

Two key enhancements should be considered for the current SCADA control system deployment. Introducing redundancy at both the SCADA/HMI layer and the server infrastructure would significantly improve system resiliency and operational continuity. These upgrades would help safeguard against single points of failure and ensure consistent performance in critical environments:

- Implementing Ignition virtualized redundancy within the SCADA system ensures continuous operation by automatically switching to a backup server during failures.
- Implementing hyperconverged infrastructure consolidates compute, storage, and networking into a unified platform, simplifying management and scaling. Compared to a single-server setup, it offers higher availability, built-in redundancy, backup, and seamless expansion without major hardware overhauls.

## Reuse guidance

This block demonstrates a useful proposal pattern distinct from the priced value-adds elsewhere in this section: presenting a genuinely valuable modification honestly as "we need more information to scope and price this" rather than forcing a premature number — this can read as credible and consultative rather than salesy. Confirm the named technologies (Ignition virtualized redundancy, hyperconverged infrastructure) are still the current recommended approach before reuse, as SCADA platforms and infrastructure products evolve. Pairs directly with `ot-scada-modernization-roadmap.md` (the Hull pursuit's three-phase OT/SCADA modernization roadmap) — that block's Phase 2 (secure remote access, redundant WAN connectivity) and Phase 3 (automation/intelligence) are a natural structural home for this SCADA redundancy recommendation if a fuller OT/SCADA narrative is needed for a given pursuit.
