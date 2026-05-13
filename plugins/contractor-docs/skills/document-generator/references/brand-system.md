# Brand System — Helper Functions v1.0

Complete Python implementation of all brand constants and helper functions for the clean white-page design system. Copy everything below into any document generation script before calling generator functions. Substitute the `{{TOKEN}}` placeholders at the top of `C`, `COMPANY_NAME`, `TAGLINE`, `FONT_PRIMARY`, and `LOGO_MAP` once per contractor brand.

---

## Required Imports

```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml, OxmlElement
import os
```

---

## Brand Constants

```python
COMPANY_NAME = "{{COMPANY_NAME}}"
TAGLINE      = "{{TAGLINE}}"
FONT_PRIMARY = "{{TYPOGRAPHY_PRIMARY}}"   # DOCX falls back to Arial if not installed

C = {
    "PRIMARY":  "{{PRIMARY_COLOR}}".lstrip("#"),  # HTML hero / footer fill only
    "ACCENT":   "{{ACCENT_COLOR}}".lstrip("#"),   # optional accent
    "INK":      "{{INK_HEX}}",   # Titles, header rules, grand totals
    "BODY":     "{{BODY_HEX}}",  # All body text, table data
    "MID":      "{{MID_HEX}}",   # Supporting text, address, totals lines
    "MUTED":    "{{MUTED_HEX}}", # Section labels, col headers, meta labels
    "LIGHT":    "{{LIGHT_HEX}}", # Bullets dash, page numbers, tertiary
    "RULE":     "{{RULE_HEX}}",  # Hairline separators, row borders
    "WHITE":    "FFFFFF",         # All backgrounds — never deviate
}

# Logos live in the sibling contractor-brand plugin
LOGO_DIR = os.path.join(
    os.environ.get("CLAUDE_PLUGIN_ROOT", os.getcwd()),
    "..", "contractor-brand", "skills", "brand", "assets", "logos"
)

# Fallback: local logos folder inside this plugin if contractor-brand isn't installed
if not os.path.isdir(LOGO_DIR):
    LOGO_DIR = os.path.join(
        os.environ.get("CLAUDE_PLUGIN_ROOT", os.getcwd()),
        "skills", "document-generator", "references", "logos"
    )

# Map division / sub-brand label → logo filename.
# The "__default__" key is the fallback when no specific match exists.
LOGO_MAP = {
    "__default__":     "{{LOGO_WORDMARK}}",
    COMPANY_NAME:      "{{LOGO_WORDMARK}}",
    # Add additional sub-brand mappings here, e.g.:
    # "{{COMPANY_NAME}} Electric": "logo-electric.svg",
    # "{{COMPANY_NAME}} A&E":      "logo-arch-eng.svg",
}
```

---

## Page Setup

```python
def setup_page(doc):
    s = doc.sections[0]
    s.page_width    = Inches(8.5)
    s.page_height   = Inches(11)
    s.top_margin    = Inches(0.85)
    s.bottom_margin = Inches(0.85)
    s.left_margin   = Inches(1.0)
    s.right_margin  = Inches(1.0)
    # Printable width = 6.5". All tables must be Inches(6.5).
```

---

## Cell Shading

```python
def set_cell_shading(cell, color):
    """Always use w:val='clear'. Never use python-docx shading enum."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}" w:val="clear"/>')
    cell._tc.get_or_add_tcPr().append(shading)
```

---

## Border Helpers

```python
def remove_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def remove_cell_borders(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def set_bottom_border(cell, color=None, size=3):
    """Hairline bottom border. Use on data rows (size=3, color=RULE)
    and table header rows (size=8, color=INK)."""
    color = color or C["RULE"]
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:bottom w:val="single" w:sz="{size}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def set_top_bottom_border(cell, top_color=None, top_size=6, bot_color=None, bot_size=6):
    """Double rule — used on subtotal and grand total rows."""
    top_color = top_color or C["INK"]
    bot_color = bot_color or C["INK"]
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{top_size}" w:space="0" w:color="{top_color}"/>'
        f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'<w:bottom w:val="single" w:sz="{bot_size}" w:space="0" w:color="{bot_color}"/>'
        f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
```

---

## Cell Margins

```python
def set_cell_margins(cell, top=60, bottom=60, left=0, right=0):
    """Set cell padding in twips (1440 twips = 1 inch)."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    margins = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(margins)
```

