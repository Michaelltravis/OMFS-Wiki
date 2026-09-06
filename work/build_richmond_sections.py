from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence
from zipfile import ZipFile

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


OUT_DIR = Path(r"C:\Users\micha\Desktop\Richmond\Draft Sections\01 Working Drafts")
LOGO = Path(r"C:\Users\micha\Desktop\Wiki\work\jacobs-logo-black.png")

BLUE_1 = "231EDC"
BLUE_2 = "0A7DFF"
NAVY = "001E55"
TEXT = "333333"
GRAY = "A5A5A5"
BORDER = "C8C8C8"
FILL = "E6E6E6"
WHITE = "FFFFFF"


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=80, start=70, bottom=80, end=70) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table, color=BORDER, size="8") -> None:
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = f"w:{edge}"
        node = borders.find(qn(tag))
        if node is None:
            node = OxmlElement(tag)
            borders.append(node)
        node.set(qn("w:val"), "single")
        node.set(qn("w:sz"), size)
        node.set(qn("w:space"), "0")
        node.set(qn("w:color"), color)


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_no_split(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tr_pr.append(OxmlElement("w:cantSplit"))


def set_repeat_header(paragraph) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    keep = OxmlElement("w:keepNext")
    p_pr.append(keep)


def add_field(run, instruction: str) -> None:
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for node in (begin, instr, separate, text, end):
        run._r.append(node)


def configure_styles(doc: Document) -> None:
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(12)
    normal.font.color.rgb = RGBColor.from_string(TEXT)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.08

    title = styles["Title"]
    title.font.name = "Arial"
    title.font.size = Pt(28)
    title.font.bold = True
    title.font.color.rgb = RGBColor(0, 0, 0)
    title.paragraph_format.space_after = Pt(10)

    for name, size in (("Heading 1", 18), ("Heading 2", 14), ("Heading 3", 12)):
        style = styles[name]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = Pt(12 if name == "Heading 1" else 8)
        style.paragraph_format.space_after = Pt(4)

    for name, size, color, bold in (
        ("Standing Head", 9, BLUE_1, True),
        ("Deck", 15, TEXT, False),
        ("Source Note", 12, GRAY, False),
        ("Placeholder", 12, NAVY, True),
        ("Table Text", 12, TEXT, False),
    ):
        if name not in styles:
            style = styles.add_style(name, 1)
        else:
            style = styles[name]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.bold = bold
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.space_after = Pt(3)
        style.paragraph_format.line_spacing = 1.0


def add_header_footer(doc: Document, section_name: str) -> None:
    for section in doc.sections:
        section.top_margin = Inches(0.78)
        section.bottom_margin = Inches(0.72)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)
        section.header_distance = Inches(0.25)
        section.footer_distance = Inches(0.25)

        header = section.header
        table = header.add_table(rows=1, cols=2, width=Inches(6.8))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        table.columns[0].width = Inches(1.35)
        table.columns[1].width = Inches(5.45)
        c1, c2 = table.rows[0].cells
        c1.width = Inches(1.35)
        c2.width = Inches(5.45)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if LOGO.exists():
            logo = p1.add_run().add_picture(str(LOGO), width=Inches(0.95))
            logo._inline.docPr.set("title", "Jacobs")
            logo._inline.docPr.set("descr", "Jacobs logo")
        else:
            r = p1.add_run("JACOBS")
            r.bold = True
            r.font.size = Pt(11)
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p2.add_run(f"City of Richmond Wastewater O&M | {section_name}")
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor.from_string(TEXT)
        for cell in (c1, c2):
            set_cell_margins(cell, top=0, start=0, bottom=30, end=0)
        set_table_borders(table, color=WHITE, size="0")

        footer = section.footer
        ft = footer.add_table(rows=1, cols=3, width=Inches(6.8))
        ft.alignment = WD_TABLE_ALIGNMENT.CENTER
        ft.autofit = False
        widths = [2.4, 1.8, 2.6]
        vals = [section_name, "Draft for Review", "Jacobs Confidential | Page "]
        aligns = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.RIGHT]
        for i, cell in enumerate(ft.rows[0].cells):
            cell.width = Inches(widths[i])
            p = cell.paragraphs[0]
            p.alignment = aligns[i]
            r = p.add_run(vals[i])
            r.font.name = "Arial"
            r.font.size = Pt(8)
            r.font.color.rgb = RGBColor.from_string(GRAY)
            if i == 2:
                add_field(p.add_run(), "PAGE")
            set_cell_margins(cell, top=20, start=0, bottom=0, end=0)
        set_table_borders(ft, color=WHITE, size="0")


def new_doc(section_label: str, title: str, deck: str) -> Document:
    doc = Document()
    configure_styles(doc)
    add_header_footer(doc, title)
    p = doc.add_paragraph(style="Standing Head")
    p.add_run(section_label.upper())
    p.paragraph_format.space_after = Pt(4)
    doc.add_paragraph(title, style="Title")
    p = doc.add_paragraph(deck, style="Deck")
    p.paragraph_format.space_after = Pt(14)
    return doc


def p(doc: Document, text: str, *, bold_lead: str | None = None, style: str | None = None) -> None:
    para = doc.add_paragraph(style=style)
    if bold_lead:
        para.add_run(bold_lead).bold = True
        para.add_run(text)
    else:
        para.add_run(text)


def bullet(doc: Document, text: str, level: int = 0) -> None:
    style = "List Bullet" if level == 0 else "List Bullet 2"
    para = doc.add_paragraph(style=style)
    para.add_run(text)
    para.paragraph_format.space_after = Pt(2)


def numbered(doc: Document, text: str) -> None:
    para = doc.add_paragraph(style="List Number")
    para.add_run(text)
    para.paragraph_format.space_after = Pt(3)


def source_note(doc: Document, report: str, locator: str, evidence_type: str | None = None) -> None:
    para = doc.add_paragraph(style="Source Note")
    para.add_run(f"Source: Due Diligence Trip Report – {report}, {locator}.")
    if evidence_type:
        para.add_run(f" Evidence type: {evidence_type}.")


def add_table(doc: Document, headers: Sequence[str], rows: Sequence[Sequence[str]], widths: Sequence[float] | None = None) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    hdr = table.rows[0]
    set_repeat_table_header(hdr)
    set_no_split(hdr)
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        set_cell_shading(cell, NAVY)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = para.add_run(h)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor.from_string(WHITE)
        set_cell_margins(cell)
    for ri, row in enumerate(rows):
        table_row = table.add_row()
        set_no_split(table_row)
        cells = table_row.cells
        if ri % 2:
            for cell in cells:
                set_cell_shading(cell, "F6F8FC")
        for i, value in enumerate(row):
            cell = cells[i]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            para = cell.paragraphs[0]
            para.style = doc.styles["Table Text"]
            para.add_run(str(value))
            set_cell_margins(cell)
    if widths:
        for row in table.rows:
            for i, width in enumerate(widths):
                row.cells[i].width = Inches(width)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_requirement_block(doc: Document, text: str, source: str) -> None:
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    left, right = table.rows[0].cells
    left.width = Inches(1.4)
    right.width = Inches(5.4)
    set_cell_shading(left, BLUE_1)
    set_cell_shading(right, "F4F4F4")
    r = left.paragraphs[0].add_run("RFP\nREQUIREMENT")
    r.bold = True
    r.font.color.rgb = RGBColor.from_string(WHITE)
    r.font.size = Pt(12)
    right.paragraphs[0].add_run(text)
    p2 = right.add_paragraph(source)
    p2.style = doc.styles["Source Note"]
    for cell in (left, right):
        set_cell_margins(cell, top=140, bottom=140)
    set_no_split(table.rows[0])
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_sources_and_decisions(doc: Document, sources: Sequence[str], decisions: Sequence[str]) -> None:
    doc.add_paragraph("Draft Source and Decision Register", style="Heading 1")
    p(doc, "This register supports proposal-team review and should be removed or converted to production notes before issue.")
    doc.add_paragraph("Sources used", style="Heading 2")
    for item in sources:
        bullet(doc, item)
    doc.add_paragraph("Unresolved decisions and placeholders", style="Heading 2")
    for item in decisions:
        bullet(doc, item)


