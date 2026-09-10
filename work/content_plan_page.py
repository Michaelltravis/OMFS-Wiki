#!/usr/bin/env python3
"""
content_plan_page.py — turn pursuits/<slug>/content-plan.md into an interactive
checklist page (HTML) for publishing as an Artifact with the `db` capability.

    python work/content_plan_page.py <slug> [--out <path.html>]

The page embeds the plan as JSON, lets the proposal manager tick topics, set a
mark (include / lead / brief), add notes and additional topics, and saves the
selection to db document plans/<slug>. apply_content_plan.py writes the saved
selection back into content-plan.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_HEADINGS = {"how to use this sheet", "evaluation weights", "rfp cross-check"}


def parse_plan(md: str) -> dict:
    lines = md.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "Content plan")
    fm = {}
    if lines and lines[0].strip() == "---":
        for l in lines[1:20]:
            if l.strip() == "---":
                break
            if ":" in l:
                k, v = l.split(":", 1)
                fm[k.strip()] = v.strip()
    weights = []
    sections = []
    cur = None
    mode = None
    for l in lines:
        if l.startswith("## "):
            h = l[3:].strip()
            mode = h.lower()
            if mode in SKIP_HEADINGS:
                cur = None
                continue
            cur = {"id": re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-"), "heading": h, "rows": [], "note": ""}
            sections.append(cur)
            continue
        if mode == "evaluation weights" and l.startswith("|"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 2 and c[0] not in ("Section", "Total") and not set(c[0]) <= {"-", ":"}:
                weights.append({"section": c[0], "weight": c[1]})
            continue
        if cur is None:
            continue
        if l.startswith("|"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) < 5 or c[0] == "#" or set(c[0]) <= {"-", ":"}:
                continue
            num, topic, source, mark, note = c[:5]
            if num == "" and topic.startswith("**"):
                cur["rows"].append({"kind": "group", "topic": topic.strip("*")})
            elif num == "—":
                continue  # blank additional-topic rows are supplied by the page
            else:
                required = source.startswith("RFP")
                cur["rows"].append({
                    "kind": "required" if required else "standard",
                    "n": num, "topic": topic, "source": source,
                    "mark": mark, "note": "" if note == "required" else note,
                })
        elif l.strip() and not l.startswith("#"):
            cur["note"] = (cur["note"] + " " + l.strip()).strip()
    return {"slug": fm.get("pursuit", ""), "title": title, "generated": fm.get("generated", ""), "weights": weights, "sections": sections}


TEMPLATE = r"""<title>__TITLE__</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@500&display=swap">
<style>
:root{
  --bg:#f5f6fa; --panel:#ffffff; --ink:#151a2d; --ink-2:#4b5170; --ink-3:#8a90ad; --line:#d9dcea; --line-2:#eceef5;
  --accent:#231edc; --accent-ink:#ffffff; --accent-soft:#e9e8fc; --navy:#001e55; --ok:#1a7f4b; --ok-soft:#e3f3ea; --warn:#a15c00; --warn-soft:#fff1dc;
  --req:#eef0f7;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#0f1220; --panel:#171b2e; --ink:#e8eaf4; --ink-2:#b3b8d0; --ink-3:#7d84a6; --line:#2b3050; --line-2:#222741;
  --accent:#7d7bff; --accent-ink:#0f1220; --accent-soft:#25275a; --navy:#c9d6ff; --ok:#5dcf8f; --ok-soft:#153426; --warn:#f0b35e; --warn-soft:#3a2a10;
  --req:#1d2238;
}}
:root[data-theme="dark"]{
  --bg:#0f1220; --panel:#171b2e; --ink:#e8eaf4; --ink-2:#b3b8d0; --ink-3:#7d84a6; --line:#2b3050; --line-2:#222741;
  --accent:#7d7bff; --accent-ink:#0f1220; --accent-soft:#25275a; --navy:#c9d6ff; --ok:#5dcf8f; --ok-soft:#153426; --warn:#f0b35e; --warn-soft:#3a2a10;
  --req:#1d2238;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 "Source Sans 3",system-ui,Segoe UI,Arial,sans-serif}
a{color:var(--accent)}
.shell{display:grid;grid-template-columns:240px minmax(0,1fr);min-height:100vh}
nav{position:sticky;top:0;height:100vh;overflow:auto;padding:28px 18px;border-right:1px solid var(--line);background:var(--panel)}
nav .brand{font-weight:700;color:var(--navy);letter-spacing:.06em;text-transform:uppercase;font-size:12px}
nav h1{font-size:17px;line-height:1.25;margin:8px 0 18px;text-wrap:balance}
nav ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px}
nav li a{display:flex;justify-content:space-between;gap:8px;padding:7px 9px;border-radius:6px;color:var(--ink-2);text-decoration:none;font-size:14px}
nav li a:hover{background:var(--accent-soft);color:var(--ink)}
nav li a .cnt{font-family:"JetBrains Mono",Consolas,monospace;font-size:11.5px;color:var(--ink-3);font-variant-numeric:tabular-nums}
nav .meta{margin-top:22px;padding-top:14px;border-top:1px solid var(--line);font-size:12.5px;color:var(--ink-3);line-height:1.5}
main{padding:32px 40px 120px;max-width:1180px}
.intro{max-width:70ch;color:var(--ink-2);margin:0 0 6px}
.legend{display:flex;flex-wrap:wrap;gap:10px 18px;font-size:13px;color:var(--ink-2);margin:12px 0 30px}
.legend b{color:var(--ink)}
section.sec{margin:0 0 42px}
section.sec h2{font-size:21px;margin:0 0 4px;color:var(--navy);text-wrap:balance;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
section.sec h2 .w{font-size:13px;font-weight:600;color:var(--accent);background:var(--accent-soft);padding:2px 8px;border-radius:4px;letter-spacing:.02em}
section.sec .sub{color:var(--ink-3);font-size:13px;margin:0 0 12px}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--panel)}
table{width:100%;border-collapse:collapse;min-width:760px}
th{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);font-weight:600}
td{padding:8px 12px;border-bottom:1px solid var(--line-2);vertical-align:top}
tr:last-child td{border-bottom:0}
td.n{font-family:"JetBrains Mono",Consolas,monospace;font-size:12px;color:var(--ink-3);font-variant-numeric:tabular-nums;width:44px;padding-top:11px}
td.t{min-width:230px}
td.t .src{display:block;font-size:12.5px;color:var(--ink-3);margin-top:2px;word-break:break-word}
tr.group td{background:var(--line-2);color:var(--ink-2);font-size:12.5px;letter-spacing:.05em;text-transform:uppercase;font-weight:600;padding:7px 12px}
tr.required td{background:var(--req)}
tr.required td.t .src{color:var(--ink-2)}
.pill{display:inline-block;font-size:11.5px;font-weight:600;padding:2px 8px;border-radius:999px;background:var(--ok-soft);color:var(--ok);white-space:nowrap}
td.c{width:150px;white-space:nowrap}
td.c label{display:inline-flex;align-items:center;gap:8px;cursor:pointer;font-weight:600}
input[type=checkbox]{width:17px;height:17px;accent-color:var(--accent);cursor:pointer}
select,input[type=text]{font:inherit;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:6px 8px}
select{margin-left:8px}
select:disabled{opacity:.45}
input[type=text]{width:100%;min-width:220px}
input:focus-visible,select:focus-visible,button:focus-visible,input[type=checkbox]:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
tr.off td.t,tr.off td.n{color:var(--ink-3)}
tr.on td.t{font-weight:600}
.addrow td{background:var(--panel)}
.add{margin:10px 0 0;display:flex;gap:10px;align-items:center}
button{font:inherit;font-weight:600;border:1px solid var(--line);background:var(--panel);color:var(--ink);padding:7px 13px;border-radius:6px;cursor:pointer}
button.ghost{border-style:dashed;color:var(--ink-2)}
button.ghost:hover{border-color:var(--accent);color:var(--accent)}
button.x{border:0;background:transparent;color:var(--ink-3);padding:4px 6px}
button.x:hover{color:var(--warn)}
.note{color:var(--ink-2);padding:14px 16px;border:1px dashed var(--line);border-radius:8px;background:var(--panel)}
.bar{position:fixed;left:240px;right:0;bottom:0;display:flex;align-items:center;gap:16px;padding:12px 40px;background:var(--panel);border-top:1px solid var(--line);z-index:5}
.bar .sum{color:var(--ink-2);font-size:14px;font-variant-numeric:tabular-nums}
.bar .sum b{color:var(--ink)}
.bar .st{margin-left:auto;font-size:13.5px;color:var(--ink-3)}
.bar .st.ok{color:var(--ok)} .bar .st.warn{color:var(--warn)}
button.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
button.primary:disabled{opacity:.5;cursor:default}
@media (max-width:860px){.shell{grid-template-columns:1fr}nav{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line)}.bar{left:0;padding:12px 16px}main{padding:20px 16px 120px}}
@media (prefers-reduced-motion:no-preference){tr{transition:background .15s}}
</style>
<div class="shell">
<nav>
  <div class="brand">Jacobs · content plan</div>
  <h1 id="ttl"></h1>
  <ol id="toc"></ol>
  <div class="meta" id="meta"></div>
