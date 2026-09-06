Regenerated against `voice/metrics.py` v2 (hard gates from `voice/rubric.json`; `numbers_per_100_words` split into `numbers_body`/`numbers_all` per voice-guide.md section 4a). Hull and Santa Monica page ranges were re-concatenated with each page's YAML frontmatter stripped — the prior run had left frontmatter fields (`page:`, `chars_text_layer:`, etc.) bleeding into adjacent paragraphs, inflating both sentence length and numeric-token counts; these figures supersede the ones in the original table.

### Hard gates

| Metric | Gate | Hull (winning) | SantaMonica (winning) | Richmond pilot (ours) | Richmond ChatGPT |
|---|---|---|---|---|---|
| sentence_median_words | 18-25 | 21 PASS | 17 FAIL | 18 PASS | 12.5 FAIL |
| sentence_p90_words | <=40 | 36.4 PASS | 37.8 PASS | 60.0 FAIL | 29.0 PASS |
| avg_paragraph_words | <=55 | 41.8 PASS | 31.4 PASS | 63.7 FAIL | 24.8 PASS |
| words_per_heading | 100-220 | 137.7 PASS | 146.9 PASS | 281.2 FAIL | 80.4 FAIL |
| numbers_all | >=4.0 | 5.22 PASS | 3.36 FAIL | 7.91 PASS | 3.92 FAIL |
| table_share | <=0.35 | 0.2487 PASS | 0.0338 PASS | 0.2416 PASS | 0.39 FAIL |
| passive_voice_rate | <=0.15 | 0.1057 PASS | 0.0328 PASS | 0.1128 PASS | 0.1167 PASS |
| client_paragraph_density | >=0.30 | 0.379 PASS | 0.432 PASS | 0.5192 PASS | 0.2162 FAIL |
| tags_in_body | ==0 | 0 PASS | 0 PASS | 52 FAIL | 19 FAIL |
| banned_words_total | ==0 | 4 FAIL | 4 FAIL | 0 PASS | 0 PASS |

### Directional (no PASS/FAIL) and new counters

| Metric | Hull | SantaMonica | Richmond pilot | Richmond ChatGPT |
|---|---|---|---|---|
| numbers_body (excl. devices) | 2.99 | 3.45 | 5.70 | 3.42 |
| punch_sentences_per_120_words | 0.58 | 1.23 | 1.28 | 1.87 |
| so_what_rate | 0.1099 | 0.3704 | 0.4054 | 0.0 |
| we_you_ratio | 1.30 | 1.00 | 0.89 | 0.0 |
| bracket_count | 0 | 0 | 54 | 24 |
| serial_comma_missing | 9 | 5 | 18 | 2 |

Note: Santa Monica's `numbers_all` (3.36) now fails the 4.0 gate on the full p0004–p0013 range documented below, unlike the ~4.9–5.0 figure the calibration log measured on the narrower ES-1–ES-8 (p0006–p0013) unit — a section-type/unit-length effect flagged as an open question in voice-guide.md's calibration log, not a code defect.

Source files (unchanged from the prior run):
- Hull: verbatim/hull-wwtf-om-2026/pages/p0005.md–p0017.md (clients: Hull, the Town)
- SantaMonica: verbatim/santamonica-swip-om-2025/pages/p0004.md–p0013.md (clients: Santa Monica, the City)
- Richmond pilot: Desktop/Richmond/Draft Sections/02 Claude Working Drafts/_work/draft_03_qualifications_edited.md (clients: Richmond, the City)
- Richmond ChatGPT: Desktop/Richmond/Draft Sections/01 Working Drafts/03_Tech_3_Firm_Qualifications_Richmond_Draft.docx (clients: Richmond, the City)