def build_cover_letter() -> Document:
    doc = new_doc("Section 8.4.1", "Cover Letter", "A reliable transition and accountable operating partnership for Richmond's wastewater systems")
    p(doc, "[CONFIRM DATE]", style="Placeholder")
    p(doc, "City of Richmond\nPublic Works Department\n[CONFIRM RECIPIENT ADDRESS]\nRichmond, California")
    p(doc, "Subject: Operation, Maintenance, and Management of the Wastewater Treatment Plant and Collection Systems", bold_lead="")
    p(doc, "Dear Members of the Evaluation Committee:")
    p(doc, "Richmond's wastewater utility supports public health, quality of life, environmental stewardship, and the City's wider economic goals. Jacobs understands that this contract must integrate a conventional activated-sludge treatment plant, 192 miles of wastewater collection system, 187 miles of stormwater system, and the associated pump stations, permits, settlement obligations, and community-facing responsibilities. We intend to perform the services described in the RFP and to begin with a controlled transition that protects continuity from the first day of operations.")
    p(doc, "Internal wiki source content states that Jacobs brings more than four decades of contract O&M experience and has served California public utilities since the 1980s. Section 8.4.3 develops the candidate corporate record and project examples; every history, scale, and performance statement remains subject to current corporate validation before issue.")
    p(doc, "The City's objectives call for accountable leadership, reliable regulatory performance, transparent data and financial reporting, disciplined asset management, and innovations that reduce lifecycle cost and ratepayer burden. Our proposed operating model places one accountable Project Manager at the center of delivery, pairs that leader with a dedicated Collection System Manager, and connects the on-site team to regional specialists in compliance, maintenance, safety, process optimization, asset management, and operational technology.")
    p(doc, "The site visit reinforced the value of an early focus on operational discipline, workforce depth, maintenance prioritization, field safety, and systems documentation. We will convert those findings into verified transition actions, with the City retaining clear visibility into decisions, priorities, costs, and progress.")
    source_note(doc, "Kelly Irving, General/Strategy/Estimating", "2. Overall Observations (Your Focus Area); 4. Notable Opportunities", "Recommendation")
    source_note(doc, "Ryan Larson, Maintenance", "2. Overall Observations (Your Focus Area) - facility condition and housekeeping", "Observed condition")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "6. Strategic Risks Requiring Attention", "Open question/data gap")
    doc.add_paragraph("Our proposal is organized around four commitments", style="Heading 2")
    bullet(doc, "Protect compliance through permit-by-permit controls, qualified coverage, and auditable reporting.")
    bullet(doc, "Improve reliability through prioritized maintenance, accurate asset data, and transparent M&R accounting.")
    bullet(doc, "Strengthen service through an accountable on-site team backed by regional technical and surge resources.")
    bullet(doc, "Pursue measurable improvements in energy, chemicals, odor, cybersecurity, and capital planning with City approval.")
    p(doc, "Draft final statement, subject to authorized review: Jacobs confirms that it has reviewed and understands the elements of the RFP, subject to all subsequently issued addenda. Any statement concerning acceptance of the RFP terms and conditions, insurance requirements, and Service Agreement remains subject to legal, risk, insurance, and bonding review. [CONFIRM FINAL LEGAL LANGUAGE AFTER REVIEW OF THE ADDENDUM-ISSUED DRAFT AGREEMENT]")
    p(doc, "Jacobs' proposal price will remain valid for at least 180 days from the proposal due date. [CONFIRM WITH COMMERCIAL LEAD]")
    p(doc, "The Jacobs office nearest Richmond is [CONFIRM OFFICE ADDRESS AND TELEPHONE]. The project will be managed from [CONFIRM MANAGING OFFICE]. The single point of contact for the RFP review process will be [CONFIRM NAME, TITLE, TELEPHONE, AND EMAIL].")
    p(doc, "Communication disclosure: [CONFIRM WHETHER ANY REPORTABLE COMMUNICATION OCCURRED SINCE THE RFP RELEASE DATE. IF YES, INSERT THE CITY REPRESENTATIVE, DATE, METHOD, AND GENERAL SUBJECT.]")
    p(doc, "Draft agreement review: [CONFIRM THAT THE ADDENDUM-ISSUED DRAFT AGREEMENT HAS BEEN REVIEWED AND INSERT ANY APPROVED QUALIFICATION LANGUAGE.]")
    p(doc, "We appreciate the opportunity to present this approach and look forward to discussing how Jacobs can help Richmond achieve reliable, transparent, and progressively stronger performance across its wastewater systems.")
    p(doc, "Sincerely,")
    p(doc, "[AUTHORIZED COMPANY OFFICIAL]\n[TITLE]\n[DIRECT TELEPHONE]\n[EMAIL]", style="Placeholder")
    p(doc, "I am authorized to represent the Proposer and attest, following final review and approval, to the accuracy of this proposal. [CONFIRM AUTHORIZED SIGNATORY AND FINAL ATTESTATION LANGUAGE]")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 1.2-1.3, 4, 8.4.1, and 10, pp. 7, 10-22, 29, and 38.",
            "Richmond Proposal Directive, Section 8.4.1 outline.",
            "Richmond Compliance Matrix and Scope Register, including controls C-014, C-016, C-040 through C-045, C-076, and S-015.",
            "Wiki: Cover Letter Structure Pattern; Executive Summary Client Readiness Framing; Firm History; California O&M Track Record.",
            "Due Diligence Trip Reports by Kelly Irving, Ryan Larson, and Iouri Ossokine, cited above.",
        ],
        [
            "Confirm authorized signatory and proposal point of contact.",
            "Confirm nearest office, managing office, addresses, and telephone numbers.",
            "Complete legal, insurance, bonding, communication-disclosure, and draft-agreement reviews.",
            "Confirm all addenda before making the final RFP-review statement.",
            "Confirm the questions deadline and all schedule dates against issued addenda before production.",
        ],
    )
    return doc


def build_exec_summary() -> Document:
    doc = new_doc("Section 8.4.2", "Executive Summary", "Positioning Richmond's wastewater systems for reliable compliance, transparent stewardship, and measurable improvement")
    add_requirement_block(doc, "Provide an overview of the proposal and value proposition reflecting the goals and objectives stated in the RFP.", "RFP Section 8.4.2, p. 29")
    p(doc, "Richmond is seeking an operating partner that can protect compliance while strengthening the systems, practices, and relationships behind reliable service. The opportunity spans a 16-MGD conventional activated-sludge plant with a 40-MGD primary-treatment rating, a 192-mile wastewater collection system, a separate 187-mile stormwater system, and a complex portfolio of pump stations, force mains, channels, outfalls, and trash-capture assets. The work also carries specific Baykeeper, stormwater, emergency-response, cybersecurity, reporting, and maintenance obligations.")
    add_table(
        doc,
        ["Operating context", "Richmond baseline", "What it requires", "Benefit to the City"],
        [
            ("Wastewater treatment", "6.50 MGD base-fee influent; 40 MGD primary-treatment rating", "Stable process control, wet-weather readiness, odor management", "Reliable treatment and defensible permit performance"),
            ("Wastewater collection", "192 gravity miles; 4 force-main miles; 16 pump stations", "Risk-based cleaning, CCTV, pump-station reliability, Baykeeper controls", "Fewer avoidable failures and transparent rehabilitation priorities"),
            ("Stormwater", "187 pipe miles; 22 channel miles; 7 pump stations; specialized trash assets", "Defined work planning, safe access, cleaning documentation, CDO support", "Visible progress toward stormwater compliance"),
            ("Asset stewardship", "$2 million first-year M&R fund", "Prioritized maintenance and complete monthly accounting", "Better decisions and improved budget predictability"),
        ],
        [1.25, 1.45, 2.15, 1.95],
    )
    doc.add_paragraph("Our value proposition", style="Heading 1")
    p(doc, "Jacobs will organize delivery around one accountable on-site leader, a dedicated collection and stormwater leader, disciplined management systems, and a regional bench that can address specialized needs without burdening the base team with every discipline. This structure is intended to give Richmond stable daily execution and access to deeper expertise when conditions, projects, or emergencies demand it.")
    add_table(
        doc,
        ["Commitment", "How Jacobs will deliver", "Expected outcome", "Benefit to the City"],
        [
            ("No compliance surprises", "Permit-by-permit responsibility matrix, due-date controls, QA/QC, and escalation", "Complete, timely, reviewable reporting", "Reduced regulatory and liquidated-damage exposure"),
            ("One accountable operating team", "Defined authority from Project Manager through plant, collection, stormwater, and support leads", "Clear ownership and faster decisions", "Consistent service across all Facilities"),
            ("Transparent asset and cost management", "NexGen/GIS/SewerAI integration, verified asset records, work-order discipline, and M&R reporting", "A common view of condition, risk, work, and cost", "Defensible maintenance and capital priorities"),
            ("Measured improvement", "Baseline performance, prioritize opportunities, pilot with City approval, and report results", "Documented gains in reliability, energy, chemicals, odor, and productivity", "Lower lifecycle cost and ratepayer burden"),
        ],
        [1.3, 2.25, 1.75, 1.5],
    )
    doc.add_paragraph("Due diligence translated into action", style="Heading 1")
    p(doc, "The site-visit reports identify conditions and questions that should be verified during transition rather than accepted as final engineering conclusions. They consistently point to five early priorities: establish accountable collection-system leadership, verify maintenance and safety conditions, baseline stormwater quantities and access constraints, document SCADA/OT ownership and cybersecurity boundaries, and reconcile inherited work with the M&R and base-fee structure.")
    add_table(
        doc,
        ["Evidence type", "Due-diligence finding", "Source", "Proposed response", "Benefit to the City"],
        [
            ("Observed condition", "Housekeeping, corrosion, temporary repairs, and inventory-control issues were observed.", "Larson - Overall Observations", "Launch a Day 1 housekeeping and safety reset, then risk-rank backlog and coatings needs.", "Safer work areas and clearer asset priorities"),
            ("Reported condition", "Collections responsibilities and recurring hot spots may create substantial annual workload.", "Buonadonna - Sanitary sewer collections", "Validate hot-spot criteria, asset access, cleaning history, and responsibility boundaries.", "A defendable annual work plan and fewer scope disputes"),
            ("Open question/data gap", "Stormwater debris quantities and special-asset requirements are not fully baselined.", "Buonadonna - Stormwater collections", "Confirm quantities, methods, access, disposal, and 'as needed' expectations before final pricing.", "Realistic staffing and cost assumptions"),
            ("Observed condition", "Safety concerns included inconsistent LOTO practices, trip hazards, roadway exposure, and off-site security.", "Cain - HSE observations", "Complete a transition safety gap assessment and implement site-specific controls and training.", "Reduced risk to employees and the public"),
            ("Open question/data gap", "SCADA network roles, remote access, ownership, and end-of-life components require validation.", "Ossokine - Documentation and Unknowns", "Perform an OT/SCADA inventory, access review, account transfer, and modernization roadmap.", "Improved continuity and cybersecurity governance"),
        ],
        [1.05, 1.55, 1.2, 1.85, 1.2],
    )
    source_note(doc, "Ryan Larson, Maintenance", "2. Overall Observations (Your Focus Area)", "Observed condition")
    source_note(doc, "Daniel Buonadonna, Collections System", "2. Overall Observations (Your Focus Area) - sanitary sewer collections", "Reported condition")
    source_note(doc, "Daniel Buonadonna, Collections System", "5. Items to Consider for Pricing / Cost Model - stormwater quantities and special assets", "Open question/data gap")
    source_note(doc, "Trey Cain, HSE", "2. Overall Observations (Your Focus Area)", "Observed condition")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "5. Documentation & Unknowns", "Open question/data gap")
    doc.add_paragraph("A controlled transition to Day 1", style="Heading 1")
    p(doc, "The current contract ends May 15, 2027. Jacobs will begin transition immediately after notice, confirm governance and decision rights, validate regulatory calendars and system access, engage the incumbent workforce, inventory critical assets and spares, test alarms and emergency communications, and verify the systems used for City and regulatory reporting. A 30-day-prior site-specific Transition Plan will convert those activities into a jointly managed readiness schedule.")
    p(doc, "Our first 120 days will move deliberately from continuity to control and then to improvement. Required deliverables will be tracked against the RFP deadlines, including the 90-day condition assessment, 120-day asset-management and data systems, odor-control and safety plans, and annual capital-planning requirements. The City will receive a visible action register showing the issue, owner, due date, status, decision required, and supporting record.")
    doc.add_paragraph("A partnership built around Richmond's decisions", style="Heading 1")
    p(doc, "Richmond will retain policy, enforcement, and capital decision authority. Jacobs will provide the operating evidence needed to make those decisions: accurate data, timely analysis, clear alternatives, cost and risk implications, and transparent follow-through. We will use the same discipline for maintenance, energy, chemicals, collection and stormwater work, cybersecurity, and innovations so that improvement proposals can be evaluated on measurable client value.")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 1.2-1.3, 3-5, 8.4.2, and 9.3; Attachments A, B, and E.",
            "Richmond Proposal Directive, Section 8.4.2 outline.",
            "Richmond Compliance Matrix and Scope Register, including controls C-046, S-003, S-004, and S-073.",
            "Wiki: Executive Summary Client Readiness Framing; Project Understanding Goals/Challenges/Response Matrix; O&M Management Systems Framework.",
            "Due Diligence Trip Reports by Ryan Larson, Daniel Buonadonna, Trey Cain, and Iouri Ossokine, cited above.",
        ],
        [
            "Confirm approved win themes and final value proposition.",
            "Confirm proposed Project Manager, Collection System Manager, and executive sponsor.",
            "Validate due-diligence observations against available photos, asset records, and City responses before issue.",
            "Confirm which innovations are included in base fee, optional, or subject to separate authorization.",
        ],
    )
    return doc


