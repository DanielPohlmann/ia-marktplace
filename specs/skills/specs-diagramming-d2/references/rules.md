# D2 Rules

Best practices and rules for D2.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use containers to represent system boundaries. | MEDIUM | [`d2-use-containers-to-represent-system-boundaries.md`](d2-use-containers-to-represent-system-boundaries.md) |
| 2 | Define style classes | MEDIUM | [`d2-define-style-classes.md`](d2-define-style-classes.md) |
| 3 | Use the `direction` keyword | MEDIUM | [`d2-use-the-direction-keyword.md`](d2-use-the-direction-keyword.md) |
| 4 | Leverage layers for progressive detail. | MEDIUM | [`d2-leverage-layers-for-progressive-detail.md`](d2-leverage-layers-for-progressive-detail.md) |
| 5 | Use scenarios to show state changes. | MEDIUM | [`d2-use-scenarios-to-show-state-changes.md`](d2-use-scenarios-to-show-state-changes.md) |
| 6 | Choose the right layout engine. | MEDIUM | [`d2-choose-the-right-layout-engine.md`](d2-choose-the-right-layout-engine.md) |
| 7 | Use `--watch` during development. | MEDIUM | [`d2-use-watch-during-development.md`](d2-use-watch-during-development.md) |
| 8 | Use `--sketch` for informal communication. | MEDIUM | [`d2-use-sketch-for-informal-communication.md`](d2-use-sketch-for-informal-communication.md) |
| 9 | Keep `.d2` files in version control. | MEDIUM | [`d2-keep-d2-files-in-version-control.md`](d2-keep-d2-files-in-version-control.md) |
| 10 | Use SQL table shapes for data modeling. | MEDIUM | [`d2-use-sql-table-shapes-for-data-modeling.md`](d2-use-sql-table-shapes-for-data-modeling.md) |
| 11 | Reference icons from the Terrastruct icon set | MEDIUM | [`d2-reference-icons-from-the-terrastruct-icon-set.md`](d2-reference-icons-from-the-terrastruct-icon-set.md) |

---

---
title: "Choose the right layout engine."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Choose the right layout engine.

Start with `dagre` for simplicity. Switch to `ELK` for complex diagrams. Use `TALA` for presentation-quality output.

---

---
title: "Define style classes"
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Define style classes

Define style classes: for consistent visual language across the diagram. Create classes for services, datastores, external systems, etc.

---

---
title: "Keep `.d2` files in version control."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Keep `.d2` files in version control.

Like all diagrams-as-code, D2 files should live in the repository alongside the systems they describe.

---

---
title: "Leverage layers for progressive detail."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Leverage layers for progressive detail.

Use a base layer for the high-level overview and named layers for zoomed-in views.

---

---
title: "Reference icons from the Terrastruct icon set"
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Reference icons from the Terrastruct icon set

Reference icons from the Terrastruct icon set: or use custom icon URLs for visual clarity in architecture diagrams.

---

---
title: "Use containers to represent system boundaries."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Use containers to represent system boundaries.

Nesting shapes inside containers clearly communicates which components belong to which subsystem.

---

---
title: "Use scenarios to show state changes."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Use scenarios to show state changes.

Scenarios are ideal for showing normal operation vs. failure modes, or before/after states.

---

---
title: "Use `--sketch` for informal communication."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Use `--sketch` for informal communication.

The hand-drawn style signals that diagrams are conceptual, not final.

---

---
title: "Use SQL table shapes for data modeling."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Use SQL table shapes for data modeling.

D2's `sql_table` shape with constraints is a concise way to document database schemas.

---

---
title: "Use the `direction` keyword"
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Use the `direction` keyword

Use the `direction` keyword: to control the overall layout orientation. `direction: right` works well for data flow; `direction: down` works well for hierarchies.

---

---
title: "Use `--watch` during development."
impact: MEDIUM
impactDescription: "general best practice"
tags: d2, specs, diagramming, architecture-diagrams, system-design-diagrams, declarative-diagramming
---

## Use `--watch` during development.

The watch mode auto-recompiles on save, giving you a live preview workflow.
