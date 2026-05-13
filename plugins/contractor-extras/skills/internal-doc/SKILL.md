---
name: internal-doc
description: Generate a flexible internal document — memo, weekly status, preconstruction notes, meeting minutes, or general team communication. Use when the user says "draft a memo", "internal doc", "weekly status", "precon notes", "meeting minutes", or "/internal-doc".
argument-hint: [memo subject or doc type]
---

# Internal Doc

A flexible internal document generator for `{{COMPANY_NAME}}` staff use. Covers memos, weekly status reports, preconstruction notes, meeting minutes, policy updates, or any short-form internal communication. Outputs DOCX through `contractor-docs`.

Use when the user needs something professional but lightweight — not as formal as a proposal or change order, but more structured than an email.

---

## Inputs Needed

Gather in two chunks. Adapt to the doc type.

### 1. Routing
- Doc type: Memo / Weekly Status / Precon Notes / Meeting Minutes / Other
- From (default `{{PM_NAME}}, {{PM_TITLE}}`)
- To (person, team, or distribution list)
- Date (default today)
- Subject / Re: line — 5-10 words

### 2. Content
- Body — the actual message, key points, or notes
- Action items (if any): who, what, by when
- Attachments referenced (if any)
- Next meeting / follow-up date (if applicable)

For specific doc types, additional inputs:

| Doc Type | Extra Inputs |
|----------|--------------|
| **Weekly Status** | Projects in flight, milestones hit, blockers, upcoming week priorities |
| **Precon Notes** | Project, attendees, scope discussed, decisions made, open items |
| **Meeting Minutes** | Date, attendees, agenda items, decisions, action items |

---

## Workflow

```
1. INTAKE     → Routing + content
2. STRUCTURE  → Pick template variant based on doc type
3. DRAFT      → Generate doc in {{VOICE_ARCHETYPE}} voice
4. EXPORT     → contractor-docs renders DOCX
```

Keep it short. If the user wants a 5-page treatise, push back — internal docs work best at one page.

---

## Output

A DOCX (or markdown if requested) with:

1. Header block — From / To / Date / Re
2. Body — paragraphs, bullets, or sections based on doc type
3. Action items table (if applicable)
4. Footer with `{{COMPANY_NAME}}` and author signature

---

## Template

### Generic Memo

```markdown
# MEMORANDUM

**To:** {RECIPIENTS}
**From:** {{PM_NAME}}, {{PM_TITLE}}
**Date:** {DATE}
**Re:** {SUBJECT}

---

{BODY_PARAGRAPHS}

## Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | {ACTION} | {OWNER} | {DUE} |

---

*{{COMPANY_NAME}} · Internal*
```

### Weekly Status

```markdown
# Weekly Status — Week of {WEEK_OF}

**Author:** {{PM_NAME}}, {{PM_TITLE}}
**Date:** {DATE}

## Projects In Flight

| Project | Phase | Status | Notes |
|---------|-------|--------|-------|
| {PROJECT} | {PHASE} | 🟢 On Track / 🟡 Watch / 🔴 At Risk | {NOTES} |

## This Week — Wins
- {WIN}

## This Week — Blockers
- {BLOCKER}

## Next Week — Priorities
- {PRIORITY}

---

*{{COMPANY_NAME}} · Internal*
```

### Preconstruction Notes

```markdown
# Preconstruction Meeting Notes — {PROJECT_NAME}

**Date:** {DATE}  ·  **Location:** {LOCATION}
**Attendees:** {ATTENDEES}

## Scope Discussed
- {ITEM}

## Decisions Made
- {DECISION}

## Open Items
| # | Item | Owner | Due |
|---|------|-------|-----|
| 1 | {ITEM} | {OWNER} | {DUE} |

## Next Meeting
{NEXT_DATE} — {NEXT_LOCATION}

---

*{{COMPANY_NAME}} · {{PM_NAME}}, {{PM_TITLE}}*
```

### Meeting Minutes

```markdown
# Meeting Minutes — {MEETING_TITLE}

**Date:** {DATE}  ·  **Time:** {START}–{END}
**Location:** {LOCATION}
**Attendees:** {ATTENDEES}
**Absent:** {ABSENT}

## Agenda & Discussion

### 1. {AGENDA_ITEM}
{DISCUSSION_SUMMARY}
**Decision:** {DECISION}

### 2. {AGENDA_ITEM}
{DISCUSSION_SUMMARY}

## Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | {ACTION} | {OWNER} | {DUE} |

## Next Meeting
{NEXT_DATE}

---

*Recorded by {{PM_NAME}} · {{COMPANY_NAME}}*
```
