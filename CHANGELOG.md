# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [Unreleased]

### Added

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
