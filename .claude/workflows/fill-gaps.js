export const meta = {
  name: 'fill-gaps',
  description: 'Create content blocks only for verbatim paragraphs that no block covers (one source per run), judge them as prose, then re-assign section order, rebuild the proof-point registry, index and lint',
  phases: [
    { title: 'Blocks', detail: 'one Opus writer per gap range, creating blocks only for the listed uncovered paragraphs' },
    { title: 'Prose judge', detail: 'Fable checks each new block is the prose, not a paraphrase; failures rewritten' },
    { title: 'Finalize', detail: 'find_uncovered → assign_block_sections → registry → regen_index → lint; testimonials if any quotes' },
  ],
}

// args: either the contents of work/fragments/ranges_gapfill_<slug>.json inline —
//   { wiki, slug, clientNames:[..], context, today, ranges:[{slug, name, sectionId, pages:[a,b], category, rfpSectionType,
//     existingBlocks:[paths], uncovered:[{page, para, words, kind, first_words, ref}]}] }
// — or the compact form { wiki, slug, rangesFile: "<absolute path to that json>" }, in which case a small Sonnet
//   agent reads the file and returns its fields (kept tiny so launches and resumes stay cheap).
// Optional: builderAddendum, judgeModel, filePrefix.
const W = args.wiki
const LOADED = { type:'object', properties:{
  slug:{type:'string'}, clientNames:{type:'array', items:{type:'string'}}, context:{type:'string'}, today:{type:'string'},
  ranges:{type:'array', items:{type:'object', properties:{
    slug:{type:'string'}, name:{type:'string'}, sectionId:{type:'string'}, pages:{type:'array', items:{type:'number'}},
    category:{type:'string'}, rfpSectionType:{type:'array', items:{type:'string'}}, existingBlocks:{type:'array', items:{type:'string'}},
    uncovered:{type:'array', items:{type:'object', properties:{ page:{type:'number'}, para:{type:'number'}, words:{type:'number'},
      kind:{type:'string'}, first_words:{type:'string'}, ref:{type:'string'} }, required:['page','para','ref']}} },
    required:['name','pages','category','rfpSectionType','existingBlocks','uncovered']}} },
  required:['slug','clientNames','context','today','ranges'] }
let cfg = args
if (!args.ranges && args.rangesFile) {
  phase('Blocks')
  cfg = await agent(`Read the JSON file ${args.rangesFile} and return its contents unchanged as the fields slug, clientNames, context, today and ranges (every range with all its existingBlocks and uncovered entries, in file order). Transcribe exactly; do not summarize, reorder, drop or add anything; do not modify any file.`, {model:'sonnet', effort:'low', phase:'Blocks', label:'load ranges', schema:LOADED})
}
const slug = cfg.slug
const clientNames = cfg.clientNames || []
const context = cfg.context || ''
const EXTRA = args.builderAddendum || ''
const JUDGE_MODEL = args.judgeModel || 'fable'
const PREFIX = args.filePrefix || ({ 'hull-wwtf-om-2026': 'hull', 'santamonica-swip-om-2025': 'swip', 'ocwut-16-26': 'ocwut', 'fulton-county-2025': 'fulton', 'mmsd-om-2028': 'mmsd' }[slug] || slug.split('-')[0])
// Date.now()/new Date() are unavailable in workflow scripts (they break resume); make_gap_ranges.py stamps today.
const TODAY = cfg.today || 'unknown-date'

const BUILD = { type:'object', properties:{
  range:{type:'string'}, files_created:{type:'array', items:{type:'string'}},
  skipped:{type:'array', items:{type:'object', properties:{ page:{type:'number'}, para:{type:'number'}, reason:{type:'string'} }, required:['page','para','reason']}},
  facts_fragment:{type:'string'}, quotes_fragment:{type:'string'}, notes:{type:'string'} },
  required:['range','files_created','skipped','facts_fragment','quotes_fragment'] }
