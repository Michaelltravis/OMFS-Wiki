#!/usr/bin/env python3
"""freshness.py — make staleness computable for every content block (zero model tokens).

Usage:
    python work/freshness.py [--today YYYY-MM-DD] [--write]
                             [--json work/curation/report.json] [--md work/curation/report.md]
                             [--source <slug>] [--only-overdue] [--only-flagged] [--include-archived]
                             [--quiet]

For every block under wiki/<category>/*.md it derives:

  volatility      people | reference | corporate-figure | safety-stat | regulatory |
                  project-outcome | evergreen — how fast the block's facts age (first rule
                  that matches wins; see classify()).
  basis date      last-verified when verified-by is set (someone actually checked it);
                  otherwise the SOURCE PROPOSAL's date from work/curation/sources.json
                  (the facts are as old as the proposal that stated them, not as old as
                  the extraction stamp); otherwise `extracted`.
  review-due      basis + the class interval from work/curation/policy.json.
  freshness-flags machine-detected currency problems: open-ended-date, divergent-figure,
                  newer-source-same-claim, person-duplicate, dead-link, link-nonreciprocal,
                  link-format, status-link-mismatch, stale-contact, feedback.

Overdue-ness (review-due < today) is computed for the report and NEVER stored — it
depends on the day you ask.

Outputs: work/curation/report.json + report.md (ranked by house-favorite, usage in
pursuits/templates/stories, overdue days, flag severity; grouped by owner), plus a
registry section (conflict rows, newest source per claim) and the unlinked dedupe pairs.

--write: set volatility / review-due / freshness-flags in each block's frontmatter via
work/patch_frontmatter.py (only files whose values change are rewritten; bodies are
never touched). This is derived metadata — the curate skill may write it without asking.
Status, supersedes links and archive fields are NEVER written here (see work/curate.py).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "work"))

from lint_blocks import (CATEGORY_DIRS, FLAG_ENUM, LINK_PATH_RE, VOLATILITY_ENUM,  # noqa: E402
                         as_list, link_stem, link_targets, load_frontmatter)
from dedupe_candidates import find_pairs, load_blocks as dd_load_blocks, load_decided_pairs  # noqa: E402
from patch_frontmatter import apply_patches  # noqa: E402

CURATION = ROOT / "work" / "curation"
NARRATIVE_CATEGORIES = {"technical-approach", "management-staffing", "win-themes",
                        "qualifications", "compliance-plans"}

DEFAULT_POLICY = {
    "intervals_days": {"people": 180, "reference": 180, "regulatory": 180, "corporate-figure": 365,
                       "safety-stat": 365, "project-outcome": 730, "evergreen": 1095},
    "default_owner": "Michael Travis",
    "dedupe_min_body_sim": 0.12,
    "report_top_n": 50,
}

SEVERITY = ["feedback", "newer-source-same-claim", "divergent-figure", "stale-contact",
            "person-duplicate", "open-ended-date", "status-link-mismatch", "dead-link",
            "link-nonreciprocal", "link-format", "unresolved-conflict"]
SEVERITY_RANK = {f: i for i, f in enumerate(SEVERITY)}

# --- detectors -------------------------------------------------------------------------
PHONE_RE = re.compile(r"(?<!\d)\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SAFETY_RE = re.compile(r"\b(TRIR|EMR|DART|LTIR|RIR|TRR)\b|\b(lost[- ]time|recordable incident|recordable injur)", re.IGNORECASE)
CORP_DOLLAR_RE = re.compile(r"\$\s?\d+(?:\.\d+)?\s?(?:B\b|billion)", re.IGNORECASE)
CORP_SCALE_RE = re.compile(r"\b(\d[\d,]*\+?)\s+(employees|professionals|staff members|people worldwide|offices|countries)\b", re.IGNORECASE)
REG_RE = re.compile(r"\b(legislation|house bill|senate bill|[HS]B\s?\d{2,5}|rulemaking|proposed rule|"
                    r"PFAS (?:limit|rule|MCL|regulation)|effective (?:date )?(?:of )?20\d\d|regulatory change|"
                    r"new (?:federal|state) (?:rule|requirement|regulation))", re.IGNORECASE)
YEARS_RE = re.compile(r"\b\d{1,2}\+?\s*years?\s+(?:of|in|with)\b", re.IGNORECASE)
OPEN_ENDED_RE = re.compile(r"\b(?:19|20)\d\d\s*(?:–|-|—|to)\s*(?:Present|Ongoing|Current|Today)\b|"
                           r"\bsince\s+(?:19|20)\d\d\b|\(ongoing\)", re.IGNORECASE)
RESUME_TITLE_PREFIX_RE = re.compile(r"^\s*(?:Resume|Résumé)\s*[—–-]\s*", re.IGNORECASE)
PP_RE = re.compile(r"\bPP-\d{4}\b")

CORPORATE_FAMILIES = {"corporate-revenue", "global-employee-count", "corporate-bonding-capacity"}


def iso(v) -> str:
    if isinstance(v, (dt.date, dt.datetime)):
        return v.strftime("%Y-%m-%d")
    return str(v).strip() if v is not None else ""


def parse_date(v) -> dt.date | None:
    s = iso(v)
    try:
        return dt.date.fromisoformat(s[:10]) if s else None
    except ValueError:
        return None


def load_json(path: Path, default):
    if not path.is_file():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def strip_reuse_guidance(body: str) -> str:
    return re.split(r"\n##\s+Reuse guidance\b", body, maxsplit=1, flags=re.IGNORECASE)[0]


def person_name_from_title(title: str) -> str | None:
    """'Resume — Amy Dembinski, CRL (Asset Manager)' -> 'Amy Dembinski';
    'Chris Catlin, PE - Manager of Operations' -> 'Chris Catlin'."""
    t = RESUME_TITLE_PREFIX_RE.sub("", str(title or ""))
    t = re.sub(r'\s*["“][^"”]+["”]\s*', " ", t)  # nicknames
    t = re.split(r"\s*(?:\(|,|\s[—–-]\s)", t, maxsplit=1)[0].strip()
    words = t.split()
    if 2 <= len(words) <= 4 and all(w[:1].isupper() for w in words):
        return " ".join(words)
    return None


def name_key(name: str) -> str:
    return re.sub(r"[^a-z]", "", name.lower())


def registry_family(row: dict) -> str | None:
    try:
        from build_proof_point_registry import FAMILIES
    except Exception:
        return None
    claim = str(row.get("claim") or "").lower()
    units = " ".join(str(v.get("unit") or "") for v in row.get("values", [])).lower()
    for name, claim_re, unit_re in FAMILIES:
        if re.search(claim_re, claim) and (unit_re is None or re.search(unit_re, units)):
            return name
    return None


# --- core ------------------------------------------------------------------------------
class Freshness:
    def __init__(self, today: dt.date, include_archived=False):
        self.today = today
        self.include_archived = include_archived
        self.policy = {**DEFAULT_POLICY, **load_json(CURATION / "policy.json", {})}
        self.intervals = {**DEFAULT_POLICY["intervals_days"], **self.policy.get("intervals_days", {})}
        self.sources = {k: v for k, v in load_json(CURATION / "sources.json", {}).items() if not k.startswith("_")}
        self.registry = {r["id"]: r for r in load_json(ROOT / "proof-points" / "registry.json", []) if r.get("id")}
        self.feedback = self._load_feedback()
        self.blocks = self._load_blocks()
        self.by_path = {b["path"]: b for b in self.blocks}
        self.by_stem = defaultdict(list)
        for b in self.blocks:
            self.by_stem[b["stem"]].append(b["path"])
        self.resume_names = self._resume_names()
        self.usage = self._usage_counts()
        self.families = {pid: registry_family(r) for pid, r in self.registry.items()}

    # -- loading
    def _load_blocks(self):
        out = []
        for cat in CATEGORY_DIRS:
            d = ROOT / "wiki" / cat
            if not d.is_dir():
                continue
            for path in sorted(d.glob("*.md")):
                text = path.read_text(encoding="utf-8")
                fm, body, err = load_frontmatter(text)
                if err:
                    continue
                out.append({
                    "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "stem": path.stem,
                    "category": cat,
                    "fm": fm,
                    "body": strip_reuse_guidance(body),
                    "reuse_notes": str(fm.get("reuse-notes") or ""),
                })
        return out

    def _load_feedback(self):
        p = CURATION / "feedback.jsonl"
        rows = []
        if p.is_file():
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except Exception:
                        pass
        return rows

    def _resume_names(self):
        names = {}
        for b in self.blocks:
            if b["category"] == "resumes" or b["fm"].get("block-type") == "roster":
                n = person_name_from_title(b["fm"].get("title"))
                if n and b["category"] == "resumes":
                    names.setdefault(name_key(n), {"name": n, "paths": []})["paths"].append(b["path"])
        return names

    def _usage_counts(self):
        texts = []
        for p in list((ROOT / "pursuits").glob("*/content-plan.md")) + \
                 [ROOT / "templates" / "standard-topics.md", ROOT / "stories" / "catalog.md"]:
            if p.is_file():
                texts.append(p.read_text(encoding="utf-8"))
        blob = "\n".join(texts)
        # a block is "used" wherever a plan, the standard-topics sheet or the story catalog names its file
        return {b["path"]: blob.count(b["stem"] + ".md") for b in self.blocks}

    # -- derivations
    def source_date(self, slug) -> dt.date | None:
        return parse_date((self.sources.get(str(slug)) or {}).get("proposal_date"))

    def owner_of(self, slug) -> str:
        return (self.sources.get(str(slug)) or {}).get("owner") or self.policy.get("default_owner", "")

    def classify(self, b) -> str:
        fm, body, cat = b["fm"], b["body"], b["category"]
        if cat == "resumes" or fm.get("block-type") == "roster":
            return "people"
        if cat == "past-performance" and (PHONE_RE.search(body) or EMAIL_RE.search(body)):
            return "reference"
        if SAFETY_RE.search(body):
            return "safety-stat"
        pp_ids = [str(x) for x in as_list(fm.get("proof-point-ids"))]
        if CORP_DOLLAR_RE.search(body) or CORP_SCALE_RE.search(body) or \
                any(self.families.get(pid) in CORPORATE_FAMILIES for pid in pp_ids):
            return "corporate-figure"
        if REG_RE.search(body):
            return "regulatory"
        if YEARS_RE.search(body) or self.names_in(body):
            return "people"
        if cat == "past-performance":
            return "project-outcome"
        return "evergreen"

    def names_in(self, body: str):
        return [v["name"] for v in self.resume_names.values() if v["name"] in body]

    def basis(self, b):
        fm = b["fm"]
        if fm.get("verified-by") and parse_date(fm.get("last-verified")):
            return parse_date(fm.get("last-verified")), "review"
        sd = self.source_date(fm.get("source"))
        if sd:
            return sd, "source"
        return parse_date(fm.get("extracted")), "extraction"

    def flags_for(self, b, volatility, basis_date, review_due):
        fm, body, path = b["fm"], b["body"], b["path"]
        flags = []  # (flag, detail, evidence)
        status = fm.get("status")

        m = OPEN_ENDED_RE.findall(body)
        if m:
            spans = sorted({x.group(0) for x in OPEN_ENDED_RE.finditer(body)})[:4]
            flags.append(("open-ended-date", "; ".join(spans), path))

        pp_ids = [str(x) for x in as_list(fm.get("proof-point-ids")) if PP_RE.match(str(x))]
        src = str(fm.get("source") or "")
        my_date = self.source_date(src)
        conflicts, newer = [], []
        for pid in pp_ids:
            row = self.registry.get(pid)
            if not row:
                continue
            if row.get("status") == "conflict":
                conflicts.append(pid)
            if my_date:
                mine = {str(v.get("number")) for v in row.get("values", []) if v.get("source_slug") == src}
                for v in row.get("values", []):
                    od = self.source_date(v.get("source_slug"))
                    if od and od > my_date and str(v.get("number")) not in mine and mine:
                        newer.append(f"{pid}: {src} says {', '.join(sorted(mine))}; {v.get('source_slug')} "
                                     f"({od.isoformat()}) says {v.get('number')} {v.get('unit') or ''}".strip())
                        break
        if conflicts:
            flags.append(("divergent-figure", ", ".join(conflicts[:6]) + (" …" if len(conflicts) > 6 else ""),
                          "proof-points/registry.md"))
        if newer:
            flags.append(("newer-source-same-claim", " | ".join(newer[:3]), "proof-points/registry.json"))

        if b["category"] == "resumes":
            n = person_name_from_title(fm.get("title"))
            if n:
                entry = self.resume_names.get(name_key(n))
                if entry and len(entry["paths"]) > 1:
                    others = [p for p in entry["paths"] if p != path]
                    linked = {link_stem(t) for k in ("supersedes", "superseded-by") for t in link_targets(fm.get(k))}
                    if not any(Path(o).stem in linked for o in others):
                        flags.append(("person-duplicate", f"{n} also in {', '.join(others)}", others[0]))

        for key in ("supersedes", "superseded-by", "pairs-with"):
            for target in link_targets(fm.get(key)):
                if not LINK_PATH_RE.match(target):
                    flags.append(("link-format", f"{key}: {target}", path))
                resolved = self.resolve(target)
                if resolved is None:
                    flags.append(("dead-link", f"{key}: {target}", path))
                    continue
                if key in ("supersedes", "superseded-by"):
                    rev = "superseded-by" if key == "supersedes" else "supersedes"
                    back = {link_stem(t) for t in link_targets(self.by_path[resolved]["fm"].get(rev))}
                    if b["stem"] not in back:
                        flags.append(("link-nonreciprocal", f"{key}: {resolved} has no {rev} back", resolved))

        has_winner = bool(link_targets(fm.get("superseded-by")))
        if status == "preferred" and has_winner:
            flags.append(("status-link-mismatch", "preferred but carries superseded-by", path))
        if status == "fallback" and not has_winner:
            flags.append(("status-link-mismatch", "fallback with no superseded-by winner", path))
        if status == "fallback" and fm.get("house-favorite") is True:
            flags.append(("status-link-mismatch", "fallback and house-favorite", path))

        if volatility == "reference" and review_due and review_due < self.today:
            flags.append(("stale-contact", f"reference contact unverified since {basis_date.isoformat()}", path))

        fb = [f for f in self.feedback
              if path in (f.get("block_paths") or []) or set(pp_ids) & set(f.get("pp_ids") or [])]
        if fb:
            flags.append(("feedback", "; ".join(str(f.get("text") or f.get("reason") or "")[:90] for f in fb[:2]),
                          "work/curation/feedback.jsonl"))

        return [f for f in flags if f[0] in FLAG_ENUM]

    def resolve(self, target: str):
        t = str(target).replace("\\", "/").strip()
        if t in self.by_path:
            return t
        hits = self.by_stem.get(link_stem(t), [])
        return hits[0] if len(hits) == 1 else None

    def compute_block(self, b) -> dict:
        fm = b["fm"]
        volatility = self.classify(b)
        basis_date, basis_kind = self.basis(b)
        interval = int(self.intervals.get(volatility, 365))
        review_due = (basis_date + dt.timedelta(days=interval)) if basis_date else None
        flags = self.flags_for(b, volatility, basis_date, review_due)
        overdue = (self.today - review_due).days if (review_due and review_due < self.today) else 0
        sev = min((SEVERITY_RANK.get(f[0], 99) for f in flags), default=99)
        return {
            "path": b["path"], "title": fm.get("title"), "category": b["category"],
            "source": fm.get("source"), "status": fm.get("status"), "house_favorite": bool(fm.get("house-favorite")),
            "volatility": volatility, "basis_date": basis_date.isoformat() if basis_date else None,
            "basis": basis_kind, "review_due": review_due.isoformat() if review_due else None,
            "overdue_days": overdue, "usage": int(self.usage.get(b["path"], 0)),
            "flags": [{"flag": f, "detail": d, "evidence": e} for f, d, e in flags],
            "severity": sev, "owner": self.owner_of(fm.get("source")),
            "current": {"volatility": fm.get("volatility"), "review_due": iso(fm.get("review-due")) or None,
                        "flags": [str(x) for x in as_list(fm.get("freshness-flags"))]},
        }

    def registry_rows(self):
        rows = []
        for pid, r in self.registry.items():
            flags = []
            if r.get("status") == "conflict":
                flags.append("unresolved-conflict")
            if any(iso(v.get("as_of")) in ("", "unknown") or re.fullmatch(r"\d{4}", iso(v.get("as_of")))
                   for v in r.get("values", [])):
                flags.append("as-of-imprecise")
            dated = [(self.source_date(v.get("source_slug")), v) for v in r.get("values", [])]
            dated = [(d, v) for d, v in dated if d]
            newest = max(dated, key=lambda x: x[0])[1].get("source_slug") if dated else None
            if r.get("status") == "conflict" and newest and len({v.get("source_slug") for v in r.get("values", [])}) > 1:
                flags.append("newer-value-available")
            if flags:
                rows.append({"id": pid, "claim": r.get("claim"), "status": r.get("status"), "flags": flags,
                             "newest_source": newest, "owner": r.get("owner") or "",
                             "family": self.families.get(pid),
                             "values": [{"number": v.get("number"), "unit": v.get("unit"), "as_of": v.get("as_of"),
                                         "source": v.get("source_slug"), "block": v.get("block")} for v in r.get("values", [])]})
        return rows

    def dedupe_pairs(self):
        blocks = dd_load_blocks(exclude_archived=True)
        decided = load_decided_pairs(CURATION / "log.jsonl")
        return find_pairs(blocks, min_body=float(self.policy.get("dedupe_min_body_sim", 0.12)),
                          skip_linked=True, decided=decided)


# --- report -----------------------------------------------------------------------------
def rank_key(r):
    return (not r["house_favorite"], -r["usage"], -r["overdue_days"], r["severity"], r["path"])


def build_report(fx: Freshness, source_filter=None, only_overdue=False, only_flagged=False):
    results = []
    for b in fx.blocks:
        if b["fm"].get("status") == "archived" and not fx.include_archived:
            continue
        if source_filter and str(b["fm"].get("source")) != source_filter:
            continue
        results.append(fx.compute_block(b))
    results.sort(key=rank_key)
    for i, r in enumerate(results, 1):
        r["rank"] = i
    shown = [r for r in results
             if (not only_overdue or r["overdue_days"] > 0) and (not only_flagged or r["flags"])]
    counts = {
        "blocks": len(results),
        "by_status": dict(Counter(r["status"] for r in results)),
        "by_volatility": dict(Counter(r["volatility"] for r in results)),
        "by_basis": dict(Counter(r["basis"] for r in results)),
        "by_flag": dict(Counter(f["flag"] for r in results for f in r["flags"])),
        "flagged_blocks": sum(1 for r in results if r["flags"]),
        "overdue": sum(1 for r in results if r["overdue_days"] > 0),
        "overdue_by_owner": dict(Counter(r["owner"] for r in results if r["overdue_days"] > 0)),
        "overdue_by_volatility": dict(Counter(r["volatility"] for r in results if r["overdue_days"] > 0)),
        "overdue_by_source": dict(Counter(str(r["source"]) for r in results if r["overdue_days"] > 0)),
    }
    reg = fx.registry_rows()
    pairs = fx.dedupe_pairs()
    counts["registry_conflicts"] = sum(1 for r in reg if "unresolved-conflict" in r["flags"])
    counts["dedupe_pairs_unlinked"] = len(pairs)
    return {"today": fx.today.isoformat(), "policy": {"intervals_days": fx.intervals},
            "counts": counts, "blocks": shown, "registry": reg, "pairs": pairs}


def render_md(rep: dict, top_n: int) -> str:
    c = rep["counts"]
    L = [f"# Freshness report — {rep['today']}", "",
         "_Generated by `python work/freshness.py`. Basis date = last-verified when verified-by is set, "
         "else the source proposal date (work/curation/sources.json). Overdue = review-due before today. "
         "Nothing here changes a block's status; see work/curate.py and the curate skill._", "",
         "## Counts", "",
         f"- Blocks: {c['blocks']} · flagged: {c['flagged_blocks']} · overdue: {c['overdue']} · "
         f"registry conflicts: {c['registry_conflicts']} · unlinked duplicate pairs: {c['dedupe_pairs_unlinked']}",
         f"- Status: {', '.join(f'{k} {v}' for k, v in sorted(c['by_status'].items()))}",
         f"- Volatility: {', '.join(f'{k} {v}' for k, v in sorted(c['by_volatility'].items(), key=lambda kv: -kv[1]))}",
         f"- Basis: {', '.join(f'{k} {v}' for k, v in sorted(c['by_basis'].items()))}",
         f"- Flags: {', '.join(f'{k} {v}' for k, v in sorted(c['by_flag'].items(), key=lambda kv: -kv[1])) or 'none'}",
         ""]
    L += ["## Overdue by owner", ""]
    if c["overdue_by_owner"]:
        L.append("| Owner | Overdue blocks | By volatility | By source |")
        L.append("|---|---:|---|---|")
        for owner, n in sorted(c["overdue_by_owner"].items(), key=lambda kv: -kv[1]):
            byv = Counter(r["volatility"] for r in rep["blocks"] if r["owner"] == owner and r["overdue_days"] > 0)
            bys = Counter(str(r["source"]) for r in rep["blocks"] if r["owner"] == owner and r["overdue_days"] > 0)
            L.append(f"| {owner} | {n} | {', '.join(f'{k} {v}' for k, v in byv.most_common())} "
                     f"| {', '.join(f'{k} {v}' for k, v in bys.most_common())} |")
    else:
        L.append("_Nothing overdue._")
    L.append("")

    L += [f"## Top {top_n} blocks to look at", "",
          "_Ranked: house-favorite first, then usage in pursuits/templates/stories, then days overdue, then flag severity._", "",
          "| # | Block | volatility | basis | review-due | overdue | flags |", "|---:|---|---|---|---|---:|---|"]
    for r in rep["blocks"][:top_n]:
        flags = "; ".join(f"**{f['flag']}** {f['detail']}" for f in r["flags"]) or "—"
        fav = " ★" if r["house_favorite"] else ""
        L.append(f"| {r['rank']} | [{r['title']}]({'../../' + r['path']}){fav} | {r['volatility']} | "
                 f"{r['basis_date']} ({r['basis']}) | {r['review_due']} | {r['overdue_days'] or '—'} | {flags} |")
    L.append("")

    dups = [r for r in rep["blocks"] if any(f["flag"] == "person-duplicate" for f in r["flags"])]
    L += ["## Duplicate people (two resume files, no supersedes link)", ""]
    if dups:
        for r in dups:
            d = next(f for f in r["flags"] if f["flag"] == "person-duplicate")
            L.append(f"- `{r['path']}` — {d['detail']}")
    else:
        L.append("_None._")
    L.append("")

    conf = [r for r in rep["registry"] if "unresolved-conflict" in r["flags"]]
    L += [f"## Registry conflicts ({len(conf)})", "",
          "_Same claim, different numbers. The newest source is usually right for corporate figures; "
          "a human owner decides (`python work/curate.py owner PP-xxxx --set <name>`)._", "",
          "| id | claim | values (source) | newest source | family |", "|---|---|---|---|---|"]
    for r in sorted(conf, key=lambda r: (r["family"] is None, r["id"])):
        vals = "; ".join(f"{v['number']} {v['unit'] or ''} ({v['source']}, as of {v['as_of']})".strip() for v in r["values"][:4])
        L.append(f"| {r['id']} | {r['claim']} | {vals} | {r['newest_source'] or '—'} | {r['family'] or '—'} |")
    L.append("")

    L += [f"## Supersession candidates — unlinked duplicate pairs ({len(rep['pairs'])})", "",
          "_From work/dedupe_candidates.py with --skip-linked; pairs already decided in work/curation/log.jsonl are dropped._", "",
          "| body_sim | title_sim | a (status) | b (status) |", "|---:|---:|---|---|"]
    for p in rep["pairs"][:60]:
        L.append(f"| {p['body_sim']:.3f} | {p['title_sim']:.3f} | `{p['a']}` ({p['a_status']}) | `{p['b']}` ({p['b_status']}) |")
    L.append("")
    return "\n".join(L).rstrip() + "\n"


# --- write ------------------------------------------------------------------------------
def build_patches(rep: dict):
    patches = []
    for r in rep["blocks"]:
        want = {"volatility": r["volatility"], "review-due": r["review_due"],
                "freshness-flags": sorted({f["flag"] for f in r["flags"]})}
        cur = r["current"]
        if (cur["volatility"] == want["volatility"] and cur["review_due"] == want["review-due"]
                and sorted(cur["flags"]) == want["freshness-flags"]):
            continue
        sets = {k: v for k, v in want.items() if v is not None}
        patches.append({"path": r["path"], "set": sets})
    return patches


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--today", default=None)
    ap.add_argument("--write", action="store_true", help="write volatility / review-due / freshness-flags into frontmatter")
    ap.add_argument("--json", dest="json_out", default=str(CURATION / "report.json"))
    ap.add_argument("--md", dest="md_out", default=str(CURATION / "report.md"))
    ap.add_argument("--source", default=None, help="restrict output and --write to one source slug")
    ap.add_argument("--only-overdue", action="store_true")
    ap.add_argument("--only-flagged", action="store_true")
    ap.add_argument("--include-archived", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    fx = Freshness(today, include_archived=args.include_archived)
    rep = build_report(fx, source_filter=args.source, only_overdue=args.only_overdue, only_flagged=args.only_flagged)

    CURATION.mkdir(parents=True, exist_ok=True)
    Path(args.json_out).write_text(json.dumps(rep, indent=1, default=str), encoding="utf-8")
    Path(args.md_out).write_text(render_md(rep, int(fx.policy.get("report_top_n", 50))), encoding="utf-8")

    c = rep["counts"]
    if not args.quiet:
        print(f"freshness {today.isoformat()}: {c['blocks']} blocks · flagged {c['flagged_blocks']} · overdue {c['overdue']} "
              f"· registry conflicts {c['registry_conflicts']} · unlinked pairs {c['dedupe_pairs_unlinked']}")
        print("  volatility: " + ", ".join(f"{k} {v}" for k, v in sorted(c["by_volatility"].items(), key=lambda kv: -kv[1])))
        print("  flags:      " + (", ".join(f"{k} {v}" for k, v in sorted(c["by_flag"].items(), key=lambda kv: -kv[1])) or "none"))
        print("  overdue by volatility: " + (", ".join(f"{k} {v}" for k, v in sorted(c["overdue_by_volatility"].items(), key=lambda kv: -kv[1])) or "none"))
        print(f"  wrote {Path(args.json_out)} and {Path(args.md_out)}")

    if args.write:
        patches = build_patches(rep)
        pfile = CURATION / "patches_freshness.json"
        pfile.write_text(json.dumps(patches, indent=1), encoding="utf-8")
        if patches:
            results = apply_patches(patches, quiet=True)
            n = sum(1 for r in results if r["action"] == "WRITE")
            print(f"  --write: {n} block(s) updated, {len(rep['blocks']) - n} unchanged (patches in {pfile.relative_to(ROOT)})")
        else:
            print(f"  --write: 0 blocks updated, {len(rep['blocks'])} unchanged")


if __name__ == "__main__":
    main()