def build_qualifications() -> Document:
    doc = new_doc("Section 8.4.3", "Firm Qualifications and Demonstrated Experience", "A financially capable O&M organization with California experience and an integrated technical support network")
    add_requirement_block(doc, "Provide corporate and legal qualifications, financial qualifications, five comparable references, corporate experience, safety and environmental performance, permit-compliance approach, and litigation disclosure.", "RFP Section 8.4.3, pp. 29-31")
    doc.add_paragraph("Requirements response", style="Heading 1")
    add_table(
        doc,
        ["RFP requirement", "Draft response", "Evidence or approval needed", "Benefit to the City"],
        [
            ("Corporate and legal profile", "Internal wiki identifies OMI as the candidate contracting entity; confirmation is required.", "Confirm entity, tax ID, addresses, authority, and California standing.", "A clearly accountable contracting party"),
            ("Financial capacity", "Jacobs offers the resources of a large, diversified infrastructure company.", "Current financial statements, revenue, insurance, and surety letter.", "Long-term performance confidence"),
            ("O&M tenure", "[CONFIRM 10 OR MORE YEARS PROVIDING WASTEWATER-TREATMENT O&M SERVICES]", "Approved corporate history and project chronology.", "Verification of required operating tenure"),
            ("California experience", "[INSERT VERIFIED CALIFORNIA REGULATORY AND WASTEWATER-UTILITY O&M EXPERIENCE]", "Approved California project evidence.", "Relevant state operating experience"),
            ("Minimum treatment experience", "[CONFIRM EXPERIENCE OPERATING AT LEAST FIVE ACTIVATED-SLUDGE WWTPS OF 10 MGD OR GREATER]", "Validated project list with dates, capacity, and operating role.", "Direct evidence of required treatment capability"),
            ("Minimum collection experience", "[CONFIRM MANAGEMENT OF AT LEAST FIVE COLLECTION SYSTEMS OF 50 MILES OR GREATER]", "Validated project list with dates, mileage, and operating role.", "Direct evidence of required collection capability"),
            ("Stormwater experience", "[INSERT VERIFIED STORMWATER O&M EXPERIENCE AND REFERENCES]", "Approved project evidence defining facilities and responsibilities.", "Relevant experience for Richmond's separate stormwater system"),
            ("Annual O&M revenue", "[CONFIRM ANNUAL O&M REVENUE EXCEEDS $50 MILLION]", "Approved current financial evidence.", "Verification of minimum financial qualification"),
            ("Five references", "Five candidate O&M references are provided for validation.", "Account-team confirmation of contacts, fees, scope, and permission.", "Comparable performance that the City can verify"),
            ("Safety and environmental record", "Jacobs uses enterprise safety and compliance management systems.", "Current TRIR, EMR, and five-year violation disclosure.", "Transparent assessment of delivery risk"),
            ("Permit compliance", "A permit-by-permit control system links obligations, owners, dates, reviews, and records.", "Richmond permit and settlement responsibility matrix.", "Consistent and auditable compliance"),
        ],
        [1.35, 2.0, 2.15, 1.3],
    )
    doc.add_paragraph("Corporate profile and legal qualifications", style="Heading 1")
    p(doc, "Internal wiki source content describes Jacobs as an integrated infrastructure and operations organization with more than four decades of contract O&M experience and California public-utility operations dating to the 1980s. These statements, all current corporate counts, revenue, backlog, and California portfolio facts must be validated through approved corporate evidence before issue. [VERIFY ALL CURRENT CORPORATE FACTS]")
    p(doc, "The internal wiki identifies Operations Management International, Inc. (OMI), a wholly owned Jacobs company, as the candidate contracting party. [CONFIRM LEGAL ENTITY AND RELATIONSHIP] The project organization will connect Richmond's on-site Project Manager to California O&M leadership and the wider Jacobs organization, creating direct lines of authority for daily delivery, technical escalation, and executive oversight.")
    add_table(
        doc,
        ["Required entity information", "Draft entry", "Verification owner", "Benefit to the City"],
        [
            ("Full legal name", "[CONFIRM CONTRACTING ENTITY]", "Legal / Contracts", "Correct and enforceable agreement"),
            ("Federal tax ID", "[CONFIRM TAX IDENTIFICATION NUMBER]", "Finance / Legal", "Accurate vendor records"),
            ("Principal office", "[CONFIRM ADDRESS AND TELEPHONE]", "Corporate Qualifications", "Clear corporate contact"),
            ("Principal contact", "[CONFIRM NAME, TITLE, TELEPHONE, EMAIL]", "Proposal Manager", "Single accountable interface"),
            ("Authorized negotiator and signatory", "[CONFIRM NAMES AND TITLES]", "Legal / Executive Sponsor", "Binding authority is clear"),
            ("Formation and years of service", "[CONFIRM INCORPORATION DATE, STATE, AND YEARS UNDER NAME]", "Corporate Secretary", "Verified operating history"),
            ("Legal standing", "[INSERT APPROVED CALIFORNIA AND HOME-STATE STATEMENT]", "Legal", "Transparent eligibility evidence"),
        ],
        [1.55, 2.15, 1.35, 1.75],
    )
    doc.add_paragraph("Financial qualifications", style="Heading 1")
    p(doc, "Jacobs' financial capacity is intended to provide Richmond with continuity over the initial 10-year term, access to corporate resources, and the ability to support insurance and bonding requirements. Final submission materials will include the company's approved financial statements and a notarized statement from the surety company confirming capacity for performance and payment bonds equal to 100 percent of the Annual Fee. [CONFIRM CURRENT FINANCIAL FIGURES, INSURANCE, AND BONDING CAPACITY]")
    bullet(doc, "Final corporate financial statements demonstrating financial health and O&M revenue.")
    bullet(doc, "Notarized statement issued by the surety company, not an agent or broker.")
    bullet(doc, "Evidence of the required insurance capacity after review of the draft Service Agreement.")
    bullet(doc, "Approved explanation of the relationship between Jacobs Solutions Inc. and the contracting entity.")
    doc.add_paragraph("Five candidate project references", style="Heading 1")
    p(doc, "The following projects are candidate references drawn from the internal proposal wiki. They demonstrate relevant combinations of activated-sludge treatment, large collection systems, transition, compliance recovery, asset management, process optimization, and regional support. Every contact, fee, term, and performance claim must be reconfirmed before issue.")
    add_table(
        doc,
        ["Candidate reference", "Comparable scope", "Years / annual fee", "Verification status", "Benefit to the City"],
        [
            ("Waterbury Wastewater System | Waterbury, CT", "27-MGD activated-sludge WWTP; about 310 collection miles; 20 pump stations; CMOM and capital support", "[VERIFY] 2018-present | $6M", "Confirm client contact, fee, facts, and permission", "Evidence at treatment and collection scale"),
            ("South Huron WWTP | Rockwood, MI", "24-MGD activated-sludge system; collection/interceptor assets; 24/7 O&M, lab, compliance, and biosolids", "[VERIFY] 2019-present | $5.3M", "Resolve source discrepancy; confirm contact, fee, facts, and permission", "Transition and integrated plant/collection delivery"),
            ("Southbridge WWTP | Southbridge, MA", "3.77-MGD WWTP; 48 collection miles; 11 lift stations; recent incumbent transition, odor and CCTV improvements", "[VERIFY] 2025-present | $1.7M", "Confirm client contact, fee, facts, and permission", "Recent contract transition proof"),
            ("Traverse City Regional WWTP | Traverse City, MI", "8.5-MGD regional system; pump stations; CMMS, compliance recovery, energy optimization", "[VERIFY] 1990-present | $3.5M", "Confirm client contact, fee, facts, and permission", "Long-term partnership and optimization"),
            ("Westerly WWTP | Westerly, RI", "3.3-MGD WWTP; nine pump stations; IPP, maintenance backlog reduction, energy and biosolids optimization", "[VERIFY] 2017-present | $2.4M", "Confirm client contact, fee, facts, and permission", "Maintenance turnaround and cost control"),
        ],
        [1.45, 2.05, 1.1, 1.45, 1.2],
    )
    p(doc, "Reference contact details will be inserted after account-team approval. [CONFIRM WHETHER THESE FIVE PROJECTS PROVIDE THE STRONGEST RESPONSE TO THE RFP'S TARGETED QUALIFICATIONS; SUBSTITUTE CALIFORNIA OR STORMWATER REFERENCES IF AVAILABLE]")
    doc.add_paragraph("Corporate experience and technical depth", style="Heading 1")
    p(doc, "Jacobs' O&M model combines on-site accountability with resources drawn from internal operations, engineering, digital, environmental, and capital-program practices. Richmond's on-site team will remain responsible for delivery; regional specialists will support defined assignments such as treatment troubleshooting, Baykeeper and stormwater compliance, condition assessment, reliability, SCADA/OT, energy, odor, biosolids, and capital planning. The fee proposal will distinguish services included in the base fee from separately authorized or reimbursable support.")
    p(doc, "The due-diligence reports reinforce the need for this integrated model. They identify collection and stormwater complexity, questions about specialized assets and inherited condition, the need for maintenance and safety support, and gaps in SCADA/OT documentation and ownership. These observations are used here to define required organizational capabilities, not to make final condition or cost conclusions.")
    source_note(doc, "Daniel Buonadonna, Collections System", "1. Pre-Visit Due Diligence Summary; 3. Notable Risks and Challenges", "Reported condition")
    source_note(doc, "Ryan Larson, Maintenance", "2. Overall Observations (Your Focus Area); 7. Additional Notes / Observations", "Observed condition")
    source_note(doc, "Trey Cain, HSE", "2. Overall Observations (Your Focus Area)", "Observed condition")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "6. Strategic Risks Requiring Attention", "Open question/data gap")
    doc.add_paragraph("Health, safety, and environmental record", style="Heading 1")
    p(doc, "Jacobs will provide its approved current Total Recordable Incident Rate, Experience Modification Rate, and five-year health, safety, and environmental violations disclosure. The project approach applies enterprise safety expectations through site-specific planning, supervisor engagement, task planning, training, audits, and corrective-action tracking. [INSERT CURRENT, APPROVED CORPORATE METRICS AND DISCLOSURES]")
    doc.add_paragraph("Meeting and guaranteeing permit compliance", style="Heading 1")
    p(doc, "Jacobs will translate every applicable permit, order, settlement requirement, and contract standard into a controlled obligation register. Each item will identify the responsible role, due date, data source, review and approval path, evidence record, and escalation threshold. The project manager remains accountable for execution, with compliance specialists providing independent checks and the City retaining review authority where the RFP requires it.")
    numbered(doc, "Confirm applicability and responsibility for every permit, order, and settlement provision.")
    numbered(doc, "Build the regulatory calendar and assign primary and backup owners.")
    numbered(doc, "Validate sampling, laboratory, data, and reporting workflows before operational responsibility begins.")
    numbered(doc, "Use documented QA/QC reviews and exception escalation before submittal.")
    numbered(doc, "Report compliance status, near exceedances, corrective actions, and Baykeeper activities to the City.")
    doc.add_paragraph("Litigation and contract termination", style="Heading 1")
    p(doc, "[LEGAL REVIEW REQUIRED] Insert the approved disclosure addressing litigation or termination for cause involving owners of prior projects during the preceding 10 years. Do not use donor-pursuit language or general SEC disclosure language as a substitute for the specific RFP response.", style="Placeholder")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 2, 7.8, 8.4.3, and 9.3, pp. 8, 26, and 29-36.",
            "Richmond Proposal Directive, Section 8.4.3 outline.",
            "Richmond Compliance Matrix and Scope Register, including controls C-001 through C-001.6, C-026, C-044, C-047 through C-052, C-056, S-001, and S-015.",
            "Wiki qualifications sources: Firm History; California O&M Track Record; Corporate Entity and Legal Qualifications; Financial Strength; Reach-Back Model.",
            "Wiki past-performance sources: Client References and candidate project narratives for Waterbury, South Huron, Southbridge, Traverse City, and Westerly.",
            "Due Diligence Trip Reports by Daniel Buonadonna, Ryan Larson, Trey Cain, and Iouri Ossokine, cited above.",
        ],
        [
            "Confirm contracting entity and every corporate/legal fact.",
            "Obtain approved financial statements, surety letter, insurance statement, current safety metrics, and five-year violation history.",
            "Select and validate five final references, including current contacts, annual fees, and permission to use.",
            "Obtain legal-approved 10-year litigation and termination disclosure.",
            "Confirm which technical support is included in base fee versus separately authorized.",
        ],
    )
    return doc


