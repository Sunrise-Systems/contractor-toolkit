# HTML styling procedure

Loaded from document-generator. Paths below are relative to the skill root. CSS presence is not visual verification.

## Clean HTML — Mandatory Styling (non-negotiable)

Every HTML document generated inherits the same canonical CSS system. This is not a per-document decision — it is the style system. Changing colors, fonts, or layout patterns breaks the brand identity.

The full canonical `<style>` block lives in `references/html-canonical.md`. Copy it verbatim into every generated HTML file. The CSS variables at the top of that block are the only place tokens should change.

### Mandatory CSS variables (top of every `<style>` block)

```css
:root {
  --primary: {{PRIMARY_COLOR}};
  --accent: {{ACCENT_COLOR}};
  --ink:    #{{INK_HEX}};
  --body:   #{{BODY_HEX}};
  --mid:    #{{MID_HEX}};
  --muted:  #{{MUTED_HEX}};
  --light:  #{{LIGHT_HEX}};
  --rule:   #{{RULE_HEX}};
  --bg:     #FFFFFF;
  --font:   '{{TYPOGRAPHY_PRIMARY}}', {{TYPOGRAPHY_FALLBACK}};
}
```

### Mandatory print block (hides browser URL/page-number chrome)

```css
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
```

**Never ship an HTML document without this print block.** Without it, Chrome/Safari paint the file URL and page counter into the margin, which ruins the design.

### Hero cover block (uses `--primary`)

```css
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
```

### Sections + labels

```css
.section { padding: 36px 56px; border-bottom: 0.5px solid var(--rule); }
.section:last-child { border-bottom: none; }
.section-label {
  font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--muted); margin-bottom: 18px; padding-bottom: 10px;
  border-bottom: 0.5px solid var(--rule); font-weight: 500;
}
```

### Scope grid — flat hairlines, NOT cards

```css
.scope-grid { display: grid; grid-template-columns: 1fr 1fr; column-gap: 28px; row-gap: 0; }
.scope-item { padding: 16px 0; border-bottom: 0.5px solid var(--rule); }
.scope-item strong {
  font-size: 10px; font-weight: 500; color: var(--muted);
  display: block; margin-bottom: 8px;
  letter-spacing: 0.12em; text-transform: uppercase;
}
.scope-item span { font-size: 13px; color: var(--ink); line-height: 1.55; display: block; }
```

**Do NOT use background fills or `border-radius` on `.scope-item`.** Flat hairlines only.

### Notice block (callout)

```css
.notice { background: var(--primary); color: #fff; border-radius: 6px; padding: 16px 18px; font-size: 12px; line-height: 1.65; }
.notice-label {
  font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--muted); margin-bottom: 8px; font-weight: 500;
}
```

### CSI budget table

```css
table { width: 100%; border-collapse: collapse; font-size: 13px; }
thead tr { border-bottom: 1.5px solid var(--ink); }
thead th {
  text-align: left; padding: 10px 0; font-size: 10px; font-weight: 500;
  letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted);
}
thead th:last-child { text-align: right; }
tbody tr { border-bottom: 0.5px solid var(--rule); }
tbody td { padding: 12px 0; vertical-align: top; color: var(--ink); line-height: 1.45; }
tbody td:last-child { text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
.subtotal-row td { font-weight: 600; font-size: 13px; padding: 14px 0; border-bottom: 1.5px solid var(--ink); color: var(--ink); }
```

The full table styles (including division headers, totals block, timeline Gantt, footer, print button) are in `references/html-canonical.md`.
