# PlantUML Rules

Best practices and rules for PlantUML.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use `@startuml` / `@enduml` blocks. | CRITICAL | [`plantuml-use-startuml-enduml-blocks.md`](plantuml-use-startuml-enduml-blocks.md) |
| 2 | Organize with `!include`. | MEDIUM | [`plantuml-organize-with-include.md`](plantuml-organize-with-include.md) |
| 3 | Use skinparam for consistent styling. | MEDIUM | [`plantuml-use-skinparam-for-consistent-styling.md`](plantuml-use-skinparam-for-consistent-styling.md) |
| 4 | Use built-in themes | MEDIUM | [`plantuml-use-built-in-themes.md`](plantuml-use-built-in-themes.md) |
| 5 | Leverage the preprocessor. | MEDIUM | [`plantuml-leverage-the-preprocessor.md`](plantuml-leverage-the-preprocessor.md) |
| 6 | Use C4-PlantUML for architecture diagrams. | MEDIUM | [`plantuml-use-c4-plantuml-for-architecture-diagrams.md`](plantuml-use-c4-plantuml-for-architecture-diagrams.md) |
| 7 | Use aliases for readability. | MEDIUM | [`plantuml-use-aliases-for-readability.md`](plantuml-use-aliases-for-readability.md) |
| 8 | Keep sequence diagrams focused. | MEDIUM | [`plantuml-keep-sequence-diagrams-focused.md`](plantuml-keep-sequence-diagrams-focused.md) |
| 9 | Use `left to right direction` | MEDIUM | [`plantuml-use-left-to-right-direction.md`](plantuml-use-left-to-right-direction.md) |
| 10 | Generate SVG for documentation. | MEDIUM | [`plantuml-generate-svg-for-documentation.md`](plantuml-generate-svg-for-documentation.md) |
| 11 | Integrate with CI. | CRITICAL | [`plantuml-integrate-with-ci.md`](plantuml-integrate-with-ci.md) |
| 12 | Use the PlantUML server | MEDIUM | [`plantuml-use-the-plantuml-server.md`](plantuml-use-the-plantuml-server.md) |

---

---
title: "Generate SVG for documentation."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Generate SVG for documentation.

SVG scales better than PNG and is searchable. Use `-tsvg` in CI pipelines.

---

---
title: "Integrate with CI."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Integrate with CI.

Add PlantUML rendering to your CI pipeline so diagrams are always up-to-date. Docker-based rendering avoids Java dependency issues.

---

---
title: "Keep sequence diagrams focused."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Keep sequence diagrams focused.

If a sequence diagram has more than 7-8 participants or 20+ messages, split it into multiple diagrams with `ref` fragments.

---

---
title: "Leverage the preprocessor."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Leverage the preprocessor.

Use variables for colors, procedures for reusable shapes, and conditionals for environment-specific rendering.

---

---
title: "Organize with `!include`."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Organize with `!include`.

Split large models into separate `.puml` files per domain concept and compose them with includes.

---

---
title: "Use aliases for readability."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use aliases for readability.

`participant "API Server" as API` makes source readable while producing clean output.

---

---
title: "Use built-in themes"
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use built-in themes

Use built-in themes: for quick, professional styling. `!theme cerulean` or `!theme blueprint` are good defaults.

---

---
title: "Use C4-PlantUML for architecture diagrams."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use C4-PlantUML for architecture diagrams.

The C4-PlantUML library provides well-designed macros that produce clean, standardized C4 diagrams.

---

---
title: "Use `left to right direction`"
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use `left to right direction`

Use `left to right direction`: in use case and component diagrams to improve readability for systems with many elements.

---

---
title: "Use skinparam for consistent styling."
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use skinparam for consistent styling.

Define a shared style file and `!include` it in every diagram for visual consistency.

---

---
title: "Use `@startuml` / `@enduml` blocks."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use `@startuml` / `@enduml` blocks.

Every PlantUML diagram must be wrapped in these tags. The optional name after `@startuml` becomes the output filename.

---

---
title: "Use the PlantUML server"
impact: MEDIUM
impactDescription: "general best practice"
tags: plantuml, specs, diagramming, sequence-diagrams, class-diagrams, activity-diagrams
---

## Use the PlantUML server

Use the PlantUML server: for team environments. A shared server provides consistent rendering and can be used as a rendering service for documentation platforms.