</nav>
<main>
  <p class="intro">Tick the topics each section should cover. Required rows come from the RFP and stay in. Everything else is the proposal manager's call — tick it, give it a mark, and add an angle if the writer needs one.</p>
  <div class="legend"><span><b>Include</b> — drafted</span><span><b>Lead</b> — carries the section's opener or closer</span><span><b>Brief</b> — one paragraph or a table row at most</span><span><b>Unticked</b> — left out</span></div>
  <div id="sections"></div>
</main>
</div>
<div class="bar">
  <div class="sum" id="sum"></div>
  <button class="primary" id="save" disabled>Save selections</button>
  <span class="st" id="st">Loading…</span>
</div>
<script id="plan" type="application/json">__PLAN_JSON__</script>
<script>
const PLAN = JSON.parse(document.getElementById('plan').textContent);
const state = { sections: {} }; // {secId: {rows:{n:{on,mark,note}}, additional:[{topic,note,mark}]}}
let db = null, dirty = false, loaded = false;
const $ = (s, r=document) => r.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

function secState(id){ return state.sections[id] ||= { rows:{}, additional:[] }; }
function rowState(id, n){ const s = secState(id); return s.rows[n] ||= { on:false, mark:'include', note:'' }; }
function markFromMd(m){ const t=(m||'').toLowerCase(); return { on:t.includes('☑'), mark:t.includes('lead')?'lead':t.includes('brief')?'brief':'include' }; }

