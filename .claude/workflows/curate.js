export const meta = {
  name: 'curate',
  description: 'Keep the content bank current: detect stale, contradicted and duplicate blocks (scripts, zero tokens), triage each into a proposed action with evidence (Sonnet), judge supersede/merge/archive proposals pairwise (Fable), and write the confirm-before-apply queue. Applies NOTHING — python work/apply_curation.py does, after the maintainer ticks.',
  phases: [
    { title: 'Detect', detail: 'freshness.py (volatility, review-due, flags, ranked list) + dedupe_candidates.py --skip-linked; one Sonnet runner transcribes the compact items file' },
    { title: 'Triage', detail: 'Sonnet, batches of 8: block + reuse-notes + registry rows + competing block + feedback → keep / verify / update-figure / supersede-with / merge-into / archive, each with evidence' },
    { title: 'Judge', detail: 'Fable reads both blocks and both verbatim pages for every supersede / merge / archive proposal; approves, reverses or rejects' },
    { title: 'Queue', detail: 'build_queue.py merges fragments + verdicts into work/curation/queue.md (ticks) and queue.json, ranked and grouped by owner' },
  ],
}

// args: { wiki, today (REQUIRED, YYYY-MM-DD — workflow scripts cannot call new Date(); the skill passes the session date),
//         scope: 'attention' (default: flagged or overdue) | 'flagged' | 'overdue' | 'source:<slug>' | 'paths',
//         paths: [repo-relative block paths, scope 'paths' only], maxItems (default 120), batchSize (default 8),
//         triageModel (default 'sonnet'), judgeModel (default 'fable'), runId (default = today) }
const W = args.wiki
if (!args.today) return { error: 'args.today (YYYY-MM-DD) is required: workflow scripts cannot read the clock, and resume replays prompts verbatim.' }
const TODAY = args.today
const RUN = args.runId || TODAY
const SCOPE = args.scope || 'attention'
const MAX = args.maxItems || 120
const BATCH = args.batchSize || 8
const TRIAGE_MODEL = args.triageModel || 'sonnet'
const JUDGE_MODEL = args.judgeModel || 'fable'
const FRAG = `${W}\\work\\fragments\\curation\\${RUN}`

const scopeFlags = () => {
  if (SCOPE === 'flagged') return '--only-flagged'
  if (SCOPE === 'overdue') return '--only-overdue'
  if (SCOPE.startsWith('source:')) return `--attention --source ${SCOPE.slice(7)}`
  if (SCOPE === 'paths') return `--paths "${(args.paths || []).join(',')}"`
  return '--attention'
}

const DETECT = { type:'object', properties:{
  report_md:{type:'string'}, items_file:{type:'string'},
  counts:{type:'object', properties:{ blocks:{type:'number'}, flagged:{type:'number'}, overdue:{type:'number'}, registry_conflicts:{type:'number'}, unlinked_pairs:{type:'number'}, selected:{type:'number'} }},
  items:{type:'array', items:{type:'object', properties:{
    rank:{type:'number'}, path:{type:'string'}, title:{type:'string'}, source:{type:'string'}, owner:{type:'string'},
    volatility:{type:'string'}, review_due:{type:'string'}, overdue_days:{type:'number'}, flags:{type:'array', items:{type:'string'}},
    details:{type:'array', items:{type:'string'}}, competitors:{type:'array', items:{type:'string'}} },
    required:['rank','path','volatility','flags']}} },
  required:['report_md','items_file','counts','items'] }

const TRIAGE = { type:'object', properties:{
  fragment:{type:'string'},
  proposals:{type:'array', items:{type:'object', properties:{
    path:{type:'string'}, action:{type:'string', enum:['keep','verify','update-figure','supersede-with','merge-into','archive']},
    target:{type:'string'}, confidence:{type:'string', enum:['high','medium','low']} }, required:['path','action']}},
  counts:{type:'object'} }, required:['fragment','proposals'] }

const JUDGE = { type:'object', properties:{
  fragment:{type:'string'},
  decisions:{type:'array', items:{type:'object', properties:{
    path:{type:'string'}, target:{type:'string'}, action_proposed:{type:'string'},
    verdict:{type:'string', enum:['approve','reverse','reject','distinct','archive-path','archive-target']},
    reason:{type:'string'} }, required:['path','action_proposed','verdict','reason']}} }, required:['fragment','decisions'] }

const TEXT = { type:'object', properties:{ summary:{type:'string'}, files:{type:'array', items:{type:'string'}}, counts:{type:'object'} }, required:['summary','files'] }

