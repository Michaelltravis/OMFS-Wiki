"""Build workflow args for the OCWUT + Fulton block build (extract-proposal.js)."""
import json, os
W = r"C:\Users\micha\Desktop\Wiki"
oc = ["Oklahoma City Water Utilities Trust", "OCWUT", "City of Oklahoma City", "Oklahoma City", "OKC"]
octx = ("Southcentral US municipal water utility trust wastewater O&M competitive procurement, 2026 award for Jan 1 2027 start; "
        "four WWTPs plus one major pump station, >110 MGD combined design capacity, Class B biosolids land application, 109 FTE proposed; "
        "challenger bid against an underperforming incumbent operator, backed by a 20-year engineering relationship; ODEQ regulatory regime.")
fc = ["Fulton County Department of Public Works", "Fulton County Public Works", "Fulton County", "North Fulton",
      "the County (only where it means the pursuit client)", "Big Creek WRF", "Johns Creek Environmental Campus", "JCEC", "Little River WRF"]
fctx = ("Southeast US county wastewater O&M pursuit (North Fulton), 2025, bid as JC Solutions, a JV of Jacobs and Atlanta-based minority-owned CERM; "
        "three water reclamation facilities (32 MGD MBR, 15 MGD MBR, 2.6 MGD) plus 28 wastewater and 5 potable water pump stations; "
        "MBR-heavy membrane operations, $750K workforce development commitment, incumbent engineering presence; Georgia EPD regulatory regime.")
O = [("Cover Letter", 4, 6, "win-themes", "cover-letter"),
     ("Executive Summary of Technical Approach", 8, 10, "win-themes", "exec-summary"),
     ("Technical Approach: Facility Understanding and Odor Strategy", 12, 16, "technical-approach", "tech-approach"),
     ("Management Plan: Leadership, Performance Framework, QA/QC, Reporting, Community Engagement", 17, 25, "management-staffing", "staffing"),
     ("Operations Plan: Process Control Strategy by Facility", 26, 33, "technical-approach", "tech-approach"),
     ("Operations Plan: Reuse Water, Regulatory Compliance, Laboratory and Sampling", 34, 38, "compliance-plans", "compliance"),
     ("Operations Plan: ODEQ Relationship and Odor Control Strategy", 39, 44, "technical-approach", "tech-approach"),
     ("Operations Plan: SCADA/OT and Cybersecurity", 45, 47, "technical-approach", "tech-approach"),
     ("Operations Plan: Safety, Site Security, Emergency Operating Plan", 48, 52, "compliance-plans", "compliance"),
     ("Operations Plan: Energy Management, Pump Station Ops, Septage Receiving", 53, 56, "technical-approach", "tech-approach"),
     ("Maintenance Plan: Findings, Facility Priorities, Asset Management System (NexGen EAM)", 57, 64, "technical-approach", "tech-approach"),
     ("Maintenance Plan: Staffing, Inventory, M&R and R&R Funds, ARM Tool, CIP Coordination", 65, 69, "technical-approach", "tech-approach"),
     ("Firm Qualifications: Corporate Structure, Oklahoma Experience, Capability Case Studies", 73, 80, "qualifications", "qualifications"),
     ("Management Structure and Management Team Qualifications", 81, 88, "management-staffing", "staffing"),
     ("Off-Site SME Support Resources (O&M and Engineering)", 89, 94, "qualifications", "staffing"),
     ("Key Team Member Resumes 1", 95, 106, "resumes", "resume"),
     ("Key Team Member Resumes 2", 107, 118, "resumes", "resume"),
     ("Key Team Member Resumes 3", 119, 122, "resumes", "resume"),
     ("Section 4: Oklahoma Law, Risk Management, Stormwater, Biosolids Legislation", 124, 126, "compliance-plans", "compliance"),
     ("Required Plan: Staffing and Training Plan", 128, 135, "management-staffing", "staffing"),
     ("Required Plan: Sludge Management Plan", 136, 138, "compliance-plans", "compliance"),
     ("Required Plan: Operational Integration Plan", 139, 143, "compliance-plans", "compliance"),
     ("Required Plan: Draft Transition Plan", 144, 154, "technical-approach", "transition"),
     ("Required Plan: Solids Management Plan", 155, 158, "compliance-plans", "compliance"),
     ("Projects and References 1 (reference table, Bixby, Jackson, Waterbury)", 164, 170, "past-performance", "past-performance"),
     ("Projects and References 2 (Westside/Marine Park, Agua Nueva DBO, San Marcos)", 171, 176, "past-performance", "past-performance"),
     ("Section 8: Innovative and Alternative Recommendations", 178, 180, "win-themes", "tech-approach")]
