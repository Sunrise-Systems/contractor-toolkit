# Python Setup Reference v1.0

---

## Installation

```bash
pip install python-docx --break-system-packages
```

For PDF rendering:

```bash
pip install weasyprint --break-system-packages
```

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

## LOGO_DIR Pattern

Logos live in the sibling `contractor-brand` plugin:

```python
LOGO_DIR = os.path.join(
    os.environ.get("CLAUDE_PLUGIN_ROOT", os.getcwd()),
    "..", "contractor-brand", "skills", "brand", "assets", "logos"
)

# Fallback: bundled logos folder if contractor-brand isn't installed
if not os.path.isdir(LOGO_DIR):
    LOGO_DIR = os.path.join(
        os.environ.get("CLAUDE_PLUGIN_ROOT", os.getcwd()),
        "skills", "document-generator", "references", "logos"
    )
```

When `CLAUDE_PLUGIN_ROOT` is set (Claude Code plugin installed), logos resolve automatically. Otherwise falls back to `os.getcwd()`.

---

## Column Width Math

All tables must total exactly **6.5 inches** (8.5" page − 1" left margin − 1" right margin).

```python
# 3-column estimate table (div / description / cost)
[Inches(0.75), Inches(4.35), Inches(1.4)]    # = 6.5"

# 2-column info/key-value table
[Inches(1.6),  Inches(4.9)]                  # = 6.5"

# 2-column totals block (right-aligned, 4.2" wide)
[Inches(2.8),  Inches(1.4)]                  # = 4.2" (intentionally narrow)

# 5-column estimate with qty/unit price
[Inches(0.5),  Inches(2.8), Inches(1.0), Inches(1.1), Inches(1.1)]  # = 6.5"

# 6-column bid form
[Inches(0.35), Inches(2.5), Inches(0.6), Inches(0.5), Inches(1.2), Inches(1.35)]  # = 6.5"

# 8-column cost breakdown
[Inches(0.35), Inches(1.9), Inches(0.5), Inches(0.5),
 Inches(0.7),  Inches(0.8), Inches(0.65), Inches(1.1)]              # = 6.5"
```

Always verify column widths sum to the intended table width before running.

---

## Common Issues

### Cell shading causes black backgrounds
**Fix:** Always use `parse_xml` with `w:val="clear"`. Never use `ShadingType` enum.
```python
# CORRECT
shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="FFFFFF" w:val="clear"/>')
cell._tc.get_or_add_tcPr().append(shading)
```

### Font not sticking (renders as Calibri)
**Fix:** Set font via both API and `w:rFonts` XML. The `r()` helper does this automatically.
Always use `r()` instead of `paragraph.add_run()` directly.

### Table not full width
**Fix:** Always set `table.width = Inches(6.5)` AND set `cell.width` on each cell in the first row.

### Borders showing on borderless tables
**Fix:** Call `remove_table_borders(table)` on the table AND `remove_cell_borders(cell)` on each cell.
Then re-apply only the specific borders you want (bottom hairlines, header rules).

### Page number field not rendering
**Fix:** Must use `OxmlElement` approach. The `setup_header_footer()` helper handles this correctly.
Never try to insert page numbers via `paragraph.add_run()` text — they won't update.

### Spacing inconsistency
**Fix:** Never use empty `doc.add_paragraph()` as a spacer. Use `space_before` / `space_after` on real paragraphs.

### Custom font missing on rendering machine
**Fix:** The DOCX still embeds the font name; Word/LibreOffice falls back gracefully. For HTML, the `:root --font` variable falls back through the `{{TYPOGRAPHY_FALLBACK}}` stack automatically. If you need pixel-identical output, self-host the woff2 file or install the font system-wide before running WeasyPrint.

---

## Output

All DOCX documents saved as `.docx`. Ready for:
- PDF export via Word, Google Docs, or LibreOffice
- `libreoffice --headless --convert-to pdf filename.docx`
- Upload to PandaDoc, DocuSign

```python
doc.save(output_path)
```

HTML documents are saved alongside their PDF sibling using the `render_to_pdf()` helper from `html-to-pdf.md`.
