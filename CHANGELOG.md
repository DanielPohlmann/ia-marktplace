# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [Unreleased]

### Added

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
