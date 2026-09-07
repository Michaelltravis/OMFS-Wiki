export const meta = {
  name: 'extract-proposal',
  description: 'Rebuild content-bank blocks from the verbatim page layer: per-section Opus block writers, Fable prose-vs-paraphrase judges, registry harvest, duplicate resolution, vocabulary, index',
  phases: [
    { title: 'Blocks', detail: 'one Opus writer per section range, reading only verbatim pages' },
    { title: 'Prose judge', detail: 'Fable checks each prose block is the prose, not a paraphrase; failures rewritten' },
    { title: 'Registries', detail: 'proof points, testimonials, stories (barrier: needs all blocks)' },
    { title: 'Merge + vocabulary', detail: 'duplicate pairs judged preferred/fallback; tags collapsed to a controlled vocabulary' },
    { title: 'Index + lint', detail: 'regenerate faceted index, lint schema v2' },
  ],
}

// args: { wiki, ranges:[{slug, name, pages:[a,b], category, rfpSectionType, clientNames:[..], context, existingBlocks:[paths]}], dryRun }
const W = args.wiki
// ranges may omit clientNames/context/existingBlocks; defaults come from args.bySlug[slug] = {clientNames, context}
const ranges = args.ranges.map(r => ({ ...r, clientNames: r.clientNames || (args.bySlug?.[r.slug]?.clientNames) || [], context: r.context || (args.bySlug?.[r.slug]?.context) || '', existingBlocks: r.existingBlocks || [] }))
const JUDGE_MODEL = args.judgeModel || 'fable'        // prose-vs-paraphrase judge (verbatim comparison; sonnet is adequate)
const PAIR_MODEL = args.pairJudgeModel || 'fable'     // duplicate-pair judge
const EXTRA = args.builderAddendum || ''              // pursuit-specific builder instructions (e.g. JV voice)

const BUILD = { type:'object', properties:{
  range:{type:'string'}, files_updated:{type:'array', items:{type:'string'}}, files_created:{type:'array', items:{type:'string'}},
  facts_fragment:{type:'string'}, quotes_fragment:{type:'string'}, uncovered_paragraphs:{type:'number'}, notes:{type:'string'} },
  required:['range','files_updated','files_created','facts_fragment','quotes_fragment','uncovered_paragraphs'] }
const JUDGE = { type:'object', properties:{ range:{type:'string'}, results:{type:'array', items:{type:'object', properties:{
  path:{type:'string'}, verdict:{type:'string', enum:['prose','paraphrase','missing-ref','recipe-ok','not-checked']}, reason:{type:'string'} }, required:['path','verdict']}} }, required:['range','results'] }
const REWRITE = { type:'object', properties:{ rewritten:{type:'array', items:{type:'string'}}, notes:{type:'string'} }, required:['rewritten'] }
const TEXT = { type:'object', properties:{ summary:{type:'string'}, files:{type:'array', items:{type:'string'}}, counts:{type:'object'} }, required:['summary','files'] }

const pagePath = (slug, p) => `${W}\\verbatim\\${slug}\\pages\\p${String(p).padStart(4,'0')}.md`