function seedFromPlan(){
  for(const sec of PLAN.sections){
    for(const r of sec.rows){
      if(r.kind==='group') continue;
      const rs = rowState(sec.id, r.n);
      const m = markFromMd(r.mark);
      rs.on = r.kind==='required' ? true : m.on; rs.mark = m.mark; rs.note = r.note || '';
    }
  }
}

function render(){
  $('#ttl').textContent = PLAN.title.replace(/^Content plan\s*[—-]\s*/,'');
  document.title = $('#ttl').textContent + ' — content plan';
  $('#meta').innerHTML = (PLAN.generated?`Generated ${esc(PLAN.generated)}<br>`:'') + `Pursuit <code>${esc(PLAN.slug)}</code>`;
  const wl = Object.fromEntries(PLAN.weights.map(w=>[w.section.toLowerCase(), w.weight]));
  const toc = $('#toc'), host = $('#sections');
  toc.innerHTML=''; host.innerHTML='';
  for(const sec of PLAN.sections){
    const li = document.createElement('li');
    li.innerHTML = `<a href="#${sec.id}"><span>${esc(sec.heading.replace(/\s*\(.*\)$/,''))}</span><span class="cnt" data-cnt="${sec.id}"></span></a>`;
    toc.appendChild(li);
    const s = document.createElement('section'); s.className='sec'; s.id=sec.id;
    const m = sec.heading.match(/^(.*?)\s*\((.*)\)\s*$/);
    const head = m ? m[1] : sec.heading, meta = m ? m[2] : '';
    let html = `<h2>${esc(head)}${meta?`<span class="w">${esc(meta)}</span>`:''}</h2>`;
    if(!sec.rows.length){ html += `<div class="note">${esc(sec.note||'No topics on this sheet.')}</div>`; s.innerHTML = html; host.appendChild(s); continue; }
    const req = sec.rows.filter(r=>r.kind==='required').length, std = sec.rows.filter(r=>r.kind==='standard').length;
    html += `<p class="sub">${req} required by the RFP · ${std} Jacobs-standard to decide</p>`;
    html += `<div class="tbl"><table><thead><tr><th>#</th><th>Topic</th><th>Include?</th><th>Notes / angle for the writer</th><th></th></tr></thead><tbody data-sec="${sec.id}">`;
    for(const r of sec.rows){
      if(r.kind==='group'){ html += `<tr class="group"><td colspan="5">${esc(r.topic)} · Jacobs standard</td></tr>`; continue; }
      const rs = rowState(sec.id, r.n);
      const src = r.kind==='required' ? r.source.replace(/^RFP\s*—\s*/,'') : r.source.split(';').map(x=>x.trim()).join(' · ');
      html += `<tr class="${r.kind} ${rs.on?'on':'off'}" data-n="${r.n}">
        <td class="n">${esc(r.n)}</td>
        <td class="t">${esc(r.topic)}<span class="src">${esc(src)}</span></td>
        <td class="c">${r.kind==='required' ? `<span class="pill">Required</span>` :
          `<label><input type="checkbox" data-k="on" ${rs.on?'checked':''}> Include</label><select data-k="mark" ${rs.on?'':'disabled'}><option value="include" ${rs.mark==='include'?'selected':''}>include</option><option value="lead" ${rs.mark==='lead'?'selected':''}>lead</option><option value="brief" ${rs.mark==='brief'?'selected':''}>brief</option></select>`}</td>
        <td><input type="text" data-k="note" value="${esc(rs.note)}" placeholder="${r.kind==='required'?'Angle (optional)':'Why, or the angle to take'}"></td>
        <td></td></tr>`;
    }
    html += `</tbody><tbody class="addrows" data-sec="${sec.id}"></tbody></table></div>
      <div class="add"><button class="ghost" data-add="${sec.id}">+ Add a topic specific to this pursuit</button></div>`;
    s.innerHTML = html; host.appendChild(s);
    renderAdditional(sec.id);
  }
  refreshCounts();
}

