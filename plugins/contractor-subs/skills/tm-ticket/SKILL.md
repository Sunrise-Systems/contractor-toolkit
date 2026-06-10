---
name: tm-ticket
description: Generate a daily time & materials ticket — crew hours by classification, materials, equipment, work description, and a GC superintendent signature line. Use when the user says "T&M ticket", "time and material", "extra work ticket", or "/tm-ticket".
argument-hint: [date or short description of the extra work]
---

# /tm-ticket — Time & Materials Ticket

The daily ticket for extra or directed work — filled out same-day, signed by the GC's super same-day. A signed T&M ticket is the strongest backup a COR can have; an unsigned one from last month is a story. Outputs a one-page DOCX or HTML through `contractor-docs`.

Use whenever crews touch work outside the subcontract scope: directed extras, concealed conditions, standby time, re-work caused by others.

## Inputs Needed

1. **Ticket number** — sequential (TM-NNN); check the working directory for the last one
2. **Date and project**
3. **Work description** — what was done and **why it's extra** (one line citing the directive, RFI, or condition — same cause discipline as `/change-order-request`)
4. **Who directed it** — name and role of the GC person
5. **Labor** — each worker or classification: hours, classification (journeyman/apprentice/foreman), straight time vs. OT
6. **Material** — items and quantities used (pricing optional on the ticket — quantities signed today, prices attached later via vendor invoices)
7. **Equipment** — what was used and for how long

## Ticket Format

```
[YOUR COMPANY] — TIME & MATERIALS TICKET  TM-014
Project: [name]              Date: [date]
Directed by: [name, GC]      Reference: [RFI/CCD/verbal directive]

DESCRIPTION OF WORK
[What was done, where, and why it is outside subcontract scope]

LABOR
Classification        ST hrs    OT hrs
Foreman               4         —
Journeyman (2)        8         2

MATERIAL                          EQUIPMENT
[item]  [qty] [unit]              [item]  [hrs/days]

Work performed as described and quantities verified:

____________________________      ____________________________
[Your foreman]                    GC Superintendent      Date
```

## Rules

1. **Same day, every time.** A ticket dated three days after the work invites a fight. If it's late, date it accurately and note when the work occurred.
2. **The signature is the ticket.** Print it, hand it to the super, get it signed before the crew leaves. An emailed unsigned PDF is the fallback, not the plan.
3. **Quantities on the ticket, pricing in the COR.** The super signs hours and materials — that's verifiable on the spot. Rates and markup come from the subcontract and land in the COR. (If the GC requires priced tickets, include rates — but signed quantities are the priority.)
4. **One issue per ticket.** Standby Tuesday and rework Thursday are two tickets, not one — they'll feed different CORs.
5. **Why-it's-extra is mandatory.** A ticket that doesn't say why the work is outside scope is just a timesheet.
6. **Roll up weekly.** When several tickets share a cause, offer to draft the COR (`/change-order-request`) with the tickets as numbered backup.