def build_staffing() -> Document:
    doc = new_doc("Section 8.4.4", "Project Staffing and Management Plan", "One accountable on-site team supported by specialized regional resources and reliable backup coverage")
    add_requirement_block(doc, "Provide the staffing and management plan, organization chart, named Project Manager and Collection System Manager, responsibility and authority, qualifications, support team, transition, subcontractors, and backup resources.", "RFP Section 8.4.4, pp. 31-32")
    doc.add_paragraph("Staffing strategy", style="Heading 1")
    p(doc, "Richmond requires continuous full-service O&M and monitoring across the treatment plant, wastewater collection system, and stormwater system. Jacobs will use a blended structure: a clearly accountable on-site organization for daily delivery; shared or off-site specialists for defined technical needs; and surge resources for vacancies, leave, unusual operating conditions, and emergencies. Final staffing quantities and shifts will be inserted after operations and estimating approve the labor model.")
    add_table(
        doc,
        ["Tier", "Primary responsibility", "Proposed roles", "Availability", "Benefit to the City"],
        [
            ("City governance", "Policy, priorities, approvals, and oversight", "Public Works Director / City representatives", "Defined governance cadence", "City authority remains clear"),
            ("On-site leadership", "Accountability for all Facilities and City coordination", "[PROJECT MANAGER]; [COLLECTION SYSTEM MANAGER]", "Full-time on site; Project Manager/designee reachable at all times", "One clear operating interface"),
            ("On-site delivery", "Plant, collections, stormwater, maintenance, lab, compliance, safety, and administration", "[CONFIRM ROLES, FTEs, SHIFTS, AND CERTIFICATIONS]", "24/7 operating and emergency coverage model", "Reliable daily service"),
            ("Regional support", "Specialized troubleshooting, audits, planning, and surge", "Process, maintenance, safety, compliance, OT/SCADA, asset, energy, odor, and capital specialists", "Planned assignments plus escalation response", "Depth without overloading the base team"),
            ("Specialty firms", "Specialty work outside approved self-perform boundaries", "[CONFIRM FIRMS AND SCOPES]", "Per approved subcontracting plan", "Specialized capacity with clear oversight"),
        ],
        [1.2, 1.55, 1.65, 1.25, 1.15],
    )
    doc.add_paragraph("Proposed organization and lines of authority", style="Heading 1")
    add_table(
        doc,
        ["Accountable role", "Direct reports / interfaces", "Decision authority", "Required confirmation", "Benefit to the City"],
        [
            ("Project Manager", "Plant leads, Collection System Manager, maintenance, compliance/lab, administration; City primary contact", "Daily execution, staffing deployment, issue escalation, emergency coordination", "Name, residence/proximity, experience, education, certifications", "Single accountable lead"),
            ("Collection System Manager", "Wastewater and stormwater crews, pump-station work, CCTV/cleaning, subcontractors", "Field work planning, permit/settlement execution, response and documentation", "Name, collection/storm experience, certifications, availability", "Focused leadership for the highest-complexity field scope"),
            ("Plant operations lead", "Shift operators and process-control activities", "Treatment strategy within permits and approved procedures", "Role, name, certification grade, shift", "Stable process performance"),
            ("Maintenance lead", "Mechanical, electrical, instrumentation, inventory, and work planning", "Work-order prioritization and M&R recommendations", "Role, name, qualifications, self-perform limits", "Improved reliability and cost visibility"),
            ("Compliance and laboratory lead", "Sampling, QA/QC, reporting, permits, Baykeeper/CDO support", "Regulatory calendar and review controls", "Role, name, certification and reporting responsibilities", "Timely, accurate, auditable reporting"),
            ("Regional Operations Manager", "Project Manager coaching, corporate escalation, surge coordination", "Resource deployment and independent operating review", "Name, location, commitment percentage", "Fast access to backup and senior judgment"),
        ],
        [1.15, 1.85, 1.55, 1.35, 1.1],
    )
    doc.add_paragraph("Due-diligence-informed staffing priorities", style="Heading 1")
    p(doc, "The trip reports consistently identify collection-system leadership, safety, maintenance capacity, and OT/SCADA support as material staffing considerations. These findings guide the proposed role architecture; they do not establish final headcount, named assignments, or commercial inclusions.")
    add_table(
        doc,
        ["Evidence type", "Finding", "Source", "Staffing response", "Benefit to the City"],
        [
            ("Recommendation", "A highly capable Collection System Manager should lead sanitary and stormwater work with regional support.", "Gorka - Staffing / Staffing Support", "Name a dedicated leader with defined authority and provide collections, compliance, and wet-weather reach-back.", "Accountability across two complex field systems"),
            ("Reported condition", "Sanitary and stormwater crews currently share resources; specialty assets may require unconventional methods.", "Buonadonna - Overall Observations", "Separate planning ownership while coordinating shared crews, equipment, and specialty subcontractors.", "More realistic work planning"),
            ("Observed condition", "Deferred maintenance, temporary repairs, corrosion, and inventory gaps may exceed steady-state workload.", "Larson - Overall Observations", "Provide a maintenance lead plus separately controlled regional backlog and condition-assessment support.", "Faster stabilization without hiding transition cost"),
            ("Observed condition", "Field safety risks include roadway work, off-site security, LOTO, trip hazards, and confined-space controls.", "Cain - HSE observations", "Assign site HSE accountability, two-person/off-site protocols where warranted, and specialist safety support.", "Reduced employee and public exposure"),
            ("Recommendation", "An on-site SCADA/electrical capability was recommended for rapid troubleshooting and OT support.", "Ossokine - Additional Notes", "Evaluate a dedicated or shared on-site SCADA/electrical role and define Calcon/subcontractor interfaces.", "Improved system continuity and response"),
        ],
        [1.25, 1.55, 1.2, 1.7, 1.1],
    )
    source_note(doc, "Daniel Gorka, Estimator", "2. Overall Observations (Your Focus Area) - Staffing / Staffing Support", "Recommendation")
    source_note(doc, "Daniel Buonadonna, Collections System", "2. Overall Observations (Your Focus Area)", "Reported condition")
    source_note(doc, "Ryan Larson, Maintenance", "2. Overall Observations (Your Focus Area)", "Observed condition")
    source_note(doc, "Trey Cain, HSE", "2. Overall Observations (Your Focus Area)", "Observed condition")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "7. Additional Notes / Observations", "Recommendation")
    doc.add_paragraph("Coverage and staffing adequacy", style="Heading 1")
    add_table(
        doc,
        ["Service requirement", "Coverage control", "Draft staffing provision", "Verification", "Benefit to the City"],
        [
            ("24/7 full-service O&M and monitoring", "Shift and on-call roster with primary and backup assignments", "[CONFIRM SHIFT PATTERN AND FTE COUNT]", "Operations and regulatory certification review", "Continuous compliant service"),
            ("24/7 customer emergency number", "Live attendant, documented call routing, escalation and closure", "[CONFIRM CALL-CENTER MODEL]", "Test before Day 1", "Reliable customer response"),
            ("1-hour business / 2-hour after-hours response", "Proximity-based on-call schedule, vehicle and access readiness", "[CONFIRM RESPONDERS AND RESIDENCE PROXIMITY]", "Timed drills and monthly reporting", "Performance-standard compliance"),
            ("Vacancy, leave, training, and surge", "Named backup pool and minimum certification matrix", "Regional operators and maintenance resources", "Quarterly coverage review", "Reduced single-person dependency"),
            ("Storm and wet-weather events", "Pre-event readiness roster and incident command", "Cross-functional plant/field/safety/OT team", "Seasonal drill and after-action review", "Faster, coordinated response"),
        ],
        [1.35, 1.85, 1.45, 1.1, 1.1],
    )
    doc.add_paragraph("Qualifications, training, and development", style="Heading 1")
    p(doc, "The final staffing matrix will list every position, assigned person, work location, shift, employment status, certifications, education, comparable experience, and backup. Jacobs will perform a skills and certification assessment during transition, close priority gaps through training and supervised qualification, and cross-train critical functions so that compliance does not depend on one individual.")
    bullet(doc, "California wastewater operator certification appropriate to assigned duties.")
    bullet(doc, "Collections-system competency in cleaning, CCTV/PACP, pump stations, SSO response, and Baykeeper work.")
    bullet(doc, "Stormwater competency in pump stations, catch basins, channels, trash-capture devices, and CDO-support documentation.")
    bullet(doc, "Safety qualification for LOTO, confined space, fall protection, roadway work, chemicals, vehicles, and emergency response.")
    bullet(doc, "OT/SCADA and cybersecurity awareness for City systems, access controls, and incident reporting.")
    doc.add_paragraph("Transition of management and operations", style="Heading 1")
    add_table(
        doc,
        ["Phase", "Key staffing actions", "Readiness evidence", "Owner", "Benefit to the City"],
        [
            ("Award to 90 days before start", "Confirm organization, recruit critical roles, and, if approved by HR and legal, engage the incumbent workforce; initiate background and credential checks", "Approved organization and hiring tracker", "Transition Manager", "Early visibility into staffing risk"),
            ("90 to 30 days before start", "If authorized, complete offers; finalize training plans, backup roster, subcontractor commitments, and system-access requests", "Coverage and access matrix", "Project Manager", "A staffed and supported Day 1 plan"),
            ("Final 30 days", "Shadow operations, test communications and alarms, validate reporting and emergency roles", "Readiness checklist and issue log", "Project Manager / discipline leads", "Continuity at takeover"),
            ("Days 1-120", "Stabilize schedules, assess skills, fill gaps, refine work plans, and validate regional support demand", "Monthly staffing and performance review", "Project Manager", "A sustainable steady-state organization"),
        ],
        [1.1, 2.2, 1.45, 0.95, 1.1],
    )
    doc.add_paragraph("Subcontractors and self-performance", style="Heading 1")
    p(doc, "The final proposal will name every subcontractor and clearly distinguish self-performed work from outsourced specialty work. Anticipated categories requiring confirmation include large-diameter CCTV, traffic control, specialized stormwater cleaning, certified laboratory services, OT/SCADA support, major electrical work, coatings, and repairs outside the approved on-site/support-team capability. [CONFIRM FIRMS, SCOPES, PERCENTAGES, AND COMMERCIAL TREATMENT]")
    doc.add_paragraph("Backup resources", style="Heading 1")
    p(doc, "The Project Manager will maintain a role-by-role backup matrix covering operations, collection and storm response, laboratory and compliance, maintenance, safety, and OT/SCADA. The matrix will identify minimum credentials, expected response time, mobilization authority, and how hours are charged. This turns regional depth into an operational commitment that the City can see and verify.")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 3.3, 6.7, 8.4.4, and 9.3; Attachment A, pp. 9-10, 24, 31, 36-37, and 41-47.",
            "Richmond Proposal Directive, Section 8.4.4 outline.",
            "Richmond Compliance Matrix and Scope Register, including controls C-053, C-054, C-064, C-080, C-087, S-024, S-032 through S-035, S-040, and S-074.",
            "Wiki: Blended On-Site/Off-Site Organization; Regional Technical Support; Surge Staffing; Staff Certification; Wastewater O&M Transition.",
            "Due Diligence Trip Reports by Daniel Gorka, Ryan Larson, Daniel Buonadonna, Trey Cain, and Iouri Ossokine, cited above.",
        ],
        [
            "Name the Project Manager and Collection System Manager and confirm residence proximity.",
            "Approve FTE counts, shifts, certifications, location assignments, and relief coverage.",
            "Define on-site SCADA/electrical coverage and current Calcon interface.",
            "Name every subcontractor and specify scope, percentage, availability, and fee treatment.",
            "Confirm incumbent-workforce strategy and authority to make offers.",
        ],
    )
    return doc