const buildPrompt = (r) => `You are rebuilding content-bank blocks for ONE section of a winning Jacobs proposal. Work only from the verbatim page files; they are the source of truth.

Read first: ${W}\\CLAUDE.md (schema v2, sanitization rules) and ${W}\\templates\\content-block.md.
Section: "${r.name}" of proposal slug ${r.slug}. Pages ${r.pages[0]}–${r.pages[1]}: ${Array.from({length:r.pages[1]-r.pages[0]+1},(_,i)=>pagePath(r.slug, r.pages[0]+i)).join(' ; ')}
Target category folder: ${W}\\wiki\\${r.category}\\ . rfp-section-type: ${r.rfpSectionType}. Pursuit context line for frontmatter: "${r.context}". Pursuit client names to generalize to [CLIENT] in narrative categories (NOT in past-performance/resumes): ${r.clientNames.join(', ')}.
Existing blocks already mapped to these pages (UPDATE these in place — keep the filename, rewrite the body so it is the prose from the verbatim pages, sanitized, and upgrade the frontmatter to schema v2; never delete a file): ${r.existingBlocks.length ? r.existingBlocks.join(' ; ') : '(none)'}

Rules:
1. Coverage: after you finish, every substantive paragraph in these pages (≥25 words, not headers/footers/TOC/boilerplate forms) must live in exactly one block, as prose — near-verbatim, sanitized only per CLAUDE.md. Create new blocks for anything the existing blocks do not cover. One topic per block; 150–900 words per block body.
2. block-type is prose for narrative, table for tables (keep GFM), exhibit for caption-only, roster for team lists. If an existing block is an instructional recipe ("Paragraph 1 — ..."), keep it but set block-type: recipe and pairs-with: <the prose block you created for that passage>.
3. Keep every number, outcome, award, client reference name, staff name. Strip only commercial fee/rate figures from commercial sections. Never write "do not restate".
4. Frontmatter v2: fill source-pages and verbatim-ref (e.g. "verbatim/${r.slug}/pages/p0012.md#¶3" — cite the ¶ of the primary passage), pursuit-type, client-type, client-size, geography, rfp-section-type [${r.rfpSectionType}], win-theme-map (choose from partner-transparency, compliance-leadership, regional-bench, odor-control, incumbent-displacement, asset-management, safety-culture, innovation-value-add, transition-continuity, workforce-development, energy-chemical-efficiency, collection-system, stormwater, community-engagement, digital-tools), proof-point-ids: [] (left empty — the registry stage fills it), status: preferred (unless you know a duplicate exists — then note it), house-favorite: false, sanitized: true, sanitization-loss (none|low|high — high if removing the client name removes the proof value), extracted: 2026-09-05, last-verified: 2026-09-05, tags (reuse existing tags where sensible, kebab-case). Keep any existing title/quality/reuse-notes that are still accurate.
5. Body ends with "## Reuse guidance".
6. Write two fragment files: ${W}\\work\\fragments\\${r.slug}\\${r.name.replace(/[^A-Za-z0-9]+/g,'-')}.facts.json = [{"claim": "...", "number": "...", "unit": "...", "as_of": "...|unknown", "page": n, "para": n, "block": "wiki/..path", "category": "outcome|scale|safety|financial|compliance|schedule|other"}] for EVERY quantified claim in the pages; and .quotes.json = [{"quote": "verbatim text", "speaker": "...", "title": "...", "org": "...", "page": n, "para": n, "block": "..."}] for every client/third-party quotation (empty list if none).
7. Do not read any other proposal's pages. Do not edit files outside wiki\\${r.category}\\ and work\\fragments\\.
${EXTRA}
Return: range name, files_updated, files_created, the two fragment paths, count of substantive paragraphs you could not place (should be 0), notes.`

const judgePrompt = (r, built) => `You are the prose judge for the content bank. For each block listed, decide whether its body IS the sanitized prose of its verbatim source or merely a paraphrase/summary of it.
Blocks: ${[...built.files_updated, ...built.files_created].join(' ; ')}
For each block: read its frontmatter verbatim-ref and source-pages, open the referenced verbatim page(s) under ${W}\\verbatim\\${r.slug}\\pages\\, and compare. Verdicts: prose (the body reproduces the source sentences near-verbatim with only [CLIENT]/location generalization and commercial figures removed), paraphrase (rewritten, condensed, or instructional — fails), missing-ref (verbatim-ref does not resolve or points to the wrong passage), recipe-ok (block-type recipe with a valid pairs-with). Be strict: a block that keeps the ideas but not the sentences is a paraphrase. Read-only — do not edit files.`

const rewritePrompt = (r, fails) => `Rewrite these content-bank blocks so each body is the sanitized PROSE of its verbatim source, not a paraphrase. Read ${W}\\CLAUDE.md sanitization rules first. For each: open the block, open its verbatim-ref page(s) under ${W}\\verbatim\\${r.slug}\\pages\\ (fix verbatim-ref if it was wrong), replace the body with the source sentences (generalize pursuit client names ${r.clientNames.join(', ')} to [CLIENT] in narrative categories only; keep every number; strip commercial fee/rate figures only), keep the frontmatter v2 fields and the "## Reuse guidance" section. Blocks and judge reasons:\n${fails.map(f => `- ${f.path}: ${f.verdict} — ${f.reason||''}`).join('\n')}`

phase('Blocks')
const perRange = await pipeline(ranges,
  r => agent(buildPrompt(r), {model:'opus', effort:'medium', phase:'Blocks', label:`build ${r.slug} ${r.name}`, schema:BUILD}),
  async (built, r) => {
    if (!built) return null
    let judged = await agent(judgePrompt(r, built), {model:JUDGE_MODEL, effort:'medium', phase:'Prose judge', label:`judge ${r.name}`, schema:JUDGE})
    let fails = (judged?.results||[]).filter(x => x.verdict==='paraphrase' || x.verdict==='missing-ref')
    for (let round=0; round<2 && fails.length; round++) {
      await agent(rewritePrompt(r, fails), {model:'opus', effort:'medium', phase:'Prose judge', label:`rewrite ${r.name} r${round+1}`, schema:REWRITE})
      judged = await agent(judgePrompt(r, {files_updated: fails.map(f=>f.path), files_created: []}), {model:JUDGE_MODEL, effort:'medium', phase:'Prose judge', label:`rejudge ${r.name} r${round+1}`, schema:JUDGE})
      fails = (judged?.results||[]).filter(x => x.verdict==='paraphrase' || x.verdict==='missing-ref')
    }
    return { range:r.name, slug:r.slug, built, residual_fails: fails }
  })
