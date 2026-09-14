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
