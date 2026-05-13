# Sub-Brand Setup Template

Most construction companies have one parent brand and one to four sub-brands (typically: architecture/engineering arm, general construction arm, specialty trade arm, real-estate arm). This file is the template for setting up each one.

## Parent Brand vs Sub-Brand — When to Use Which

| Context | Use |
|---------|-----|
| General company content, "about" pages, first impressions | Parent: {{COMPANY_NAME}} |
| End-to-end project proposals (design through construction, multiple services) | Parent: {{COMPANY_NAME}} |
| Service-specific content (one division's offering only) | The relevant sub-brand |
| Subcontractor bid invitations (specific trade scope) | The sub-brand performing that trade |
| Content that spans multiple divisions | Parent: {{COMPANY_NAME}} |
| Social media (company-wide) | Parent: {{COMPANY_NAME}} |
| Social media (division-specific job site post) | The relevant sub-brand |
| Recruiting (company-wide) | Parent: {{COMPANY_NAME}} |
| Recruiting (trade-specific journeyman role) | The relevant sub-brand |

**Rule of thumb:** If the content applies to the whole company or spans divisions, use the parent. If it's specifically about one division's service, use that sub-brand.

---

## Sub-Brand Template (fill in for each)

Copy this block for every sub-brand. The `/initialize` command will populate the placeholders.

### {{SUBBRAND_N_NAME}}

**Full name:** {{SUBBRAND_N_FULL_NAME}}
**Abbreviation:** {{SUBBRAND_N_ABBREVIATION}} (acceptable in {{SUBBRAND_N_ABBREVIATION_CONTEXT}})
**Scope:** {{SUBBRAND_N_SCOPE}}
**Logo files:**
- Stacked: `{{SUBBRAND_N_LOGO_STACKED}}`
- Horizontal: `{{SUBBRAND_N_LOGO_HORIZONTAL}}`

**Voice nuance:** {{SUBBRAND_N_VOICE_NUANCE}}

**Key differentiators / proof points:**
- {{SUBBRAND_N_PROOF_1}}
- {{SUBBRAND_N_PROOF_2}}
- {{SUBBRAND_N_PROOF_3}}

**Sample content:**
> {{SUBBRAND_N_SAMPLE_COPY}}

---

## Common Sub-Brand Patterns in Construction

When picking sub-brand calibration, the most common patterns are:

### Architecture & Engineering Arm

**Typical name:** "{{COMPANY_SHORT}} Architecture & Engineering" / "{{COMPANY_SHORT}} A&E" / "{{COMPANY_SHORT}} Design"

**Voice nuance:** Slightly more precise and design-forward than the parent brand. More emphasis on the "why" behind design decisions. Speaks most to the Dreamer audience and to architect peers.

**Typical proof points:**
- In-house architects AND engineers — rare for a GC
- Deep local code expertise reduces permit-rejection risk
- Faster permit timelines vs market average
- Direct relationships with city permitting offices
- High conversion rate from design-phase clients to full construction

**Sample line:**
> "Most firms outsource their engineering. Our architects and engineers sit in the same office. When a question comes up, they walk over and figure it out in five minutes."

### General Construction Arm

**Typical name:** "{{COMPANY_SHORT}} General" / "{{COMPANY_SHORT}} Construction" / "{{COMPANY_SHORT}} Build"

**Voice nuance:** The most direct and action-oriented of the sub-brands. This is the division that shows up, does the work, and delivers. Speaks most to Pragmatists.

**Typical proof points:**
- Journeyman-skilled tradespeople, not handymen
- Aggressive response/communication SLAs
- Buildout timelines vs market average
- Transparent pricing — no hidden change orders
- Single point of accountability from permit to punch list
- Repeat-client volume

**Sample line:**
> "Most contractors, you can't get them on the phone. You leave a message, maybe they call back, maybe they show up next week. We don't operate like that."

### Specialty Trade Arm (Electrical / Mechanical / Civil / etc.)

**Typical name:** "{{COMPANY_SHORT}} Electric" / "{{COMPANY_SHORT}} Mechanical" / etc.

**Voice nuance:** The most safety-conscious and technically credible of the sub-brands. Emphasize depth of specialized expertise and the safety/code implications of getting this trade right.

**Typical proof points:**
- Decades of specialty expertise
- Commercial/industrial vs residential specialization
- Integrated with the GC arm for seamless delivery
- Safety record (incident-free years, EMR rating, etc.)
- Licensed, bonded, insured for the scope

**Sample line:**
> "Electrical fires are the number one cause of commercial building fires. That's not a scare tactic — it's a fact. And it's exactly why you don't want the lowest bidder handling your building's electrical."

### Real Estate / Development Arm

**Typical name:** "{{COMPANY_SHORT}} Development" / "{{COMPANY_SHORT}} Real Estate"

**Voice nuance:** Investor-facing and outcome-oriented. Talks in IRRs, holding periods, and stabilized NOI when the audience is sophisticated; talks in monthly rent and after-repair value when it's not. Quieter than the construction-side voice — fewer exclamation-of-confidence moments, more "here are the numbers."

**Typical proof points:**
- Total assets under management / total value developed
- Holding philosophy (long-term vs merchant-build)
- Vertical integration with the construction arm (cost certainty)
- Track record with specific asset classes

**Sample line:**
> "Our construction arm gives us cost certainty most developers can't get. When we underwrite a deal, the GC number isn't an estimate — it's a price."

---

## Naming Convention Rules

- **Parent name appears first** in every sub-brand name. "{{COMPANY_SHORT}} A&E" not "A&E by {{COMPANY_SHORT}}."
- **Trade/service descriptor is short and clear.** "Electric" not "Electrical Construction Services Inc."
- **Legal vs marketing name.** Use the full legal entity name on contracts, the marketing short form everywhere else.
- **Abbreviations only in informal/internal contexts** unless the abbreviation is itself the marketing name.

---

## Logo Rules for Sub-Brands

- Every sub-brand has its own stacked AND horizontal logo file.
- Sub-brand logos use the same typeface, wordmark style, and clear-space rules as the parent.
- Sub-brand logos are used ONLY when the content is specifically about that division's scope. When in doubt, use the parent.
- Never combine two sub-brand logos on a single page. If the content spans divisions, the parent logo is correct.
- Sub-brand color: see the main `SKILL.md` Logo Color Decision Tree. The default mapping is the brand accent for the parent and a distinct accent for each sub-brand if the company uses department colors; otherwise, all sub-brand logos are the same monochrome as the parent and the division name carries the differentiation.

---

## Sub-Brand Voice Calibration — Quick Reference

| Sub-brand pattern | Voice shift from parent | Best audience |
|---|---|---|
| A&E / Design arm | More design-forward, more "why" | Dreamers, architects |
| General Construction arm | More direct, more action-oriented, more numbers | Pragmatists, building owners |
| Specialty Trade arm | More technical, more safety-conscious, more credentialed | Professionals, AHJs |
| Development / Real Estate arm | More numbers-driven, more outcome-focused, quieter | Investors, sophisticated owners |

The parent voice is the baseline. Each sub-brand calibrates from that baseline — it doesn't replace it. A {{COMPANY_NAME}} reader should be able to read content from any sub-brand and recognize the same underlying voice.
