---
name: specs-documentation-userguide
description: Use when generating, updating, or auditing customer-facing feature docs in markdown derived from the codebase. USE FOR: user guides, help-center articles, feature catalogs, release-note prose, end-user onboarding, syncing docs after code changes, flagging docs for removed features. DO NOT USE FOR: internal requirements (use specs-documentation-prd), technical docs (use specs-documentation-trd), research knowledge bases (use specs-llm-wiki).
---

# User Guide & Feature Documentation

Generate, update, and audit **client-facing** feature documentation as markdown. The
output is written for the end customer — the person who *uses* the product — not for
the engineer who builds it.

Modeled on the [doc-it pattern](https://dosu.dev/blog/claude-code-skill-doc-it): scan
the repo, produce new pages, patch existing ones, and flag stale references. The
difference is **audience and altitude**: doc-it documents the codebase; this skill
documents *what the customer can do with the product*.

## The one rule that changes everything: audience

Every choice flows from a single question — **"would a paying customer, who has never
seen the code, understand this?"**

| Write this (customer voice) | Not this (engineer voice) |
|---|---|
| "Schedule an appointment and your client gets a confirmation email." | "The `Scheduling` module publishes an `AppointmentCreated` event consumed by `Notifications`." |
| "Payments are processed securely; you receive a receipt." | "`Payments` calls the Stripe gateway via `PaymentIntentHandler`." |
| "You can invite team members and set their permissions." | "`Identity` exposes `POST /users/invite` guarded by the `Admin` policy." |

The code is your **source of truth** for *what exists*. It is never your *vocabulary*.
Strip module names, class names, endpoints, event names, table names, and stack detail
from the output. Keep verbs the customer performs and outcomes they observe.

## Output Location & Structure

Default to a dedicated, publishable tree separate from internal specs:

```
docs/user-guide/
├── index.md                 # Table of contents, grouped by theme
├── getting-started.md       # First-run: what the product is, first task
├── <feature-area>.md        # One page per customer-recognizable feature area
└── assets/                  # Screenshots, diagrams referenced by pages
```

Keep it under `docs/` so it lives with the code and can be published as-is to a docs
site (Docusaurus, Starlight, Mintlify, GitBook) or a help center later. Ask the user if
they want a different root.

## Voice & Style Rules

- **Second person, present tense, active voice** — "You create…", not "The system allows creation of…".
- **Lead with the outcome**, then the steps. Customers scan for "can I do X?".
- **No internal names.** If you catch a module, class, endpoint, event, or table name in a draft, it's a bug — rewrite it as a user action or outcome.
- **No stack detail.** The customer doesn't care that it's .NET, Postgres, or RabbitMQ.
- **Name features the way the UI names them.** Reuse button labels and menu text.
- **Short pages, scannable.** Headings, short paragraphs, numbered steps. A page should be usable in under a minute.
- **Screenshots over prose** where a screen is involved — reference `assets/`, and note where one should be added if you can't capture it.
- **Say what's gated.** If a capability requires a plan/role, state it plainly.

## Pitfalls

- **Documenting the architecture instead of the product.** The most common failure: pages that read like a TRD. If a sentence names a module or endpoint, it leaked.
- **Mirroring the code structure.** One doc page per module produces a guide no customer navigates. Organize by what the customer wants to *do*.
- **Documenting internal/admin-only capabilities as customer features.** Confirm the capability is customer-facing (in the public frontend / customer plan) before writing it. When unsure, list it in the report and ask.
- **Inventing behavior the code doesn't have.** Every claim traces to an endpoint, handler, or UI page. If you can't find it, don't promise it.
- **Rewriting instead of patching on update.** Preserve the existing voice; make the smallest change that restores accuracy.
- **Auto-editing during an audit.** Audit reports first; it edits only when the user asks.

## Project Context

`references/example-project-context.md` is a worked example for one codebase — a
scheduling SaaS built as a .NET modular monolith with an admin SPA and a public Nuxt
site: module→feature mapping, where to look for each signal, before/after examples.
Adapt its paths to the target repository.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/three-operations.md](references/three-operations.md) | Three Operations — 1. Generate, 2. Update, 3. Audit |
| [references/feature-discovery-mapping-code-to-customer-capab.md](references/feature-discovery-mapping-code-to-customer-capab.md) | Feature Discovery — mapping code to customer capabilities |
| [references/details.md](references/details.md) | Page Template |

## References

- [doc-it: a Claude Code skill for auto-generating project docs](https://dosu.dev/blog/claude-code-skill-doc-it)
- [Diátaxis — a documentation framework (tutorials / how-to / reference / explanation)](https://diataxis.fr/)
- [Google developer documentation style guide](https://developers.google.com/style)