def build_technical() -> Document:
    doc = new_doc("Section 8.4.5", "Project Understanding and Technical Approach", "An integrated operating system for compliance, reliability, transparency, and continuous improvement")
    add_requirement_block(doc, "Address operations, maintenance, asset management, City interaction, energy, transition, specific deliverables, emergencies, housekeeping, and beneficial innovations.", "RFP Section 8.4.5, pp. 31-32")
    doc.add_paragraph("Understanding Richmond's operating environment", style="Heading 1")
    p(doc, "Richmond's Facilities form one operating portfolio with three distinct service environments. The WWTP is a conventional activated-sludge facility averaging about 7 MGD, with a 6.50-MGD base-fee influent assumption and wet-weather pathways that can require storage and blending. The 192-mile wastewater collection system carries Baykeeper obligations and annual cleaning/CCTV standards. The separate 187-mile stormwater system includes channels, pump stations, outfalls, catch basins, and specialized trash-capture assets governed by a municipal stormwater permit and Cease and Desist Order.")
    p(doc, "The City's objectives extend beyond minimum compliance. Richmond wants its operator to maximize asset life, provide financial and data transparency, support capital planning, improve energy and chemical efficiency, align with community values, bring practical green initiatives, and identify revenue or savings opportunities that reduce ratepayer burden. Our approach turns those objectives into named management systems, measurable work plans, and City-visible records.")
    add_table(
        doc,
        ["City goal or requirement", "Key delivery challenge", "Jacobs response", "Benefit to the City"],
        [
            ("Conclude Baykeeper obligations by 2028", "Multiple shared responsibilities, schedules, and evidence requirements", "Maintain a responsibility matrix, annual work plan, QA/QC, and status dashboard", "Visible, defensible progress"),
            ("Reliable plant and wet-weather performance", "Variable flows, blending events, process stability, odor and aging assets", "Unit-process control, wet-weather SOPs, alarm readiness, and specialist support", "Fewer surprises and stable treatment"),
            ("Manage wastewater and stormwater systems", "Large distributed networks, specialized assets, access and security constraints", "Separate accountable planning with coordinated crews, condition data, and safe work methods", "More reliable field execution"),
            ("Maximize asset life", "Deferred work, incomplete asset records, and constrained M&R funding", "Verified inventory, criticality, PM/PdM, backlog ranking, and five-year capital planning", "Defensible investment decisions"),
            ("Transparent reporting", "Multiple operational, regulatory, cost, and performance data sources", "City-readable dashboards, monthly reports, data access, and exception escalation", "Faster decisions and public accountability"),
            ("Innovation and green initiatives", "Ideas must produce measurable value and respect City authority", "Baseline, business case, pilot, measure, and scale with approval", "Lower lifecycle cost and reduced ratepayer burden"),
        ],
        [1.45, 1.75, 2.5, 1.1],
    )
    doc.add_paragraph("Operational approach", style="Heading 1")
    p(doc, "Jacobs will operate the Facilities through an integrated management system covering safety, compliance, operations, maintenance, laboratory, people, financial controls, project governance, community coordination, and customer response. The Project Manager will use a single action and performance register to connect daily rounds and alarms with work orders, permit obligations, reporting, M&R decisions, and longer-term capital recommendations.")
    doc.add_paragraph("Wastewater treatment plant", style="Heading 2")
    p(doc, "The operating plan will establish approved unit-process control procedures for headworks, primary clarification, aeration and secondary clarification, disinfection/dechlorination, anaerobic digestion, thickening, biosolids transfer, odor systems, and wet-weather facilities. Operators will define target ranges, monitoring points, alarms, response steps, documentation, and escalation for each process. Procedures will be reconciled with permits, manufacturer guidance, operating manuals, and City-approved practices.")
    p(doc, "During transition, Jacobs will validate process baselines and confirm the status of the new rotary thickener, aeration instrumentation, clarifier performance, chemical systems, digesters, flare, biosolids pipeline, shared WCWD interfaces, and wet-weather storage and blending controls. Site-visit observations regarding sludge appearance, odor, and instrumentation will be treated as diagnostic prompts requiring data review and testing, not as final process conclusions.")
    source_note(doc, "Daniel Gorka, Estimator", "2. Overall Observations (Your Focus Area) - WWTP process, odor, and digesters", "Observed condition")
    source_note(doc, "Kelly Irving, General/Strategy/Estimating", "2. Overall Observations (Your Focus Area)", "Observed condition")
    p(doc, "An operations-focused site report identified potential issues involving grit accumulation in digesters, bar-screen redundancy, wet-weather storage constraints, and primary-clarifier chain-and-flight maintenance. Jacobs will treat each item as an open verification point, review available records, and confirm field condition before incorporating it into operating, maintenance, or capital plans.")
    source_note(doc, "Roy Aristizabal, Operations", "3. Notable Risks and Challenges", "Open question/data gap")
    doc.add_paragraph("Compliance, laboratory, and reporting", style="Heading 2")
    p(doc, "Before Day 1, Jacobs will build a permit-by-permit obligations register covering the WWTP NPDES permit, wastewater collection order, stormwater NPDES permit, stormwater Cease and Desist Order, Baykeeper Settlement Agreement, air permits, and other applicable requirements. The register will identify each activity, report, due date, owner, backup, source data, reviewer, City approval step, and retained evidence.")
    p(doc, "A controlled data workflow will connect operator rounds, laboratory results, alarms, maintenance, collection and stormwater work, customer calls, energy, and M&R spending. Monthly reports covering the prior month's activity will be submitted by the 10th of each month, address the RFP-required topics, and be reviewed with the City in a formal meeting. Any violation, near exceedance, late-data risk, or missed field standard will be escalated promptly with cause, immediate response, corrective action, owner, and closure evidence.")
    doc.add_paragraph("Wastewater collection system", style="Heading 2")
    p(doc, "Jacobs will build an annual collection-system work plan that completes the 25-percent cleaning cycle by December 31 and the 10-percent CCTV cycle by June 1 while also addressing Baykeeper risk priorities, recurring hot spots, root control, complaints, pump-station condition, force-main needs, and emergency response. All notified collection-line blockage cleaning will start within two hours. Cleaning, CCTV, inspection, and repair recommendations will be recorded in City-approved NexGen, GIS, and SewerAI workflows, with responsibility for PACP accuracy and condition reporting clearly assigned.")
    add_table(
        doc,
        ["Program element", "RFP baseline", "Proposed control", "Due-diligence qualification", "Benefit to the City"],
        [
            ("Gravity sewer cleaning", "25% annually; more often for problem areas", "Risk-based route plan, production tracking, QA sampling, and monthly/annual confirmation", "Validate hot-spot entry/exit criteria and inaccessible assets", "Required work with transparent extra demand"),
            ("CCTV", "10% annually; City uses SewerAI", "PACP quality controls, data handoff, defect escalation, and annual condition plan", "Obtain complete PACP database and define large-pipe subcontracting", "Defensible condition and CIP data"),
            ("Pump stations and force mains", "Operate, maintain, respond, and assess", "Alarm review, inspections, runtime balancing, valve/vent/corrosion controls", "Verify high-point vents, ownership, access, and condition history", "Reduced service and corrosion risk"),
            ("SSO response", "Immediate identification/notification/cleanup support", "Incident command, depth verification, cause documentation, evidence retention", "Clarify structural versus O&M responsibility scenarios", "Faster response and fewer disputes"),
        ],
        [1.1, 1.35, 1.9, 1.55, 1.1],
    )
    source_note(doc, "Daniel Buonadonna, Collections System", "2. Overall Observations (Your Focus Area) - sanitary sewer collections", "Reported condition")
    source_note(doc, "Daniel Buonadonna, Collections System", "5. Items to Consider for Pricing / Cost Model - sanitary sewer collections", "Open question/data gap")
    source_note(doc, "Daniel Gorka, Estimator", "2. Overall Observations (Your Focus Area) - Collections", "Observed condition")
    doc.add_paragraph("Stormwater collection system", style="Heading 2")
    p(doc, "The stormwater work plan will separately identify pipes, force mains, pump stations, catch basins, inline trash-capture devices, hydrodynamic separators, gross-solids removal devices, drainage channels, outfalls, and the detention basin. Annual schedules will complete the 10-percent cleaning/CCTV requirement by June 30 and address twice-yearly cleaning frequencies, rainy-season readiness, additional work triggered by blockage or flooding, debris testing and disposal coordination, and documentation that supports the City's permit and CDO obligations.")
    p(doc, "Because the site-visit reports describe limited precedent, specialized cleaning methods, access constraints, and uncertain debris quantities, Jacobs will verify asset configuration and baseline condition before locking the long-term production model. The initial catch-basin plan will document quantities, condition, cleaning method, expected debris, access and traffic controls, disposal path, and criteria for 'as needed' work.")
    source_note(doc, "Daniel Buonadonna, Collections System", "2. Overall Observations (Your Focus Area) - stormwater collections; 3. Notable Risks and Challenges", "Open question/data gap")
    source_note(doc, "Daniel Gorka, Estimator", "2. Overall Observations (Your Focus Area) - Stormwater", "Observed condition")
    doc.add_paragraph("Recurring performance controls", style="Heading 2")
    add_table(
        doc,
        ["Control", "RFP standard", "Due / trigger", "Evidence", "Benefit to the City"],
        [
            ("Wastewater cleaning", "25% of system annually", "December 31", "Monthly and annual cleaning summaries", "Visible completion of required work"),
            ("Wastewater CCTV", "10% of system annually", "June 1", "PACP records in City systems", "Timely condition and CIP data"),
            ("Stormwater cleaning/CCTV", "10% of system annually", "June 30", "Asset-level work and disposal records", "Documented permit-supporting work"),
            ("Collection-line blockage cleaning", "Start within two hours", "Upon notification", "Call, dispatch, arrival, and work-start timestamps", "Fast response and auditable compliance"),
            ("Monthly O&M report", "Prior-month activities and required topics", "10th of each month", "Submitted report and City review record", "Predictable, transparent reporting"),
        ],
        [1.35, 1.55, 1.15, 1.85, 1.15],
    )
    doc.add_paragraph("Maintenance plan", style="Heading 1")
    p(doc, "The maintenance program will shift the portfolio toward planned, risk-based work. Jacobs will validate the asset hierarchy, reconcile City-owned equipment and warranties, establish criticality, load preventive and predictive maintenance, control work orders, identify critical spares, and apply the RFP cost boundary consistently. The base fee includes all required O&M, preventive and predictive maintenance, housekeeping, and Contract Operator labor provided for corrective maintenance. Only eligible repair and major-maintenance costs may be charged to the M&R fund under the RFP approval rules. Work history and condition data will support annual repair planning and the five-year CIP.")
    add_table(
        doc,
        ["Maintenance control", "Initial action", "Ongoing method", "Record", "Benefit to the City"],
        [
            ("Asset and spare-parts inventory", "Physical count and tagging within 90 days", "Controlled issue, reorder levels, obsolescence and critical-spares review", "NexGen inventory and asset records", "Faster repairs and transparent City property"),
            ("PM/PdM", "Validate manuals, warranties, and current tasks", "Risk-based scheduling, route completion, exceptions and failure analysis", "Work orders and monthly KPI", "Longer asset life and fewer failures"),
            ("Backlog", "Identify safety, compliance, service, and cost risks", "Jointly rank, estimate, approve, execute, and close", "Backlog and M&R decision register", "Resources focus on highest consequence"),
            ("M&R fund", "Confirm inherited condition and cost assumptions", "Itemized monthly accounting and written approval above thresholds", "Monthly M&R statement", "Budget visibility and contract compliance"),
            ("Capital planning", "Link defects and condition to risk", "Five-year prioritized plan updated annually", "Five-year CIP record", "Defensible long-term investment"),
        ],
        [1.25, 1.55, 1.7, 1.2, 1.1],
    )
    p(doc, "The maintenance report observed extensive housekeeping needs, corrosion, temporary repairs, inconsistent inventory controls, and safety-related deficiencies. Jacobs proposes an immediate safety and housekeeping stabilization effort, followed by a documented condition and backlog assessment. This evidence will be used to forecast workload and prioritize eligible M&R needs; it does not narrow the required base scope or the RFP requirement that Contract Operator corrective-maintenance labor be included in the base fee. Any requested extra-contract work would require an expressly negotiated and City-approved contract mechanism.")
    source_note(doc, "Ryan Larson, Maintenance", "2. Overall Observations (Your Focus Area); 7. Additional Notes / Observations", "Observed condition")
    source_note(doc, "Trey Cain, HSE", "2. Overall Observations (Your Focus Area)", "Observed condition")
    doc.add_paragraph("Self-performance and subcontracting controls", style="Heading 2")
    p(doc, "The final proposal will name all subcontractors. The following draft allocation identifies the decisions still required without treating specialty support as an exception to mandatory scope.")
    add_table(
        doc,
        ["System", "Draft self-performed work", "Potential subcontracted work", "Required decision", "Benefit to the City"],
        [
            ("WWTP", "Operations, laboratory, routine maintenance, PM/PdM, housekeeping, work control, and corrective-maintenance labor within the approved staffing model", "Specialty equipment rebuilds, coatings, major electrical work, and other work outside approved staff capability", "Name firms; confirm scope, staff capability, and base-fee/M&R allocation", "Clear ownership and cost control"),
            ("Wastewater collection", "Management, dispatch, inspections, pump-station O&M, emergency response, work tracking, and approved cleaning/CCTV delivery model", "Large-diameter cleaning/CCTV, bypass pumping, traffic control, and specialty repair services", "Confirm cleaning/CCTV self-perform split, named firms, rates, and response", "Defensible annual production plan"),
            ("Stormwater", "Program management, inspections, pump-station O&M, response, documentation, testing coordination, and approved routine cleaning model", "Specialty cleaning, traffic control, access support, and unusual debris handling", "Confirm asset-by-asset method, quantities, named firms, and commercial treatment", "Transparent delivery for specialized assets"),
        ],
        [1.0, 2.0, 1.7, 1.45, 1.0],
    )
    doc.add_paragraph("Asset management", style="Heading 1")
    p(doc, "Within 120 days, Jacobs will implement an asset-management plan and CMMS workflow scaled to Richmond's portfolio. The plan will integrate City-required NexGen and GIS for linear assets, SewerAI CCTV data, treatment-plant records, criticality, condition, work history, cost, warranty, spare-parts, and capital recommendations. Richmond will have real-time read-only access, and City data ownership will be preserved.")
    numbered(doc, "Establish the verified asset and location hierarchy.")
    numbered(doc, "Assign criticality using safety, compliance, service, cost, and redundancy consequences.")
    numbered(doc, "Complete the 90-day condition assessment and risk-rank findings.")
    numbered(doc, "Load approved PM/PdM, inspection, warranty, and inventory controls.")
    numbered(doc, "Use work and condition history to support monthly decisions and the annual five-year CIP.")
    doc.add_paragraph("Managing and interacting with the City", style="Heading 1")
    p(doc, "The Project Manager will serve as the City's primary operating contact and maintain a no-surprises protocol. Daily operational coordination will be supplemented by weekly action reviews during transition and stabilization, formal monthly O&M meetings, periodic executive governance, and annual planning. Every recurring forum will produce a written output: action log, performance dashboard, decision record, risk update, or approved plan.")
    add_table(
        doc,
        ["Forum", "Cadence", "Led by", "Written output", "Benefit to the City"],
        [
            ("Daily operations coordination", "Daily / as needed", "Project Manager or designee", "Shift and exception log", "Immediate awareness and handoff"),
            ("Transition and action review", "Weekly through Day 120", "Transition Manager / Project Manager", "Readiness and decision register", "Visible progress and early issue resolution"),
            ("O&M performance review", "Monthly", "Project Manager", "RFP-required monthly report and dashboard", "Transparent operating, compliance, cost, and M&R status"),
            ("Executive governance", "Quarterly or agreed", "City and Jacobs executives", "Strategic decisions and risk log", "Aligned priorities and escalation"),
            ("Innovation and capital workshop", "Annual", "City / Project Manager", "Prioritized business cases and five-year CIP inputs", "Measured improvement tied to City value"),
        ],
        [1.25, 1.0, 1.55, 2.0, 1.0],
    )
    doc.add_paragraph("Energy and chemical management", style="Heading 1")
    p(doc, "Jacobs will establish an auditable baseline for electricity, gas, water, and process chemicals, normalize performance for flow and loading, and report monthly trends and explanations. The City-established 2050 kWh/MG power baseline and 50/50 sharing mechanism will be administered transparently. Potential improvements such as dissolved-oxygen control, pumping optimization, aeration tuning, chemical-feed control, and odor-system alternatives will proceed only after data validation, lifecycle-cost analysis, and City approval.")
    source_note(doc, "Daniel Gorka, Estimator", "4. Notable Opportunities - aeration DO control and odor-control observations", "Recommendation")
    doc.add_paragraph("Transition plan", style="Heading 1")
    add_table(
        doc,
        ["Phase", "Primary actions", "Key milestone", "Evidence", "Benefit to the City"],
        [
            ("Mobilize", "Governance, workforce, permits, data requests, contracts, access, and asset priorities", "Transition Plan due 30 days before start", "Approved readiness schedule", "Early control of critical dependencies"),
            ("Validate", "Shadowing, process baselines, alarms, reporting, cybersecurity, spares, emergency procedures", "Day 1 readiness review", "Signed readiness checklist", "No avoidable service interruption"),
            ("Stabilize", "Safety/housekeeping reset, critical work, staffing, compliance calendar, data controls", "Days 1-30", "Weekly action and risk reports", "Fast control of inherited risk"),
            ("Baseline", "Condition assessment, work plans, asset hierarchy, stormwater quantities, cost drivers", "Days 31-90", "90-day condition assessment", "Shared understanding of scope and condition"),
            ("Optimize", "CMMS/data systems, CIP, operational improvements, approved pilots", "Days 91-120 and annual", "Required plans and business cases", "Measured, sustainable improvement"),
        ],
        [1.05, 2.0, 1.2, 1.45, 1.1],
    )
    doc.add_paragraph("Specific contract deliverables", style="Heading 1")
    add_table(
        doc,
        ["Deliverable", "RFP due date", "Draft production method", "Review / acceptance", "Benefit to the City"],
        [
            ("Site-specific Transition Plan", "30 days before start", "Integrated schedule, owners, readiness gates, dependencies", "City review", "Controlled takeover"),
            ("Asset condition assessment", "90 days after start", "Risk-based field verification linked to assets and work orders", "Joint prioritization", "Defensible backlog and CIP"),
            ("Asset management plan and CMMS", "120 days after start", "NexGen/GIS/SewerAI-aligned workflows and City access", "City configuration approval", "Transparent lifecycle management"),
            ("Process/regulatory data system", "120 days after start", "Controlled data sources, QA/QC, dashboards, and retention", "City protocol approval", "Reliable reporting"),
            ("Five-year CIP", "120 days; then annually within 30 days after the renewal date", "Condition, risk, cost, and delivery-priority model", "City capital process", "Long-term asset stewardship"),
            ("Catch-basin cleaning plan", "90 days; annually by March 1", "Asset-level schedule, methods, access, debris and evidence", "City and permit alignment", "CDO-supporting execution"),
            ("Drainage-ditch maintenance plan", "120 days", "Inventory, inspection, safe access, cleaning and disposal approach", "City approval", "Reduced flooding and debris risk"),
            ("Odor Control Plan", "60 days", "Source inventory, monitoring, complaint response, optimization roadmap", "City / air-permit review", "Improved community responsiveness"),
            ("Subcontracting Plan", "Before start", "Named firms, scope, controls, self-perform split, costs", "City review", "Clear accountability"),
            ("Staffing Plan", "Before start", "Named staff, shifts, certifications, coverage and backups", "City review", "Adequate, verifiable coverage"),
            ("Safety Plan", "60 days", "Site-specific risk controls, training, emergency and audit program", "City coordination", "Safer facilities and field work"),
        ],
        [1.45, 1.05, 2.1, 1.1, 1.1],
    )
    doc.add_paragraph("Emergency response and resilience", style="Heading 1")
    p(doc, "Jacobs will maintain a live 24/7 customer emergency number and a documented response structure capable of meeting the one-hour business-hours and two-hour after-hours on-site standards. Event-specific procedures will address treatment process failures, wet-weather and blending events, sewer blockages and SSOs, pump-station failures, stormwater flooding, power loss, chemical incidents, cyber incidents, and field-security constraints. Drills, call records, response times, corrective actions, and after-action reviews will be retained and reported.")
    doc.add_paragraph("Housekeeping and site stewardship", style="Heading 1")
    p(doc, "Housekeeping will be managed as an operating control, not an appearance campaign. The first 30 days will establish safe access and storage, remove debris, correct immediate hazards, assign area ownership, and create repeatable inspection standards. Longer-term work involving coatings, structural repair, equipment condition, and capital renewal will be risk-ranked and routed through approved maintenance and capital processes.")
    source_note(doc, "Kelly Irving, General/Strategy/Estimating", "2. Overall Observations (Your Focus Area) - housekeeping", "Observed condition")
    source_note(doc, "Ryan Larson, Maintenance", "2. Overall Observations (Your Focus Area) - Housekeeping & Site Cleanliness", "Observed condition")
    doc.add_paragraph("Safety, security, and cybersecurity", style="Heading 1")
    p(doc, "The transition safety assessment will verify LOTO, confined space, fall protection, electrical safety, chemical handling, traffic control, vehicle operation, eyewash and spill response, walking surfaces, off-site security, and emergency coordination. Controls will be documented through training, task plans, equipment inspection, supervision, and corrective-action tracking.")
    p(doc, "For OT/SCADA, Jacobs will comply with City account, device, access, monitoring, and one-hour cyber-incident-notification requirements. A transition assessment will inventory systems, ownership, communication paths, remote access, end-of-life components, backups, alarms, vendor contracts, and City/Veolia account-transfer needs. The resulting cybersecurity plan will align with a recognized framework and establish risk ownership, access control, incident response, recovery, monitoring, and annual review.")
    source_note(doc, "Trey Cain, HSE", "2. Overall Observations (Your Focus Area); 3. Notable Risks and Challenges", "Observed condition")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "2. Network & Cybersecurity Posture; 5. Documentation & Unknowns; 6. Strategic Risks Requiring Attention", "Open question/data gap")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "7. Recommended Actions Following Successful Project Onboarding", "Recommendation")
    doc.add_paragraph("Innovation and green initiatives", style="Heading 1")
    p(doc, "Jacobs will apply a disciplined improvement process: establish the baseline, define the client outcome, quantify cost and risk, test at appropriate scale, report results, and expand only with City approval. Initial candidates for evaluation include aeration and dissolved-oxygen optimization, odor and corrosion diagnostics, collections prioritization tools, fleet productivity and safety monitoring, SCADA/OT modernization, spare-parts controls, energy recovery, biosolids optimization, and grant or funding support.")
    p(doc, "No candidate is presented as a guaranteed saving or base-fee inclusion until scope, data, performance baseline, ownership, commercial treatment, and approval are confirmed. This protects Richmond from technology-for-technology's-sake and keeps improvement tied to measurable public value.")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 1-5 and 8.4.5; Attachments A, B, and E, pp. 6-22, 31-32, and 40-55.",
            "Richmond Proposal Directive, Section 8.4.5 outline.",
            "Richmond Compliance Matrix and Scope Register, including controls C-004, C-005, C-079, C-081, C-084, C-089, C-102, C-103, C-106 through C-109, C-115, C-117, C-118, C-121, S-004, S-005, S-032, S-034, S-037, S-042, S-055, S-056, S-059 through S-061, S-068 through S-072, and S-075.",
            "Wiki technical sources: O&M Management Systems; Collection System O&M; CMMS Asset Management; Energy Management; Process Control and Compliance; Odor Control; OT/SCADA Roadmap; Reporting Protocol.",
            "Wiki compliance/staffing sources: Emergency Response; Integrated Safety/Security/Cybersecurity; Six-Point Compliance; Transition and Regional Support.",
            "Due Diligence Trip Reports by Kelly Irving, Daniel Gorka, Ryan Larson, Roy Aristizabal, Daniel Buonadonna, Trey Cain, and Iouri Ossokine.",
        ],
        [
            "Validate every trip-report observation against data, photos, City answers, and available asset records.",
            "Obtain and reconcile all addenda, the draft Service Agreement, permits, Baykeeper agreement, CDO, asset lists, and document-room data.",
            "Confirm staffing, subcontractors, self-perform boundaries, service levels, and commercial inclusions.",
            "Resolve responsibility for structural defects, inaccessible assets, hot spots, force-main work, shared WCWD interfaces, and special stormwater assets.",
            "Approve any proposed technology, vendor, pilot, saving, or value-added commitment before issue.",
        ],
    )
    return doc