---

## Text Run Helper

```python
def r(p, text, font=None, size=Pt(10), color=None, bold=False, italic=False):
    """
    Add a formatted text run. Always sets font via both API and XML.
    Never pass kern/tracking — natural type spacing only.
    """
    font  = font  or FONT_PRIMARY
    color = color or C["BODY"]
    run = p.add_run(text)
    run.font.name  = font
    run.font.size  = size
    run.font.color.rgb = RGBColor.from_string(color)
    run.font.bold  = bold
    run.font.italic = italic
    el  = run._element
    rPr = el.get_or_add_rPr()
    rf  = rPr.find(qn('w:rFonts'))
    if rf is None:
        rPr.append(parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font}" w:hAnsi="{font}"/>'))
    else:
        rf.set(qn('w:ascii'), font)
        rf.set(qn('w:hAnsi'), font)
    return run
```

---

## Hairline Rule

```python
def hairline(doc, color=None, weight=3, space_before=0, space_after=0):
    """
    Thin paragraph bottom-border rule. Used as section dividers and after section labels.
    Default: RULE at weight 3. Never use heavier rules for decoration.
    """
    color = color or C["RULE"]
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    pPr = p._element.get_or_add_pPr()
    pPr.append(parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="{weight}" w:space="1" w:color="{color}"/>'
        f'</w:pBdr>'
    ))
    r(p, "", size=Pt(2))
    return p
```

---

## Cover Page

```python
def add_cover(doc, division_sub, doc_type_label, project_title,
              project_addr, meta_pairs, logo_path):
    """
    White cover page. Logo image top-left at Inches(1.6).
    Hairline rule divides logo from project info.
    Meta grid (3 columns) at bottom.

    division_sub:   sub-brand or division name (e.g. "General Construction")
    doc_type_label: e.g. "Rough Order of Magnitude — Budget Estimate"
    project_title:  e.g. "[Project Name] — [Project Type]"
    project_addr:   e.g. "[Address, City, State ZIP  ·  APN #########]"
    meta_pairs:     [(label, value), ...] — typically 3 items
    logo_path:      full path to logo file
    """
    # Logo — single image, compact, top-left
    p_logo = doc.add_paragraph()
    p_logo.paragraph_format.space_before = Pt(0)
    p_logo.paragraph_format.space_after  = Pt(40)
    p_logo.add_run().add_picture(logo_path, width=Inches(1.6))

    # Hairline rule
    hairline(doc, color=C["RULE"], weight=3, space_before=0, space_after=28)

    # Doc type label
    p_type = doc.add_paragraph()
    p_type.paragraph_format.space_after = Pt(10)
    r(p_type, doc_type_label, size=Pt(9), color=C["MUTED"])

    # Project title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(8)
    r(p_title, project_title, size=Pt(26), color=C["INK"], bold=True)

    # Address / subtitle
    p_addr = doc.add_paragraph()
    p_addr.paragraph_format.space_after = Pt(48)
    r(p_addr, project_addr, size=Pt(10), color=C["MID"])

    # Meta grid
    hairline(doc, color=C["RULE"], weight=3, space_before=0, space_after=16)

    cols = len(meta_pairs)
    t = doc.add_table(rows=1, cols=cols)
    t.width = Inches(6.5)
    remove_table_borders(t)
    for i, (label, value) in enumerate(meta_pairs):
        c = t.cell(0, i)
        c.width = Inches(6.5 / cols)
        set_cell_shading(c, C["WHITE"])
        set_cell_margins(c, top=40, bottom=40, left=0, right=80)
        remove_cell_borders(c)
        p_lbl = c.paragraphs[0]
        p_lbl.paragraph_format.space_after = Pt(3)
        r(p_lbl, label, size=Pt(8), color=C["MUTED"])
        p_val = c.add_paragraph()
        p_val.paragraph_format.space_after = Pt(0)
        r(p_val, value, size=Pt(11), color=C["INK"])
```

---

## Section Label

```python
def section_label(doc, text, space_before=28, space_after=14):
    """
    Small muted label text followed by a RULE hairline.
    This is the only visual section divider — no bold headers, no large type.
    """
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(5)
    r(p, text, size=Pt(8.5), color=C["MUTED"])
    hairline(doc, color=C["RULE"], weight=3, space_before=0, space_after=space_after)
```

