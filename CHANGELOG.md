# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [Unreleased]

### Added

- New skill `dev-system-design` (`dev` plugin, now 44 skills): an 8-step
  procedure for designing or reviewing systems under volume, spikes, live
  updates or data growth — requirements with numbers, estimation, entities,
  API, naive-first high-level design, deep dives — with references on
  estimation, the scaling ladder, load balancing, database selection
  (CAP/PACELC), sharding, real-time delivery, contention and spikes, and large
  files / ID generation.
- New skill `dev-craftsmanship-oo-review`: OO design checklist for code review —
  signal → principle → minimal correction table, a YAGNI gate before every
  finding, severity guide, language/ORM exceptions and a finding format; with
  references for a signals catalog and object calisthenics (as review alarms,
  not laws).
- `dev-backend-data-modeling/references/numeric-precision.md`: money and exact
  quantities as decimal or integer minor units, database precision/scale,
  rounding policy, narrowing conversions and serialization pitfalls.

- New skill `workflows-tamandua` (`workflows` plugin, now 2 skills): operator
  guide for Tamandua delivery runs — start a run for a plan or spec, read
  status and logs, explain open gate findings, tell paused (rate limit) from
  blocked (budget, dispute, read-only violation, non-code failure) from failed,
  and resume a blocked run after a human decision. References: CLI catalog,
  findings contract (`FINDINGS_JSON` / `RESOLVED` / `DISPUTED_JSON`, severities,
  fingerprints, dispute rule), troubleshooting. Invoked as
  `workflows:workflows-tamandua`.
- New plugin `product` (4 skills, 3 agents): gated product discovery pipeline —
  `product` (router), `product-ideation`, `product-design`, `product-architecture`
  (with force-driven pattern selection) — handing off through
  `docs/product/<slug>/` artifacts, with subagents `product-market-researcher`,
  `product-design-reviewer` and `product-architecture-critic`.
- `verify_marketplace.py` validates `<plugin>/agents/*.md` (`check_agent()`),
  covered by `scripts/test_verify_marketplace.py` in CI.
- New skill `dev-integration-patterns-transactional-outbox` (`dev` plugin, now
  42 skills): the dual-write problem and its strategies — transactional outbox
  with polling publisher or CDC/log tailing, inbox/idempotent consumers,
  listen-to-yourself, event sourcing, reconciliation, and why not 2PC. Sibling
  descriptions cross-link to it.
- New plugin `specs` (19 skills): specifications & architecture documentation.
  Flattened from the `agent-skills` authoring repo's nested `specs` tree into the
  standard flat layout — diagramming (C4, Mermaid, UML, PlantUML, D2, ERD, TOGAF,
  ArchiMate, functional) and specification documents (PRD, TRD, BRD, ADR, RFC,
  Gherkin, Gauge). The source `tools` subtree (Spec Kit) was intentionally
  excluded. Invoked as `specs:<skill>` (e.g. `specs:specs-diagramming-c4-diagrams`).

### Changed

- `dev-craftsmanship-clean-code`: function length and argument counts are now
  review signals, not verdicts; language conventions override generic naming
  rules (the C# `I` interface prefix is no longer listed as an encoding to
  remove); "Don't Return Null" lists idiomatic alternatives (Try-pattern,
  nullable reference types, Optional, empty collections); the Law of Demeter
  example now shows real tell-don't-ask and when the law does not apply (DTOs,
  fluent APIs, query pipelines).
- `dev-craftsmanship-refactoring`: "deadline is imminent" now has a decision
  criterion, and a new `references/design-rot.md` covers rigidity, fragility,
  immobility and viscosity with review signals.
- `dev-craftsmanship-solid`: restructured around review guardrails — each
  principle now lists detectable signals, the correction and when not to apply
  it. SRP is framed by actors (technical-step splits are called out as
  separation of concerns), OCP states where the variant selection lives, LSP
  lists concrete client- and override-side signals, and DIP gains a two-step
  rule (own the dependency, then invert only for tests, a second
  implementation or a module boundary). Code examples moved to
  `references/examples.md`; body is back under the 1500-word budget.