def build_forms() -> Document:
    doc = new_doc("Section 8.4.6", "Required Forms", "A controlled attachment checklist for legal review, authorized certification, and final submission")
    add_requirement_block(doc, "Submit the Sanctuary City Compliance Statement and Limited Liability Disclosure Affidavit with the technical proposal as attachments.", "RFP Section 8.4.6 and Attachment D, pp. 32 and 50-52")
    p(doc, "This section is a submission-control draft. It does not make or imply either required legal certification. The original City forms must be completed, reviewed, signed by an authorized representative, and attached without altering the City's language.")
    add_table(
        doc,
        ["Required form", "Required action", "Status / approval", "Final control"],
        [
            ("Sanctuary City Compliance Statement", "Review Ordinance 12-18 applicability; complete entity and signatory fields; execute under penalty of perjury", "[LEGAL REVIEW PENDING] [SIGNATORY TBD]", "Use current City form; verify every field, signature, and date"),
            ("Limited Liability Disclosure Affidavit", "Determine applicability to the contracting entity; disclose the required ownership chain if applicable; complete and sign", "[LEGAL REVIEW PENDING] [SIGNATORY TBD]", "Use current City form; verify entity consistency and signature"),
        ],
        [1.55, 2.45, 1.45, 1.35],
    )
    doc.add_paragraph("Submission quality-control checklist", style="Heading 1")
    bullet(doc, "Use the forms contained in Attachment D or the latest form issued by addendum.")
    bullet(doc, "Confirm the contracting entity is consistent across the proposal, fee submission, W-9, forms, and agreement.")
    bullet(doc, "Confirm every required field is complete or appropriately marked not applicable.")
    bullet(doc, "Obtain legal approval before any certification or ownership disclosure is signed.")
    bullet(doc, "Confirm the signatory has authority and that signature and date are present.")
    bullet(doc, "Place the completed forms in the technical-proposal attachment package and include them in final compliance review.")
    bullet(doc, "Retain a signed submission copy and BidsOnline confirmation record.")
    doc.add_paragraph("Post-award items tracked separately", style="Heading 1")
    p(doc, "The RFP also identifies certificates of insurance, a current signed W-9, and a City of Richmond business license as post-award requirements due within 10 days of notification unless otherwise specified. These items are not substitutes for the two proposal forms and should remain on the contract-readiness tracker.")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 7.3, 7.10, 7.11, and 8.4.6; Attachment D, pp. 25, 27, 32, and 50-52.",
            "Richmond Proposal Directive, Section 8.4.6 outline.",
            "Richmond Compliance Matrix, including controls C-030, C-031, C-057, C-119, and C-120.",
        ],
        [
            "Confirm the final contracting entity and applicability of the LLC disclosure.",
            "Complete legal review of the Sanctuary City certification.",
            "Identify authorized signatory and execute current City-issued forms.",
            "Check all addenda for revised or additional forms.",
        ],
    )
    return doc


