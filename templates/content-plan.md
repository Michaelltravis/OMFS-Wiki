---
pursuit: <slug>
version: 1
status: draft
directive: <path to the Proposal Directive .docx>
rfp: <path to the RFP pdf>
generated: <date>
---

# Content plan — <pursuit name>
_One sheet that tells the writers which topics go in each section. Sections follow the Proposal Directive outline, checked against the RFP. Under each section, the RFP-required topics are already ticked; the Jacobs-standard topics are the ones the proposal manager decides on._

## How to use this sheet

**Selection rule.** A ticked topic (☑) is drafted; an unticked topic (☐) is not. A ticked topic with a note gets that angle. RFP-required rows stay ticked. Add pursuit-specific topics in the *Additional topics* rows under any section. The spec sheet locks the numbers, proofs and references the ticked topics will use; this sheet only decides what is covered.

**Marks.** `☑ lead` — the topic carries the section's opener or closer · `☑` — include · `☑ brief` — one paragraph or a table row at most · `☐` — leave out.

**Start from.** Each section can name a source proposal section the writer reads first and adapts as the backbone of the draft, before searching the library for anything else. A starting point, not a copy: the client's outline still governs the structure. `—` means no steer.

**Pull from.** Any row can point at a specific wiki block or verbatim pages to use for that topic; it overrides the preferred block in the Source column. Blank means the writer uses the Source column's block, or searches the library.

**Sources.** RFP-required rows come from the Directive's PROPOSAL OUTLINE table and the requirement exports in `pursuits/<slug>/reqs/`. Jacobs-standard rows come from `templates/standard-topics.md`, each with its preferred wiki block.

## Evaluation weights

| Section | Weight |
|---|---|
| <from the Directive EVALUATION CRITERIA table> | |

## RFP cross-check

<one line per finding: sections in the Directive with no reqs export, reqs exports with no Directive section, requirement-count differences. "No mismatches found" when clean.>

## <8.4.n Section title> (<weight>, <pages> pages)

**Start from:** <— | source slug — section title, pages a–b · note>

| # | Topic | Source | Include? | Pull from | Notes / angle |
|---|---|---|---|---|---|
| 1 | <RFP sub-heading from the Directive> | RFP — <quoted requirement, trimmed> | ☑ | <block path or slug — section, pages a–b; optional> | required |
| 2 | <Jacobs-standard topic> | Jacobs standard — <preferred block path> | ☐ | | <why it is always there> |
| — | Additional topic | | ☐ | | |
| — | Additional topic | | ☐ | | |
| — | Additional topic | | ☐ | | |
