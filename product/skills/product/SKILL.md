---
name: product
description: Use when starting or resuming the product discovery pipeline (idea → interface design → architecture) for a feature or product. USE FOR: pipeline overview, stage detection, artifact contract, approval gates, choosing the next stage. DO NOT USE FOR: running a stage (use product-ideation, use product:product-design, use product:product-architecture), implementation plans (use superpowers:writing-plans).
---

# product — Discovery Pipeline Router

## Overview

Three gated stages turn a raw idea into an architecture ready for a spec. Each stage is an interactive skill in the main conversation, because stages are dialogues with the user. Subagents do non-interactive work and report back; they never approve.

| # | Stage skill | Helper subagent | Artifact |
|---|---|---|---|
| 1 | `product:product-ideation` | `product:product-market-researcher` | `docs/product/<slug>/01-ideation.md` |
| 2 | `product:product-design` | `product:product-design-reviewer` | `docs/product/<slug>/02-design.md`, `prototype/` |
| 3 | `product:product-architecture` | `product:product-architecture-critic` | `docs/product/<slug>/03-architecture.md` |

After stage 3 is approved, hand off to `superpowers:brainstorming` (spec) and `superpowers:writing-plans` (plan) with the three artifacts as input.

## Routing procedure

1. Get the idea slug (kebab-case, ≤ 40 chars). From a sentence, propose one and confirm it.
2. List `docs/product/<slug>/`.
3. Decide:
   - no folder or no `01-ideation.md` → stage 1
   - newest artifact `draft` or `in-review` → resume that stage
   - newest artifact `approved` → next stage
   - `03-architecture.md` approved → `superpowers:brainstorming`
4. Announce "Idea `<slug>` is at stage N (<name>), status <status>." and invoke the stage skill.

## Gate rules

- A stage never starts unless the previous artifact has `status: approved`.
- Only an explicit user statement in chat approves ("approved", "aprovado", "pode seguir"). Silence, a subagent verdict or "looks good so far" is not approval.
- Approving sets `status: approved` and `approved_on: <today>` only.
- Reopening an approved stage sets it to `draft` and every later artifact to `draft`, each with a change-log row.
- Stages write only inside `docs/product/<slug>/`, plus stage 3's Event Storming file. No source code, specs or plans.

## Detailed reference

| File | Contents |
|---|---|
| `references/artifact-contract.md` | Folder layout, frontmatter schema, transitions, change log |