def build_fee() -> Document:
    doc = new_doc("Section 8.4.7", "Fee Proposal", "A separate, transparent commercial submission aligned to Richmond's operating scope and risk allocation")
    add_requirement_block(doc, "Submit the Fee Proposal separately. Provide fees for the WWTP and wastewater collection system, stormwater as a standalone service, and the $2,000,000 M&R fund; address utilities, gain-sharing, and fee adjustments.", "RFP Section 8.4.7, pp. 32-35")
    p(doc, "This document establishes the required fee structure and commercial narrative. It intentionally contains no proposed prices. Amounts will be inserted only after the operating model, staffing, subcontracting, chemical, safety, stormwater, collection-system, OT/SCADA, and risk assumptions are approved by the commercial lead.")
    doc.add_paragraph("Base annual fee", style="Heading 1")
    add_table(
        doc,
        ["Category", "Amount", "Basis", "Approval / control"],
        [
            ("WWTP and wastewater collection system", "[TBD]", "Approved staffing, chemicals, PM/PdM, field work, support, and reporting", "Commercial review pending"),
            ("Stormwater collection system", "[TBD]", "Standalone O&M price excluding M&R allocation", "Commercial review pending"),
            ("M&R Fund", "$2,000,000", "City-established first-year fund", "RFP-defined; monthly accounting"),
            ("Total", "[TBD]", "Sum of approved categories", "Executive approval pending"),
        ],
        [1.65, 0.9, 2.65, 1.6],
    )
    p(doc, "The initial base fee remains in effect through May 15, 2028. The base annual fee will cover the services included in the final approved proposal and contract, including all required O&M, preventive and predictive maintenance, housekeeping, and Contract Operator labor provided for corrective maintenance. Pre-contractual proposal and negotiation expenses will not be included.")
    doc.add_paragraph("Commercial principles", style="Heading 1")
    bullet(doc, "Map every price element to an approved scope, quantity, frequency, performance standard, and responsibility.")
    bullet(doc, "Keep required base O&M—including PM/PdM, housekeeping, and corrective-maintenance labor—distinct from eligible M&R repair costs, City capital work, and optional services accepted through an authorized contract mechanism.")
    bullet(doc, "Identify all subcontracted work and ensure it is consistent with the staffing and technical sections.")
    bullet(doc, "State assumptions and exclusions clearly enough to support negotiation without weakening RFP compliance.")
    bullet(doc, "Provide complete monthly transparency for M&R, energy, chemicals, and other agreed cost drivers.")
    doc.add_paragraph("Due-diligence cost drivers and data gaps", style="Heading 1")
    p(doc, "The trip reports identify potential cost drivers that require validation before final pricing. They are presented as observations, recommendations, or open questions rather than settled quantities or contractual exceptions.")
    add_table(
        doc,
        ["Evidence type", "Cost driver or data gap", "Source", "Proposed pricing treatment", "Benefit to the City"],
        [
            ("Open question/data gap", "Stormwater debris quantities, special-asset methods, access, and 'as needed' workload are not fully baselined.", "Buonadonna - Items to Consider for Pricing", "Develop asset/quantity baseline; define included production and unit-rate or T&M treatment for approved excess work.", "A realistic and auditable stormwater price"),
            ("Reported condition", "Hot-spot cleaning may materially increase annual sanitary cleaning effort.", "Buonadonna - Sanitary sewer collections", "Validate list, frequencies, closure criteria, and production history before setting labor/equipment assumptions.", "Pricing aligned to actual workload"),
            ("Recommendation", "Early maintenance backlog and safety correction may exceed normal steady-state demand.", "Larson - Additional Notes", "Include required base O&M and Contract Operator corrective-maintenance labor in the base fee; forecast eligible M&R costs and identify any requested extra-contract work only through a City-approved mechanism.", "Transparent allocation without narrowing RFP scope"),
            ("Open question/data gap", "M&R repair demand may exceed the combined $2 million first-year fund.", "Gorka - Notable Risks", "Use joint prioritization, transparent forecasting, and contract procedures for additional funding; do not guarantee sufficiency.", "Early warning and better repair decisions"),
            ("Open question/data gap", "Chemical demand and vendor arrangements for hydrogen peroxide, SulFeLox, ferric, hypochlorite, bisulfite, and polymer require validation.", "Gorka - Cost Drivers", "Confirm consumption, unit pricing, control responsibility, service contracts, and baseline before final amount.", "Transparent chemical assumptions"),
            ("Recommendation", "OT/SCADA end-of-life components and account transfers may require capital or separately authorized work.", "Ossokine - Strategic Risks", "Include required operating support in the base fee; treat only City-approved modernization capital and vendor services through authorized mechanisms.", "Clear separation of O&M and modernization"),
            ("Observed condition", "Roadway work and off-site access may require traffic control or security measures.", "Cain - HSE observations", "Include anticipated routine controls in the base fee and identify specialized third-party subcontracting transparently.", "Safer field work with visible cost"),
        ],
        [1.25, 1.55, 1.2, 1.75, 1.05],
    )
    source_note(doc, "Daniel Buonadonna, Collections System", "5. Items to Consider for Pricing / Cost Model", "Open question/data gap")
    source_note(doc, "Ryan Larson, Maintenance", "7. Additional Notes / Observations", "Recommendation")
    source_note(doc, "Daniel Gorka, Estimator", "3. Notable Risks and Challenges; 5. Items to Consider for Pricing / Cost Model", "Open question/data gap")
    source_note(doc, "Iouri Ossokine, OT/SCADA", "6. Strategic Risks Requiring Attention; 7. Recommended Actions Following Successful Project Onboarding", "Recommendation")
    source_note(doc, "Trey Cain, HSE", "2. Overall Observations (Your Focus Area); 5. Items to Consider for Pricing / Cost Model", "Observed condition")
    doc.add_paragraph("Utilities and gain-sharing", style="Heading 1")
    p(doc, "The City will pay electricity, gas, and water invoices as described in the RFP, while the Contract Operator remains responsible for efficient utilization and monthly reporting. Electrical performance will be evaluated against the 2050 kWh/MG baseline using annual averages, with gains or excess costs shared 50/50 under the RFP mechanism. The final fee submission will describe data sources, normalization, baseline exceptions, calculation review, and any alternative arrangement offered for City consideration.")
    doc.add_paragraph("RFP-defined disposal responsibilities", style="Heading 1")
    bullet(doc, "The City will haul and dispose of WWTP screenings and grit.")
    bullet(doc, "For stormwater debris, the Contract Operator will deliver material to the WWTP and perform required disposal testing; the City will arrange final disposal through its solid-waste contractor in coordination with the Contract Operator.")
    p(doc, "The final pricing basis will reflect these allocations and will not shift them based solely on trip-report recommendations.")
    doc.add_paragraph("Maintenance and Repair Fund", style="Heading 1")
    add_table(
        doc,
        ["M&R rule", "Draft commercial treatment", "Control", "Open decision"],
        [
            ("First-year fund", "$2,000,000 included as the RFP-defined fund", "Separate account and monthly roll-forward", "Confirm invoice/cash-flow mechanism"),
            ("Corrective work less than $5,000", "Charge eligible repair and major-maintenance costs, excluding Contract Operator labor, without City preapproval", "Single-work-order definition and itemized records", "Confirm eligible cost categories"),
            ("Work exactly $5,000", "Do not assume treatment; obtain written City clarification", "Threshold question log and approved direction", "Resolve gap between 'less than' and 'exceeding'"),
            ("Work exceeding $5,000", "Prior written City approval", "Asset, failure, scope, cost, labor/material breakdown", "Confirm emergency exception process"),
            ("Subcontracted repair labor", "City preapproval when work is normally performed by plant staff", "Scope and capability check", "Confirm named firms and rates"),
            ("Contract Operator-owned equipment", "Do not charge its maintenance to the M&R fund", "Ownership and asset-record check", "Confirm equipment inventory"),
            ("Operator-caused repairs", "Contract Operator bears total repair cost when caused by negligence or failure to follow approved manuals, manufacturer recommendations, or the standard of care", "Cause review and approval record", "Confirm dispute-resolution workflow"),
            ("Unused funds", "Return unused funds to the City", "Year-end reconciliation", "Confirm accounting timing"),
        ],
        [1.35, 2.35, 1.7, 1.4],
    )
    doc.add_paragraph("Fee adjustments", style="Heading 1")
    p(doc, "The final proposal will acknowledge the annual adjustment method based on the CPI U.S. city average, Water and Sewerage Maintenance, not seasonally adjusted, Series ID CUSR0000SEHG01. It will also describe the process for demonstrating cost impacts when system flow, loading, or size exceeds baseline conditions by more than 10 percent.")
    p(doc, "Annual Adjusted Fee = Prior Annual Fee x (Current February Index / Prior February Index). The final commercial review will confirm interpretation, timing, downward adjustments, rounding, and treatment of added or removed scope.")
    doc.add_paragraph("Draft assumptions and exclusions", style="Heading 1")
    bullet(doc, "[CONFIRM] Final fee is based on 6.50 MGD annual-average influent, BOD 375 mg/L, and TSS 450 mg/L.")
    bullet(doc, "[OPEN QUESTION/DATA GAP] Verify the inventory and condition of transferred City-owned equipment; this draft assumes no warranty or condition standard beyond the final RFP and agreement.")
    bullet(doc, "[CONFIRM] Capital improvements remain City-authorized and are not embedded in the base fee unless expressly identified.")
    bullet(doc, "[CONFIRM] Pricing will classify required base O&M, eligible M&R expenses, City-authorized capital, and any expressly accepted scope change without excluding mandatory RFP work.")
    bullet(doc, "[OPEN QUESTION/DATA GAP] Confirm how future bioswales, bioretention, and low-impact-development assets would be incorporated if constructed; no exclusion is assumed in this draft.")
    bullet(doc, "[CONFIRM] Required operating support is included in the base fee; major modernization capital, specialty studies, and optional technologies will use only City-authorized contract mechanisms unless specifically included.")
    bullet(doc, "[OPEN QUESTION/DATA GAP] The RFP identifies sodium bisulfate for dechlorination, while a trip report identifies sodium bisulfite; confirm the chemical identity from authorized City records before finalizing quantities and pricing.")
    bullet(doc, "[CONFIRM] Every exclusion and qualification will be reconciled with legal review and the draft Service Agreement before issue.")
    add_sources_and_decisions(
        doc,
        [
            "City of Richmond RFP, Sections 4.1.2, 7.2, 8.4.7, and 9.3; Attachment A, pp. 14, 25, 32-35, and 40-47.",
            "Richmond Proposal Directive, Section 8.4.7 outline.",
            "Richmond Compliance Matrix and Scope Register, including controls C-022, C-058 through C-071, C-078, C-084, S-013, S-015 through S-030, S-037, S-043, S-058, S-064, and S-065.",
            "Wiki: Financial Transparency; Energy Management; Maintenance and Asset Management; Collection System O&M.",
            "Due Diligence Trip Reports by Daniel Gorka, Daniel Buonadonna, Ryan Larson, Trey Cain, and Iouri Ossokine, cited above.",
        ],
        [
            "Insert approved prices, staffing, chemicals, subcontractors, equipment, allowances, and rates.",
            "Reconcile final assumptions and exclusions with all addenda and the draft Service Agreement.",
            "Define commercial treatment for inherited backlog, special assets, extraordinary debris, access/security, and work beyond the M&R fund.",
            "Confirm utility data, gain-sharing calculation, and any alternative arrangement.",
            "Resolve the exactly-$5,000 M&R approval threshold and the sodium bisulfate/bisulfite source conflict.",
            "Confirm all trip-report cost observations with estimating and available source data.",
        ],
    )
    return doc


def save_document(doc: Document, filename: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / filename
    doc.save(path)
    with ZipFile(path) as zf:
        required = {"[Content_Types].xml", "word/document.xml", "word/styles.xml"}
        missing = required - set(zf.namelist())
        if missing:
            raise RuntimeError(f"{filename}: missing DOCX parts {sorted(missing)}")
    return path


def main() -> None:
    outputs = [
        (build_cover_letter(), "01_Tech_1_Cover_Letter_Richmond_Draft.docx"),
        (build_exec_summary(), "02_Tech_2_Executive_Summary_Richmond_Draft.docx"),
        (build_qualifications(), "03_Tech_3_Firm_Qualifications_Richmond_Draft.docx"),
        (build_staffing(), "04_Tech_4_Staffing_Management_Richmond_Draft.docx"),
        (build_technical(), "05_Tech_5_Technical_Approach_Richmond_Draft.docx"),
        (build_forms(), "06_Tech_6_Required_Forms_Richmond_Draft.docx"),
        (build_fee(), "07_Fee_Proposal_Richmond_Draft.docx"),
    ]
    for doc, filename in outputs:
        print(save_document(doc, filename))


if __name__ == "__main__":
    main()