function renderAdditional(id){
  const tb = document.querySelector(`tbody.addrows[data-sec="${id}"]`); if(!tb) return;
  const list = secState(id).additional;
  tb.innerHTML = list.map((a,i)=>`<tr class="addrow" data-i="${i}">
    <td class="n">+</td>
    <td class="t"><input type="text" data-a="topic" value="${esc(a.topic)}" placeholder="Topic"></td>
    <td class="c"><select data-a="mark"><option value="include" ${a.mark==='include'?'selected':''}>include</option><option value="lead" ${a.mark==='lead'?'selected':''}>lead</option><option value="brief" ${a.mark==='brief'?'selected':''}>brief</option></select></td>
    <td><input type="text" data-a="note" value="${esc(a.note)}" placeholder="Why, source, or the block / verbatim page to use"></td>
    <td><button class="x" data-del="${i}" title="Remove">✕</button></td></tr>`).join('');
}

function refreshCounts(){
  let on=0, total=0, extra=0;
  for(const sec of PLAN.sections){
    const st = secState(sec.id);
    const rows = sec.rows.filter(r=>r.kind!=='group');
    const picked = rows.filter(r=>rowState(sec.id,r.n).on).length + st.additional.length;
    const el = document.querySelector(`[data-cnt="${sec.id}"]`); if(el) el.textContent = rows.length ? `${picked}/${rows.length+st.additional.length}` : '';
    on += picked; total += rows.length + st.additional.length; extra += st.additional.length;
  }
  $('#sum').innerHTML = `<b>${on}</b> of ${total} topics selected${extra?` · ${extra} added for this pursuit`:''}`;
}

function setDirty(){ dirty = true; $('#save').disabled = !db; $('#st').textContent = 'Unsaved changes'; $('#st').className='st warn'; }