// ---------------------------------------------------------------------------------------
phase('Detect')
const det = await agent(`Run the freshness detectors for the Jacobs content bank and hand back the compact item list. Do not modify any wiki/ file.
From ${W} run, in order, capturing output:
1. python "${W}\\work\\freshness.py" --today ${TODAY} ${scopeFlags()} --limit ${MAX} --items-out "${FRAG}\\items.json" --md "${W}\\work\\curation\\report.md" --json "${W}\\work\\curation\\report.json"
   (it prints counts; --items-out writes the selected, ranked items with their flag details and competitor paths; create the folder ${FRAG} if the script did not)
2. python "${W}\\work\\dedupe_candidates.py" --min 0.12 --skip-linked --exclude-archived --decided "${W}\\work\\curation\\log.jsonl" --out "${FRAG}\\pairs.json"
Then open ${FRAG}\\items.json and return its entries UNCHANGED as items (every field, in file order — do not summarize, drop or reorder), plus report_md, items_file, and counts {blocks, flagged, overdue, registry_conflicts, unlinked_pairs, selected} from the printed output.`,
  {model:'sonnet', effort:'low', phase:'Detect', label:'detect', schema:DETECT})
const items = det?.items || []
log(`Detect: ${det?.counts?.selected ?? items.length} items selected of ${det?.counts?.blocks ?? '?'} blocks (flagged ${det?.counts?.flagged ?? '?'}, overdue ${det?.counts?.overdue ?? '?'}, registry conflicts ${det?.counts?.registry_conflicts ?? '?'}, unlinked pairs ${det?.counts?.unlinked_pairs ?? '?'})`)
if (!items.length) return { run: RUN, scope: SCOPE, counts: det?.counts, note: 'nothing to triage' }

// ---------------------------------------------------------------------------------------
phase('Triage')
const batches = []
for (let i = 0; i < items.length; i += BATCH) batches.push(items.slice(i, i + BATCH))
const heavy = (b) => b.some(it => it.volatility === 'corporate-figure' || (it.flags||[]).includes('feedback') || (it.flags||[]).includes('newer-source-same-claim'))

const triagePrompt = (b, i) => `You are triaging content-bank blocks that the freshness detectors flagged, for the maintainer's confirm-before-apply queue. Read ${W}\\CLAUDE.md section "Keeping the bank current" first. You are READ-ONLY on wiki/, verbatim/, proof-points/ — you write exactly one fragment file.

Today ${TODAY}. Items (rank · path · volatility · review-due · overdue days · flags · detector details · competing blocks):
${b.map(it => `- #${it.rank} ${it.path} · ${it.volatility} · due ${it.review_due||'—'} · overdue ${it.overdue_days||0} d · flags [${(it.flags||[]).join(', ')}]${(it.details||[]).length ? '\n    details: ' + it.details.join(' | ') : ''}${(it.competitors||[]).length ? '\n    competitors: ' + it.competitors.join(' ; ') : ''}`).join('\n')}

