#!/usr/bin/env python3
"""assemble_section.py — pull one section of a source proposal, in reading order.

Usage:
    python work/assemble_section.py <slug> "<section query or section-id>"
        [--mode verbatim|blocks] [--to-page N] [--pages A-B] [--raw] [--anchors]
        [--no-recovered] [--include-fallback] [--docx] [--out PATH] [--pick N] [--list]

<slug> may be a full source slug (hull-wwtf-om-2026) or a unique prefix (hull, mmsd,
ocwut, fulton, santamonica).

verbatim mode (default): the section's paragraphs from verbatim/<slug>/pages/, in PDF
order, with running headers/footers dropped, exhibit picture-text dropped (asset ids
kept as [graphic: id]), recovered-text tails moved to the end of their page, headings
re-levelled, and client / location / facility names generalized per
verbatim/<slug>/sanitize.json (--raw disables).
blocks mode: the wiki blocks whose section-id is in the section's subtree, in
section-order, with a coverage trailer.

Exit codes: 0 ok · 2 ambiguous query (candidates printed; rerun with --pick N) · 3 not found.
Default output: work/pulls/<slug>/<section-slug>[.blocks].md (+ .docx with --docx).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verbatim_sections import (  # noqa: E402
    ROOT, VERBATIM, GRAPHIC_ID_RE, CAPTION_RE, DASHES, Sanitizer, is_substantive,
    load_pages, load_sanitize, load_sections, norm_repeat, plain_text, resolve_query,
    subtree_ids, HEADING_LINE_RE,
)

ACRONYMS = {
    "o&m", "scada", "cmms", "ot", "pm", "cm", "pdm", "cip", "i/i", "cctv", "ams", "iso", "samp",
    "amp", "amps", "ai", "kpi", "kpis", "wrf", "wrfs", "wwtp", "wwtps", "wwtf", "hr", "it",
    "qa/qc", "uv", "mbr", "daf", "ras", "was", "sop", "sops", "plc", "hmi", "erp", "emr",
    "osha", "epa", "wpdes", "npdes", "cso", "sso", "fog", "gis", "mopo", "arm", "jcec", "pe",
    "wef", "awtf", "grrp", "cip", "m&r", "r&r", "ebpr", "wats", "ot/scada", "hvac", "rng",
    "swip", "mmsd", "ocwut", "jiwrf", "sswrf", "wdnr", "odeq", "massdep", "usa", "us",
}
SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or",
         "the", "to", "vs", "via", "with", "from", "into", "over", "per"}


def smart_title(s: str) -> str:
    """Title-case an ALL-CAPS heading without mangling acronyms; leave mixed case alone."""
    letters = re.sub(r"[^A-Za-z]", "", s)
    if not letters or not letters.isupper():
        return s
    out = []
    for i, w in enumerate(s.split()):
        core = w.strip("():,;.’'\"")
        lw = core.lower()
        if lw in ACRONYMS or re.fullmatch(r"[A-Z0-9&/.-]{1,5}", core) and "&" in core:
            out.append(w)
            continue
        if "/" in w:
            out.append("/".join(smart_title(p) if p.isupper() else p for p in w.split("/")))
            continue
        if lw in SMALL and i != 0:
            out.append(w.lower())
        else:
            out.append(w[:1].upper() + w[1:].lower())
    return " ".join(out)


def resolve_slug(arg: str) -> str:
    if (VERBATIM / arg).is_dir():
        return arg
    cands = sorted(p.name for p in VERBATIM.iterdir() if p.is_dir() and p.name.startswith(arg.lower()))
    if len(cands) == 1:
        return cands[0]
    if not cands:
        cands = sorted(p.name for p in VERBATIM.iterdir() if p.is_dir() and arg.lower() in p.name)
        if len(cands) == 1:
            return cands[0]
    print(f"unknown source '{arg}'; candidates: {', '.join(cands) or 'none'}", file=sys.stderr)
    sys.exit(3)


def exhibit_titles(slug: str) -> dict[str, str]:
    """asset id -> exhibit/title from wiki/graphics/<slug>.md summary table."""
    out: dict[str, str] = {}
    cat = ROOT / "wiki" / "graphics" / f"{slug}.md"
    if not cat.is_file():
        return out
    for line in cat.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        ids = re.findall(r"`([^`]+)`", cells[0])
        for gid in ids:
            gid = gid.replace("\\_", "_")
            if GRAPHIC_ID_RE.fullmatch(gid) and gid not in out:
                out[gid] = cells[1]
    return out


def clean_line(s: str) -> str:
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"</?(sup|sub|mark|u|span|div)[^>]*>", "", s)
    s = s.replace("~~", "")
    for d in "‑‐":
        s = s.replace(d, "-")
    s = re.sub(r"^\s*(?:µ|•|▪|■|❖|➢||▪)\s*", "- ", s)
    s = re.sub(r"(\*\*|_)\s+([.,;:])", r"\1\2", s)   # "**bold** ." -> "**bold**."
    return re.sub(r"[ \t]+", " ", s).rstrip()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("query", nargs="?", default=None)
    ap.add_argument("--mode", choices=["verbatim", "blocks"], default="verbatim")
    ap.add_argument("--to-page", type=int, default=None)
    ap.add_argument("--pages", default=None, help="A-B: pull an explicit page range instead of a section")
    ap.add_argument("--raw", action="store_true", help="no sanitization")
    ap.add_argument("--anchors", action="store_true", help="keep <!-- pNNNN ¶n --> anchors")
    ap.add_argument("--no-recovered", action="store_true", help="drop recovered-text tails")
    ap.add_argument("--include-fallback", action="store_true", help="blocks mode: include status: fallback blocks")
    ap.add_argument("--docx", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--pick", type=int, default=None)
    ap.add_argument("--list", action="store_true", help="list the section tree with ids and exit")
    args = ap.parse_args()

    slug = resolve_slug(args.slug)
    doc = load_sections(slug)
    pages = load_pages(slug)
    counts = {p: max((x.n for x in paras), default=0) for p, (_fm, paras) in pages.items()}
    repeating = set(doc.get("repeating_lines") or [])
    by_id = {s["id"]: s for s in doc["sections"]}
    order_index = {s["id"]: i for i, s in enumerate(doc["sections"])}

    if args.list:
        for s in doc["sections"]:
            if s.get("minor"):
                continue
            print(f"{'  ' * (s['level'] - 1)}{s['title']}  p{s['start']['page']}–{s['end']['page']}  <{s['id']}>")
        return

    # ---- resolve the span ---------------------------------------------------
    section = None
    if args.pages:
        a, b = (int(x) for x in args.pages.split("-"))
        start, end = (a, 1), (b, counts.get(b, 1))
        title = f"Pages {a}–{b}"
        sec_level = min((s["level"] for s in doc["sections"] if a <= s["start"]["page"] <= b), default=1)
        outline_title = ""
        sid = f"{slug}:pages-{a}-{b}"
    else:
        if not args.query:
            ap.error("give a section query / id, or --pages A-B, or --list")
        cands = resolve_query(doc, args.query)
        if not cands:
            print(f"no section in {slug} matches '{args.query}' (try --list)", file=sys.stderr)
            sys.exit(3)
        if len(cands) > 1:
            if args.pick and 1 <= args.pick <= len(cands):
                cands = [cands[args.pick - 1]]
            else:
                print(f"'{args.query}' is ambiguous in {slug}; rerun with --pick N:")
                for i, s in enumerate(cands, 1):
                    print(f"  {i}. {s['id']} — {s['title']} (pp. {s['start']['page']}–{s['end']['page']}, level {s['level']})")
                sys.exit(2)
        section = cands[0]
        start = (section["start"]["page"], section["start"]["para"])
        end = (section["end"]["page"], section["end"]["para"])
        title = smart_title(section["title"])
        sec_level = section["level"]
        outline_title = section.get("outline_title") or ""
        sid = section["id"]
    if args.to_page:
        end = (args.to_page, counts.get(args.to_page, 1))

    span_txt = f"p{start[0]:04d}¶{start[1]}–p{end[0]:04d}¶{end[1]}"
    slug_title = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60] or "section"
    out_dir = ROOT / "work" / "pulls" / slug
    out_path = Path(args.out) if args.out else out_dir / f"{slug_title}{'.blocks' if args.mode == 'blocks' else ''}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    cfg = None if args.raw else load_sanitize(slug)
    san = Sanitizer(cfg) if cfg else None
    ambiguous = (cfg or {}).get("ambiguous") or []

    # heading level lookup by anchor position
    heading_level = {(s["start"]["page"], s["start"]["para"]): s["level"] for s in doc["sections"] if s["kind"] != "outline"}

    lines: list[str] = []
    notes = {"exhibits_dropped": 0, "recovered_tails": 0, "footer_lines_dropped": 0, "ambiguous": {}}

    def S(text: str) -> str:
        return san.apply(text) if san else text

    def SH(text: str) -> str:
        """Sanitize a heading: names generalized, but no first-use descriptor inside headings."""
        return san.apply(text, descriptor=False) if san else text

    if args.mode == "verbatim":
        gtitles = exhibit_titles(slug)
        raw_span_text = []
        for pno in sorted(pages):
            if pno < start[0] or pno > end[0]:
                continue
            _fm, paras = pages[pno]
            tail: list[str] = []
            seen_gids: set[str] = set()
            for para in paras:
                pos = (pno, para.n)
                if pos < start or pos > end:
                    continue
                raw_span_text.append(para.text)
                anchor = f"<!-- p{pno:04d} ¶{para.n} -->" if args.anchors else None
                # exhibits / picture text → asset-id markers only
                if para.picture:
                    for gid in GRAPHIC_ID_RE.findall(para.text):
                        if gid in seen_gids:
                            continue
                        seen_gids.add(gid)
                        label = f"[graphic: {gid}" + (f" — {gtitles[gid]}" if gid in gtitles else "") + "]"
                        lines += ([anchor] if anchor else []) + [label, ""]
                    notes["exhibits_dropped"] += 1
                    continue
                if para.recovered:
                    if args.no_recovered:
                        continue
                    tail.append(para.text)
                    continue
                first = para.first_line
                rest_lines = para.text.splitlines()[1:] if para.is_heading else para.text.splitlines()
                if para.is_heading:
                    m = HEADING_LINE_RE.match(first)
                    htext = plain_text(m.group(2))
                    if CAPTION_RE.match(htext):
                        lines += ([anchor] if anchor else []) + [f"_{SH(htext)}_", ""]
                    elif pos in heading_level:
                        d = heading_level[pos] - sec_level
                        t = SH(smart_title(htext))
                        if d <= 0:
                            lines += ([anchor] if anchor else []) + [f"# {t}", ""]
                        elif d == 1:
                            lines += ([anchor] if anchor else []) + [f"## {t}", ""]
                        elif d == 2:
                            lines += ([anchor] if anchor else []) + [f"### {t}", ""]
                        else:
                            lines += ([anchor] if anchor else []) + [f"**{t}**", ""]
                    elif norm_repeat(first) in repeating:
                        notes["footer_lines_dropped"] += 1
                    else:
                        lines += ([anchor] if anchor else []) + [f"**{SH(htext)}**", ""]
                    if not rest_lines:
                        continue
                    anchor = None
                # body lines
                kept = []
                for ln in rest_lines:
                    s = ln.rstrip()
                    if not s.strip():
                        kept.append("")
                        continue
                    if s.strip().startswith("<!--"):
                        continue
                    if norm_repeat(s) in repeating:
                        notes["footer_lines_dropped"] += 1
                        continue
                    c = clean_line(s)
                    if c.strip().startswith("|"):
                        kept.append(c)            # table row: keep as-is (cells already <br>→space)
                    else:
                        kept.append(c)
                text = "\n".join(kept).strip("\n")
                if not text.strip():
                    continue
                # move any asset ids in prose into markers (they sit mid-sentence in some pages)
                for gid in GRAPHIC_ID_RE.findall(text):
                    text = text.replace(gid, "").strip()
                    if gid not in seen_gids:
                        seen_gids.add(gid)
                        lines += [f"[graphic: {gid}" + (f" — {gtitles[gid]}" if gid in gtitles else "") + "]", ""]
                text = re.sub(r"[ \t]{2,}", " ", text)
                lines += ([anchor] if anchor else []) + [S(text), ""]
            if tail:
                notes["recovered_tails"] += 1
                lines += [f"_Recovered from text layer (PDF p. {pno}):_", ""]
                for t in tail:
                    tt = "\n".join(clean_line(x) for x in t.splitlines() if x.strip() and not x.strip().startswith("<!--"))
                    for gid in GRAPHIC_ID_RE.findall(tt):
                        tt = tt.replace(gid, "").strip()
                    if tt.strip():
                        lines += [S(tt), ""]
        for name in ambiguous:
            n = sum(len(re.findall(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])", t)) for t in raw_span_text)
            if n:
                notes["ambiguous"][name] = n

        # ensure the first line is an H1 (build_docx needs it)
        if not lines or not lines[0].startswith("# "):
            lines = [f"# {S(title)}", ""] + lines
        repl = sum(san.counts.values()) if san else 0
        deck = (f"_Pulled verbatim from `{slug}`" + (f" ({outline_title})" if outline_title else "")
                + f", PDF pp. {start[0]}–{end[0]} · span {span_txt} · "
                + (f"{repl} sanitization replacements" if san else "unsanitized (--raw)")
                + f" · generated {dt.date.today().isoformat()}_")
        lines.insert(2, deck)
        lines.insert(3, "")
        body = "\n".join(lines).rstrip() + "\n"
        notes_lines = ["", "## Notes", "",
                       f"- Exhibit/picture-text blocks dropped (asset ids kept as markers): {notes['exhibits_dropped']}",
                       f"- Running header/footer lines dropped: {notes['footer_lines_dropped']}",
                       f"- Recovered-text tails kept at page end: {notes['recovered_tails']}"]
        if san:
            notes_lines.append("- Sanitization replacements: " + (", ".join(f"{k} {v}" for k, v in sorted(san.counts.items())) or "none"))
        if notes["ambiguous"]:
            notes_lines.append("- Names left as-is for review (listed as ambiguous in sanitize.json): "
                               + ", ".join(f"{k} ×{v}" for k, v in notes["ambiguous"].items()))
        body += "\n".join(notes_lines) + "\n"
        header = ("---\n"
                  f"source: {slug}\nsection-id: {sid}\nsection-title: \"{title}\"\nspan: {span_txt}\n"
                  f"pages: [{start[0]}, {end[0]}]\nmode: verbatim\nsanitized: {'false' if args.raw else 'true'}\n"
                  f"generated-by: work/assemble_section.py\n---\n\n")
        out_path.write_text(header + body, encoding="utf-8")
        words = len(plain_text(body).split())
        print(f"wrote {out_path.relative_to(ROOT) if out_path.is_relative_to(ROOT) else out_path}")
        print(f"section: {title} · {span_txt} · ~{words} words · replacements: {repl} · exhibits dropped: {notes['exhibits_dropped']}")
        if notes["ambiguous"]:
            print("ambiguous names left as-is: " + ", ".join(f"{k} ×{v}" for k, v in notes["ambiguous"].items()))

    else:  # blocks mode
        sys.path.insert(0, str(ROOT / "work"))
        from map_blocks_to_pages import parse_frontmatter as pf, strip_reuse_guidance, normalize, shingles  # noqa: E402
        idx = json.loads((ROOT / "wiki" / "index.json").read_text(encoding="utf-8"))
        if args.pages:
            wanted = None
        else:
            wanted = set(subtree_ids(doc, sid))
        ref_re = re.compile(r"p(\d{4})\.md#¶(\d+)")
        chosen = []
        for b in idx:
            if str(b.get("source")) != slug:
                continue
            if wanted is not None:
                if b.get("section-id") not in wanted:
                    continue
            else:
                refs = b.get("verbatim-ref") or []
                m = ref_re.search(str(refs[0])) if refs else None
                if not m or not (start[0] <= int(m.group(1)) <= end[0]):
                    continue
            if b.get("status") == "fallback" and not args.include_fallback:
                continue
            chosen.append(b)
        chosen.sort(key=lambda b: (order_index.get(b.get("section-id"), 10**6), int(b.get("section-order") or 0), b["path"]))
        lines.append(f"# {title} — blocks")
        lines.append("")
        lines.append(f"_{len(chosen)} blocks from `{slug}` in section order ({span_txt}); "
                     f"fallback blocks {'included' if args.include_fallback else 'hidden'} · generated {dt.date.today().isoformat()}_")
        lines.append("")
        union = set()
        for n, b in enumerate(chosen, 1):
            path = ROOT / b["path"]
            fm, bodytxt = pf(path.read_text(encoding="utf-8"))
            bodytxt = strip_reuse_guidance(bodytxt)
            union |= shingles(normalize(bodytxt))
            bl = bodytxt.strip("\n").splitlines()
            if bl and bl[0].startswith("# "):
                bl = bl[1:]
            # demote the block's own sub-headings one level so they sit under "## n. Title"
            bl = [("#" + ln) if re.match(r"^#{2,5}\s", ln) else ln for ln in bl]
            refs = b.get("verbatim-ref") or []
            m = ref_re.search(str(refs[0])) if refs else None
            ref = f"p{m.group(1)}¶{m.group(2)}" if m else "—"
            sec = by_id.get(b.get("section-id"), {})
            lines.append(f"## {n}. {b.get('title')}")
            lines.append(f"`{b['path']}` · {b.get('block-type')} · {b.get('status')} · {ref} · section: {sec.get('title', b.get('section-id'))}"
                         + (f" · superseded by `{b.get('superseded-by')}`" if b.get("superseded-by") else ""))
            lines.append("")
            lines.append("\n".join(bl).strip("\n"))
            lines.append("")
        # coverage trailer over the span
        subst, covered, uncovered = 0, 0, []
        for pno in sorted(pages):
            if pno < start[0] or pno > end[0]:
                continue
            for para in pages[pno][1]:
                pos = (pno, para.n)
                if pos < start or pos > end:
                    continue
                ok, _why = is_substantive(para, repeating)
                if not ok:
                    continue
                subst += 1
                sh = shingles(normalize(para.text))
                frac = len(sh & union) / len(sh) if sh else 0.0
                if frac >= 0.5:
                    covered += 1
                else:
                    uncovered.append(f"p{pno:04d}¶{para.n} ({len(plain_text(para.text).split())} w, {int(frac*100)}%)")
        lines += ["## Coverage", "",
                  f"{len(chosen)} blocks; {covered} of {subst} substantive paragraphs in the span are covered (≥50% of 6-word shingles)."]
        if uncovered:
            lines.append("Uncovered: " + ", ".join(uncovered))
        header = ("---\n"
                  f"source: {slug}\nsection-id: {sid}\nsection-title: \"{title}\"\nspan: {span_txt}\nmode: blocks\n"
                  f"generated-by: work/assemble_section.py\n---\n\n")
        out_path.write_text(header + "\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"wrote {out_path.relative_to(ROOT) if out_path.is_relative_to(ROOT) else out_path}")
        print(f"{len(chosen)} blocks · coverage {covered}/{subst} substantive paragraphs")

    if args.docx:
        docx = out_path.with_suffix(".docx")
        label = outline_title or title
        rc = subprocess.call([sys.executable, str(ROOT / "work" / "build_docx.py"), str(out_path), str(docx),
                              "--section-label", label, "--header", f"{slug} — {title}"])
        if rc == 0:
            print(f"wrote {docx}")
        else:
            print(f"build_docx.py exited {rc}", file=sys.stderr)


if __name__ == "__main__":
    main()
