import json, re
from pathlib import Path

reg = json.load(open('proof-points/registry.json', encoding='utf-8'))
by_number = {}
for pp in reg:
    for v in pp['values']:
        num = v.get('number','').replace(',','')
        by_number.setdefault(num, []).append((pp['id'], v.get('unit',''), pp['claim'], v.get('block','')))

files = """wiki/technical-approach/asset-management-improvement-shifts-table.md
wiki/technical-approach/innovation-workshop-sample-agenda-structure.md
wiki/technical-approach/om-management-systems-framework.md
wiki/technical-approach/sensor-dispersion-model-odor-early-warning-system.md
wiki/technical-approach/swip-cmms-inventory-management-value-add.md
wiki/technical-approach/swip-community-involvement-outreach-program.md
wiki/technical-approach/swip-digital-kpi-reporting-dashboard.md
wiki/technical-approach/swip-dpr-readiness-expert-bench-and-monitoring.md
wiki/technical-approach/swip-firm-approach-section-opener-understanding.md
wiki/technical-approach/swip-inventory-management-asset-tracking.md
wiki/technical-approach/swip-mbr-fouling-mitigation-case-study.md
wiki/technical-approach/swip-replica-digital-twin-plant-digital-tools.md
wiki/technical-approach/value-added-innovations-menu-om-contracts.md
wiki/management-staffing/blended-onsite-offsite-org-structure.md
wiki/management-staffing/surge-staffing-backup-resource-planning.md
wiki/management-staffing/workforce-retention-transition-continuity.md
wiki/win-themes/community-stewardship-public-engagement-program.md
wiki/win-themes/cover-letter-structure-pattern.md
wiki/win-themes/differentiator-traditional-vs-enhanced-om-comparison.md
wiki/win-themes/embedded-client-testimonial-technical-narrative.md
wiki/win-themes/embedded-differentiator-case-study-callout.md
wiki/win-themes/exec-summary-client-readiness-framing.md
wiki/win-themes/leadership-team-and-coordinated-operations-narrative.md
wiki/win-themes/past-performance-narrative-structure.md
wiki/win-themes/project-narrative-contract-transition-turnaround.md
wiki/win-themes/project-narrative-long-term-dbo-performance-excellence.md
wiki/win-themes/project-narrative-new-contract-mobilization-innovation.md
wiki/win-themes/project-narrative-utility-partnership-cost-savings.md
wiki/win-themes/project-narrative-workforce-transition-biosolids-modernization.md
wiki/win-themes/similar-facilities-comparison-table-framing.md
wiki/win-themes/swip-bottom-line-close-and-positioning-statement.md
wiki/win-themes/swip-compliance-reliability-transparency-narrative.md
wiki/win-themes/swip-safety-emergency-preparedness-risk-management.md
wiki/win-themes/swip-top-water-reuse-experts-on-call.md
wiki/qualifications/full-service-lifecycle-capability-and-capital-planning-support.md
wiki/qualifications/reference-portfolio-comparability-and-similar-facilities.md
wiki/qualifications/representative-past-performance-narrative-patterns.md
wiki/compliance-plans/capital-planning-construction-support-innovation-studies.md
wiki/compliance-plans/regulatory-compliance-reporting-dashboard.md
wiki/compliance-plans/transition-due-diligence-governance-checklist.md
wiki/compliance-plans/transition-team-organization-roster.md
wiki/resumes/proposed-team-roster-hull-wwtf-om-2026.md""".splitlines()

pat = re.compile(r'\$[\d,]+(?:\.\d+)?|\b\d[\d,]*(?:\.\d+)?%|\b\d[\d,]*(?:\.\d+)?\s?(?:MGD|mi\.|miles|million|billion|kWh|hours?|years?|households|employees|complaints|gallons|acres|GPD|mgd)\b', re.I)

out = []
for f in files:
    text = Path(f).read_text(encoding='utf-8')
    parts = text.split('---\n', 2)
    body = parts[2] if len(parts) >= 3 else text
    found = pat.findall(body)
    nums = set()
    for m in found:
        n = re.search(r'[\d,.]+', m)
        if n:
            nums.add(n.group(0).replace(',','').rstrip('.'))
    matches = {}
    for n in nums:
        if n in by_number:
            for (pid, unit, claim, blk) in by_number[n]:
                matches.setdefault(pid, []).append((n, unit, claim, blk))
    out.append("### " + f)
    out.append("  raw: " + repr(found))
    if matches:
        for pid, lst in matches.items():
            for (n,unit,claim,blk) in lst:
                out.append(f"    {pid} n={n} unit={unit} claim={claim}")
    else:
        out.append("  (none)")

Path('work/fragments/pp_match_output.txt').write_text("\n".join(out), encoding='utf-8')
print("done", len(out))
