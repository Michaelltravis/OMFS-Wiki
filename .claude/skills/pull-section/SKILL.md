---
name: pull-section
description: Pull one whole section of an extracted source proposal, in its original reading order — verbatim prose, sanitized, with exhibits reduced to asset-id markers — or list the wiki blocks that cover it in order. Use when the user says "pull the X section from Y", "give me the safety section from MMSD", "I need the asset management section from Hull, in order, verbatim", "what did we say about transition in OCWUT", "which blocks cover odor control in Fulton", or asks for a source section "as a Word doc". Runs on Sonnet; zero model tokens for the pull itself.
---

# Pull a section

The section layer (`verbatim/<slug>/sections.json`, built by `work/build_sections.py`) knows every heading in every extracted proposal with its page and paragraph span. `work/assemble_section.py` turns a section into one ordered document. This skill only runs that script and hands the result over; it never edits `wiki/` or `verbatim/`.

## Map the source phrase to a slug

| user says | slug |
|---|---|
| Hull, Town of Hull | `hull-wwtf-om-2026` |
| MMSD, Milwaukee | `mmsd-om-2028` |
| OCWUT, Oklahoma City | `ocwut-16-26` |
| Fulton, Fulton County, JC Solutions | `fulton-county-2025` |
| Santa Monica, SWIP | `santamonica-swip-om-2025` |

The script also accepts a unique prefix (`hull`, `mmsd`, `ocwut`, `fulton`, `santamonica`).

## Steps

1. **Run the pull** (zero tokens):
   `python work/assemble_section.py <slug> "<section words>"`
   - Add `--mode blocks` when the user asks which blocks cover the section, or wants block-level reuse notes.
   - Add `--docx` when they ask for a Word document.
   - Add `--raw` only if they explicitly want the unsanitized text (real client name).
   - Add `--pages A-B` when they give PDF page numbers instead of a section name; `--to-page N` extends a section to page N.
   - `--list` prints the whole section tree with ids if the user wants to browse.
2. **Exit code 2** means the query matched several sections: show the numbered candidates the script printed, ask which one, rerun with `--pick N`. **Exit 3**: nothing matched — run `--list` and offer the closest headings.
3. **Send the file** with `SendUserFile` (`work/pulls/<slug>/<section>.md`, plus the `.docx` if requested; `display: "attach"`).
4. **Reply in a few lines**: the section title and span (pages, paragraphs), the headings it contains, approximate word count, the sanitization replacement count, and any names the script listed as "left as-is for review" (e.g. `Veolia`, `the City`). Never paste the body into chat.

## Rules

- Verbatim mode is the source of truth for prose; blocks mode is the reuse view. If the user wants to write from it, point them at the `## Reuse guidance` in the blocks rather than the verbatim pull.
- Sanitization lists live in `verbatim/<slug>/sanitize.json` (`review_status: draft` until the proposal team confirms them). If a pull shows a client or facility name that slipped through, add it there and rerun — do not hand-edit the output.
- Exhibit text is intentionally dropped; `[graphic: <id> — <exhibit title>]` markers point at `wiki/graphics/<slug>.md` and the DAM.
- Do not run `--raw` output into a deliverable without the proposal team's QC; the verbatim layer carries the real client name by design.
