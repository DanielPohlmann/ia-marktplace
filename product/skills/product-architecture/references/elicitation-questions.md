# Architecture — elicitation question bank

Questions to ask **before** the Event Storming and the technical design. They
come from established architecture methods; each block names its source. The
approved idea brief and design answer *what* and *for whom* — these questions
find the **forces and constraints** the architecture must satisfy.

## How to run the interview

- **Ask everything that applies.** Too many questions beat an architecture
  built on assumptions. Skip a question only when the earlier artifacts, the
  architecture/conventions documents or an earlier answer already answer it —
  say which.
- **One question per message**, multiple choice when the options are known,
  always with an "other / don't know" way out. Offer a sensible default the
  user can accept ("Most apps like this accept 1 h of data loss — OK?").
- **Every quality answer becomes a scenario with a number** (ATAM quality
  attribute scenario): *source → stimulus → environment → artifact → response
  → response measure*. "Fast", "always up", "secure", "scalable" are weak
  signals → ask "How fast, measured how, under which load?".
- **"Don't know" is valid.** Record the assumption you will design for under
  `## Open questions`, marked as an assumption to confirm.
- **Record answers** in the technical design's `## Interview notes` table in
  the user's words, and use them to fill the sections listed per block.
- Close every block with: "Anything about <block topic> I didn't ask?"

## A. Business drivers and constraints — ATAM business drivers, arc42 §2

Fills: `Summary`, `Decisions (ADRs)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| A1 | What are the top 3 business goals this feature must serve? Rank them. | All equal → force a ranking; it drives trade-offs |
| A2 | Deadline? What is fixed: date, scope or quality? | Everything fixed → flag |
| A3 | Team: how many people, which skills, who operates it in production? | Skills gap → prefer known tech |
| A4 | Mandated or forbidden technologies, vendors, clouds or licences? | — |
| A5 | Build, buy or integrate: is there a SaaS / library that already does this? | — |
| A6 | Budget for infrastructure and third-party services per month? | — |
| A7 | Expected lifetime: experiment to be thrown away, or core for years? | Experiment → simplest thing |
| A8 | Which quality matters most when two conflict (e.g. consistency vs availability, speed vs cost)? | — |

## B. Volumetrics and growth — back-of-the-envelope estimation

Fills: `Data model` (indexes), `Patterns`, `Testing strategy` (load).

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| B1 | How many users / tenants now, in 1 year, in 3 years? | — |
| B2 | How many of the key actions per day? Peak per minute / second? | "A lot" → order of magnitude (10, 1 000, 100 000) |
| B3 | When are the peaks (time of day, day of month, campaigns, Black Friday)? How spiky? | — |
| B4 | Read/write ratio for the main data? | — |
| B5 | How much data per record and how many records per year? Files or media sizes? | — |
| B6 | How long is data kept? Does history grow forever? | — |
| B7 | Any fan-out (one action notifies or updates many)? | Fan-out → async / queues |
| B8 | Any batch or scheduled jobs (nightly reports, billing runs, imports)? Time window? | — |

## C. Performance — ATAM scenarios, ISO 25010 performance efficiency

Fills: `Patterns`, `Testing strategy`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| C1 | Acceptable response time for each key interaction (p95)? | "Fast" → a number in ms or s |
| C2 | Which operations may be slow or asynchronous (with a "processing" state)? | — |
| C3 | Throughput target at peak? | — |
| C4 | Time limit for batch jobs or reports? | — |
| C5 | Search requirements: full-text, filters, geo, ranking? Result latency? | Search engine decision |

## D. Availability and reliability — SRE (SLO / error budget), Well-Architected reliability

Fills: `Patterns`, `Decisions (ADRs)`, `Threat model`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| D1 | What is the cost of 1 hour of downtime of this feature? | — |
| D2 | Availability target (99 %, 99.9 %, 99.99 %)? During which hours? | "100 %" → explain cost, pick a real target |
| D3 | **RPO**: how much data can we lose in a disaster (0, 1 min, 1 h, 1 day)? | — |
| D4 | **RTO**: how long may recovery take? | — |
| D5 | If a dependency (payment, SMS, email, maps) is down, what should still work? Graceful degradation? | — |
| D6 | Can the operation be retried safely? What happens on a duplicate request? | Idempotency requirement |
| D7 | Maintenance windows allowed? Zero-downtime deploys required? | — |

## E. Consistency, transactions and time — DDD aggregates, distributed systems

Fills: `Context map`, `Commands and domain events`, `Integration events` (delivery guarantee).

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| E1 | Which business rules must never be violated, even for a second (invariants)? | These define aggregate boundaries |
| E2 | Which data may be stale, and for how long (eventual consistency is OK for…)? | — |
| E3 | Does the order of events matter? Per what (per customer, per order)? | — |
| E4 | What if the same message is delivered twice? Lost? | Delivery guarantee + idempotent consumer |
| E5 | Concurrent edits: last write wins, optimistic locking, or merge? | — |
| E6 | Long-running processes spanning several steps or contexts (booking → payment → notification)? Compensation on failure? | Saga / process manager |
| E7 | Time-based rules (expiry, reminders, deadlines, time zones)? | Scheduled jobs, time-zone handling |
| E8 | Must actions be auditable (who did what, when, before/after)? | Audit log or event sourcing decision |

## F. Domain discovery — Event Storming prompts (Alberto Brandolini)

Fills: `Event Storming`, `Commands and domain events`, `Context map`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| F1 | What are all the things that *happen* in this flow, as facts in the past tense? | Present tense / CRUD names → rephrase as facts |
| F2 | Put them in order: what happens first, what last? | — |
| F3 | What triggers each event: a user command, an external system, time, or another event? | — |
| F4 | Who (actor/role) issues each command? | — |
| F5 | Policies: "Whenever <event>, then <command>" — which automatic reactions exist? | Hidden manual policies → make them explicit |
| F6 | What information does the actor need to see before deciding (read models)? | — |
| F7 | Which external systems are involved? | — |
| F8 | When can a command be rejected, and why? | Fills "Rejected when" |
| F9 | Hotspots: where do people disagree, not know, or see risk? | Record every hotspot |
| F10 | Which words mean different things to different people (e.g. "client", "booking")? | Bounded-context boundary signal |
| F11 | Which existing bounded context owns each concept? Does anything not fit any? | New context needs justification |

## G. Integration — Enterprise Integration Patterns, contract design

Fills: `Integration events`, `HTTP API`, `Patterns`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| G1 | Which external systems do we call, and which call us? | — |
| G2 | Protocol and format (REST, webhook, queue, file, SOAP)? Who owns the contract? | — |
| G3 | Their limits: rate limits, quotas, timeouts, sandbox availability, cost per call? | — |
| G4 | What if they are slow, down or return garbage? | Anti-corruption layer, retries, circuit breaker |
| G5 | Do we need webhooks / callbacks? How are they authenticated and replayed? | — |
| G6 | Who else (other contexts, other teams, partners) needs to know when this happens? | Integration event consumers |
| G7 | Versioning: who consumes our API / events, and how do we evolve them without breaking? | — |

## H. Data — data ownership, lifecycle, privacy

Fills: `Data model`, `Threat model`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| H1 | Which context owns each piece of data (single source of truth)? | Two owners → conflict |
| H2 | Which personal or sensitive data is stored? Is each field necessary? | Point at `legal:legal-privacy-data-protection` |
| H3 | Retention: how long for each data type? Legal minimum and maximum? | — |
| H4 | Deletion and anonymization on user request (LGPD/GDPR)? | — |
| H5 | Reporting / analytics needs: who queries what, how fresh, how heavy? | Read model or warehouse |
| H6 | Existing data to migrate or backfill? Volume? | — |
| H7 | Backups: frequency, retention, tested restore? | — |
| H8 | Multi-tenancy: data isolation level required (shared table, schema, database)? | — |

## I. Security — STRIDE, OWASP ASVS

Fills: `Threat model (STRIDE)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| I1 | Who must authenticate, and how (password, SSO, magic link, API key)? | — |
| I2 | Authorization model: roles, ownership, per-tenant, per-record? | — |
| I3 | What is the most valuable thing an attacker could steal or change here? | — |
| I4 | Any public or anonymous entry points (forms, links, webhooks)? Abuse or spam risk? | Rate limiting, captcha |
| I5 | Payments, card data or financial operations? | PCI scope — flag |
| I6 | Secrets and keys involved? Where do they live? | — |
| I7 | Compliance regimes (LGPD, GDPR, PCI DSS, HIPAA, SOC 2)? | — |
| I8 | What must be logged for security, and what must never be logged? | — |

