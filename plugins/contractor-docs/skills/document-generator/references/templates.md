# Document Templates v1.0

Complete Python implementations for all document types. Each function requires all helpers from `references/brand-system.md` to be defined first. All visual tokens (`C["INK"]`, `LOGO_DIR`, `COMPANY_NAME`, etc.) come from the brand-system module.

---

## Boilerplate (top of every script)

```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml, OxmlElement
import os

# === Paste all helpers from brand-system.md here ===
# C, COMPANY_NAME, TAGLINE, FONT_PRIMARY, LOGO_DIR, LOGO_MAP,
# setup_page, set_cell_shading, remove_table_borders,
# remove_cell_borders, set_bottom_border, set_top_bottom_border,
# set_cell_margins, r, hairline, add_cover, section_label,
# body, bullet, info_table, line_item_table, totals_block,
# signature_block, setup_header_footer, add_page_break
```

---

## 1. Construction Estimate / ROM Budget

```
PAGE 1 — COVER
├── Logo (Inches(1.6), top-left)
├── Hairline rule
├── Doc type label (muted, 9pt)
├── Project title (26pt bold)
├── Address/APN (10pt MID)
├── Hairline rule
└── Meta grid: Project Type | Building Area | Date Issued

PAGE 2 — SCOPE + BUDGET TABLE
├── section_label("Scope of Work")
├── body() — 2-3 paragraph scope overview
├── section_label("Budget by CSI Division")
├── line_item_table() — div/row/subtotal rows
├── totals_block() — contingency, GC O&P, permits, grand total
├── section_label("Assumptions & Exclusions")
└── bullet() list

PAGE 3 — DOCUMENT INFO + SIGNATURE
├── section_label("Document Information")
├── info_table() — client, project, date, doc#, preparer
├── section_label("Acceptance")
├── body() — acceptance language
└── signature_block()
```

```python
def generate_estimate(
    client_name,
    project_name,
    project_address,
    estimate_number,
    date,
    prepared_by,
    prepared_by_title,
    division=None,
    scope_paragraphs=None,
    line_items=None,        # list of ("div"/"row"/"subtotal", data) tuples
    subtotal_label="Direct Construction Subtotal",
    subtotal_amount="$0",
    contingency_pct="15%",
    contingency_amount="$0",
    gc_op_pct="12%",
    gc_op_amount="$0",
    permits_amount="$0",
    grand_total="$0",
    psf_note="",
    assumptions=None,
    exclusions=None,
    output_path="./estimate.docx"
):
    division = division or COMPANY_NAME
    doc = Document()
    setup_page(doc)
    setup_header_footer(doc, division_sub=division, doc_type="Budget Estimate")

    logo_file = LOGO_MAP.get(division, LOGO_MAP["__default__"])
    logo_path = os.path.join(LOGO_DIR, logo_file)

    # ── Cover ──
    add_cover(doc,
        division_sub   = division,
        doc_type_label = "Rough Order of Magnitude — Budget Estimate",
        project_title  = project_name,
        project_addr   = project_address,
        meta_pairs     = [
            ("Project Type",  "Construction"),
            ("Estimate #",    estimate_number),
            ("Date Issued",   date),
        ],
        logo_path = logo_path,
    )
    add_page_break(doc)

    # ── Scope ──
    section_label(doc, "Scope of Work", space_before=0)
    for para in (scope_paragraphs or ["[Scope overview goes here.]"]):
        body(doc, para)

    # ── Budget table ──
    section_label(doc, "Budget by CSI Division")
    line_item_table(
        doc,
        headers    = ["Division", "Description & Scope Notes", "Est. Cost"],
        col_widths = [Inches(0.75), Inches(4.35), Inches(1.4)],
        rows       = line_items or [],
    )
    totals_block(doc,
        lines = [
            (f"Contingency — design development ({contingency_pct})", contingency_amount),
            (f"GC overhead & profit ({gc_op_pct})",                   gc_op_amount),
            ("Permits, fees & utility connections",                    permits_amount),
        ],
        grand_label  = "ROM Total",
        grand_amount = grand_total,
        sub_note     = psf_note,
    )

    # ── Assumptions ──
    section_label(doc, "Assumptions & Exclusions")
    for item in (assumptions or []):
        bullet(doc, item)
    if exclusions:
        body(doc, "Excluded from this estimate:", color=C["MUTED"], size=8.5)
        for item in exclusions:
            bullet(doc, item)

    # ── Document info + signature ──
    add_page_break(doc)
    section_label(doc, "Document Information", space_before=0)
    info_table(doc, [
        ("Client",       client_name),
        ("Project",      project_name),
        ("Address",      project_address),
        ("Estimate #",   estimate_number),
        ("Date",         date),
        ("Prepared By",  prepared_by),
    ])
    section_label(doc, "Acceptance")
    body(doc,
         f"By signing below, the client acknowledges receipt of this estimate and "
         f"authorizes {COMPANY_NAME} to proceed with pre-construction services as "
         f"outlined. This estimate is valid for 90 days from the date of issue.")
    signature_block(doc, prepared_by, prepared_by_title, division)

    doc.save(output_path)
    return output_path
```

