---
name: product-architecture
description: Use when an approved interface design must become a technical design before writing a spec or plan. USE FOR: event storming, bounded-context mapping, aggregates, commands and events, integration contracts, API shape, pattern selection, ADRs, C4 diagrams, threat model, architecture critique. DO NOT USE FOR: ideation (use product-ideation), UI design (use product-design), implementation plans (use superpowers:writing-plans).
---

# product-architecture — Stage 3: Technical Design

**Announce at start:** "Using product-architecture for `<slug>`."

## Gate

Read `01-ideation.md` and `02-design.md` in `docs/product/<slug>/`. If `02-design.md` is not `approved`, stop and route through `product:product`.

## Step 0 — Current architecture is a constraint

Read the architecture document (path under an `Architecture` heading in `CLAUDE.md`, else the first `**/ARCHITECTURE.md`), the conventions document next to it if present, and the concerns/tech-debt document. Fit the existing style, contexts and conventions; every departure needs an ADR.

## Process

Skills referenced in this skill are used when installed; otherwise apply the practice directly.

1. **Artifact** from `references/architecture-template.md`, `inputs: [01-ideation.md, 02-design.md]`.
2. **Event Storming** from the design's handoff table: domain events (past tense), commands, actors, policies, read models, hotspots. Use the project template (`**/event-storming/_template.md`, default `.planning/event-storming/<slug>.md`). Follow `dev:dev-architecture-domain-driven-design` and `dev:dev-architecture-event-driven`.
3. **Context mapping.** Assign each aggregate to an existing bounded context or justify a new one. Aggregates reference each other by ID; one aggregate per transaction.
4. **Contracts.** Integration events: name, producer, consumers, minimal payload (IDs over embedded objects). HTTP: method, route, request, response, errors (`dev:dev-backend-api-design`).
5. **Data.** Tables/collections and their owning aggregate (`dev:dev-backend-data-modeling`).
6. **Patterns.** See below.
7. **Diagrams.** C4 context and container in Mermaid plus a sequence diagram of the main flow (`specs:specs-diagramming-c4-diagrams`, `specs:specs-diagramming-mermaidjs`).
8. **Decisions.** One ADR per significant choice (`specs:specs-documentation-adr`).
9. **Threat model.** STRIDE over new flows and data (`security:security-threat-modeling`); flag personal data (`legal:legal-privacy-data-protection`).
10. **Testing strategy** (`engineering:testing-strategy`).
11. **Critique.** Dispatch `product:product-architecture-critic` with the artifact, Event Storming and architecture document paths. Resolve blocking findings; list the rest under Open questions.
12. **Approval.** `status: in-review`, ask: "Approve the architecture so we can write the spec and plan?"
13. **Handoff.** After approval, invoke `superpowers:brainstorming` with the three artifacts, then `superpowers:writing-plans`.

## Patterns

Choose a pattern only against a **written force** — a concrete problem in this feature. Never add one speculatively.

| Level | Examples | Rule |
|---|---|---|
| Integration / architectural | transactional outbox, inbox / idempotent consumer, saga or process manager, CQRS read model, anti-corruption layer | **Mandatory decision** whenever a flow crosses contexts or an external system: every cross-context event declares its delivery guarantee |
| Design (GoF) | Strategy, Adapter, Factory, Decorator, State | Name it only when a force exists; the implementation plan details it |

1. **Reuse first.** Search the conventions/architecture documents and the code for an equivalent pattern already in use. Introducing a new one where an equivalent exists requires an ADR.
2. Record every choice in `## Patterns`: force, pattern, simpler alternative rejected and why, existing precedent.
3. Skills: `dev:dev-integration-patterns` and children (including `dev:dev-integration-patterns-transactional-outbox`), `dev:dev-design-patterns`, `dev:dev-design-patterns-behavioral`, `dev:dev-design-patterns-structural`, `dev:dev-craftsmanship-solid`.

## Pitfalls

- A new style instead of extending the existing one.
- Fat integration events; two aggregates in one transaction.
- Patterns without a force, or cross-context events without a delivery strategy.
- Diagrams that disagree with the text.

## Detailed reference

| File | Contents |
|---|---|
| `references/architecture-template.md` | Skeleton of `03-architecture.md` |