## J. Operability — Well-Architected operational excellence, SRE

Fills: `Testing strategy`, `Decisions (ADRs)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| J1 | How will we know it is broken before users tell us (metrics, alerts)? | — |
| J2 | Which business metrics must be observable (bookings per hour, payment failures)? | — |
| J3 | Who is on call, and what runbook do they need? | — |
| J4 | Rollout: feature flag, gradual rollout, internal first? | — |
| J5 | Rollback: can we turn it off without a deploy? Reversible migrations? | — |
| J6 | Environments needed (dev, staging, preview)? Test data? | — |

## K. Evolvability and maintainability — ISO 25010 maintainability

Fills: `Patterns`, `Decisions (ADRs)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| K1 | What is most likely to change in the next year (rules, providers, channels, pricing)? | Only those deserve extension points |
| K2 | Will other products, partners or a mobile app reuse this? | — |
| K3 | Any part likely to be extracted into its own service later? | — |
| K4 | Configuration per tenant / per customer expected? | — |
| K5 | What would make this hard to delete if the experiment fails? | — |

## L. Cost — Well-Architected cost optimization

Fills: `Decisions (ADRs)`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| L1 | Acceptable cost per transaction / per user / per month? | — |
| L2 | Which third-party calls are billed per use (SMS, maps, AI, payments)? Volume × price? | — |
| L3 | Can expensive work be cached, batched or done off-peak? | — |

## M. Acceptance and testing

Fills: `Testing strategy`.

| # | Question | Weak-answer signal → follow-up |
|---|---|---|
| M1 | How will we prove it works — which scenarios must pass before release? | — |
| M2 | Any load or performance test required before go-live? | Use the numbers from B and C |
| M3 | External systems with sandboxes for integration tests? | — |
| M4 | Who signs off the release? | — |