F = [("Section 1: Executive Summary", 9, 11, "win-themes", "exec-summary"),
     ("RFP Wayfinding Crosswalk (pattern artifact)", 4, 7, "win-themes", "exec-summary"),
     ("2.1-2.4 Comprehensive O&M Approach, Deliverables Commitment, Project Execution and Administration", 13, 18, "technical-approach", "tech-approach"),
     ("2.5 Project Understanding, County Goals, Facility-by-Facility Challenges", 19, 26, "technical-approach", "tech-approach"),
     ("2.6 Benefits: Value-Added Extras, Investments, Digital Tools, Energy Management", 27, 33, "win-themes", "tech-approach"),
     ("2.6 Benefits: Maintenance AI, Replica Digital Twin, Advanced Analytics", 34, 39, "win-themes", "tech-approach"),
     ("2.7 Approach to Providing Qualified and Licensed Personnel", 40, 43, "management-staffing", "staffing"),
     ("2.8 Guiding Principles, QA/QC System, Staffing Plan, Shift Schedules, Subcontractors", 44, 51, "management-staffing", "staffing"),
     ("2.8 Culture, Training Plan, Certification, Career Development, Recruiting and Succession", 52, 57, "management-staffing", "staffing"),
     ("2.8 O&M Plans: Process Control, Data Management, Optimization, MBR Membrane Performance, UV", 58, 69, "technical-approach", "tech-approach"),
     ("2.8 Regulatory Compliance, EMS, Laboratory Management and Sampling Plan", 70, 75, "compliance-plans", "compliance"),
     ("2.8 Sludge/Biosolids Management, Emerging Contaminants, Odor and Noise Mitigation", 76, 80, "technical-approach", "tech-approach"),
     ("2.8 Asset Management and Maintenance, Condition Assessments, Equipment Performance Testing", 81, 90, "technical-approach", "tech-approach"),
     ("2.8 Safety Plan, Security Plan, Cybersecurity, Emergency Response and Disaster Preparedness", 91, 99, "compliance-plans", "compliance"),
     ("2.8 Customer Service Plan, Communications and Reporting, Innovation Workshop", 101, 108, "technical-approach", "tech-approach"),
     ("2.8 Public Education and Community Outreach Plan", 109, 114, "win-themes", "tech-approach"),
     ("2.9 Transition Plan and Exit Transition Plan", 115, 125, "technical-approach", "transition"),
     ("Section 3: Team Organization and Subcontractors", 127, 129, "management-staffing", "staffing"),
     ("Key Personnel Resumes 1", 130, 141, "resumes", "resume"),
     ("Key Personnel Resumes 2", 142, 153, "resumes", "resume"),
     ("Key Personnel Resumes 3", 154, 158, "resumes", "resume"),
     ("Section 3: Executive Sponsors, Additional Management, O&M and Consulting Resources", 159, 166, "qualifications", "staffing"),
     ("Section 4: Prior Experience, US Treatment Facility and Pump Station Portfolio", 168, 171, "past-performance", "past-performance"),
     ("Section 4: Reference Projects (Traverse City MI DBO, Spokane County DBO, Clovis CA Reuse)", 174, 179, "past-performance", "past-performance"),
     ("Section 5: Environmental Protection, Mitigation, and Compliance Record", 181, 182, "compliance-plans", "compliance"),
     ("Section 6: Availability of Key Staff and Plan for Commitment", 184, 184, "management-staffing", "staffing")]
R = [dict(slug="ocwut-16-26", name=n, pages=[a, b], category=c, rfpSectionType=t, clientNames=oc, context=octx, existingBlocks=[]) for n, a, b, c, t in O]
R += [dict(slug="fulton-county-2025", name=n, pages=[a, b], category=c, rfpSectionType=t, clientNames=fc, context=fctx, existingBlocks=[]) for n, a, b, c, t in F]
ADD = ("ADDITIONAL RULES FOR THIS RUN: (a) Fulton County proposal: the proposer is 'JC Solutions (a Jacobs/CERM JV)' - keep the JV voice; "
       "attribute capability to Jacobs and local presence/workforce development to CERM; never collapse to 'Jacobs'; add tag jv-structure and "
       "pursuit-type jv-delivery on such blocks. Generalize client facility names (Big Creek WRF, Johns Creek Environmental Campus/JCEC, Little River WRF) "
       "to [FACILITY A/B/C] with a descriptor on first use in narrative categories; 'the County' becomes [CLIENT] only where it means the pursuit client. "
       "(b) OCWUT: 'the City' often refers to OTHER cities in case studies - sanitize only the pursuit client (OCWUT, Oklahoma City Water Utilities Trust, "
       "City of Oklahoma City, Oklahoma City, OKC); keep 'Oklahoma' and 'ODEQ'. NexGen EAM consultant statements: keep verbatim, tag nexgen-eam, and write in "
       "reuse-notes 'approved-for-external-use: pending - sourced from a live pursuit'. Waterbury odor 55% figure: keep every wording and its stated time window "
       "exactly; do not harmonize. Keep Sludge Management, Solids Management and Operational Integration plans as three separate blocks. "
       "(c) Fulton pages 4-7 (RFP wayfinding crosswalk): create ONE block-type table block wiki/win-themes/rfp-wayfinding-crosswalk-pattern.md capturing the device "
       "(RFP criterion -> page) with the rows generalized; set house-favorite: true. "
       "(d) Allowed new facet values: geography 'Southcentral / OK / ODEQ' or 'Southeast / GA / GA EPD'; pursuit-type may include multi-facility, solids, "
       "mbr-membrane, jv-delivery; client-type trust (OCWUT) or county (Fulton).")
out = os.path.join(W, "work", "fragments", "ranges_ocwut_fulton.json")
json.dump({"wiki": W, "judgeModel": "sonnet", "pairJudgeModel": "opus", "builderAddendum": ADD, "ranges": R}, open(out, "w", encoding="utf-8"), indent=1)
print(len(R), "ranges;", sum(b - a + 1 for r in R for a, b in [r["pages"]]), "pages ->", out)