---

## Body Text

```python
def body(doc, text, color=None, size=10, space_after=8):
    color = color or C["BODY"]
    p = doc.add_paragraph()
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.line_spacing = Pt(15)
    r(p, text, size=Pt(size), color=color)
    return p
```

---

## Bullet

```python
def bullet(doc, text, space_after=5):
    """Em-dash bullet. Dash in LIGHT, text in BODY."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.left_indent  = Inches(0.15)
    p.paragraph_format.line_spacing = Pt(14)
    r(p, "—  ", size=Pt(10), color=C["LIGHT"])
    r(p, text,  size=Pt(10), color=C["BODY"])
    return p
```

---

## Info Table (Key-Value)

```python
def info_table(doc, pairs, col_widths=(1.6, 4.9)):
    """
    Borderless key-value table. Each row has a RULE hairline below.
    Used for document metadata, project info, contact details.

    pairs: [("Client", "ABC Corp"), ("Date", "April 2026"), ...]
    """
    t = doc.add_table(rows=len(pairs), cols=2)
    t.width = Inches(6.5)
    remove_table_borders(t)
    for i, (k, v) in enumerate(pairs):
        kc = t.cell(i, 0)
        vc = t.cell(i, 1)
        kc.width = Inches(col_widths[0])
        vc.width = Inches(col_widths[1])
        set_cell_margins(kc, top=36, bottom=36, left=0, right=80)
        set_cell_margins(vc, top=36, bottom=36, left=0, right=0)
        for c in (kc, vc):
            set_cell_shading(c, C["WHITE"])
            remove_cell_borders(c)
            set_bottom_border(c, color=C["RULE"], size=3)
        r(kc.paragraphs[0], k, size=Pt(8.5), color=C["MUTED"])
        r(vc.paragraphs[0], v, size=Pt(10),  color=C["INK"])
    return t
```

---

## Line Item Table

```python
def line_item_table(doc, headers, rows, col_widths):
    """
    CSI-style line item table. Three row types:

      ("div",      "03  Concrete")
          — Division group header. Light number, regular-weight label text.

      ("row",      ["03", ("Main description", "Sub-note text"), "$55,000"])
          — Data row. Cell content can be a string or (main, note) tuple.
            Last column right-aligns. Each row has RULE bottom hairline.

      ("subtotal", [["Direct Construction Subtotal"], ["$512,000 – $679,000"]])
          — Subtotal row. Bold, top+bottom INK rules.

    headers:    list of column header strings
    col_widths: list of Inches() values summing to Inches(6.5)
    """
    num_cols = len(headers)
    t = doc.add_table(rows=1 + len(rows), cols=num_cols)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.width = Inches(6.5)
    remove_table_borders(t)

    # ── Header row ──
    hrow = t.rows[0]
    for j, h in enumerate(headers):
        c = hrow.cells[j]
        c.width = col_widths[j]
        set_cell_shading(c, C["WHITE"])
        set_cell_margins(c, top=80, bottom=80, left=0, right=60)
        remove_cell_borders(c)
        set_bottom_border(c, color=C["INK"], size=8)
        p = c.paragraphs[0]
        if j == num_cols - 1:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r(p, h.upper(), size=Pt(8), color=C["MUTED"])

    # ── Data rows ──
    for i, row_data in enumerate(rows):
        tr = t.rows[i + 1]
        kind = row_data[0]

        if kind == "div":
            for j in range(num_cols):
                c = tr.cells[j]
                c.width = col_widths[j]
                set_cell_shading(c, C["WHITE"])
                set_cell_margins(c, top=120, bottom=40, left=0, right=60)
                remove_cell_borders(c)
            p = tr.cells[0].paragraphs[0]
            label = row_data[1]
            num_part  = label[:2].strip()
            rest_part = label[2:].strip()
            r(p, num_part + "  ", size=Pt(8.5), color=C["LIGHT"])
            r(p, rest_part,       size=Pt(8.5), color=C["MID"])

        elif kind == "subtotal":
            for j in range(num_cols):
                c = tr.cells[j]
                c.width = col_widths[j]
                set_cell_shading(c, C["WHITE"])
                set_cell_margins(c, top=110, bottom=110, left=0, right=60)
                remove_cell_borders(c)
                set_top_bottom_border(c, top_color=C["INK"], top_size=6,
                                         bot_color=C["INK"], bot_size=6)
            p0 = tr.cells[0].paragraphs[0]
            r(p0, row_data[1][0][0], size=Pt(10.5), color=C["INK"], bold=True)
            p_last = tr.cells[-1].paragraphs[0]
            p_last.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r(p_last, row_data[1][-1][0], size=Pt(10.5), color=C["INK"], bold=True)

        else:  # "row"
            cells_data = row_data[1]
            for j, cell_text in enumerate(cells_data):
                c = tr.cells[j]
                c.width = col_widths[j]
                set_cell_shading(c, C["WHITE"])
                set_cell_margins(c, top=90, bottom=90, left=0, right=60)
                remove_cell_borders(c)
                set_bottom_border(c, color=C["RULE"], size=3)
                p = c.paragraphs[0]
                p.paragraph_format.line_spacing = Pt(14)
                if j == len(cells_data) - 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                if isinstance(cell_text, tuple):
                    r(p, cell_text[0], size=Pt(10), color=C["BODY"])
                    if cell_text[1]:
                        p2 = c.add_paragraph()
                        p2.paragraph_format.space_after  = Pt(0)
                        p2.paragraph_format.line_spacing = Pt(13)
                        r(p2, cell_text[1], size=Pt(8.5), color=C["MUTED"])
                else:
                    r(p, str(cell_text), size=Pt(10), color=C["BODY"])
    return t
```

