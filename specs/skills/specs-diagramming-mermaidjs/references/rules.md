# Mermaid.js Rules

Best practices and rules for Mermaid.js.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use Mermaid for documentation-embedded diagrams. | MEDIUM | [`mermaidjs-use-mermaid-for-documentation-embedded-diagrams.md`](mermaidjs-use-mermaid-for-documentation-embedded-diagrams.md) |
| 2 | Keep diagrams small and focused. | MEDIUM | [`mermaidjs-keep-diagrams-small-and-focused.md`](mermaidjs-keep-diagrams-small-and-focused.md) |
| 3 | Choose the right diagram type. | MEDIUM | [`mermaidjs-choose-the-right-diagram-type.md`](mermaidjs-choose-the-right-diagram-type.md) |
| 4 | Use subgraphs in flowcharts | MEDIUM | [`mermaidjs-use-subgraphs-in-flowcharts.md`](mermaidjs-use-subgraphs-in-flowcharts.md) |
| 5 | Add labels to all links. | CRITICAL | [`mermaidjs-add-labels-to-all-links.md`](mermaidjs-add-labels-to-all-links.md) |
| 6 | Use `LR` (left-to-right) for process flows | MEDIUM | [`mermaidjs-use-lr-left-to-right-for-process-flows.md`](mermaidjs-use-lr-left-to-right-for-process-flows.md) |
| 7 | Use aliases for readability. | MEDIUM | [`mermaidjs-use-aliases-for-readability.md`](mermaidjs-use-aliases-for-readability.md) |
| 8 | Leverage alt/loop/par blocks | MEDIUM | [`mermaidjs-leverage-alt-loop-par-blocks.md`](mermaidjs-leverage-alt-loop-par-blocks.md) |
| 9 | Test locally before committing. | MEDIUM | [`mermaidjs-test-locally-before-committing.md`](mermaidjs-test-locally-before-committing.md) |
| 10 | Pin the Mermaid version | HIGH | [`mermaidjs-pin-the-mermaid-version.md`](mermaidjs-pin-the-mermaid-version.md) |
| 11 | Use themes consistently | MEDIUM | [`mermaidjs-use-themes-consistently.md`](mermaidjs-use-themes-consistently.md) |
| 12 | Escape special characters. | MEDIUM | [`mermaidjs-escape-special-characters.md`](mermaidjs-escape-special-characters.md) |

---

---
title: "Add labels to all links."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Add labels to all links.

Unlabeled arrows create ambiguity. Always describe what flows along a connection.

---

---
title: "Choose the right diagram type."
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Choose the right diagram type.

Use flowcharts for processes, sequence diagrams for interactions, class diagrams for structure, ER diagrams for data models.

---

---
title: "Escape special characters."
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Escape special characters.

Mermaid uses characters like `{}`, `()`, `[]`, `<>` for syntax. Wrap labels containing these in quotes.

---

---
title: "Keep diagrams small and focused."
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Keep diagrams small and focused.

If a diagram has more than 15-20 nodes, split it into multiple diagrams.

---

---
title: "Leverage alt/loop/par blocks"
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Leverage alt/loop/par blocks

Leverage alt/loop/par blocks: in sequence diagrams to show conditional logic, loops, and parallel processing.

---

---
title: "Pin the Mermaid version"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Pin the Mermaid version

Pin the Mermaid version: in documentation sites (Docusaurus, MkDocs) to avoid rendering changes from upstream updates.

---

---
title: "Test locally before committing."
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Test locally before committing.

Use the Mermaid Live Editor (https://mermaid.live) to preview and debug diagrams.

---

---
title: "Use aliases for readability."
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Use aliases for readability.

In sequence diagrams, `participant API as API Server` makes the diagram source easier to read while showing a clean label.

---

---
title: "Use `LR` (left-to-right) for process flows"
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Use `LR` (left-to-right) for process flows

Use `LR` (left-to-right) for process flows: and `TD` (top-down) for hierarchies.

---

---
title: "Use Mermaid for documentation-embedded diagrams."
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Use Mermaid for documentation-embedded diagrams.

Its native rendering on GitHub and GitLab makes it ideal for READMEs, PRs, ADRs, and wiki pages.

---

---
title: "Use subgraphs in flowcharts"
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Use subgraphs in flowcharts

Use subgraphs in flowcharts: to visually group related nodes (e.g., "Frontend", "Backend", "Database Layer").

---

---
title: "Use themes consistently"
impact: MEDIUM
impactDescription: "general best practice"
tags: mermaidjs, specs, diagramming, flowcharts, sequence-diagrams, class-diagrams
---

## Use themes consistently

Use themes consistently: across a project. Set a theme directive at the top of each diagram or configure it globally in your documentation framework.
