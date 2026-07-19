# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [Unreleased]

### Added

- New plugin `specs` (19 skills): specifications & architecture documentation.
  Flattened from the `agent-skills` authoring repo's nested `specs` tree into the
  standard flat layout — diagramming (C4, Mermaid, UML, PlantUML, D2, ERD, TOGAF,
  ArchiMate, functional) and specification documents (PRD, TRD, BRD, ADR, RFC,
  Gherkin, Gauge). The source `tools` subtree (Spec Kit) was intentionally
  excluded. Invoked as `specs:<skill>` (e.g. `specs:specs-diagramming-c4-diagrams`).

### Changed

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
