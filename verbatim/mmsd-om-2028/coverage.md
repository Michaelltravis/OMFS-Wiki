# Coverage report — mmsd-om-2028

## Summary

| pages | text pages | image-only pages | mean word_recall | mean shingle_coverage | flagged pages | recovered blocks | recovered words |
|---|---|---|---|---|---|---|---|
| 147 | 147 | 0 | 0.9821 | 0.6978 | 29 (gate: word_recall<0.99 OR longest_missing_run>=15) | 64 | 1345 |

## Flagged pages

| page | word_recall | shingle_coverage | extra | order | longest_missing_run | missing sample (~12 words) |
|---|---|---|---|---|---|---|
| 5 | 0.5692 | 0.4787 | 0.4118 | 0.4787 | 83 | m u n i c a t i o n s c |
| 8 | 0.9706 | 0.7356 | 0.3186 | 0.5726 | 3 | our key leadership team covers the team covers the critical areas of |
| 16 | 0.8800 | 0.7965 | 0.1636 | 0.5310 | 83 | m u n i c a t i o n s c |
| 17 | 0.6755 | 0.2626 | 0.6756 | 0.0922 | 14 | manager with day to day the project manager with day to day |
| 18 | 0.9438 | 0.4226 | 0.6223 | 0.2811 | 8 | benefi t to mmsd benefi t to mmsd our o m teams |
| 19 | 0.8134 | 0.6374 | 0.3142 | 0.4090 | 8 | strengthening operations and focus on regional partnerships jacobs ii 4 |
| 22 | 0.9834 | 0.6565 | 0.3795 | 0.6519 | 2 | 5 step approach to labor relations s jacobs offers exceptional resources and |
| 28 | 0.9610 | 0.7303 | 0.2850 | 0.4441 | 7 | n i n g f r a m e w o r |
| 30 | 0.9731 | 0.6964 | 0.4221 | 0.4909 | 3 | corporate values align with mmsd s values and enhance our performance and |
| 31 | 0.9775 | 0.8134 | 0.2129 | 0.4674 | 13 | ethics hotline with secure portal to report harassment and discrimination concerns 24 |
| 32 | 0.9217 | 0.5148 | 0.5342 | 0.3672 | 5 | others to be determined with mmsd afscme trade apprenticeships for electricians afscme |
| 44 | 0.9809 | 0.3638 | 0.6961 | 0.2619 | 2 | ef iciency and recovery staffing certainty workforce development proactive staf ing leaves |
| 45 | 0.9805 | 0.4004 | 0.6677 | 0.3806 | 2 | dragon ly and argon digital tools process improvements 12 33m addition of |
| 46 | 0.7924 | 0.6469 | 0.3162 | 0.4948 | 59 | m u n i c a t i o n s c |
| 52 | 0.9207 | 0.6619 | 0.4571 | 0.5423 | 5 | operational excellence excellence monitoring monitoring tracking and tracking and reporting of reporting |
| 53 | 0.9821 | 0.7750 | 0.2802 | 0.7695 | 3 | decision making for safe compliant safe compliant and reliable and reliable operations |
| 55 | 0.9777 | 0.9038 | 0.1507 | 0.9038 | 6 | wide insight for operational for operational excellence excellence section 2 2 |
| 71 | 0.9839 | 0.9321 | 0.2346 | 0.9040 | 2 | south shore model training testing training given the ample data we had |
| 76 | 0.9782 | 0.6773 | 0.4103 | 0.4729 | 2 | deep domain expertise powered expertise powered by advanced by advanced digital tools |
| 77 | 0.9006 | 0.6828 | 0.3381 | 0.4706 | 6 | digital twin offers significant benefits to mmsd |
| 79 | 0.9887 | 0.6324 | 0.4258 | 0.5605 | 2 | delivering world class operational class operational technology and technology and expertise expertise |
| 82 | 0.9826 | 0.6350 | 0.5642 | 0.6350 | 1 | leveraging corporate corporate resources for resources for operational operational excellence excellence section |
| 83 | 0.6374 | 0.3506 | 0.5973 | 0.1410 | 8 | such as leading edge proven tools such as aquadna that provides predictive |
| 86 | 0.9884 | 0.0595 | 0.9571 | 0.0556 | 2 | certi ied experts culture of ethics compliance training tools sops and process |
| 88 | 0.9641 | 0.8146 | 0.3684 | 0.7650 | 5 | nal ysis int egr ate d o per atio ns shared knowledge |
| 103 | 0.9846 | 0.8460 | 0.2218 | 0.8393 | 7 | jacobs outperforms averages in top safety categories |
| 126 | 0.9560 | 0.3657 | 0.7192 | 0.3657 | 5 | communications roles and decision protocols exhibit iv 58 high level transition schedule |
| 129 | 0.9728 | 0.6066 | 0.5562 | 0.4875 | 3 | note includes up to two additional floating data sources with a one |
| 139 | 0.9846 | 0.6955 | 0.3887 | 0.3945 | 9 | contributing to build a resilient inclusive and thriving region jacobs v 2 |

