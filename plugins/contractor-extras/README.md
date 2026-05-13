# contractor-extras

Construction deliverable skills for the `contractor-toolkit` marketplace. Each skill is a guided workflow that walks you through filling out a real industry document, then hands the content to `contractor-docs` for branded styling.

## Skills

| Skill | Trigger | What It Does |
|-------|---------|--------------|
| **proposal** | `/proposal` | Client proposal with scope, schedule of values, timeline, and terms |
| **project-timeline** | `/project-timeline` | HTML Gantt-style construction timeline in tonal grays |
| **change-order** | `/change-order` | Formal AIA G701-style change order with cost and schedule impact |
| **rfi** | `/rfi` | One-page Request for Information with drawing/spec references |
| **submittal** | `/submittal` | Submittal cover sheet and log entry |
| **daily-log** | `/daily-log` | Daily site report — crews, work, weather, deliveries, safety |
| **internal-doc** | `/internal-doc` | Flexible internal memo / weekly status / preconstruction notes |
| **project-intake** | `/project-intake` | Qualify a prospective project and generate a brief for estimating |

## Brand Identity

Every skill uses the shared template placeholders configured by `contractor-initialize` and `contractor-brand`: `{{COMPANY_NAME}}`, `{{COMPANY_LEGAL_NAME}}`, `{{TAGLINE}}`, `{{PM_NAME}}`, `{{PM_TITLE}}`, `{{PM_EMAIL}}`, `{{PM_PHONE}}`, `{{OPERATING_ADDRESS}}`, `{{DOMAIN}}`, `{{VOICE_ARCHETYPE}}`, `{{PRIMARY_COLOR}}`.

Final styling — fonts, colors, headers, footers — is applied by the `contractor-docs` document-generator when output goes to DOCX, PDF, or HTML.

## Install

This plugin is part of the `contractor-toolkit` marketplace. Install the marketplace, then enable `contractor-extras`.

## License

MIT
