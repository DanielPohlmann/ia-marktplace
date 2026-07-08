# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

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

- Replaced the previous "way2-ai-plugin" template scaffold (marketplace.json,
  README, CLAUDE.md, AGENTS.md) — its plugin entries referenced directories that
  never existed in this repo.