---

## Totals Block

```python
def totals_block(doc, lines, grand_label, grand_amount, sub_note=""):
    """
    Right-aligned totals summary. Supporting lines above, grand total below double rule.
    """
    p_wrap = doc.add_paragraph()
    p_wrap.paragraph_format.space_before = Pt(24)
    p_wrap.paragraph_format.space_after  = Pt(0)

    # Supporting lines
    if lines:
        t = doc.add_table(rows=len(lines), cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.RIGHT
        t.width = Inches(4.2)
        remove_table_borders(t)
        for i, (lbl, amt) in enumerate(lines):
            lc = t.cell(i, 0)
            rc = t.cell(i, 1)
            lc.width = Inches(2.8)
            rc.width = Inches(1.4)
            for c in (lc, rc):
                set_cell_shading(c, C["WHITE"])
                set_cell_margins(c, top=40, bottom=40, left=0, right=0)
                remove_cell_borders(c)
                set_bottom_border(c, color=C["RULE"], size=3)
            r(lc.paragraphs[0], lbl, size=Pt(9.5), color=C["MID"])
            p_r = rc.paragraphs[0]
            p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            r(p_r, amt, size=Pt(9.5), color=C["BODY"])

    # Grand total
    t2 = doc.add_table(rows=1, cols=2)
    t2.alignment = WD_TABLE_ALIGNMENT.RIGHT
    t2.width = Inches(4.2)
    remove_table_borders(t2)
    gl = t2.cell(0, 0)
    gr = t2.cell(0, 1)
    gl.width = Inches(2.8)
    gr.width = Inches(1.4)
    for c in (gl, gr):
        set_cell_shading(c, C["WHITE"])
        set_cell_margins(c, top=110, bottom=60, left=0, right=0)
        remove_cell_borders(c)
        set_top_bottom_border(c, top_color=C["INK"], top_size=8,
                                 bot_color=C["INK"], bot_size=8)
    r(gl.paragraphs[0], grand_label,  size=Pt(14), color=C["INK"], bold=True)
    p_gr = gr.paragraphs[0]
    p_gr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r(p_gr, grand_amount, size=Pt(14), color=C["INK"], bold=True)

    if sub_note:
        p_note = doc.add_paragraph()
        p_note.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_note.paragraph_format.space_before = Pt(6)
        p_note.paragraph_format.space_after  = Pt(0)
        r(p_note, sub_note, size=Pt(8), color=C["MUTED"])
```

---

## Signature Block

