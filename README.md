# ia-marketplace

A Claude Code **plugin marketplace** hosting reusable skills, organized one
plugin per domain. These skills previously lived inside the LinkDaily project
(`.claude/skills/`) and are now distributed from here so any project can install
the subsets it needs.

---

## Plugins

| Plugin | Install | Skills | Scope |
|--------|---------|--------|-------|
| **dev** | `/plugin install dev@ia-marketplace` | 42 | Design patterns, algorithms & data structures, architectural styles (DDD, hexagonal, microservices, event-driven, monoliths), backend/frontend architecture, craftsmanship (SOLID, clean code, refactoring, 12-factor), enterprise integration patterns |
| **stack** | `/plugin install stack@ia-marketplace` | 19 | .NET library selection & usage: MassTransit, MediatR, AutoMapper, Dapper, Serilog, Polly, Redis, Validot, NCrontab, Topshelf, OpenAPI, ASP.NET Identity, i18n, observability/OTLP, Plunk email, Docker, hygiene |
| **security** | `/plugin install security@ia-marketplace` | 16 | OWASP, threat modeling, auth, cryptography, data protection, input validation, API security, logging/monitoring, supply chain, pen testing, red teaming, secure SDLC, AI security |
| **legal** | `/plugin install legal@ia-marketplace` | 16 | Privacy & data protection (GDPR/LGPD/CCPA), open-source licensing, billing & taxation, accessibility, consumer protection, content moderation, contracts, compliance, IP, AI regulation |
| **tools** | `/plugin install tools@ia-marketplace` | 3 | Docker & Git |
| **QA** | `/plugin install QA@ia-marketplace` | 3 | Browser automation & E2E testing (playwright-cli) + BDD/Gherkin `.feature` authoring (bdd-gherkin) + Aspire/Playwright .NET functional tests (e2e-functional-testing) |
| **workflows** | `/plugin install workflows@ia-marketplace` | 2 | Plan execution orchestrator (workflows) + Tamandua pipeline run operation (workflows-tamandua) |
| **specs** | `/plugin install specs@ia-marketplace` | 21 | Specifications & architecture documentation: diagramming (C4, Mermaid, UML, PlantUML, D2, ERD, TOGAF, ArchiMate, functional), specification documents (PRD, TRD, BRD, ADR, RFC, Gherkin, Gauge, user guide) and knowledge-base building (LLM Wiki) |
| **custom-agent** | `/plugin install custom-agent@ia-marketplace` | 1 | graphify — knowledge-graph building & querying over any input |
| **product** | `/plugin install product@ia-marketplace` | 4 | Product discovery pipeline: ideation → design → architecture, with research/review/critique subagents |

**127 skills total.**

---

## Product pipeline

The `product` plugin runs a gated discovery flow, handing off through
`docs/product/<slug>/` artifacts:

```
Skill("product:product")               # router
  → product:product-ideation           # idea → validated problem/opportunity
  → product:product-design             # opportunity → product design
  → product:product-architecture       # design → architecture (force-driven patterns)
  → superpowers:brainstorming          # hand off to implementation planning
```

Subagents (`product:product-market-researcher`, `product:product-design-reviewer`,
`product:product-architecture-critic`) are dispatched by the skills.

---

## Installation

This marketplace is published on GitHub (`DanielPohlmann/ia-marktplace`) and can
also be registered as a local-directory source. Register it once, then install
the plugins you need.

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
    "specs@ia-marketplace": true,
    "custom-agent@ia-marketplace": true,
    "product@ia-marketplace": true
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
| `workflows-tamandua` | workflows | `Skill("workflows:workflows-tamandua")` |
| `graphify` | custom-agent | `Skill("custom-agent:graphify")` |

Each domain keeps a **thin index skill** (`dev`, `stack`, `security`, `legal`,
`tools`) that maps the domain and points to the specific `<domain>-*` skill to
reach for. Prefer the most specific skill over its index.

---

## Structure

```
ia-marktplace/
├── .claude-plugin/marketplace.json     ← 10 plugins
├── dev/          .claude-plugin/plugin.json + skills/  (42)
├── stack/        .claude-plugin/plugin.json + skills/  (19)
├── security/     .claude-plugin/plugin.json + skills/  (16)
├── legal/        .claude-plugin/plugin.json + skills/  (16)
├── tools/        .claude-plugin/plugin.json + skills/  (3)
├── QA/           .claude-plugin/plugin.json + skills/  (3)
├── workflows/    .claude-plugin/plugin.json + skills/  (2)
├── specs/        .claude-plugin/plugin.json + skills/  (21)
├── custom-agent/ .claude-plugin/plugin.json + skills/  (1)
├── product/      .claude-plugin/plugin.json + skills/  (4) + agents/
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
