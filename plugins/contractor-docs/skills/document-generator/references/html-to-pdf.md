# HTML → PDF Rendering

Convert a generated HTML document to PDF in a single Python call. Every command that produces HTML should also produce the PDF sibling in the same working directory.

---

## Primary Path — WeasyPrint (pure Python, no browser required)

**Install once:**

```bash
pip install weasyprint --break-system-packages
```

On macOS you may also need:
```bash
brew install pango gdk-pixbuf libffi
```

**Usage:**

```python
def render_html_to_pdf(html_path, pdf_path=None):
    """
    Render an HTML document to PDF using WeasyPrint.
    Preserves @page margin rules, flat hairline layouts, and tonal Gantt bars.

    Args:
        html_path: path to the generated .html file
        pdf_path: optional output path; defaults to replacing .html with .pdf

    Returns: the PDF path written to disk
    """
    from weasyprint import HTML
    import os

    if pdf_path is None:
        pdf_path = os.path.splitext(html_path)[0] + ".pdf"

    # base_url is the directory of the HTML so relative assets resolve
    base = os.path.dirname(os.path.abspath(html_path))
    HTML(filename=html_path, base_url=base).write_pdf(pdf_path)
    return pdf_path
```

**Why WeasyPrint:**
- No browser required — runs in any Python environment
- Excellent `@page` margin support — matches our `@page { margin: 0 }` rule exactly
- Supports CSS Grid, Flexbox, `letter-spacing`, `text-transform` — all the CSS we use
- Preserves print colors perfectly with `print-color-adjust: exact`
- Fast — renders a typical ROM in under 2 seconds

**Caveats:**
- Custom fonts may fall back if the primary typeface isn't installed system-wide. Still looks correct via the fallback stack.
- Very old WeasyPrint (<60) didn't support CSS Grid. Require version ≥ 60.

---

## Fallback Path — Chrome Headless

Use this when WeasyPrint can't be installed (rare) or when you need pixel-identical output to what the user sees in the browser.

```python
def render_html_to_pdf_chrome(html_path, pdf_path=None):
    """
    Render HTML to PDF using Chrome/Chromium in headless mode.
    Produces pixel-identical output to what you see in the browser.

    Args:
        html_path: path to the generated .html file
        pdf_path: optional output path; defaults to replacing .html with .pdf
    """
    import os, shutil, subprocess

    if pdf_path is None:
        pdf_path = os.path.splitext(html_path)[0] + ".pdf"

    # Locate Chrome or Chromium
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("chrome"),
    ]
    chrome = next((c for c in candidates if c and os.path.exists(c)), None)
    if not chrome:
        raise RuntimeError(
            "No Chrome/Chromium/Edge found. Install one or use WeasyPrint."
        )

    subprocess.run([
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",       # suppresses URL/page-counter chrome
        f"--print-to-pdf={pdf_path}",
        f"file://{os.path.abspath(html_path)}",
    ], check=True, capture_output=True)
    return pdf_path
```

---

## Unified Helper (with automatic fallback)

Drop this into every document-generating script. Tries WeasyPrint first, falls back to Chrome headless.

```python
def render_to_pdf(html_path, pdf_path=None):
    """
    Render HTML to PDF. Tries WeasyPrint first, Chrome headless as fallback.
    Raises RuntimeError if neither is available.
    """
    import os

    if pdf_path is None:
        pdf_path = os.path.splitext(html_path)[0] + ".pdf"

    # Try WeasyPrint first
    try:
        from weasyprint import HTML
        base = os.path.dirname(os.path.abspath(html_path))
        HTML(filename=html_path, base_url=base).write_pdf(pdf_path)
        return pdf_path
    except ImportError:
        pass

    # Fall back to Chrome headless
    try:
        return render_html_to_pdf_chrome(html_path, pdf_path)
    except (RuntimeError, FileNotFoundError, Exception) as e:
        raise RuntimeError(
            f"Could not render PDF. Install WeasyPrint (`pip install weasyprint "
            f"--break-system-packages`) or ensure Chrome/Chromium is available. "
            f"Underlying error: {e}"
        )
```

---

## Standard Generate-and-Render Pattern

Every HTML-producing command follows this pattern:

```python
def generate_rom(project_data, output_dir="."):
    """
    Generate a ROM — produces both HTML and PDF in the output directory.
    Returns (html_path, pdf_path).
    """
    import os

    company_slug = project_data["company_slug"]    # e.g. "acme"
    slug = project_data["slug"]
    date = project_data["date_yyyy_mm"]
    html_path = os.path.join(output_dir, f"{company_slug}_rom_{slug}_{date}.html")
    pdf_path  = os.path.join(output_dir, f"{company_slug}_rom_{slug}_{date}.pdf")

    # 1. Generate HTML from template
    html_content = render_rom_template(project_data)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # 2. Render PDF from the HTML
    render_to_pdf(html_path, pdf_path)

    return html_path, pdf_path
```

User sees TWO files in the working directory — the HTML (for browser review / sharing / further editing) and the PDF (ready to send).

---

## Verifying the Output

After rendering, verify:

1. **File size** — a valid PDF is 20KB+; a failed render is often < 5KB or empty
2. **No URL chrome** — open the PDF and confirm the file path doesn't appear in the margin
3. **Page breaks** — confirm the cover, footer, and tables don't split awkwardly (the print CSS should handle this, but check)
4. **Colors** — confirm the hero block is solid `{{PRIMARY_COLOR}}`, not faded (caused by `print-color-adjust` not applying)

If any of the above fails, check that the HTML includes the mandatory `@media print` block from `html-canonical.md`.

---

## When Users Don't Have Python or a Browser

Fall back to the built-in browser print button. Every generated HTML includes a `<button class="print-btn" onclick="window.print()">↓ Print / Save as PDF</button>` — users can always open the HTML in any browser and click it. The mandatory `@page { margin: 0 }` CSS ensures the URL chrome stays hidden.

This is the universal fallback — no install, no Python, no dependencies.