const done = perRange.filter(Boolean)
log(`Blocks: ${done.length}/${ranges.length} ranges; residual paraphrase failures: ${done.reduce((n,d)=>n+d.residual_fails.length,0)}`)

phase('Registries')
const slugs = [...new Set(ranges.map(r=>r.slug))]
const [registry, testimonials, stories] = await parallel([
  () => agent(`Build the proof-point registry for the content bank. Read every ${W}\\work\\fragments\\*\\*.facts.json (all slugs: ${slugs.join(', ')}) and, if it exists, the current ${W}\\proof-points\\registry.json. Cluster claims that describe the same fact (e.g. corporate revenue stated as $12B, $15B, $16B; NPDES compliance 99.8% vs 99.98%; collection miles 310 vs 320) into ONE id each with all observed values and their as-of/source; mark status: consistent | conflict | single-source. Assign ids PP-0001… (keep existing ids stable). Write ${W}\\proof-points\\registry.json (list of {id, claim, values:[{number, unit, as_of, source_slug, page, para, block}], status, category, owner: "", approved_for_external_use: "pending", conflicts_with:[]}) and ${W}\\proof-points\\registry.md (a readable table plus a "Conflicts to resolve" section listing every conflict id with its competing values). Then write ${W}\\work\\fragments\\pp_patches.json in the format expected by ${W}\\work\\patch_frontmatter.py: for each block, set proof-point-ids to the list of ids whose values appear in that block. Run: python "${W}\\work\\patch_frontmatter.py" "${W}\\work\\fragments\\pp_patches.json". Return summary, files, counts {claims, ids, conflicts, blocks_patched}.`, {model:'opus', effort:'medium', phase:'Registries', label:'proof-point registry', schema:TEXT}),
  () => agent(`Build the testimonials inventory. Read every ${W}\\work\\fragments\\*\\*.quotes.json (slugs ${slugs.join(', ')}) and also grep ${W}\\verbatim\\*\\pages\\*.md for quotation marks preceded/followed by an attribution line (— Name, Title, Org) to catch quotes the fragments missed. Write ${W}\\testimonials\\inventory.md: table with id TM-0001…, speaker, title, organization, verbatim quote, source slug/page/¶, permission: unknown, contact (if present in the verbatim page), used-in (blocks). Then patch testimonial-ids into the blocks that contain each quote via ${W}\\work\\patch_frontmatter.py (write ${W}\\work\\fragments\\tm_patches.json first). Return summary, files, counts.`, {model:'opus', effort:'medium', phase:'Registries', label:'testimonials', schema:TEXT}),
  () => agent(`Build the story catalog for Jacobs proposal writers. Read ${W}\\wiki\\index.md, then every block under ${W}\\wiki\\past-performance\\ and ${W}\\wiki\\win-themes\\ and any technical-approach block whose title contains turnaround, transition, case, savings, odor, or optimization. Identify every narrative that tells a before/after story with an outcome (e.g. a contract turnaround removing six 30-yard containers of debris; an enforcement action resolved; $12.7M estimated savings; a biofilter media upgrade saving $134K; an incumbent displacement with a client quote). Write ${W}\\stories\\catalog.md: for each story id ST-0001…: title, one-line arc, THE BEAT (the specific sentence or fact that makes it land), proof-point claims it depends on, testimonial if any, best-for rfp-section-types, pursuit types it fits (wwtp-om, collections, stormwater, incumbent-displacement, regulatory-settlement, odor), the block path(s) and verbatim page(s), and a house-favorite recommendation with one-line reason. Rank the top 10 at the top of the file. Then patch story-ids into the source blocks via ${W}\\work\\patch_frontmatter.py (write ${W}\\work\\fragments\\st_patches.json first). Return summary, files, counts.`, {model:'fable', effort:'high', phase:'Registries', label:'story catalog', schema:TEXT}),
])
log(`Registries: ${registry?.summary||'-'} | ${testimonials?.summary||'-'} | ${stories?.summary||'-'}`)

