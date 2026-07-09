# ia-marketplace — Claude Code Skills Marketplace

This repository is a **Claude Code plugin marketplace**. It hosts skills that
were previously vendored inside the LinkDaily project and are now distributed
as installable plugins, organized **one plugin per domain**.

## Structure

```
ia-marktplace/
├── .claude-plugin/
│   └── marketplace.json          ← declares the 8 plugins
├── dev/                          ← plugin: dev (41 skills)
│   ├── .claude-plugin/plugin.json
│   └── skills/<skill>/SKILL.md
├── stack/                        ← plugin: stack (19 skills)
│   ├── .claude-plugin/plugin.json
│   └── skills/…
├── security/                     ← plugin: security (16 skills)
├── legal/                        ← plugin: legal (16 skills)
├── tools/                        ← plugin: tools (3 skills)
├── QA/                           ← plugin: QA (2 skills)
├── workflows/                    ← plugin: workflows (1 skill)
├── specs/                        ← plugin: specs (21 skills)
├── CLAUDE.md
├── README.md
├── AGENTS.md
├── CHANGELOG.md
└── LICENSE
```

Each plugin directory holds `.claude-plugin/plugin.json` (manifest) plus a
`skills/` folder. Every skill is a flat directory containing exactly one
`SKILL.md`, plus optional `references/` and `scripts/`. **No nesting** — Claude
Code only discovers `SKILL.md` one level deep inside `skills/`.

## Naming & invocation

- Skill directory name **equals** the SKILL.md `name:` frontmatter (kebab-case,
  `^[a-z0-9-]+$`, ≤ 64 chars). Names carry their domain prefix
  (`dev-architecture`, `stack-mediatr`, `security-owasp`).
- Once installed from this marketplace, a skill is **auto-namespaced by its
  plugin**: skill `stack-mediatr` in plugin `stack` is invoked as
  `stack:stack-mediatr`. The frontmatter `name` is never changed by the
  namespace — the prefix is applied only at invocation time.
- `description` is a single line (≤ 1024 chars) with a `USE FOR` / `DO NOT USE
  FOR` structure. `DO NOT USE FOR` cross-links the sibling skill that should win
  **by its flat name** (e.g. `use dev-architecture-microservices`) — those
  cross-links stay valid because sibling names are unchanged.
- Frontmatter keeps only `name` + `description` (plus `allowed-tools` where a
  skill needs it). No `license`, `compatibility`, or `references` keys — dropped
  reference URLs live in a `## References` body section.

## The 8 plugins

| Plugin | Skills | Domain |
|---|---|---|
| `dev` | 41 | Design patterns, algorithms, architectural styles, backend/frontend, craftsmanship, integration patterns |
| `stack` | 19 | .NET library selection & usage (MassTransit, MediatR, Dapper, Serilog, Polly, Redis, …) |
| `security` | 16 | OWASP, threat modeling, auth, crypto, input validation, supply chain, pen testing |
| `legal` | 16 | Privacy/GDPR/LGPD, licensing, billing/taxation, accessibility, compliance |
| `tools` | 3 | Docker & Git |
| `QA` | 2 | Browser automation, E2E testing & BDD/Gherkin authoring |
| `workflows` | 1 | Plan execution orchestrator |
| `specs` | 21 | Diagramming (C4, Mermaid, UML, PlantUML, D2, ERD, TOGAF, ArchiMate, functional), specification documents (PRD, TRD, BRD, ADR, RFC, Gherkin, Gauge, user guide) & knowledge-base building (LLM Wiki) |

## Adding a skill

1. Pick the plugin (`dev`, `stack`, `security`, `legal`, `tools`, …).
2. Create `<plugin>/skills/<skill-name>/SKILL.md` with `name` + `description`
   frontmatter. `name` must equal the directory name and carry the domain prefix.
3. Put implementation detail in `<plugin>/skills/<skill-name>/references/`.
4. If the plugin is brand new, add `<plugin>/.claude-plugin/plugin.json` and a
   new entry in `.claude-plugin/marketplace.json`.
5. Update this file's plugin table and `README.md`.

## Consuming this marketplace

A project registers it as a **local-directory** marketplace in its
`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "ia-marketplace": {
      "source": {
        "source": "directory",
        "path": "C:\\workspace\\Diary\\Projeto\\ia-marktplace"
      }
    }
  },
  "enabledPlugins": {
    "dev@ia-marketplace": true,
    "stack@ia-marketplace": true
  }
}
```

`enabledPlugins` keys are `<pluginName>@ia-marketplace`. LinkDaily is the
primary consumer — see its `.claude/settings.json`.
