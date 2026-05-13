---
name: brand
description: Enforce {{COMPANY_NAME}} brand identity — colors, typography, voice, logos, sub-brand guidelines, document archetypes. Auto-invoke for any branded content: proposals, estimates, social, ads, internal docs.
---

# {{COMPANY_NAME}} Brand Enforcement

{{COMPANY_NAME}} is a {{OWNERSHIP_TYPE}} {{COMPANY_TYPE}} in {{MARKET_CITY}} with {{YEARS_EXPERIENCE}} of experience. Everything we produce — every word, every layout, every piece of content — must reflect who we are.

**Tagline:** {{TAGLINE}}

**Core belief:** {{CORE_BELIEF}}

This skill is the source of truth for all visual and verbal identity. Load it for ANY branded output (proposals, estimates, web copy, social, ads, decks, letters, internal docs).

---

## 1. Visual Identity

### Color Palette

The default {{COMPANY_NAME}} system is **premium monochrome**: a primary near-black, a full neutral scale, white paper, and a single optional accent. Weight comes from bold typography, generous whitespace, and hairline separators — not from color. This is what photographs and prints best and what most premium construction brands settle on.

If your `/initialize` chose a colored accent, it is reserved for: cover bars, section underlines, grand-total borders, primary CTAs, and division marks. Never used to "decorate."

| Role | Token | Hex | Usage |
|------|-------|-----|-------|
| **PRIMARY** | Pure primary | `{{PRIMARY_COLOR}}` | Hero/cover blocks, footer blocks, print CTAs (white-on-primary). |
| **INK** | Near-black | `{{INK_COLOR}}` | Titles, bold labels, table header rule, grand total. Used instead of pure black for body text — pure black is too harsh at small sizes. |
| **BODY** | Body text | `{{BODY_COLOR}}` | All body text, table data. |
| **MID** | Mid gray | `{{MID_COLOR}}` | Supporting text, address lines, total supporting lines. |
| **MUTED** | Muted gray | `{{MUTED_COLOR}}` | Section labels, column headers, meta labels, footer sub-label. |
| **LIGHT** | Cool gray | `{{LIGHT_COLOR}}` | Em-dash bullets, tertiary info, page numbers, division number prefix. |
| **RULE** | Hairline gray | `{{RULE_COLOR}}` | Section dividers, table row separators, info-table borders. |
| **SOFT_FILL** | Off-white fill | `{{SOFT_FILL_COLOR}}` | CSI division header bands, scope cards (HTML only — not used in DOCX). |
| **PAPER** | Pure white | `{{NEUTRAL_COLOR}}` | All page, cell, and table backgrounds. |
| **ACCENT** (optional) | Brand accent | `{{ACCENT_COLOR}}` | Cover bar, section underlines, grand-total border, primary CTA. Sparingly. |

**Usage rules — non-negotiable:**
- **Black-on-white is the default.** White-on-primary is reserved for cover/hero blocks, footer blocks, callout/notice blocks, and print CTAs.
- **Dividers are hairlines, not lines.** Use `{{RULE_COLOR}}` at 0.5px. Above subtotals and grand totals, use `{{INK_COLOR}}` at 1.5px. These are the only allowed rule weights.
- **The only fill color on light sections is `{{SOFT_FILL_COLOR}}`** — used for scope cards and CSI division header bands. Everywhere else is white.
- **Never use pure black (`#000000`) for body text** — too harsh at small sizes. Use `{{INK_COLOR}}` for body, reserve pure primary for hero/footer blocks.
- **If an accent color is used, it is "earned."** If accent appears in more than 5 places on a page, it's overused.
- **No gradients. No shadows. No drop-shadows on cards.** Flat only.

### Typography

Typography carries the entire visual load — so weight, size, tracking, and whitespace must be exact.

**Primary font:** {{TYPOGRAPHY_PRIMARY}} (fallback: {{TYPOGRAPHY_FALLBACK}})
**DOCX fallback:** Arial — guaranteed cross-platform match.

The typeface should carry presence at regular weight. Bold is rarely needed. Reserve heavier weights for the wordmark, grand totals, and division headers.