---

## 2. Proposal

```
PAGE 1 — COVER
PAGE 2 — APPROACH (Project Understanding, Approach, Deliverables)
PAGE 3 — INVESTMENT + SIGNATURE
```

```python
def generate_proposal(
    client_name,
    project_name,
    project_address,
    date,
    prepared_by,
    prepared_by_title,
    division=None,
    understanding_paragraphs=None,
    approach_bullets=None,
    deliverables_bullets=None,
    fee_lines=None,        # [(label, amount), ...]
    total_fee="$0",
    next_steps_paragraphs=None,
    output_path="./proposal.docx"
):
    division = division or COMPANY_NAME
    doc = Document()
    setup_page(doc)
    setup_header_footer(doc, division_sub=division, doc_type="Proposal")

    logo_file = LOGO_MAP.get(division, LOGO_MAP["__default__"])
    logo_path = os.path.join(LOGO_DIR, logo_file)

    add_cover(doc,
        division_sub   = division,
        doc_type_label = "Project Proposal",
        project_title  = project_name,
        project_addr   = project_address,
        meta_pairs     = [
            ("Prepared For", client_name),
            ("Date",         date),
            ("Submitted By", prepared_by),
        ],
        logo_path = logo_path,
    )
    add_page_break(doc)

    section_label(doc, "Project Understanding", space_before=0)
    for para in (understanding_paragraphs or ["[Project understanding here.]"]):
        body(doc, para)

    section_label(doc, "Our Approach")
    for b in (approach_bullets or []):
        bullet(doc, b)

    section_label(doc, "Deliverables")
    for b in (deliverables_bullets or []):
        bullet(doc, b)

    add_page_break(doc)
    section_label(doc, "Investment", space_before=0)
    if fee_lines:
        info_table(doc, fee_lines)
    totals_block(doc, lines=[], grand_label="Total Fee", grand_amount=total_fee)

    section_label(doc, "Next Steps")
    for para in (next_steps_paragraphs or ["[Next steps here.]"]):
        body(doc, para)

    signature_block(doc, prepared_by, prepared_by_title, division)
    doc.save(output_path)
    return output_path
```

---

## 3. Report

```python
def generate_report(
    client_name,
    report_title,
    project_name,
    date,
    prepared_by,
    prepared_by_title,
    division=None,
    sections=None,   # list of {"label": str, "content": [str, ...], "bullets": [str, ...]}
    output_path="./report.docx"
):
    division = division or COMPANY_NAME
    doc = Document()
    setup_page(doc)
    setup_header_footer(doc, division_sub=division, doc_type=report_title)

    logo_file = LOGO_MAP.get(division, LOGO_MAP["__default__"])
    logo_path = os.path.join(LOGO_DIR, logo_file)

    add_cover(doc,
        division_sub   = division,
        doc_type_label = report_title,
        project_title  = project_name,
        project_addr   = client_name,
        meta_pairs     = [
            ("Prepared For", client_name),
            ("Date",         date),
            ("Prepared By",  prepared_by),
        ],
        logo_path = logo_path,
    )
    add_page_break(doc)

    first = True
    for sec in (sections or []):
        section_label(doc, sec["label"], space_before=0 if first else 28)
        first = False
        for para in sec.get("content", []):
            body(doc, para)
        for b in sec.get("bullets", []):
            bullet(doc, b)

    section_label(doc, "Document Information")
    info_table(doc, [
        ("Prepared For", client_name),
        ("Project",      project_name),
        ("Date",         date),
        ("Prepared By",  f"{prepared_by}, {division}"),
    ])
    doc.save(output_path)
    return output_path
```