- `dev-design-patterns-creational/-structural/-behavioral`: every pattern now
  has review signals and when-not-to-use guidance; adds Simple Factory (not
  GoF), Singleton thread-safety, Observer pitfalls, State transition signals,
  and Template Method only after duplication exists.
- `dev-backend-caching`: write-through is no longer described as strongly
  consistent (it is a dual write); adds when to cache at all, invalidate after
  commit, stampede, cache-down fallback and multi-instance in-process drift.
- `dev-architecture-event-driven`: concrete CQRS adoption signals (a read
  replica is not CQRS; feed the read store via outbox/CDC), log vs queue
  brokers, and publishing reliably.
- `dev-architecture-event-driven` (event sourcing): when to use it and when an
  append-only history or temporal table is enough; stream design; appending with
  an expected version; validating commands on the write side, never on the read
  model; snapshots only for measured rehydration latency, versioned and
  disposable; compensating events instead of rewriting history, with replays
  that never re-run side effects; recorded vs effective time; upcasting, with
  stored events kept apart from integration events; personal data via
  crypto-shredding; Kafka as a store needs infinite retention and no
  compaction. Projections are idempotent with a checkpoint and rebuilt in
  parallel. `dev-integration-patterns-transactional-outbox` no longer implies
  exactly-once delivery for event sourcing.
- `dev-architecture-microservices` and `dev-integration-patterns` now state the
  same sync vs async rule instead of contradicting each other.
- `dev-integration-patterns-messaging-endpoints`: Transactional Client
  atomicity caveat with a separate broker; Idempotent Receiver records the
  message ID in the same transaction under a unique constraint.
- `dev-backend-api-design`: money modeled as decimal / minor units instead of
  `Float` / `double` in GraphQL, gRPC and JSON examples.
- `dev` and `dev-craftsmanship` routers point to the two new skills.
- `README.md` total corrected to 124 skills.
- Removed skill `tamandua-agents` from the `custom-agent` plugin (now 1 skill:
  `graphify`); marketplace now ships 121 skills.
- Token-efficiency pass over all skills:
  - Rewrote every `description` to a short trigger + keyword format (total
    87k → 46k chars, median 718 → 375), cutting the always-loaded skill
    listing roughly in half. Cross-links preserved.
  - Progressive disclosure for the 64 skills over 1500 words: catalogs,
    templates, and deep dives moved to `references/` behind a
    `## Detailed reference` table (median body 1551 → ~845 words).
  - Removed consumer-project (LinkDaily) specifics so skills are generic;
    `specs-documentation-userguide/references/linkdaily-context.md` →
    `example-project-context.md`.
  - `verify_marketplace.py` now warns on descriptions > 600 chars and
    bodies > 1500 words.
- Renamed plugin `playwright-cli` → `QA` (directory, `marketplace.json` entry, and
  `plugin.json` manifest). The skill inside remains `playwright-cli`, so it is now
  invoked as `QA:playwright-cli`.
- Renamed plugin `run-plan` → `workflows` (directory, `marketplace.json` entry,
  and `plugin.json` manifest). The skill inside was also renamed `run-plan` →
  `workflows`, so it is now invoked as `workflows:workflows`.

---

## [1.0.0] — 2026-07-08

### Added

- Initial marketplace release. Imported the 97 skills previously vendored in the
  LinkDaily project (`.claude/skills/`) and organized them into **7 domain
  plugins**: `dev` (41), `stack` (19), `security` (16), `legal` (16), `tools`
  (3), `playwright-cli` (1), `run-plan` (1).
- `.claude-plugin/marketplace.json` declaring the 7 plugins.
- Per-plugin `.claude-plugin/plugin.json` manifests.

### Changed

- Replaced the previous plugin template scaffold (marketplace.json,
  README, CLAUDE.md, AGENTS.md) — its plugin entries referenced directories that
  never existed in this repo.