For EACH item: open the block (frontmatter, reuse-notes, body); open every registry row it cites that the details name (grep "${W}\\proof-points\\registry.md" for the PP id — each row lists value, as-of, source, page/¶, block); open each competing block named above or in the details; read any matching lines in ${W}\\work\\curation\\feedback.jsonl; check ${W}\\work\\curation\\sources.json for each source's proposal date. Then decide ONE action:
- keep — the facts are evergreen or the flag is a false positive; say why in one sentence.
- verify — the facts are time-bound (people, contacts, corporate figures, safety stats, legislation) and nothing in the bank contradicts them; the maintainer confirms them with the account team, then runs curate.py verify. Name exactly which facts to confirm.
- update-figure — the registry holds a NEWER value for the same claim from a later-dated source (quote both values, both sources, both dates, the PP id) and the block's figure should change to it. proposed_value = the newer figure with unit. ALSO for the newer-year-available flag (year-series stats: TRIR, EMR, DART, training hours): the bank must carry the latest year any source states — propose appending the newer year's row(s) from the block the detail names and updating any "current"/headline figure in the prose to that year's value; proposed_value names the year, value and source block.
- supersede-with — another live block covers the same topic better (more complete / more quantified / newer / better prose); target = that block's path. Say what the target has that this one lacks.
- merge-into — this block is a strict subset of target; target = the fuller block.
- archive — ONLY when (a) a preferred twin exists and this block adds nothing (name it as target), or (b) the block is a placeholder / exclusion record / recipe whose prose block already exists, or (c) its facts are known-false or retired and nothing should ever cite them again. Never archive a resume or a reference block for being old — those are verify.
Status-link contradictions (preferred with superseded-by, fallback without a winner, fallback + house-favorite) are decisions: propose the resolution as supersede-with / keep (with a note to delete the stray field) / archive and explain.
Every item needs evidence: 1–4 entries, each {kind: registry|block|verbatim|feedback|reuse-notes|dedupe, ref: an exact path / PP id / verbatim page ref that exists, text: the quoted line}. confidence high only when the evidence is explicit (two registry values, a named twin). Write the fragment ${FRAG}\\triage_${String(i+1).padStart(2,'0')}.json as {"items":[{"path","action","target","proposed_value","evidence":[...],"confidence","rationale","flags":[...],"owner","volatility","rank"}]} (one entry per item, all fields present, empty string / list when not applicable). Return fragment, proposals (path, action, target, confidence for every item) and counts by action.`

const triaged = (await parallel(batches.map((b, i) => () => agent(triagePrompt(b, i),
  {model:TRIAGE_MODEL, effort: heavy(b) ? 'medium' : 'low', phase:'Triage', label:`triage ${i+1}/${batches.length}`, schema:TRIAGE})))).filter(Boolean)
const proposals = triaged.flatMap(t => t.proposals || [])
const byAction = proposals.reduce((m, p) => (m[p.action] = (m[p.action]||0) + 1, m), {})
log(`Triage: ${triaged.length}/${batches.length} batches; ${proposals.length} proposals — ${Object.entries(byAction).map(([k,v]) => `${k} ${v}`).join(', ')}`)

// ---------------------------------------------------------------------------------------
phase('Judge')
const toJudge = proposals.filter(p => ['supersede-with','merge-into','archive'].includes(p.action))
const jBatches = []
for (let i = 0; i < toJudge.length; i += 10) jBatches.push(toJudge.slice(i, i + 10))
const judgePrompt = (b, i) => `You are the Fable judge for supersession in the Jacobs content bank. Read ${W}\\CLAUDE.md sections "Content block format" and "Keeping the bank current". READ-ONLY on wiki/ and verbatim/; you write one fragment file.
Proposals (path → action → target):
${b.map(p => `- ${p.path} → ${p.action} → ${p.target || '(none)'}`).join('\n')}
For each: open BOTH blocks fully (frontmatter + body + reuse guidance) and the verbatim page behind each one's first verbatim-ref (${W}\\verbatim\\<source>\\pages\\pNNNN.md). Decide:
- approve — the proposal is right: the target is the block writers should reach for (more complete, more quantified, newer source where the facts are time-bound, better prose) and the path block should become fallback (supersede-with / merge-into) or archived (archive, only under the CLAUDE.md archive conditions).
- reverse — same topic, but the PATH block is the better one; the target should be the fallback.
- distinct — different topics or complementary angles; both stay preferred (the triage was wrong to pair them).
- reject — the proposal is unsafe or unsupported (e.g. archive of a block that is the only home of a fact, or of a resume / reference); say what to do instead.
- archive-path / archive-target — one side is a placeholder, exclusion record, or duplicate recipe that should be archived outright (name which).
Prefer the block from the newer-dated source (${W}\\work\\curation\\sources.json) when the two carry the same time-bound facts with different values; prefer the more quantified block when they are evergreen. Never approve an archive of a block cited in ${W}\\templates\\standard-topics.md. Write ${FRAG}\\judge_${String(i+1).padStart(2,'0')}.json as {"decisions":[{"path","target","action_proposed","verdict","reason"}]} and return fragment + decisions.`
const judged = jBatches.length ? (await parallel(jBatches.map((b, i) => () => agent(judgePrompt(b, i),
  {model:JUDGE_MODEL, effort:'medium', phase:'Judge', label:`judge ${i+1}/${jBatches.length}`, schema:JUDGE})))).filter(Boolean) : []
const verdicts = judged.flatMap(j => j.decisions || [])
const byVerdict = verdicts.reduce((m, d) => (m[d.verdict] = (m[d.verdict]||0) + 1, m), {})
log(`Judge: ${toJudge.length} proposals judged — ${Object.entries(byVerdict).map(([k,v]) => `${k} ${v}`).join(', ') || 'none'}`)

// ---------------------------------------------------------------------------------------
phase('Queue')
const q = await agent(`Build the curation queue from this run's fragments. From ${W} run:
python "${W}\\work\\build_queue.py" --run "${RUN}" --today ${TODAY} --fragments "${FRAG}"
It merges triage_*.json with judge_*.json (verdicts override proposals), assigns CQ-nnnn ids, checks that every evidence ref resolves (paths exist, PP ids are in the registry, verbatim refs resolve), ranks and groups by owner, and writes ${W}\\work\\curation\\queue.json and queue.md. Do not edit the fragments or any wiki/ file. Return summary (counts by action, how many evidence refs failed to resolve and were marked), files, counts.`,
  {model:'sonnet', effort:'low', phase:'Queue', label:'build queue', schema:TEXT})
log(`Queue: ${q?.summary || '-'}`)

return { run: RUN, scope: SCOPE, today: TODAY, detect: det?.counts, proposals: byAction, verdicts: byVerdict,
         queue: q?.summary, files: q?.files, next: 'Review work/curation/queue.md, tick the items to apply, then: python work/apply_curation.py --dry-run && python work/apply_curation.py' }
