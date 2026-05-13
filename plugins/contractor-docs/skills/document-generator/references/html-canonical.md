# HTML Canonical CSS — v1.0

Copy this entire `<style>` block verbatim into every HTML document the skill generates. Substitute the `{{TOKEN}}` placeholders once in the `:root` block at the top — everywhere else uses CSS variables and inherits automatically. If you need a new pattern, add it to this file so all documents get it.

---

## The Mandatory `<style>` Block

```html
<style>
  /* ─── BRAND TOKENS (the only place to swap values) ──────────────────── */
  :root {
    --primary: {{PRIMARY_COLOR}};
    --accent:  {{ACCENT_COLOR}};
    --ink:     #{{INK_HEX}};
    --body:    #{{BODY_HEX}};
    --mid:     #{{MID_HEX}};
    --muted:   #{{MUTED_HEX}};
    --light:   #{{LIGHT_HEX}};
    --rule:    #{{RULE_HEX}};
    --bg:      #FFFFFF;
    --font:    '{{TYPOGRAPHY_PRIMARY}}', {{TYPOGRAPHY_FALLBACK}};
  }

  /* ─── RESET ─────────────────────────────────────────────────────────── */
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: var(--font); color: var(--ink); background: var(--bg); }
  .wordmark {
    font-family: var(--font);
    font-weight: 700; text-transform: uppercase; letter-spacing: -0.01em;
  }
  .wrap { max-width: 900px; margin: 0 auto; padding: 0; background: var(--bg); }

  /* ─── COVER (PRIMARY HERO) ──────────────────────────────────────────── */
  .cover { background: var(--primary); color: #fff; padding: 56px 56px 44px; }
  .cover-tag {
    font-size: 11px; letter-spacing: 0.14em; color: var(--muted);
    text-transform: uppercase; margin-bottom: 28px;
    border-bottom: 0.5px solid rgba(255,255,255,0.15); padding-bottom: 14px;
  }
  .cover-logo {
    font-size: 56px; font-weight: 700; letter-spacing: -0.025em;
    color: #fff; line-height: 0.95; margin-bottom: 6px; text-transform: uppercase;
  }
  .cover-sub {
    font-size: 12px; color: var(--muted); letter-spacing: 0.1em;
    text-transform: uppercase; margin-bottom: 36px; font-weight: 400;
  }
  .cover-title { font-size: 22px; font-weight: 500; color: #fff; line-height: 1.3; margin-bottom: 8px; }
  .cover-addr { font-size: 13px; color: rgba(255,255,255,0.65); margin-bottom: 36px; }
  .cover-meta {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 0;
    border-top: 0.5px solid rgba(255,255,255,0.15); padding-top: 22px;
  }
  .cover-meta-item label {
    font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase;
    color: rgba(255,255,255,0.55); display: block; margin-bottom: 6px;
  }
  .cover-meta-item span { font-size: 14px; color: #fff; font-weight: 500; }

  /* Optional accent stripe — drop just below the cover for branded contexts */
  .cover-accent { height: 4px; background: var(--accent); }

  /* ─── SECTIONS ──────────────────────────────────────────────────────── */
  .section { padding: 36px 56px; border-bottom: 0.5px solid var(--rule); }
  .section:last-child { border-bottom: none; }
  .section-label {
    font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 18px; padding-bottom: 10px;
    border-bottom: 0.5px solid var(--rule); font-weight: 500;
  }

  /* ─── SCOPE GRID (FLAT, HAIRLINES — NOT CARDS) ──────────────────────── */
  .scope-grid { display: grid; grid-template-columns: 1fr 1fr; column-gap: 28px; row-gap: 0; }
  .scope-item { padding: 16px 0; border-bottom: 0.5px solid var(--rule); }
  .scope-item strong {
    font-size: 10px; font-weight: 500; color: var(--muted);
    display: block; margin-bottom: 8px;
    letter-spacing: 0.12em; text-transform: uppercase;
  }
  .scope-item span { font-size: 13px; color: var(--ink); line-height: 1.55; display: block; }
  .scope-grid .scope-item:nth-last-child(-n+2) { border-bottom: none; }
  .scope-grid .scope-item:nth-last-child(1):nth-child(odd) { border-bottom: 0.5px solid var(--rule); }

  /* ─── NOTICE BLOCK (PRIMARY CALLOUT) ────────────────────────────────── */
  .notice { background: var(--primary); color: #fff; border-radius: 6px; padding: 16px 18px; font-size: 12px; line-height: 1.65; }
  .notice-label {
    font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 8px; font-weight: 500;
  }

  /* ─── CSI BUDGET TABLE ──────────────────────────────────────────────── */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  thead tr { border-bottom: 1.5px solid var(--ink); }
  thead th {
    text-align: left; padding: 10px 0; font-size: 10px; font-weight: 500;
    letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted);
  }
  thead th:last-child { text-align: right; }
  tbody tr { border-bottom: 0.5px solid var(--rule); }
  tbody tr:last-child { border-bottom: none; }
  tbody td { padding: 12px 0; vertical-align: top; color: var(--ink); line-height: 1.45; }
  tbody td:last-child { text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
  .div-header td {
    font-size: 11px; font-weight: 600; text-transform: uppercase;
    letter-spacing: 0.08em; color: var(--mid); background: #f5f5f5;
    padding: 8px 10px; border-bottom: none;
  }
  .div-num { font-size: 11px; color: var(--light); margin-right: 10px; font-weight: 400; }
  .div-desc { font-size: 13px; color: var(--ink); line-height: 1.5; }
  .div-note { font-size: 11px; color: var(--mid); display: block; margin-top: 4px; line-height: 1.55; }
  .subtotal-row td { font-weight: 600; font-size: 13px; padding: 14px 0; border-bottom: 1.5px solid var(--ink); color: var(--ink); }

  /* ─── TOTALS BLOCK ──────────────────────────────────────────────────── */
  .total-block { display: flex; justify-content: flex-end; padding-top: 24px; }
  .total-inner { text-align: right; min-width: 320px; }
  .total-line { display: flex; justify-content: space-between; font-size: 13px; color: var(--mid); padding: 5px 0; gap: 40px; }
  .total-line strong { color: var(--ink); font-weight: 500; }
  .total-grand {
    display: flex; justify-content: space-between; font-size: 22px;
    font-weight: 700; color: var(--ink); padding: 14px 0 0;
    border-top: 1.5px solid var(--ink); margin-top: 10px; gap: 40px; letter-spacing: -0.01em;
  }
  /* Optional: swap the grand-total top rule to the accent color */
  .total-grand.accented { border-top-color: var(--accent); }
  .total-sub { font-size: 11px; color: var(--muted); margin-top: 6px; text-align: right; }

  /* ─── TIMELINE (GANTT-STYLE WITH TONAL BARS) ────────────────────────── */
  .tl-wrap { overflow-x: auto; }
  .tl-label { padding: 12px 0 4px; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); }
  .tl-row td { padding: 8px 4px; }
  .tl-bar { height: 7px; background: var(--ink); border-radius: 2px; }
  .tl-bar-a { background: var(--ink); }
  .tl-bar-b { background: var(--body); }
  .tl-bar-c { background: var(--mid); }
  .tl-bar-d { background: var(--light); }
  .tl-legend { display: flex; gap: 22px; margin-top: 18px; flex-wrap: wrap; }
  .tl-legend-item { display: flex; align-items: center; gap: 8px; font-size: 11px; color: var(--mid); }
  .tl-legend-swatch { width: 22px; height: 7px; border-radius: 2px; }
  .tl-note { font-size: 11px; color: var(--muted); margin-top: 12px; line-height: 1.55; }

  /* ─── FOOTER (PRIMARY, MATCHES COVER) ───────────────────────────────── */
  .footer { background: var(--primary); color: #fff; padding: 28px 56px; display: flex; justify-content: space-between; align-items: center; }
  .footer-logo { font-size: 22px; font-weight: 700; letter-spacing: -0.02em; text-transform: uppercase; line-height: 1; }
  .footer-sub { font-size: 11px; color: rgba(255,255,255,0.55); margin-top: 4px; letter-spacing: 0.02em; }
  .footer-note { font-size: 10.5px; color: rgba(255,255,255,0.55); text-align: right; line-height: 1.7; }

  /* ─── PRINT CTA ─────────────────────────────────────────────────────── */
  .print-btn {
    display: block; margin: 0 56px 28px; padding: 14px 24px;
    background: var(--primary); color: #fff;
    font-family: var(--font);
    font-size: 12px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
    border: none; cursor: pointer; border-radius: 4px; width: calc(100% - 112px);
  }
  .print-btn:hover { background: var(--ink); }

  /* ─── PRINT (MANDATORY — HIDES BROWSER URL/PAGE-NUMBER CHROME) ──────── */
  @media print {
    @page { size: 8.5in 11in; margin: 0; }
    html, body { margin: 0; padding: 0; }
    .print-btn { display: none; }
    * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .wrap { max-width: none; }
    .section, .cover, .footer { page-break-inside: avoid; }
    .cover, .footer { break-inside: avoid; }
    table { page-break-inside: auto; }
    tr    { page-break-inside: avoid; page-break-after: auto; }
  }

  /* ─── RESPONSIVE (MOBILE COLLAPSE) ──────────────────────────────────── */
  @media (max-width: 600px) {
    .cover, .section, .footer { padding-left: 28px; padding-right: 28px; }
    .print-btn { margin-left: 28px; margin-right: 28px; width: calc(100% - 56px); }
    .scope-grid { grid-template-columns: 1fr; column-gap: 0; }
    .scope-grid .scope-item:nth-last-child(-n+2) { border-bottom: 0.5px solid var(--rule); }
    .scope-grid .scope-item:last-child { border-bottom: none; }
    .cover-meta { grid-template-columns: 1fr; gap: 14px; }
    .footer { flex-direction: column; align-items: flex-start; gap: 16px; }
    .footer-note { text-align: left; }
  }
</style>
```