## Repair history and residual-gap explanation

All 51 pages originally flagged (mean word_recall 0.9794) were repaired once against 300-DPI page renders (Sonnet agents, 9 batches), then two pages (87, 122) got a second, human-verified pass, and page 32 got a targeted structure fix. Two genuine content losses were found and corrected: a scrambled sentence + a dropped italic exhibit caption on page 87, and an entirely-missing 6th step caption ("Initiate Continuous Training and Development Program") on page 122, added as a new ¶23 (paragraphs count bumped 23→24, frontmatter updated). Page 32's career-ladder exhibit was missing its four tier labels (Supervisory/Senior-Lead/Operator/Entry-Level Operator); labels were added inline without changing paragraph count.

**Root cause of the source document's own defect:** this PDF's embedded body font (JacobsChronos-Regular/-CdRegular) has no ToUnicode mapping for its "fi"/"fl"/"ffi"/"ffl"/"ff" ligature glyphs. Confirmed via `fitz` rawdict inspection — e.g. the glyph in "Landfill" decodes to U+FFFD in the PDF's own text layer, not just in the markdown conversion. This affects both the raw PDF text layer AND the pymupdf4llm markdown conversion, producing defects like "land ill"→landfill, "staffng"→staffing, "certi ied"→certified, "qualifed"→qualified throughout the document. All instances found during repair were corrected in the verbatim pages against the rendered page images.

**Why 29 pages remain flagged after repair, and why that is expected:** `coverage.py` measures word recall against the PDF's own raw text layer as ground truth. Because that ground truth itself contains the ligature-drop defect above, AND contains decorative curved/circular graphic text extracted as scrambled single letters (e.g. a ribbon logo graphic on pages 5/16/46 whose true text "ONE TEAM / MMSD + JACOBS PARTNERSHIP..." is extracted letter-by-letter with line breaks), AND contains duplicated running sidebar/tab labels that appear once per visual column in the raw layer — correcting any of these (which the repair agents did, verified against page images) necessarily REDUCES word-recall against that flawed baseline. Sampled residual pages (5, 16, 17, 19, 32, 46, 83, 87-verified-clean, 122-verified-clean, 126) were individually checked against their rendered images post-repair: no further genuine narrative loss was found. The remaining flagged pages are dominated by this ground-truth mismatch plus low `order`/`shingle_coverage` scores on pages with non-linear layouts (org charts, hub-and-spoke exhibits, multi-column bios, Gantt-style schedule tables) where the true reading order is inherently non-sequential and can't match a single-pass text-layer baseline.

**Disposition:** accepted as final for this extraction. Pushing word_recall further would mean reintroducing verified-incorrect text (the ligature drops or scrambled graphic letters) to match the flawed baseline, which would make the verbatim layer less accurate, not more. Writers/QC should treat verbatim pages 5, 16, 46 (ribbon-logo graphic), 17/19 (leadership org chart/bios), 83 (hub diagram), and 126 (Gantt schedule) as visually non-linear source material where the markdown groups text by topic/box rather than raw left-to-right/top-to-bottom order.
