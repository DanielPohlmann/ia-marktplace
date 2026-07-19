# C4 Diagrams Rules

Best practices and rules for C4 Diagrams.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start at Level 1. | CRITICAL | [`c4-diagrams-start-at-level-1.md`](c4-diagrams-start-at-level-1.md) |
| 2 | Use hierarchical decomposition. | CRITICAL | [`c4-diagrams-use-hierarchical-decomposition.md`](c4-diagrams-use-hierarchical-decomposition.md) |
| 3 | Name elements consistently. | MEDIUM | [`c4-diagrams-name-elements-consistently.md`](c4-diagrams-name-elements-consistently.md) |
| 4 | Limit detail per diagram. | MEDIUM | [`c4-diagrams-limit-detail-per-diagram.md`](c4-diagrams-limit-detail-per-diagram.md) |
| 5 | Tag elements for styling. | MEDIUM | [`c4-diagrams-tag-elements-for-styling.md`](c4-diagrams-tag-elements-for-styling.md) |
| 6 | Skip Level 4 unless necessary. | MEDIUM | [`c4-diagrams-skip-level-4-unless-necessary.md`](c4-diagrams-skip-level-4-unless-necessary.md) |
| 7 | Version your DSL. | MEDIUM | [`c4-diagrams-version-your-dsl.md`](c4-diagrams-version-your-dsl.md) |
| 8 | Use `autolayout` | MEDIUM | [`c4-diagrams-use-autolayout.md`](c4-diagrams-use-autolayout.md) |
| 9 | Add deployment views | MEDIUM | [`c4-diagrams-add-deployment-views.md`](c4-diagrams-add-deployment-views.md) |
| 10 | Export to Mermaid | MEDIUM | [`c4-diagrams-export-to-mermaid.md`](c4-diagrams-export-to-mermaid.md) |

---

---
title: "Add deployment views"
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Add deployment views

Add deployment views: for infrastructure mapping — they show how containers map to cloud services, VMs, or Kubernetes clusters.

---

---
title: "Export to Mermaid"
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Export to Mermaid

Export to Mermaid: for embedding in Markdown documentation. Use the Structurizr CLI `export -format mermaid` command.

---

---
title: "Limit detail per diagram."
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Limit detail per diagram.

Keep each diagram to 5-20 elements. If a diagram is too crowded, it means the container or component needs further decomposition.

---

---
title: "Name elements consistently."
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Name elements consistently.

Use the same name for an element across all levels so readers can trace from Context down to Component.

---

---
title: "Skip Level 4 unless necessary."
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Skip Level 4 unless necessary.

Code-level diagrams are better generated from source code. Reserve manual Level 4 diagrams for algorithmically complex components.

---

---
title: "Start at Level 1."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Start at Level 1.

Always begin with a System Context diagram to define boundaries and external dependencies before zooming in.

---

---
title: "Tag elements for styling."
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Tag elements for styling.

Use tags like `"Database"`, `"External"`, `"WebBrowser"` to apply consistent visual styles.

---

---
title: "Use `autolayout`"
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Use `autolayout`

Use `autolayout`: to get consistent, automated positioning. Override with explicit positioning only when automatic layout produces poor results.

---

---
title: "Use hierarchical decomposition."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Use hierarchical decomposition.

Each level should tell a coherent story at its abstraction level. Do not mix abstractions (e.g., do not show database tables in a Container diagram).

---

---
title: "Version your DSL."
impact: MEDIUM
impactDescription: "general best practice"
tags: c4-diagrams, specs, diagramming, c4-model-diagrams, system-context-diagrams, container-diagrams
---

## Version your DSL.

Store `workspace.dsl` in Git alongside the source code it describes. Treat it as a first-class artifact.
