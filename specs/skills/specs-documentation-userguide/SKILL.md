---
name: specs-documentation-userguide
description: Use when generating, updating, or auditing client-facing feature documentation as markdown — user guides, help-center articles, "what you can do" pages written for the end customer, not the engineer. Discovers features from the codebase (API endpoints, module handlers, frontend routes/pages) plus existing PRDs, then writes plain-language `.md` a customer can read. Modeled on the doc-it pattern (generate / update / audit + stale-reference detection). USE FOR: user guides, help-center content, feature catalogs for customers, release-note prose, onboarding docs for end users, syncing published docs after code changes, flagging docs that describe removed features DO NOT USE FOR: internal product requirements (use specs-documentation-prd), technical/API design docs (use specs-documentation-trd), business justification (use specs-documentation-brd), architecture decisions (use specs-documentation-adr), executable acceptance criteria (use specs-documentation-gherkin), an internal research knowledge base (use specs-llm-wiki)
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

## Three Operations

Invoke by intent — the user says "generate the user guide", "update the docs", or
"audit the docs".

### 1. Generate

Produce customer-facing docs from scratch (or for a feature area that has none).

① **Discover features from the codebase.** Map code artifacts to user-visible
capabilities (see *Feature Discovery* below). Group by what the customer perceives as
a feature area, NOT by module or service boundary.

② **Cross-check against existing specs.** Read any PRDs (`specs-documentation-prd`
output), READMEs, and `docs/` already present — they carry the intended user value and
naming. Prefer product names the team already uses.

③ **Decide the page set.** One page per feature area a customer would look up. Don't
mirror the code structure — a single customer feature ("Online booking page") may span
several modules.

④ **Write each page** using the template below, in the customer's language. Every
sentence describes something the user does, sees, or receives.

⑤ **Build navigation.** Write/refresh `docs/user-guide/index.md` (or `README.md` in the
docs root) with a table of contents grouped by theme, and a one-line summary per page.

⑥ **Report** every file created, and list features you found in code but intentionally
did NOT document (internal-only, admin-only, not yet shipped) so the user can confirm.

### 2. Update

Sync already-published docs after the product changed.

① **Read the existing docs** and the recent diff / changed areas.
② **Detect drift** — new capabilities not yet documented, changed behavior, renamed or
removed features.
③ **Patch minimally** — edit the affected pages, preserve the existing voice and
structure, bump any "last updated" line. Don't rewrite pages wholesale.
④ **Report** each page changed and why, in one line each.

### 3. Audit

Health-check the docs against the code — the doc-it "stale reference" pass, adapted.

① **Removed features:** doc pages describing capabilities no longer present in the code
(endpoint gone, route deleted, module removed) → flag as **stale**.
② **Undocumented features:** shipped, customer-visible capabilities with no page → flag
as **gap**.
③ **Voice leaks:** pages that mention internal names (module/class/endpoint/event/table),
stack detail, or engineer jargon → flag as **voice**.
④ **Broken cross-links** between doc pages and missing images/assets.
⑤ **Staleness:** pages whose behavior no longer matches current code paths.
⑥ **Report** grouped by severity: stale (describes something gone) > gap (missing) >
voice > broken links > minor staleness. Give the file path and the concrete fix for
each. Don't auto-edit during an audit unless asked — report first.

## Feature Discovery — mapping code to customer capabilities

The customer never sees your architecture. Translate these signals into features:

| Code signal | What to read | Yields |
|---|---|---|
| **E2E tests** | End-to-end/browser test files, scenario/test names, the flows they drive | Verified user journeys — the strongest signal for "what a customer actually does" |
| **BDD `.feature` files** | Gherkin scenarios (Given/When/Then), if present | Behavior already phrased in near-customer language — reuse the wording |
| **API endpoints** | Controllers / minimal-API routes, their HTTP verbs and route names | Actions the customer can trigger |
| **Module handlers** | Command/query handlers per module (the business operations) | The verbs behind each capability |
| **Frontend routes/pages** | SPA routes, Nuxt pages, page titles and forms | The screens the customer actually navigates |
| **Public UI copy / i18n** | Translation files, labels, button text | The product's own vocabulary — reuse it |
| **PRDs & READMEs** | `specs/` PRDs, project README | Intended value, feature names, personas |
| **Config/feature flags** | Flags, plans/tiers | Which capabilities are gated / plan-specific |

**Prefer the frontend and UI copy as your naming source** — it's the closest thing to
what the customer sees. Fall back to endpoints/handlers to confirm a capability exists
and to find ones the UI doesn't obviously expose.

**E2E tests and `.feature` files are the highest-value discovery signal.** They encode
complete, *verified* user journeys — a test named `Booking_WhenSlotSelected_SendsConfirmation`
maps almost one-to-one to a "How to use it" section. The page/route each test drives
confirms the flow is customer-facing and actually works. Read the scenario/test names
first, then the steps. But keep the audience rule: a test asserts on selectors and
status codes — translate the *journey* it proves, never its assertions. If the repo has
a QA/browser-automation skill (e.g. `playwright-cli`, `bdd-gherkin`), those tests are
where its scenarios live.

**Group by customer mental model.** "Booking", "Payments & invoices", "Your clients",
"Notifications & reminders", "Team & permissions", "Your account" — these are feature
areas a customer recognizes, and each may be assembled from several modules.

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

## Page Template

```markdown
# <Feature name, in the customer's words>

> One-sentence promise: what this lets you do and why it matters.

## What it does

[Plain-language description of the capability. No jargon. Focus on the outcome
the customer gets.]

## How to use it

1. [Step the customer takes — start from the screen/button they see]
2. [Next step]
3. [What they see / receive when it works]

## What to expect

- [Observable behavior: emails sent, confirmations, timing, limits]
- [Edge behavior the customer would notice, in their terms]

## Good to know

- [Plan/tier gating, if any — "Available on the Pro plan"]
- [Common questions or gotchas, in the customer's language]

_Last updated: YYYY-MM-DD_
```

Not every page needs every section. Cut sections that carry no signal for that feature.

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

This skill was built with the **LinkDaily** project in mind — a scheduling SaaS for
independent professionals, structured as a .NET modular monolith (Identity, Scheduling,
Payments, Notifications, Logistics modules) with an admin SPA and a public Nuxt site.
See `references/linkdaily-context.md` for the concrete module→feature mapping, where to
look for each signal, and worked before/after examples in that codebase.

## References

- [doc-it: a Claude Code skill for auto-generating project docs](https://dosu.dev/blog/claude-code-skill-doc-it)
- [Diátaxis — a documentation framework (tutorials / how-to / reference / explanation)](https://diataxis.fr/)
- [Google developer documentation style guide](https://developers.google.com/style)
