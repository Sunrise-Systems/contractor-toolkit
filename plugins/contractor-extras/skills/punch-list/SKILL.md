---
name: punch-list
description: Generate a punch list from walkthrough notes — items by area with trade, responsible sub, and status; re-run to track completion toward closeout. Use when the user says "punch list", "punch walk", "closeout items", or "/punch-list".
argument-hint: [project or walkthrough date]
---

# Punch List

Turn walkthrough notes (dictated, typed, or photo descriptions) into a structured punch list organized by area, with each item assigned to a trade and responsible sub. Re-run it as items close to track progress toward substantial completion sign-off. Outputs DOCX or HTML through `contractor-docs`.

Use at substantial completion walkthroughs, owner/architect punch walks, and any pre-handover QC pass.

## Inputs Needed

1. **Project and walkthrough info** — project name, date, who walked (owner, architect, super)
2. **The raw notes** — in any form; the skill structures them
3. **Sub roster** — which sub owns which trade, if known (pulls from `/subcontract` outputs in the working directory when present)
4. **Existing punch list** — if this is a re-walk, the prior list to update statuses against

## Structure

Organize by **area** (room/floor/elevation), then by item:

```
AREA: Suite 210 — Open Office
──────────────────────────────────────────────────────────────────
#    Item                                Trade      Responsible      Status
──────────────────────────────────────────────────────────────────
21   Touch up paint at N wall outlets    Painting   [self-perform]   Open
22   ACT tile cracked at grid B-4        Ceilings   Apex Acoustics   Open
23   Door 210A latch misaligned          Doors/Hdw  [self-perform]   Complete
──────────────────────────────────────────────────────────────────
```

Each item: sequential number (stable across re-walks — never renumber), description specific enough that the sub doesn't need a phone call, trade, responsible party, status (Open / In Progress / Complete / Verified), and date verified.

## Re-walk Updates

When updating an existing list: keep all item numbers, update statuses, append newly found items with new numbers, and lead the document with a summary block — items total / open / complete / verified, plus per-sub open counts so the super knows who to chase.

## Outputs

- **Punch list DOCX or HTML** — `{company-slug}_punch-list_{project-slug}_{YYYY-MM-DD}.{docx|html}`
- **Per-sub extract on request** — just their items, ready to email
- **Optional XLSX** for projects over ~50 items

## Rules

1. **One item, one trade.** If a note spans trades ("fix wall and repaint"), split it.
2. **Specific or it bounces.** "Touch up paint" fails; "touch up paint at N wall outlets, Suite 210" closes.
3. **Numbers never change.** Item 22 is item 22 until the project closes out.
4. **Verified ≠ Complete.** Subs mark complete; the super marks verified. Track both.