| Element | Weight | Size | Color | Notes |
|---------|--------|------|-------|-------|
| Cover wordmark | Bold | 52–56px | Paper on Primary | Tracked `-0.025em`, uppercase |
| Cover subtitle (division name) | Regular | 12px | Muted | Tracked `0.1em`, uppercase |
| Cover title (project name) | Medium | 22px | Paper | Line-height 1.3 |
| Cover address | Regular | 13px | Muted | |
| Cover meta label | Regular | 10px | Muted | Tracked `0.12em`, uppercase |
| Cover meta value | Medium | 14px | Paper | |
| Section label (micro) | Medium | 10px | Muted | Tracked `0.14em`, uppercase, hairline underline |
| Section body | Regular | 13px | Ink | Line-height 1.5 |
| Scope card title | SemiBold | 12px | Ink | |
| Scope card body | Regular | 11.5px | Mid | Line-height 1.55 |
| Table header | Medium | 10px | Muted | Tracked `0.1em`, uppercase |
| Table body | Regular | 13px | Ink | Line-height 1.45 |
| Division header row | SemiBold | 11px | Mid on Soft_Fill | Tracked `0.08em`, uppercase |
| Division number | Regular | 11px | Light | Inline prefix, `margin-right: 10px` |
| Subtotal row | SemiBold | 13px | Ink | 1.5px Ink rule top/bottom |
| Grand total | Bold | 22px | Ink | Tracked `-0.01em`, 1.5px Ink top border |
| Notice body | Regular | 12px | Paper on Primary | Line-height 1.65 |
| Footer wordmark | Bold | 22px | Paper on Primary | Tracked `-0.02em`, uppercase |
| Footer subtitle | Regular | 11px | Muted | |

**Typographic rules:**
- Headlines are short, punchy, and confident. Never longer than one line on desktop.
- Body text uses line-height 1.45–1.55 for clean readability without feeling airy.
- Letter-spacing on tight headlines: `-0.01em` to `-0.025em`. Letter-spacing on uppercase micro-labels: `0.08em` to `0.14em`.
- ALL CAPS is the signature device — used for micro-labels, section labels, the wordmark, meta labels. Never for running sentences.
- No italic for emphasis — use weight or restructure the sentence.
- `font-variant-numeric: tabular-nums` on any column containing currency or numeric values — figures must align.

### Logo Assets

All logos live at `skills/brand/assets/logos/` inside this plugin. Reference them via `${CLAUDE_PLUGIN_ROOT}/skills/brand/assets/logos/`.

| File | Brand | Use Case |
|------|-------|----------|
| `{{LOGO_PRIMARY_STACKED}}` | {{COMPANY_NAME}} (parent) | Stacked wordmark — primary use on documents, presentations, hero sections |
| `{{LOGO_PRIMARY_HORIZONTAL}}` | {{COMPANY_NAME}} (parent) | Horizontal single-line wordmark — headers, footers, compact spaces |
| `{{LOGO_WHITE}}` | {{COMPANY_NAME}} | White wordmark — dark backgrounds, hero covers, footer blocks |
| `{{LOGO_BLACK}}` | {{COMPANY_NAME}} | Black wordmark — formal contexts, light backgrounds |
| `{{LOGO_SUBBRAND_1}}` | {{SUBBRAND_1_NAME}} | Sub-brand specific documents |
| `{{LOGO_SUBBRAND_2}}` | {{SUBBRAND_2_NAME}} | Sub-brand specific documents |
| `{{LOGO_SUBBRAND_3}}` | {{SUBBRAND_3_NAME}} | Sub-brand specific documents |

**Logo rules — MANDATORY:**
- **Always reference a real bundled file** in `skills/brand/assets/logos/`. Never improvise SVG paths, never recolor a variant that doesn't exist, never substitute a different logo silently.
- **If the file you need is missing, stop and ask the user.** A wrong logo is worse than a delayed one.
- **Minimum clear space:** equal to the height of the first character of the wordmark on all sides.
- **Never stretch, rotate, recolor, or add effects** to logos. Use the bundled variants.
- **On dark backgrounds, use white versions.** On light backgrounds, use black or accent versions per the decision rules below.
- **Parent vs sub-brand:** when content spans divisions or is company-wide, always use the parent wordmark. When content is specifically about one division's service, use that sub-brand.
- **Cover pages only.** Body pages do not get a logo. The footer uses a text wordmark, not the logomark.

### Logo Color Decision Tree

Pick the logo color top-to-bottom:

1. **Is this artifact specifically about a single sub-brand or department?** → use that sub-brand's logo.
2. **Is the surface dark (hero, footer, dark UI)?** → use the white variant.
3. **Otherwise (company-wide, multi-department, ops/admin/leadership, unsure)** → use the primary/default variant.
4. **If still unsure, ASK the user before rendering.**