document.addEventListener('input', e => {
  const t = e.target, tr = t.closest('tr'), tb = t.closest('tbody'); if(!tr||!tb) return;
  const id = tb.dataset.sec;
  if(tr.classList.contains('addrow')){ secState(id).additional[+tr.dataset.i][t.dataset.a] = t.value; setDirty(); refreshCounts(); return; }
  const rs = rowState(id, tr.dataset.n);
  if(t.dataset.k==='on'){ rs.on = t.checked; tr.classList.toggle('on', rs.on); tr.classList.toggle('off', !rs.on); tr.querySelector('select').disabled = !rs.on; }
  else if(t.dataset.k==='mark'){ rs.mark = t.value; }
  else if(t.dataset.k==='note'){ rs.note = t.value; }
  setDirty(); refreshCounts();
});
document.addEventListener('click', e => {
  const add = e.target.closest('[data-add]'); if(add){ secState(add.dataset.add).additional.push({topic:'',mark:'include',note:''}); renderAdditional(add.dataset.add); setDirty(); refreshCounts(); const last=document.querySelector(`tbody.addrows[data-sec="${add.dataset.add}"] tr:last-child input`); last&&last.focus(); return; }
  const del = e.target.closest('[data-del]'); if(del){ const id = del.closest('tbody').dataset.sec; secState(id).additional.splice(+del.dataset.del,1); renderAdditional(id); setDirty(); refreshCounts(); }
});

async function save(){
  if(!db) return;
  const btn = $('#save'); btn.disabled = true; $('#st').textContent='Saving…'; $('#st').className='st';
  try{
    await db.doc('plans/'+PLAN.slug).set({ slug: PLAN.slug, updatedAt: new Date().toISOString(), sections: state.sections });
    dirty = false; $('#st').textContent = 'Saved ' + new Date().toLocaleTimeString(); $('#st').className='st ok';
  }catch(err){ $('#st').textContent = 'Could not save (' + (err && err.code || 'error') + ') — try again'; $('#st').className='st warn'; btn.disabled=false; }
}
$('#save').addEventListener('click', save);
window.addEventListener('beforeunload', e => { if(dirty){ e.preventDefault(); e.returnValue=''; } });

seedFromPlan(); render();
(async () => {
  db = await claude.use('db');
  if(!db){ $('#st').textContent = 'Saving is not available in this view — selections stay on this screen only.'; $('#st').className='st warn'; return; }
  try{
    const snap = await db.doc('plans/'+PLAN.slug).get();
    if(snap.exists){
      const d = snap.data();
      for(const [id, s] of Object.entries(d.sections||{})){ const t = secState(id); Object.assign(t.rows, s.rows||{}); t.additional = (s.additional||[]).map(a=>({topic:a.topic||'',mark:a.mark||'include',note:a.note||''})); }
      for(const sec of PLAN.sections) for(const r of sec.rows) if(r.kind==='required') rowState(sec.id,r.n).on = true;
      render();
      $('#st').textContent = 'Loaded selections saved ' + new Date(d.updatedAt).toLocaleString(); $('#st').className='st ok';
    } else { $('#st').textContent = 'No selections saved yet'; $('#st').className='st'; }
  }catch(err){ $('#st').textContent = 'Could not load saved selections — starting from the sheet'; $('#st').className='st warn'; }
  loaded = true; $('#save').disabled = false;
})();
</script>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    src = ROOT / "pursuits" / a.slug / "content-plan.md"
    if not src.exists():
        sys.exit(f"{src} not found — run work/new_content_plan.py first")
    plan = parse_plan(src.read_text(encoding="utf-8"))
    plan["slug"] = plan["slug"] or a.slug
    out = a.out or (ROOT / "pursuits" / a.slug / "content-plan-page.html")
    html = TEMPLATE.replace("__TITLE__", plan["title"].replace("Content plan — ", "") + " — content plan") \
                   .replace("__PLAN_JSON__", json.dumps(plan, ensure_ascii=False).replace("</", "<\\/"))
    out.write_text(html, encoding="utf-8")
    n = sum(len([r for r in s["rows"] if r["kind"] != "group"]) for s in plan["sections"])
    print(f"Wrote {out}: {len(plan['sections'])} sections, {n} topics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
