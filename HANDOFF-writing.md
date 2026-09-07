# Handoff — writing the Richmond proposal from the content bank

Written 2026-09-06 for whoever picks up the writing stage (Michael, a teammate, or a fresh Claude session). Everything below is on disk; nothing depends on the conversation that built it.

## 1. What exists

| Asset | Where | State |
|---|---|---|
| Verbatim prose of four winning/recent proposals, page-anchored, ¶-numbered | `verbatim/<slug>/pages/pNNNN.md`, `full.md`, `coverage.md` | Hull (104 pp), Santa Monica (119), OCWUT (184), Fulton County (507; body p1–195) |
| Sanitized content blocks, schema v2, back-pointers to verbatim | `wiki/<category>/*.md`; faceted index `wiki/index.md` + `index.json` | Hull + Santa Monica complete (187 blocks, lint zero). OCWUT + Fulton build launched 2026-09-06 (run `wf_d5351da9-a97`); see README status table for final counts |
| Proof-point registry | `proof-points/registry.md` / `.json` | 696 ids (Hull+SWIP), 31 conflicts awaiting an owner; OCWUT/Fulton increment appends |
| Testimonials | `testimonials/inventory.md` | 46 quotes, **all permission-unknown** → none printable until consent is on file |
| Story catalog | `stories/catalog.md` | ranked house narratives with "the beat" and proof ids |
| Controlled vocabulary | `vocabulary/tags.md`, `tag-aliases.yaml` | 128 tags |
| Voice guide + rubric | `voice/voice-guide.md` (35 rules, 12 before/after pairs, calibration log), `voice/rubric.json`, `voice/metrics.py` | Calibrated: winners score 6.75–8.0, pilot and ChatGPT drafts ~2.8. Exemplar folder `voice/exemplar/` is still empty — drop Michael's exemplar there and re-run the voice-guide workflow to re-derive |
| Richmond pursuit inputs | `pursuits/richmond-2026/` → `pursuit.md`, `trip-report-digest.md`, `reqs/00–07*.md` (Compliance Matrix rows by §8.4.x), `spec-sheet.md/.json`, `Richmond_Spec_Sheet_v1_FOR_APPROVAL.docx`, `write-args/*.json` | Spec sheet **draft-for-approval**; 26 decisions D-01…D-26 |
| Renderer and validator | `work/build_docx.py` (markdown → Jacobs-Blue docx + `_notes.docx` companion; STAT/QUOTE/FACTBOX/CALLOUT devices; tags stripped from body), `work/validate_v2.py` | Tested |
| Workflows (Claude Code Workflow tool) | `.claude/workflows/extract-proposal.js`, `spec-sheet.js`, `write-section.js` | All resumable by run id |
| Skill | `.claude/skills/extract-proposal/SKILL.md` | Script-first v2 ingestion runbook |
| Prior drafts (benchmarks, do not modify) | `Desktop\Richmond\Draft Sections\01 Working Drafts` (ChatGPT), `02 Claude Working Drafts` (first Claude pilot) | Output target for v2: `03 Claude v2\` |

## 2. Before writing: lock the spec sheet

1. Michael ticks ☐ Approve / ☐ Change per row in `Richmond_Spec_Sheet_v1_FOR_APPROVAL.docx` (or states choices in chat).
2. Run, from `Desktop\Wiki`:
   ```bash
   python work/read_spec_decisions.py --dry-run
   python work/read_spec_decisions.py            # writes status: locked into spec-sheet.md/.json
   ```
   Overrides for chat answers: `--override "D-04=change:Use Traverse City instead of Southbridge"`.
3. Blank rows keep the default recommendation. The seven that most change the writing: D-01/D-02 (Mckenzie role; naming PM and Collection System Manager), D-04 (five references), D-07/D-10 (win-theme set), D-12 (never name the incumbent), D-20 (no pull quotes without permission).

## 3. Writing a section

One Workflow call per section. Args files are ready in `pursuits/richmond-2026/write-args/` (paste the JSON as `args`):

```
Workflow({ scriptPath: "C:\\Users\\micha\\Desktop\\Wiki\\.claude\\workflows\\write-section.js", args: <contents of write-args/03_qualifications.json> })
```

Pipeline: brief (Opus) → N angle drafts → judge panel → synthesis → attack loop (City evaluator, incumbent strategist, compliance walk, fact-check against registry + spec, metrics gates) → revise → render docx + notes companion → validator. Thresholds: every rubric dimension ≥8, mean ≥8.5, compliance all IDs addressed, fact-check zero unsupported, metrics hard gates green. Residual findings after the last round land in `<stem>_notes.docx`, never in body text.

**Order:** Qualifications first as the acceptance test (compare with `01 Working Drafts\03_…` and `02 Claude Working Drafts\03_…`). Then Staffing (30%) and Technical (30%), then the rest. A final cross-section pass for theme threading is a one-agent job: give it all seven drafts and the voice guide.

**Resume:** if a session limit interrupts, call the same script with `resumeFromRunId` from the launch message; completed agents replay from cache.

Optional args keys (default to the paths in §1 when omitted): `voiceGuide`, `rubric`, `spec`, `registry`, `testimonials`, `stories`, `index`. Use them only to point a run at an alternate spec sheet or voice guide.

### Profiles (set in the args file)

| Profile | writerModel | judgeModel | synthModel | angles / judges / rounds | ~tokens per 6-page section | Fable |
|---|---|---|---|---|---|---|
| A. Full v2 | fable | fable | fable | 4 / 3 / 3 | 4.0M | ~60% |
| B. Fable-finish | opus | opus | **fable** | 4 / 3 / 3 | 3.0M | ~0.4M |
| C. All-Opus | opus | opus | opus | 4 / 3 / 3 | 3.0M | 0 |
| **D. Lean Opus (default in write-args)** | opus | opus | opus | 2 / 2 / 2 | 1.5M | 0 |
| E. Sonnet smoke | sonnet | opus | opus | 2 / 2 / 2 | 0.9M | 0 |

Recommendation: D for the Qualifications acceptance run; B for Staffing and Technical; C for the rest. Fable has its own usage cap separate from the session window; if a run fails with "Fable limit", switch `synthModel` to opus and resume.

## 4. Human-owned items the pipeline cannot close

These are recorded as gap decisions in the spec sheet and will surface in the notes companions. Body text never carries a placeholder for them.

- Notarized surety statement and bonding capacity (nothing in the bank).
- Names of the on-site Project Manager and Collection System Manager; Mack Mckenzie's role and availability.
- Annual fees for the Clovis and West Basin references; written reference permissions.
- Written permission for any client quote (all 46 unknown).
- Current TRIR, EMR, DART; the ten-year litigation and termination list (legal).
- Waterbury quote attribution (two different speakers across sources).
- Account-team clearance to cite the Oklahoma City NexGen EAM work (live pursuit).
- Owner sign-off on the 31 registry conflicts (each has a recommended lock in spec §1).

## 5. Known limits and open questions

- Session usage limits interrupt long workflows; everything is resumable and committed incrementally. Commit after each resume (`git -C Desktop\Wiki add -A . && git commit`).
- Rubric gate `numbers_all ≥ 4.0` is calibrated on full-section units; on short units the winners themselves fall under it (see the calibration log in the voice guide). Treat it as directional for anything under ~1,000 words.
- The voice guide is derived from the winning proposals because no exemplar was supplied. Re-derive when one lands.
- The Wiki has its own git repo; two early snapshot commits also exist on the home-directory repo (harmless).
- Ingesting a new proposal: follow `.claude/skills/extract-proposal/SKILL.md` — converter → `pdf_to_verbatim.py` → `coverage.py` → `extract-proposal.js` with a ranges file (see `work/make_ranges_ocwut_fulton.py` for the pattern).