### Layout Principles

- **Generous whitespace.** Let content breathe. Padding of 36–56px between sections minimum.
- **Left-aligned by default.** Center alignment only for hero sections and single-line CTAs.
- **Maximum content width:** 900px for full documents. 720px for body text when wrapped.
- **No clutter.** If a visual element doesn't serve the content, remove it. No decorative borders, no drop shadows, no ornamental rules. The only lines allowed are hairline section dividers and the 1.5px subtotal/grand-total rules.
- **Grid:** 12-column grid for web layouts. 4-column for mobile.
- **Premium through restraint.** The document feels expensive because of what it leaves out — not what it adds. Every element earns its place.
- **Test without color.** Remove all accent color. If the document still reads as professional and structured, the hierarchy is correct.

---

## 2. Document Archetypes — The Four Canonical Patterns

Every {{COMPANY_NAME}} deliverable maps to one of these four structural patterns. See `references/document-archetypes.md` for full structural specs.

### Picking the Right Archetype

| Deliverable | Archetype | Format |
|---|---|---|
| ROM / conceptual budget / pre-design estimate | Archetype 1 | HTML |
| Investment Guide / capabilities deck | Archetype 1 or 4 | HTML |
| Formal bid / construction proposal | Archetype 2 | DOCX |
| Subcontractor bid invitation | Archetype 2 | DOCX |
| Letter of engagement / task order | Archetype 3 | DOCX |
| Change order | Archetype 3 | DOCX |
| Progress report / site report | Archetype 4 | HTML |
| Scope check / gap analysis | Archetype 4 | HTML |

### Archetype Quick Reference

**Archetype 1 — ROM / Conceptual Budget Document.** HTML-first visual budget for pre-design feasibility, conceptual estimates, and investment decks. Black hero cover, scope cards on Soft_Fill, CSI-division-organized budget table with subtotals and grand total, assumptions/exclusions, timeline, dark footer block. Format: HTML (print-to-PDF via browser).

**Archetype 2 — Formal Bid / Proposal Document.** Text-heavy, division-organized construction proposal. Header, contacts, project summary, schedule of values, division-by-division scope with line items and inline exclusions, optional contract appendix. Voice: direct, "Provide and install…" opens most scope lines. Format: DOCX (the client needs to mark it up).