phase('Merge + vocabulary')
const PAIRS = { type:'object', properties:{ decisions:{type:'array', items:{type:'object', properties:{ a:{type:'string'}, b:{type:'string'}, decision:{type:'string', enum:['a-preferred','b-preferred','distinct','merge-into-a','merge-into-b']}, reason:{type:'string'} }, required:['a','b','decision']}} }, required:['decisions'] }
const cand = await agent(`Run: python "${W}\\work\\dedupe_candidates.py" --min 0.12 --out "${W}\\work\\dedupe_candidates.json" and return its summary; list the total number of candidate pairs and the path. Do nothing else.`, {model:'sonnet', effort:'low', phase:'Merge + vocabulary', label:'dedupe candidates', schema:TEXT})
const judgeBatches = Array.from({length: 12}, (_, i) => i)
const decisions = (await parallel(judgeBatches.map(i => () => agent(`You are judging duplicate-topic candidate pairs in the Jacobs content bank. Open ${W}\\work\\dedupe_candidates.json, take pairs with index in [${i*10}, ${i*10+10}) (0-based; if none exist for this slice, return an empty decisions list). For each pair read both blocks fully. Decide: a-preferred or b-preferred (same topic; one should be the writer's default because it is more complete, more quantified, or better prose — say why), distinct (genuinely different topics or complementary angles), merge-into-a / merge-into-b (one is a strict subset). Do NOT edit files. Return decisions.`, {model:PAIR_MODEL, effort:'medium', phase:'Merge + vocabulary', label:`judge pairs ${i*10}-${i*10+9}`, schema:PAIRS})))).filter(Boolean).flatMap(d => d.decisions)
const merge = await agent(`Apply duplicate decisions to the content bank. Decisions JSON: ${JSON.stringify(decisions)}. For a-preferred/b-preferred: set status: preferred on the winner and status: fallback plus superseded-by: <winner path> on the other, and supersedes: <loser path> on the winner. For merge-into-X: same as preferred, and append any facts/sentences present only in the loser to the winner's body under a "### Additional detail (merged)" heading before "## Reuse guidance" (sanitized), keeping the loser file as fallback. For distinct: no change. Write ${W}\\work\\fragments\\merge_patches.json and run python "${W}\\work\\patch_frontmatter.py" on it; do body merges with careful text edits. Return summary, files, counts {preferred, fallback, merged, distinct}.`, {model:'opus', effort:'medium', phase:'Merge + vocabulary', label:'apply merge', schema:TEXT})
const vocab = await agent(`Build the controlled tag vocabulary. Collect every tag from every block frontmatter under ${W}\\wiki\\**\\*.md (excluding index.md, graphics/). Cluster synonyms and near-duplicates (transition/transition-plan, regional-support/regional-bench, key-personnel/resume-bio, etc.) into ~100–130 canonical kebab-case tags organized by facet (scope, discipline, section, device, theme, geography). Write ${W}\\vocabulary\\tags.md (one canonical tag per line as "- tag — one-line definition", grouped under facet headings) and ${W}\\vocabulary\\tag-aliases.yaml (alias: canonical). Then write ${W}\\work\\fragments\\tag_patches.json that replaces each block's tags with their canonical forms (deduplicated, max 12 per block) and run python "${W}\\work\\patch_frontmatter.py" on it. Return summary, files, counts {tags_before, tags_after, blocks_patched}.`, {model:'opus', effort:'medium', phase:'Merge + vocabulary', label:'tag vocabulary', schema:TEXT})
log(`Merge: ${merge?.summary||'-'} | Vocab: ${vocab?.summary||'-'}`)

phase('Index + lint')
const fin = await agent(`Finalize the content bank. Run in order and capture outputs: python "${W}\\work\\regen_index.py" (writes wiki/index.md and wiki/index.json); python "${W}\\work\\lint_blocks.py" --json "${W}\\work\\lint_report.json". Then read the lint report: fix ONLY mechanical violations yourself (missing required key with an obvious value such as extracted/last-verified dates 2026-09-05, status preferred default, house-favorite false, sanitized true, proof-point-ids [] when absent, category/folder mismatch by moving the value not the file) using ${W}\\work\\patch_frontmatter.py; re-run the linter. Do not touch bodies. Update the status table in ${W}\\README.md for the slugs ${slugs.join(', ')} (blocks by category, verbatim pages, registry rows) and fix the stale line in ${W}\\ONBOARDING.md that says Santa Monica is queued. Return summary, files, counts {blocks, lint_violations_before, lint_violations_after, unresolved_rules}.`, {model:'sonnet', effort:'low', phase:'Index + lint', label:'index + lint', schema:TEXT})
log(`Final: ${fin?.summary||'-'}`)

return { ranges: done.map(d => ({range:d.range, slug:d.slug, updated:d.built.files_updated.length, created:d.built.files_created.length, uncovered:d.built.uncovered_paragraphs, residual_fails:d.residual_fails})), registry, testimonials, stories, dedupe: cand, decisions_count: decisions.length, merge, vocab, fin }
