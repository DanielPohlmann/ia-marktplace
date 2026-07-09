# ia-marketplace

A Claude Code **plugin marketplace** hosting reusable skills, organized one
plugin per domain. These skills previously lived inside the LinkDaily project
(`.claude/skills/`) and are now distributed from here so any project can install
the subsets it needs.

---

## Plugins

| Plugin | Install | Skills | Scope |
|--------|---------|--------|-------|
| **dev** | `/plugin install dev@ia-marketplace` | 41 | Design patterns, algorithms & data structures, architectural styles (DDD, hexagonal, microservices, event-driven, monoliths), backend/frontend architecture, craftsmanship (SOLID, clean code, refactoring, 12-factor), enterprise integration patterns |
| **stack** | `/plugin install stack@ia-marketplace` | 19 | .NET library selection & usage: MassTransit, MediatR, AutoMapper, Dapper, Serilog, Polly, Redis, Validot, NCrontab, Topshelf, OpenAPI, ASP.NET Identity, i18n, observability/OTLP, Plunk email, Docker, hygiene |
| **security** | `/plugin install security@ia-marketplace` | 16 | OWASP, threat modeling, auth, cryptography, data protection, input validation, API security, logging/monitoring, supply chain, pen testing, red teaming, secure SDLC, AI security |
| **legal** | `/plugin install legal@ia-marketplace` | 16 | Privacy & data protection (GDPR/LGPD/CCPA), open-source licensing, billing & taxation, accessibility, consumer protection, content moderation, contracts, compliance, IP, AI regulation |
| **tools** | `/plugin install tools@ia-marketplace` | 3 | Docker & Git |
| **QA** | `/plugin install QA@ia-marketplace` | 2 | Browser automation & E2E testing (playwright-cli) + BDD/Gherkin `.feature` authoring (bdd-gherkin) |
| **workflows** | `/plugin install workflows@ia-marketplace` | 1 | Plan execution orchestrator |
| **specs** | `/plugin install specs@ia-marketplace` | 19 | Specifications & architecture documentation: diagramming (C4, Mermaid, UML, PlantUML, D2, ERD, TOGAF, ArchiMate, functional) and specification documents (PRD, TRD, BRD, ADR, RFC, Gherkin, Gauge) |

**117 skills total.**

---

## Installation

This marketplace lives on the local filesystem (it is not published to a git
remote). Register it once, then install the plugins you need.

### Option A — via CLI

```
/plugin marketplace add C:\workspace\Diary\Projeto\ia-marktplace
/plugin install dev@ia-marketplace
/plugin install stack@ia-marketplace
```

### Option B — via project settings (auto-enable for a repo)

Add to the consuming project's `.claude/settings.json`:

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
    "stack@ia-marketplace": true,
    "security@ia-marketplace": true,
    "legal@ia-marketplace": true,
    "tools@ia-marketplace": true,
    "QA@ia-marketplace": true,
    "workflows@ia-marketplace": true,
    "specs@ia-marketplace": true
  }
}
```

`LinkDaily` is configured this way — see its `.claude/settings.json`.

---

## Invocation

Skills are auto-namespaced by their plugin once installed:

| Skill (flat name) | Plugin | Invoke as |
|---|---|---|
| `dev-architecture-domain-driven-design` | dev | `Skill("dev:dev-architecture-domain-driven-design")` |
| `stack-mediatr` | stack | `Skill("stack:stack-mediatr")` |
| `security-owasp` | security | `Skill("security:security-owasp")` |
| `tools-git` | tools | `Skill("tools:tools-git")` |
| `workflows` | workflows | `Skill("workflows:workflows")` |

Each domain keeps a **thin index skill** (`dev`, `stack`, `security`, `legal`,
`tools`) that maps the domain and points to the specific `<domain>-*` skill to
reach for. Prefer the most specific skill over its index.

---

## Structure

```
ia-marktplace/
├── .claude-plugin/marketplace.json     ← 8 plugins
├── dev/          .claude-plugin/plugin.json + skills/  (41)
├── stack/        .claude-plugin/plugin.json + skills/  (19)
├── security/     .claude-plugin/plugin.json + skills/  (16)
├── legal/        .claude-plugin/plugin.json + skills/  (16)
├── tools/        .claude-plugin/plugin.json + skills/  (3)
├── QA/           .claude-plugin/plugin.json + skills/  (2)
├── workflows/    .claude-plugin/plugin.json + skills/  (1)
├── specs/        .claude-plugin/plugin.json + skills/  (19)
├── CLAUDE.md · AGENTS.md · CHANGELOG.md · LICENSE
```

Each skill directory has exactly one `SKILL.md` plus optional `references/` and
`scripts/`. No nesting; no `AGENTS.md`/`README.md`/`metadata.json` inside skills.

---

## Contributing

See [`CLAUDE.md`](CLAUDE.md) for the "add a skill" workflow, naming rules, and
frontmatter conventions. Skill directory name must equal the SKILL.md `name`,
and `description` stays a single line with `USE FOR` / `DO NOT USE FOR`.

---

_Maintained by Daniel Heler Pohlmann._
