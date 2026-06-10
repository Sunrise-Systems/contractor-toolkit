# contractor-subs

Skills for the other side of the table — subcontractors and specialty trades working under a GC. Same branded document system, pointed at the paperwork subs actually live in: quoting bid invitations, getting paid, and getting paid for changes.

Mirrors the GC pipeline: a GC's `/sub-bid-package` is exactly what `/sub-quote` responds to.

## Skills

| Skill | Trigger | What It Does |
|-------|---------|--------------|
| **sub-quote** | `/sub-quote` | Respond to a GC bid invitation — scope review, quote letter with inclusions/exclusions/alternates |
| **change-order-request** | `/change-order-request` | COR to the GC with cause, cost breakdown, schedule impact, and backup list |
| **tm-ticket** | `/tm-ticket` | Daily time & materials ticket with GC signature line — the paper behind every COR |
| **sub-pay-app** | `/sub-pay-app` | Monthly progress invoice against a schedule of values with retainage math |

## Brand Identity

Uses the same `contractor-initialize` wizard and `contractor-brand`/`contractor-docs` plugins — a sub's company config works identically to a GC's. Run `/initialize` first.

## Install

Part of the `contractor-toolkit` marketplace. Install the marketplace, then enable `contractor-subs`.

## License

MIT