---

## Markup Skeleton

Every generated HTML document follows this structure:

```html
<div class="wrap">

  <!-- COVER (primary hero) -->
  <div class="cover">
    <div class="cover-tag">[Document Type] — [Subtitle]</div>
    <div class="cover-logo wordmark">{{COMPANY_NAME}}</div>
    <div class="cover-sub">{{TAGLINE}}</div>
    <div class="cover-title">[Project Title]</div>
    <div class="cover-addr">[Address / APN]</div>
    <div class="cover-meta">
      <div class="cover-meta-item">
        <label>[Label 1]</label><span>[Value 1]</span>
      </div>
      <div class="cover-meta-item">
        <label>[Label 2]</label><span>[Value 2]</span>
      </div>
      <div class="cover-meta-item">
        <label>[Label 3]</label><span>[Value 3]</span>
      </div>
    </div>
  </div>
  <div class="cover-accent"></div>  <!-- optional accent stripe -->

  <!-- SCOPE OF WORK (flat hairline grid) -->
  <div class="section">
    <div class="section-label">Scope of Work</div>
    <div class="scope-grid">
      <div class="scope-item">
        <strong>[Scope Label]</strong>
        <span>[Scope body text]</span>
      </div>
      <!-- ... 4–6 items total ... -->
    </div>
  </div>

  <!-- NOTICE (optional, primary callout) -->
  <div class="section" style="padding-top:20px; padding-bottom:20px;">
    <div class="notice">
      <div class="notice-label">[Notice Label]</div>
      [Notice body — premium explanation, coordination note, etc.]
    </div>
  </div>

  <!-- CSI BUDGET TABLE -->
  <div class="section">
    <div class="section-label">Budget by CSI Division</div>
    <table>
      <thead>
        <tr>
          <th style="width:64px;">Division</th>
          <th>Description &amp; Scope Notes</th>
          <th style="width:130px;">Est. Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr class="div-header">
          <td colspan="3"><span class="div-num">01</span>General Requirements</td>
        </tr>
        <tr>
          <td></td>
          <td class="div-desc">[Description]
            <span class="div-note">[Note line]</span>
          </td>
          <td>[Cost Range]</td>
        </tr>
        <!-- ... more division headers and rows ... -->
        <tr class="subtotal-row">
          <td colspan="2">Direct Construction Subtotal</td>
          <td>[Subtotal]</td>
        </tr>
      </tbody>
    </table>

    <!-- TOTALS -->
    <div class="total-block">
      <div class="total-inner">
        <div class="total-line"><span>[Line Label]</span><strong>[Amount]</strong></div>
        <!-- ... -->
        <div class="total-grand">
          <span>[Grand Total Label]</span>
          <span>[Grand Total Amount]</span>
        </div>
        <div class="total-sub">[SF · $/SF · Market Context]</div>
      </div>
    </div>
  </div>

  <!-- ASSUMPTIONS & EXCLUSIONS -->
  <div class="section">
    <div class="section-label">Assumptions &amp; Exclusions</div>
    <div class="scope-grid">
      <div class="scope-item">
        <strong>Included</strong>
        <span>[Included items]</span>
      </div>
      <div class="scope-item">
        <strong>Excluded</strong>
        <span>[Excluded items]</span>
      </div>
      <div class="scope-item">
        <strong>Basis of Estimate</strong>
        <span>[Cost sources, market context]</span>
      </div>
      <div class="scope-item">
        <strong>Validity</strong>
        <span>[Range, duration, escalation notes]</span>
      </div>
    </div>
  </div>

  <!-- TIMELINE GANTT -->
  <div class="section">
    <div class="section-label">Projected Construction Schedule — [Duration]</div>
    <div class="tl-wrap">
      <table><!-- phase rows with .tl-bar cells --></table>
    </div>
    <div class="tl-legend"><!-- swatches + labels --></div>
  </div>

  <!-- PRINT BUTTON -->
  <button class="print-btn" onclick="window.print()">↓ Print / Save as PDF</button>

  <!-- FOOTER (primary) -->
  <div class="footer">
    <div>
      <div class="footer-logo wordmark">{{COMPANY_NAME}}</div>
      <div class="footer-sub">{{TAGLINE}}</div>
    </div>
    <div class="footer-note">
      Prepared for: [Client Name]<br>
      Architect of Record: [Architect Firm]<br>
      [Document disclaimer]
    </div>
  </div>

</div>
```

---

## Generation Workflow

1. **Copy the full `<style>` block verbatim.** Substitute brand tokens in the `:root` block once.
2. **Substitute only content** in the markup — cover metadata, scope items, notice body, CSI rows, totals, assumptions, timeline phases, footer.
3. **Save** to the working directory: `{company-slug}_{doctype}_{project-slug}_{YYYY-MM}.html`.
4. **Instruct the user** to open in a browser and click the in-page **↓ Print / Save as PDF** button.

No additional formatting work is required. The CSS handles everything — cover, sections, tables, totals, timeline, print chrome suppression, responsive collapse.