---

## 4. Letter / Agreement

```python
def generate_letter(
    recipient_name,
    recipient_title,
    recipient_company,
    date,
    subject,
    body_paragraphs,
    sender_name,
    sender_title,
    division=None,
    output_path="./letter.docx"
):
    division = division or COMPANY_NAME
    doc = Document()
    setup_page(doc)
    setup_header_footer(doc, division_sub=division, doc_type="Letter")

    logo_file = LOGO_MAP.get(division, LOGO_MAP["__default__"])
    logo_path = os.path.join(LOGO_DIR, logo_file)

    # Logo
    p_logo = doc.add_paragraph()
    p_logo.paragraph_format.space_after = Pt(32)
    p_logo.add_run().add_picture(logo_path, width=Inches(1.6))

    hairline(doc, color=C["RULE"], weight=3, space_before=0, space_after=24)

    # Date
    p_date = doc.add_paragraph()
    p_date.paragraph_format.space_after = Pt(20)
    r(p_date, date, size=Pt(10), color=C["MUTED"])

    # Recipient
    info_table(doc, [
        ("To",      f"{recipient_name}, {recipient_title}"),
        ("Company", recipient_company),
        ("Re",      subject),
    ], col_widths=(0.8, 5.7))

    p_gap = doc.add_paragraph()
    p_gap.paragraph_format.space_after = Pt(8)

    # Body
    for para in body_paragraphs:
        body(doc, para)

    p_gap2 = doc.add_paragraph()
    p_gap2.paragraph_format.space_after = Pt(24)

    # Signature
    signature_block(doc, sender_name, sender_title, division)
    doc.save(output_path)
    return output_path
```

---

## 5. Sub Bid Invitation

```python
def generate_bid_invitation(
    project_name,
    project_address,
    gc_name,
    gc_contact,
    trade_name,
    bid_due_date,
    scope_items,     # list of strings
    bid_line_items,  # list of (description, unit, qty, "___") tuples
    division=None,
    output_path="./bid-invitation.docx"
):
    division = division or COMPANY_NAME
    doc = Document()
    setup_page(doc)
    setup_header_footer(doc, division_sub=division, doc_type="Bid Invitation")

    logo_file = LOGO_MAP.get(division, LOGO_MAP["__default__"])
    logo_path = os.path.join(LOGO_DIR, logo_file)

    add_cover(doc,
        division_sub   = division,
        doc_type_label = f"Subcontractor Bid Invitation — {trade_name}",
        project_title  = project_name,
        project_addr   = project_address,
        meta_pairs     = [
            ("Trade",      trade_name),
            ("Bid Due",    bid_due_date),
            ("GC Contact", gc_contact),
        ],
        logo_path = logo_path,
    )
    add_page_break(doc)

    section_label(doc, "Scope of Work", space_before=0)
    for item in scope_items:
        bullet(doc, item)

    section_label(doc, "Instructions to Bidders")
    body(doc,
         f"Please submit your complete bid to {gc_contact} by {bid_due_date}. "
         f"Include all labor, material, equipment, and applicable taxes. "
         f"Bid must remain valid for 30 days.")
    bullet(doc, "Provide unit pricing where applicable.")
    bullet(doc, "List all clarifications and exclusions separately.")
    bullet(doc, "Acknowledge receipt of all issued drawings and specifications.")

    add_page_break(doc)
    section_label(doc, "Bid Form", space_before=0)
    info_table(doc, [
        ("Project", project_name),
        ("Trade",   trade_name),
        ("Bidder",  "___________________________"),
        ("Date",    "___________________________"),
    ])

    p_gap = doc.add_paragraph()
    p_gap.paragraph_format.space_after = Pt(12)

    line_item_table(doc,
        headers    = ["#", "Description", "Unit", "Qty", "Unit Price", "Total"],
        col_widths = [Inches(0.35), Inches(2.5), Inches(0.6),
                      Inches(0.5),  Inches(1.2), Inches(1.35)],
        rows       = [("row", [str(i+1), desc, unit, str(qty), "$ ___________", "$ ___________"])
                      for i, (desc, unit, qty, _) in enumerate(bid_line_items)]
              + [("subtotal", [["Total Bid Amount"], ["$ ___________"]])],
    )
    doc.save(output_path)
    return output_path
```