```python
def signature_block(doc, signer_name, signer_title, company):
    """Two-column signature block with hairline signature lines."""
    t = doc.add_table(rows=1, cols=2)
    t.width = Inches(6.5)
    remove_table_borders(t)

    for col_idx in range(2):
        c = t.cell(0, col_idx)
        c.width = Inches(3.25)
        set_cell_shading(c, C["WHITE"])
        set_cell_margins(c, top=200, bottom=120, left=0, right=120)
        remove_cell_borders(c)

    left = t.cell(0, 0)
    p1 = left.paragraphs[0]
    p1.paragraph_format.space_after = Pt(30)
    r(p1, "Authorized Signature", size=Pt(8.5), color=C["MUTED"])
    p2 = left.add_paragraph()
    pPr = p2._element.get_or_add_pPr()
    pPr.append(parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="4" w:space="1" w:color="{C["RULE"]}"/>'
        f'</w:pBdr>'
    ))
    p2.paragraph_format.space_after = Pt(8)
    r(p2, "", size=Pt(10))
    p3 = left.add_paragraph()
    r(p3, signer_name, size=Pt(10), color=C["INK"], bold=True)
    p4 = left.add_paragraph()
    r(p4, f"{signer_title}, {company}", size=Pt(9), color=C["MUTED"])

    right = t.cell(0, 1)
    p5 = right.paragraphs[0]
    p5.paragraph_format.space_after = Pt(30)
    r(p5, "Client Signature", size=Pt(8.5), color=C["MUTED"])
    p6 = right.add_paragraph()
    pPr6 = p6._element.get_or_add_pPr()
    pPr6.append(parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="4" w:space="1" w:color="{C["RULE"]}"/>'
        f'</w:pBdr>'
    ))
    p6.paragraph_format.space_after = Pt(8)
    r(p6, "", size=Pt(10))
    p7 = right.add_paragraph()
    r(p7, "[Client Name]", size=Pt(10), color=C["INK"], bold=True)
    p8 = right.add_paragraph()
    r(p8, "[Title, Company]", size=Pt(9), color=C["MUTED"])
    return t
```

---

## Header & Footer

```python
def setup_header_footer(doc, division_sub=None, doc_type="Document"):
    """
    Running header: right-aligned "{{COMPANY_NAME}}  ·  DOC TYPE" in LIGHT.
    Footer: "{{COMPANY_NAME}}  {{TAGLINE / DIVISION}}" left, "Page N" right.
    """
    division_sub = division_sub or TAGLINE
    for section in doc.sections:
        # Header
        header = section.header
        header.is_linked_to_previous = False
        hp = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        hp.clear()
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r(hp, f"{COMPANY_NAME.upper()}  ·  {doc_type.upper()}",
          size=Pt(7.5), color=C["LIGHT"])

        # Footer
        footer = section.footer
        footer.is_linked_to_previous = False
        fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        fp.clear()
        r(fp, COMPANY_NAME.upper(), size=Pt(8), color=C["INK"], bold=True)
        r(fp, f"   {division_sub.upper()}", size=Pt(8), color=C["MUTED"])

        fp.paragraph_format.tab_stops.add_tab_stop(Inches(6.5), WD_ALIGN_PARAGRAPH.RIGHT)
        r(fp, "\tPage ", size=Pt(8), color=C["LIGHT"])

        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')
        r1 = fp.add_run(); r1._r.append(fldChar1)

        instrText = OxmlElement('w:instrText')
        instrText.set(qn('xml:space'), 'preserve')
        instrText.text = ' PAGE '
        r2 = fp.add_run()
        r2.font.size = Pt(8)
        r2.font.color.rgb = RGBColor.from_string(C["LIGHT"])
        r2.font.name = FONT_PRIMARY
        r2._r.append(instrText)

        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'end')
        r3 = fp.add_run(); r3._r.append(fldChar2)
```

---

## Page Break

```python
def add_page_break(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run().add_break(WD_BREAK.PAGE)
```

---

## Design Checklist

Before finalizing any document, verify:

- [ ] All cell backgrounds are `FFFFFF` — no gray, no tinted fills
- [ ] No letter-spacing/kern on any text run
- [ ] Logo appears only on cover page at `Inches(1.6)`
- [ ] No "Black" / display weight body type — bold of the primary face only
- [ ] Table headers: white bg, muted uppercase text, heavy INK bottom border
- [ ] Data rows: white bg, RULE hairline bottom border
- [ ] Subtotal rows: INK top + bottom border, bold text
- [ ] Section labels: muted small text followed immediately by hairline
- [ ] All tables are `Inches(6.5)` wide, column widths sum to 6.5"
- [ ] Footer has `COMPANY_NAME` wordmark left, page number right
- [ ] No empty paragraphs used as spacers