const JUDGE = { type:'object', properties:{ range:{type:'string'}, results:{type:'array', items:{type:'object', properties:{
  path:{type:'string'}, verdict:{type:'string', enum:['prose','paraphrase','missing-ref','recipe-ok','not-checked']}, reason:{type:'string'} }, required:['path','verdict']}} }, required:['range','results'] }
const REWRITE = { type:'object', properties:{ rewritten:{type:'array', items:{type:'string'}}, notes:{type:'string'} }, required:['rewritten'] }
const TEXT = { type:'object', properties:{ summary:{type:'string'}, files:{type:'array', items:{type:'string'}}, counts:{type:'object'} }, required:['summary','files'] }

const pagePath = (p) => `${W}\\verbatim\\${slug}\\pages\\p${String(p).padStart(4,'0')}.md`
const fragName = (r) => r.name.replace(/[^A-Za-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,60)

const buildPrompt = (r) => `You are ADDING content-bank blocks for paragraphs of a winning Jacobs proposal that no existing block covers. Work only from the verbatim page files; they are the source of truth.

Read first: ${W}\\CLAUDE.md (schema v2, sanitization rules) and ${W}\\templates\\content-block.md.
Source slug ${slug}; section "${r.name}" (section-id ${r.sectionId}); pages ${r.pages[0]}–${r.pages[1]}: ${Array.from({length:r.pages[1]-r.pages[0]+1},(_,i)=>pagePath(r.pages[0]+i)).join(' ; ')}
Target category folder: ${W}\\wiki\\${r.category}\\ . rfp-section-type: ${JSON.stringify(r.rfpSectionType)}. Pursuit context line for frontmatter: "${context}". Pursuit client names to generalize to [CLIENT] in narrative categories (NOT in past-performance/resumes): ${clientNames.join(', ')}.

Create blocks ONLY for these uncovered paragraphs (page ¶, word count, kind, opening words):
${r.uncovered.map(u => `- p${String(u.page).padStart(4,'0')} ¶${u.para} (${u.words} w, ${u.kind}): "${u.first_words}…"  [${u.ref}]`).join('\n')}

Existing blocks in this section — READ-ONLY context, open them only to avoid duplicating what they already say; never edit them: ${r.existingBlocks.length ? r.existingBlocks.join(' ; ') : '(none)'}

Rules:
1. One block per contiguous topical run of the listed paragraphs (150–900 words; a single listed paragraph may be its own block when it is a distinct topic). Include every listed paragraph that belongs to the run. Do not pull in paragraphs that are not listed, except the run's own heading line and an adjacent short lead-in sentence when the paragraph would otherwise start mid-thought.
2. The body IS the paragraphs' sentences, near-verbatim, sanitized only per CLAUDE.md (client names above → [CLIENT] with a generalized descriptor on first use, pursuit location and named facilities generalized in narrative categories). Keep every number, outcome, award, reference-client name and staff name; strip commercial fee/rate figures only. Never write "do not restate".
3. block-type: prose for narrative, table for tables (keep GFM), exhibit for caption-only, roster for team lists.
4. Frontmatter v2 (see template): title, category ${r.category}, tags from ${W}\\vocabulary\\tags.md ONLY, source ${slug}, source-section "${r.name}", source-pages, verbatim-ref (the primary paragraph, e.g. "verbatim/${slug}/pages/p${String(r.pages[0]).padStart(4,'0')}.md#¶${r.uncovered[0].para}"), pursuit-type, client-type, client-size, geography, rfp-section-type ${JSON.stringify(r.rfpSectionType)}, win-theme-map (from partner-transparency, compliance-leadership, regional-bench, odor-control, incumbent-displacement, asset-management, safety-culture, innovation-value-add, transition-continuity, workforce-development, energy-chemical-efficiency, collection-system, stormwater, community-engagement, digital-tools), proof-point-ids: [] (the registry step fills it), testimonial-ids: [], story-ids: [], status: preferred, house-favorite: false, sanitized: true, sanitization-loss (none|low|high), extracted: ${TODAY}, last-verified: ${TODAY}, context, quality, reuse-notes. Do NOT write section-id or section-order — a script sets them. Quote any frontmatter value that contains a colon.
5. Body: "# <title>", the prose, then "## Reuse guidance".
6. Filenames: ${W}\\wiki\\${r.category}\\${PREFIX}-<topic-slug>.md — check the path does not already exist; never overwrite any file.
7. Fragments: write ${W}\\work\\fragments\\${slug}\\gapfill-${fragName(r)}.facts.json = [{"claim","number","unit","as_of","page","para","block","category"}] for every quantified claim in the paragraphs you used, and ...gapfill-${fragName(r)}.quotes.json = [{"quote","speaker","title","org","page","para","block"}] for every client/third-party quotation (empty list if none).
8. You may skip a listed paragraph ONLY with a reason: exhibit-internal (figure labels / chart text), form-boilerplate, commercial (fee or rate content), duplicate-of:<existing block path> (its prose is already in that block), continuation-of:<path> (it belongs to that block's passage and adding it would split one thought — do not edit that block; just report). Every listed paragraph must be either in a new block or in skipped.
9. Do not read any other proposal's pages. Do not edit files outside wiki\\${r.category}\\ and work\\fragments\\.
${EXTRA}
Return: range, files_created (the NEW BLOCK paths only — never the fragment files, which go in facts_fragment / quotes_fragment), skipped (page, para, reason), the two fragment paths, notes.`

const judgePrompt = (r, files) => `You are the prose judge for the content bank. For each block listed, decide whether its body IS the sanitized prose of its verbatim source or merely a paraphrase/summary of it.
Blocks: ${files.join(' ; ')}
For each block: read its frontmatter verbatim-ref and source-pages, open the referenced verbatim page(s) under ${W}\\verbatim\\${slug}\\pages\\, and compare. Verdicts: prose (the body reproduces the source sentences near-verbatim with only [CLIENT]/location/facility generalization and commercial figures removed), paraphrase (rewritten, condensed, or instructional — fails), missing-ref (verbatim-ref does not resolve or points to the wrong passage), recipe-ok (block-type recipe with a valid pairs-with). Be strict: a block that keeps the ideas but not the sentences is a paraphrase. Read-only — do not edit files.`

const rewritePrompt = (r, fails) => `Rewrite these content-bank blocks so each body is the sanitized PROSE of its verbatim source, not a paraphrase. Read ${W}\\CLAUDE.md sanitization rules first. For each: open the block, open its verbatim-ref page(s) under ${W}\\verbatim\\${slug}\\pages\\ (fix verbatim-ref if it was wrong), replace the body with the source sentences (generalize pursuit client names ${clientNames.join(', ')} to [CLIENT] in narrative categories only; keep every number; strip commercial fee/rate figures only), keep the frontmatter v2 fields and the "## Reuse guidance" section. Blocks and judge reasons:\n${fails.map(f => `- ${f.path}: ${f.verdict} — ${f.reason||''}`).join('\n')}`

phase('Blocks')
const perRange = await pipeline(cfg.ranges,
  r => agent(buildPrompt(r), {model:'opus', effort:'medium', phase:'Blocks', label:`gapfill ${slug} ${r.name}`, schema:BUILD}),
  async (built, r) => {
    if (!built) return null
    let files = built.files_created || []
    let fails = []
    if (files.length) {
      let judged = await agent(judgePrompt(r, files), {model:JUDGE_MODEL, effort:'medium', phase:'Prose judge', label:`judge ${r.name}`, schema:JUDGE})
      fails = (judged?.results||[]).filter(x => x.verdict==='paraphrase' || x.verdict==='missing-ref')
      for (let round=0; round<2 && fails.length; round++) {
        await agent(rewritePrompt(r, fails), {model:'opus', effort:'medium', phase:'Prose judge', label:`rewrite ${r.name} r${round+1}`, schema:REWRITE})
        judged = await agent(judgePrompt(r, fails.map(f=>f.path)), {model:JUDGE_MODEL, effort:'medium', phase:'Prose judge', label:`rejudge ${r.name} r${round+1}`, schema:JUDGE})
        fails = (judged?.results||[]).filter(x => x.verdict==='paraphrase' || x.verdict==='missing-ref')
      }
    }
    return { range:r.name, created:files.length, skipped:(built.skipped||[]).length, skipped_reasons:built.skipped||[], residual_fails:fails, quotes_fragment:built.quotes_fragment }
  })
const done = perRange.filter(Boolean)
log(`Blocks: ${done.length}/${cfg.ranges.length} ranges; created ${done.reduce((n,d)=>n+d.created,0)}; skipped ${done.reduce((n,d)=>n+d.skipped,0)}; residual paraphrase failures: ${done.reduce((n,d)=>n+d.residual_fails.length,0)}`)

phase('Finalize')
const quoteFrags = done.map(d => d.quotes_fragment).filter(Boolean)
const fin = await agent(`Finalize the content bank after a gap-fill run for source ${slug}. Run these in order from ${W} and capture outputs:
1. python "${W}\\work\\find_uncovered.py" ${slug}   — report the residual uncovered count (it should not exceed the paragraphs the writers deliberately skipped: ${done.reduce((n,d)=>n+d.skipped,0)}).
2. python "${W}\\work\\assign_block_sections.py" --slug ${slug}   — sets section-id/section-order on the new blocks.
3. python "${W}\\work\\build_proof_point_registry.py"   then   python "${W}\\work\\patch_frontmatter.py" "${W}\\work\\fragments\\pp_patches.json"
4. python "${W}\\work\\regen_index.py"
5. python "${W}\\work\\lint_blocks.py" --json "${W}\\work\\lint_report.json"
Then read the lint report and fix ONLY mechanical violations on blocks whose path contains "/${PREFIX}-" and whose extracted date is ${TODAY} (unquoted colon in a frontmatter value, missing key with an obvious default such as testimonial-ids [] / story-ids [] / house-favorite false, tag not in vocabulary → replace with the closest canonical tag from ${W}\\vocabulary\\tags.md) using ${W}\\work\\patch_frontmatter.py; re-run steps 2, 4 and 5. Do not touch bodies or older blocks. Return summary, files, counts {residual_uncovered, blocks_assigned, lint_violations_before, lint_violations_after}.`, {model:'sonnet', effort:'low', phase:'Finalize', label:'finalize', schema:TEXT})
log(`Finalize: ${fin?.summary||'-'}`)

let testimonials = null
if (quoteFrags.length) {
  testimonials = await agent(`Append any NEW client/third-party quotes to the testimonials inventory. Read these fragments: ${quoteFrags.map(q => `${W}\\work\\fragments\\${slug}\\${q.split(/[\\/]/).pop()}`).join(' ; ')} (skip empty lists). For each quote not already in ${W}\\testimonials\\inventory.md (compare speaker + first 8 words), add a row continuing the TM- numbering with speaker, title, organization, verbatim quote, source slug/page/¶, permission: unknown, contact if present on the page, used-in (block path). Write ${W}\\work\\fragments\\tm_patches_gapfill.json and run python "${W}\\work\\patch_frontmatter.py" on it to set testimonial-ids on the new blocks. Return summary, files, counts {added, already_present}.`, {model:'opus', effort:'medium', phase:'Finalize', label:'testimonials', schema:TEXT})
  log(`Testimonials: ${testimonials?.summary||'-'}`)
}

return { slug, ranges: done, fin, testimonials }