---

## 6. Detailed Cost Breakdown (Internal)

```python
def generate_cost_breakdown(
    project_name,
    project_address,
    date,
    prepared_by,
    division=None,
    line_items=None,   # ("div"/"row"/"subtotal", data) — 8-col rows
    output_path="./cost-breakdown.docx"
):
    division = division or COMPANY_NAME
    doc = Document()
    setup_page(doc)
    setup_header_footer(doc, division_sub=division, doc_type="Cost Breakdown")

    logo_file = LOGO_MAP.get(division, LOGO_MAP["__default__"])
    logo_path = os.path.join(LOGO_DIR, logo_file)

    p_logo = doc.add_paragraph()
    p_logo.paragraph_format.space_after = Pt(20)
    p_logo.add_run().add_picture(logo_path, width=Inches(1.6))

    hairline(doc, color=C["RULE"], weight=3, space_before=0, space_after=16)

    info_table(doc, [
        ("Project",     project_name),
        ("Address",     project_address),
        ("Date",        date),
        ("Prepared By", prepared_by),
    ], col_widths=(1.2, 5.3))

    section_label(doc, "Detailed Cost Breakdown by CSI Division")

    # 8-column breakdown table:
    # Div | Description | Unit | Qty | Labor | Material | Sub | Total
    line_item_table(doc,
        headers    = ["Div", "Description", "Unit", "Qty",
                      "Labor", "Material", "Sub", "Total"],
        col_widths = [Inches(0.35), Inches(1.9), Inches(0.5), Inches(0.5),
                      Inches(0.7),  Inches(0.8), Inches(0.65), Inches(1.1)],
        rows       = line_items or [],
    )
    doc.save(output_path)
    return output_path
```

---

## Usage Example

```python
generate_estimate(
    client_name      = "[Client Name]",
    project_name     = "[Project Name] — [Project Type]",
    project_address  = "[Street Address, City, State ZIP · APN ##########]",
    estimate_number  = "EST-2026-001",
    date             = "April 2026",
    prepared_by      = "[Preparer Name]",
    prepared_by_title= "General Contractor",
    division         = None,  # defaults to COMPANY_NAME
    scope_paragraphs = [
        "[Two-to-three paragraphs describing the project scope, site conditions, and any premium drivers (hillside, occupied-adjacent, healthcare, etc.).]",
        "[Reference the design set, the cost basis, and the market context.]",
    ],
    line_items = [
        ("div",  "01  General Requirements"),
        ("row",  ["01",
                  ("Project management, permitting, inspections",
                   "Licensed special inspections per S.1"),
                  "$XX,XXX – $XX,XXX"]),
        ("div",  "03  Concrete"),
        ("row",  ["03",
                  ("Foundations, slab, mass walls",
                   "Premium for site conditions where applicable"),
                  "$XX,XXX – $XXX,XXX"]),
        # ... additional divisions ...
        ("subtotal", [["Direct Construction Subtotal"],
                      ["$XXX,XXX – $XXX,XXX"]]),
    ],
    subtotal_amount    = "$XXX,XXX – $XXX,XXX",
    contingency_pct    = "15%",
    contingency_amount = "$XX,XXX – $XXX,XXX",
    gc_op_pct          = "12%",
    gc_op_amount       = "$XX,XXX – $XX,XXX",
    permits_amount     = "$XX,XXX – $XX,XXX",
    grand_total        = "$XXX,XXX – $XXX,XXX",
    psf_note           = "[SF]  ·  ≈ $[X,XXX] / SF all-in  ·  [Market Context]",
    assumptions = [
        "All work shown on [Architect] [drawing set] and [Engineer] [structural set].",
        "[Site-specific premiums included or excluded.]",
        "Excluded: architect/engineering fees, Title 24 documentation, solar PV, landscaping beyond hardscape.",
        "ROM ±25–35%. Valid 90 days. Escalation not included beyond current pricing.",
    ],
    output_path = "./[project-slug]-estimate.docx"
)
```