**Archetype 3 — Letter / Agreement / Short Correspondence.** One-to-three-page professional correspondence. Wordmark header (horizontal, 2.0" wide), date + recipient + `Re:` line, 3–4 body paragraphs, closing + signature, enclosures. Format: DOCX (or HTML for eSignature delivery).

**Archetype 4 — Multi-Page Report.** Progress reports, site reports, status updates, capabilities decks. Dark cover block, uppercase section labels with hairline underlines, body at 13px / 1.5 leading with 2-column info blocks, optional Gantt/progress tracker, footer with page number + document reference. Format: HTML (external) or DOCX (internal/editable).

**Universal rules for every archetype:**
- Use "Investment" not "Cost" or "Price" for the pricing section.
- CSI division terminology when organizing scope: `Division 03 - Concrete`, `Division 05 - Metals`, etc. Division number prefix in Light gray, division name in Mid.
- Schedule of Values uses division number + name + total dollar amount, right-aligned currency.
- Line items open with "Provide and install…", "Furnish and install…", or "Demo and dispose…" — direct verbs.
- Inline exclusions and alternates per scope item — not buried in a separate appendix.
- Tabular numerics on any currency column.

---

## 3. Verbal Identity

Full voice spec at `references/voice-guide.md`. The summary:

### Persona: {{VOICE_ARCHETYPE}}

{{VOICE_ARCHETYPE_DESCRIPTION}}

**Core tension that defines the voice:** We know more than almost anyone in the room, but we never make the reader feel stupid for not knowing it themselves.

### Tone Attributes

{{TONE_ATTRIBUTES}}

The voice should always feel:
- **Conversational** — write like you talk. Use contractions. Use "you" and "we." No stiff corporate speak.
- **Confident** — own what you know. No hedging with "we think" or "we believe" when stating facts about expertise.
- **Candid** — tell the truth even when uncomfortable. Explain costs, timelines, and trade-offs honestly. This is the foundation of trust.
- **Specific** — numbers, names, dates. Specificity is what separates contractor copy from every other contractor's copy.

### Language Rules

1. **Use plain language.** "Building" not "structure." "Plans" not "architectural drawings" (unless precision matters). "Get started" not "commence the engagement."
2. **Explain the why.** Don't just state what we do — explain why it matters to the reader.
3. **Show, don't claim.** Don't say "We're the best." Show it with a specific outcome.
4. **Use specific numbers.** "{{YEARS_EXPERIENCE}}" not "decades of experience." "8-month buildouts" not "faster timelines."
5. **First person is encouraged.** "We" for the company. "I" when content is attributed to a specific person.
6. **No passive voice.** "We delivered the permits in six weeks," not "Permits were delivered."
7. **One idea per sentence.** Logical progression.

### Words to Use

- "{{TAGLINE}}" (always as written — punctuation matters)
- "From concept to completion"
- "One team, one roof" (if you operate integrated services)
- "Obsessive attention to detail"
- "The right way is the only way"
- "Straight shooters"
- "Your building partner" / "your development partner"
- "Hands-on"
- "{{OWNERSHIP_TYPE}} since {{FOUNDED_YEAR}}"
- "{{YEARS_EXPERIENCE}} of experience"

### Words to Avoid

These corporate-speak words are banned. They make our copy sound like every other contractor's copy:

- "Solutions" (vague)
- "Leverage" / "utilize" (say "use")
- "Synergy" / "synergistic" (never)
- "World-class" / "best-in-class" (show, don't claim)
- "Cutting-edge" / "state-of-the-art" (say what the technology actually is)
- "Stakeholders" (say "clients," "partners," "team members")
- "Going forward" / "at this time" / "at the end of the day" (filler)
- "Trusted partner" (earned by behavior, not self-applied)
- "Turn-key" without explanation (explain what we actually handle)
- "Disrupting" / "disruption" (we're builders, not Silicon Valley)
- "Excited to announce" (just announce it)
- "Holistic" / "innovative" / "game-changing" / "scalable" (without context) / "end-to-end" (prefer specifics)

### Copy Don'ts

- No emojis in professional content.
- No exclamation marks in body copy.
- No urgency language ("Act now!", "Don't miss out!", "Limited time!").
- No unsubstantiated superlatives.
- No passive voice.

### Writing Formulas

**Headlines:** [Specific benefit] + [proof or specificity]
- "Permits in 6 weeks, not 6 months."
- "One team from first sketch to open sign."

**Opening sentences:** Start with the reader's problem or desire, not with {{COMPANY_NAME}}.
- Bad: "{{COMPANY_NAME}} is a leading construction firm…"
- Good: "Your lease started three months ago and you're still waiting on permits."

**CTAs:** Direct and specific, not generic.
- Bad: "Contact us today"
- Good: "Get a real estimate in 48 hours"
- Good: "Talk to a builder, not a salesperson"

---

## 4. Audience Awareness

GC clients fall into a small number of patterns. Calibrate tone accordingly.

### The Pragmatists

**Who they are:** Small business owners, franchisees, building owners, large-scale developers. They have a job to do and a budget to keep. Design and sustainability aren't their first priority — getting it done right, on time, and on budget is.

**How to speak to them:**
- Lead with speed, cost control, and accountability.
- Use concrete proof points: specific timelines, specific dollars, specific track record.
- Address their fears directly: getting ripped off, timeline slippage, unresponsive contractors.
- Don't open with design philosophy — they don't care yet. Lead with "we show up, we deliver, we don't play games."

**Example:** "You've got a lease burning a hole in your pocket and no idea how long this buildout is actually going to take. We'll give you a real number — timeline and cost — within 48 hours. No games, no lowball bids that balloon later."

### The Dreamers

**Who they are:** Niche developers, specialized small business owners, high-end homeowners, architects with vision. They already care about design and sustainability. They want collaboration, input, and a partner who shares their vision.

**How to speak to them:**
- Lead with design thinking, craftsmanship, and the "why behind the what."
- Emphasize collaboration: "We build with you, not just for you."
- Use the heritage and community commitment — this audience responds to values.
- Talk about materials, sustainability, and long-term thinking.

**Example:** "Every building tells a story. Our job is to make sure yours says exactly what you want it to — through materials that last, design that works, and craftsmanship that shows in every corner."

### The Professionals (Architects / Owner's Reps / Project Managers)

**Who they are:** Other industry professionals evaluating us as a trade partner. They want competence signals, code fluency, and clear communication.

**How to speak to them:**
- Use CSI division terminology naturally.
- Cite relevant code sections when explaining decisions.
- Be precise about scope boundaries, exclusions, and assumptions.
- Drop the marketing language entirely. They can smell it.

**Example:** "We've assumed Type V-B construction per CBC Table 601 and have priced fire-rated assemblies at corridors only. If the AHJ requires a 1-hour rated demising wall here, that's a $X,XXX add — happy to revise."

### Switching Between Audiences

When the audience is mixed or unknown, default to the Pragmatist voice with Dreamer undertones. Lead with practical value, then layer in the vision. This works because Pragmatists won't be turned off by a well-placed line about quality, but Dreamers will be turned off by content that feels purely transactional.

**Mixed-audience formula:** [Practical benefit] + [Specific proof] + [Bigger picture connector]

---

## 5. Content Rules

### Value Propositions to Reinforce

Every piece of {{COMPANY_NAME}} content should reinforce at least one of these pillars. Weave them in naturally — don't list them.

1. **{{PILLAR_1}}**
2. **{{PILLAR_2}}**
3. **{{PILLAR_3}}**
4. **{{PILLAR_4}}**
5. **{{PILLAR_5}}**

Common pillars across construction firms (pick or adapt during `/initialize`):
- **Expertise** — In-house services, deep specialty knowledge, decades of pattern recognition.
- **Relationships** — Long-tenured relationships with inspectors, subs, and city officials. Faster permits, smoother projects.
- **Accountability** — One team, one point of contact, no finger-pointing.
- **Durability** — Building things that last. Smartest methods, most efficient materials.
- **Integrity** — Candor, commitment, and fairness in every decision.

### "{{TAGLINE}}" Integration

The tagline appears naturally in content, not forced. Guidelines:

- **Standalone:** As a sign-off, section closer, or tagline placement. Always formatted exactly as written, including punctuation.
- **Woven in:** Reference the underlying idea without quoting the tagline verbatim.
- **Never forced:** If it doesn't fit naturally, don't use it. It's better absent than awkward.
- **Frequency:** Maximum once per page/section. Less is more.
- **Context:** Works best after demonstrating something specific that IS different, not as an empty claim.

### Heritage / Ownership Narrative

{{COMPANY_NAME}} was founded in {{FOUNDED_YEAR}} and has been {{OWNERSHIP_TYPE}} ever since. This is a differentiator in an industry full of faceless outfits. Use it, but don't overdo it.

**When to use it:**
- Introductory content (About pages, proposals, first impressions)
- When establishing trust (long tenure = real skin in the game)
- When explaining why {{COMPANY_SHORT}} operates differently
- In community-focused content

**When NOT to use it:**
- Technical specs or pricing documents (feels out of place)
- Repeatedly in the same document (once is enough)
- As a substitute for actual proof of expertise

### {{YEARS_EXPERIENCE}} Positioning

This is not a throwaway line. It carries specific weight:

- **It means institutional knowledge.** We know every {{MARKET_REGION}} building code, every inspector's preference, every permitting shortcut. Use it to explain WHY things go faster with us.
- **It means relationships.** Long tenure means deep networks with the people who approve permits and the subs who do the work.
- **It means track record.** Thousands of completed projects. That's proof, not a claim.
- **It means stability.** In an industry where contractors come and go, we've been here since {{FOUNDED_YEAR}} and we'll be here tomorrow.

---

## 6. Sub-Brand Guidelines

Full setup template at `references/sub-brands.md`.

### When to Use Parent vs. Sub-Brand

| Context | Use |
|---------|-----|
| General company content, "about" pages, first impressions | {{COMPANY_NAME}} (parent) |
| End-to-end project proposals (multiple services) | {{COMPANY_NAME}} (parent) |
| Service-specific content (one division only) | The relevant sub-brand |
| Content that spans multiple divisions | {{COMPANY_NAME}} (parent) |
| Social media (company-wide) | {{COMPANY_NAME}} (parent) |
| Recruiting content | {{COMPANY_NAME}} (parent) |

**Rule of thumb:** If the content applies to the whole company or spans divisions, use the parent. If it's specifically about one division's service, use that sub-brand.

### Sub-Brand Roster

{{SUBBRAND_ROSTER}}

Each sub-brand has its own:
- Full legal name and accepted abbreviation
- Stacked and horizontal logo file
- Voice nuance (typically a slight calibration of the parent voice — more design-forward, more technical, more action-oriented, etc.)
- Key differentiators / proof points specific to that division
- Sample content showing the calibration

See `references/sub-brands.md` for the per-sub-brand spec.

---

## 7. Content Type Guidelines

### Proposals and Estimates
- Open with the client's problem or goal, not with {{COMPANY_NAME}}'s credentials.
- Use "Investment" not "Cost" or "Price" for the pricing section.
- Include specific timelines with milestone dates.
- Close with a clear, direct next step — not "We look forward to hearing from you."
- Use the parent brand logo unless the proposal is division-specific.
- Inline exclusions and assumptions per scope item — not buried in an appendix.

### Website Copy
- Headlines: benefit-driven, specific, under 10 words.
- Subheads: expand on the headline with proof or specificity.
- Body: short paragraphs (3-4 sentences max), scannable, conversational.
- Every page should have one clear CTA.
- Use the heritage / family story on the About page, not everywhere.

### Email (Outreach / Cold)
- Subject lines: specific and curiosity-driven, not salesy.
- First line: about the recipient, not about {{COMPANY_SHORT}}.
- Keep under 150 words for cold emails.
- Close with a question, not a demand.
- Sign off as a person, not "The {{COMPANY_SHORT}} Team."

### Social Media
- Shorter, punchier versions of the brand voice.
- Show the work — project photos, job site updates, team moments.
- Use "{{TAGLINE}}" as an occasional hashtag or sign-off.
- Don't be corporate. Be the people behind the company.

### Blog / Long-Form Content
- Teach something real. Share actual expertise, not surface-level content marketing.
- Use specific examples from real projects (anonymized if needed).
- Conversational tone throughout — imagine explaining to a smart friend.
- 800-1,500 words. No fluff. Every paragraph earns its place.

### Ads / Paid Creative
- One idea per ad. One headline, one proof point, one CTA.
- Visual: typography-driven, with the accent color as the single point of emphasis.
- No stock photos of hard-hatted models. Real project photography or pure-type ads only.

---

## 8. Brand Enforcement Checklist

Before publishing any {{COMPANY_NAME}} content, verify:

**Voice & Copy:**
- [ ] Does this sound like {{VOICE_ARCHETYPE}}? Would a real person say this?
- [ ] Is every term understandable to someone outside construction?
- [ ] Are claims backed by specific numbers or examples?
- [ ] Is this speaking to Pragmatists, Dreamers, or Professionals? Is the tone calibrated?
- [ ] Is there a clear, specific next step (CTA)?
- [ ] Does this build trust or does it sound like every other contractor?
- [ ] Honest about costs, timelines, and trade-offs?
- [ ] No banned words. No emojis. No exclamation marks in body copy. No passive voice.
- [ ] "{{COMPANY_NAME}}" spelled correctly throughout.
- [ ] Tagline "{{TAGLINE}}" formatted exactly as written, if used.

**Visual:**
- [ ] Colors from official palette only.
- [ ] Typography uses {{TYPOGRAPHY_PRIMARY}} (or documented fallback).
- [ ] Logo file is a real bundled file from `skills/brand/assets/logos/` — no inline-generated logos, no recolors of variants that don't exist.
- [ ] Logo color matches the decision tree (sub-brand specific OR primary default OR white-on-dark).
- [ ] Logo variant appropriate for background.
- [ ] Proper logo clear space.
- [ ] Accent color used sparingly (≤5 placements per page).
- [ ] No gradients, drop shadows, or decorative fills.

**Structural:**
- [ ] Right archetype picked for the deliverable (ROM=1, Bid=2, Letter=3, Report=4).
- [ ] Right format for archetype (HTML for visual, DOCX for editable).
- [ ] "Investment" used instead of "Cost" or "Price" in pricing sections.
- [ ] CSI division terminology when organizing scope.
- [ ] Inline exclusions and assumptions per scope item.
- [ ] Tabular numerics on currency columns.
- [ ] Footer wordmark + page number on every page of multi-page documents.

**Sub-Brand:**
- [ ] Right brand chosen (parent vs sub-brand) for the content type.
- [ ] Sub-brand voice nuance applied if using a sub-brand.

---

## References

- `references/voice-guide.md` — Full voice guide, four archetype options, language rules, sample copy.
- `references/sub-brands.md` — Sub-brand setup template and per-division spec.
- `references/document-archetypes.md` — Full structural specs for all four document archetypes.
- `references/brand-compliance-checklist.md` — Pre-publish QA checklist (printable).
- `assets/logos/` — Bundled logo files. Drop yours here and update the Logo Assets table above.
