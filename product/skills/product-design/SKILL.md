---
name: product-design
description: Use when an idea brief is approved and the experience must be designed (journeys, screens, states, copy, accessibility) plus HTML prototypes aligned to the project's design system. USE FOR: user journeys, screen inventory, wireframes, interaction states, UX copy keys, design tokens, accessibility checklist, prototype review. DO NOT USE FOR: business ideation (use product-ideation), component implementation (use vue-best-practices), technical design (use product:product-architecture).
---

# product-design — Stage 2: Interface & Experience Design

**Announce at start:** "Using product-design for `<slug>`."

## Gate

Read `docs/product/<slug>/01-ideation.md`. If it is not `approved`, stop and route through `product:product`.

## Step 0 — Design system

Find the design-system document: the path under a `Design system` heading in `CLAUDE.md`, else the first `**/DESIGN-SYSTEM.md`.

- **Found:** read it fully. Canonical patterns are constraints, the "do not copy" list is forbidden, and open decisions this idea touches must be raised with the user.
- **Missing:** before any screen work, draft one from theme files, CSS variables, utility-CSS config, component usage and layouts; get it approved; save it where the user says (default `.planning/codebase/DESIGN-SYSTEM.md`).

Each screen targets exactly one **surface** declared in the design system.

## Process

Skills named in parentheses are used when installed; otherwise apply the practice directly.

1. **Artifact** from `references/design-template.md`, `inputs: [01-ideation.md]`.
2. **Figma (optional).** If the brief links a Figma file and a Figma MCP is available, read it as reference. The deliverable is still HTML.
3. **Journeys** per persona and job: trigger → steps → outcome, low point marked (`customer-journey-map:customer-journey-map`).
4. **Story map**: activities backbone and first-release walking skeleton (`user-story-mapping:user-story-mapping`). Scope, not tickets.
5. **Screen inventory**: surface, purpose, primary action, data shown, entry points.
6. **States** per screen: empty, loading, error, success, no-permission, edge cases (long text, zero, many).
7. **Copy**: every user-facing string is a localization key with default text (`design:ux-copy`). No string in a prototype without a key.
8. **Quality**: back-office surfaces follow `interface-design`; public surfaces follow `frontend-design:frontend-design`. Run `design:design-critique` on your proposal before showing it.
9. **Prototype**: one self-contained HTML file per key screen in `docs/product/<slug>/prototype/`, using the design system's real tokens as CSS variables, light and dark if the surface supports both (`playground:playground`).
10. **Review**: dispatch `product:product-design-reviewer` with prototype paths, the design-system path and the screen inventory. Fix every blocking finding. Record all findings, blocking (as resolved) and non-blocking, in the `## Review findings` table with a Resolution.
11. **Accessibility**: fill the WCAG 2.2 AA checklist (`legal:legal-accessibility`, `design:accessibility-review`).
12. **Handoff**: data each screen reads and writes, state-changing actions, real-time needs, permissions (`design:design-handoff`).
13. **Approval**: `status: in-review`, list the prototype paths, ask: "Approve the design so we can move to architecture?"

## Pitfalls

- A new visual style instead of the design system.
- Copying patterns listed as leftovers.
- Hardcoded strings in prototypes.
- Happy path only.

## Detailed reference

| File | Contents |
|---|---|
| `references/design-template.md` | Skeleton of `02-design.md` |
