# Functional Diagrams Rules

Best practices and rules for Functional Diagrams.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start at the context level. | MEDIUM | [`functional-diagrams-start-at-the-context-level.md`](functional-diagrams-start-at-the-context-level.md) |
| 2 | Maintain level consistency. | CRITICAL | [`functional-diagrams-maintain-level-consistency.md`](functional-diagrams-maintain-level-consistency.md) |
| 3 | Label every data flow. | MEDIUM | [`functional-diagrams-label-every-data-flow.md`](functional-diagrams-label-every-data-flow.md) |
| 4 | Limit elements per diagram. | MEDIUM | [`functional-diagrams-limit-elements-per-diagram.md`](functional-diagrams-limit-elements-per-diagram.md) |
| 5 | Use verb-noun naming for processes. | HIGH | [`functional-diagrams-use-verb-noun-naming-for-processes.md`](functional-diagrams-use-verb-noun-naming-for-processes.md) |
| 6 | Distinguish between data flow and control flow. | CRITICAL | [`functional-diagrams-distinguish-between-data-flow-and-control-flow.md`](functional-diagrams-distinguish-between-data-flow-and-control-flow.md) |
| 7 | Validate data conservation. | CRITICAL | [`functional-diagrams-validate-data-conservation.md`](functional-diagrams-validate-data-conservation.md) |
| 8 | Use BPMN pools for organizational boundaries. | MEDIUM | [`functional-diagrams-use-bpmn-pools-for-organizational-boundaries.md`](functional-diagrams-use-bpmn-pools-for-organizational-boundaries.md) |
| 9 | Use Mermaid flowcharts as a practical approximation. | MEDIUM | [`functional-diagrams-use-mermaid-flowcharts-as-a-practical-approximation.md`](functional-diagrams-use-mermaid-flowcharts-as-a-practical-approximation.md) |
| 10 | Cross-reference between diagram types. | HIGH | [`functional-diagrams-cross-reference-between-diagram-types.md`](functional-diagrams-cross-reference-between-diagram-types.md) |

---

---
title: "Cross-reference between diagram types."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Cross-reference between diagram types.

When using both DFDs and BPMN, ensure process names and data labels are consistent across all diagrams. A process called "Validate Order" in the DFD should have the same name in the BPMN model.

---

---
title: "Distinguish between data flow and control flow."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Distinguish between data flow and control flow.

In DFDs, arrows represent data movement. In BPMN, arrows represent sequence flow. Do not mix paradigms on a single diagram.

---

---
title: "Label every data flow."
impact: MEDIUM
impactDescription: "general best practice"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Label every data flow.

Unlabeled arrows are the most common DFD error and make diagrams ambiguous.

---

---
title: "Limit elements per diagram."
impact: MEDIUM
impactDescription: "general best practice"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Limit elements per diagram.

Follow the 3-7 process guideline per decomposition level. More than 7 processes on a single diagram reduces readability.

---

---
title: "Maintain level consistency."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Maintain level consistency.

All processes at the same decomposition level should be at the same granularity. Do not mix high-level and detailed processes on the same diagram.

---

---
title: "Start at the context level."
impact: MEDIUM
impactDescription: "general best practice"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Start at the context level.

Whether using DFD or IDEF0, begin with a single-process context diagram before decomposing. This establishes scope and boundaries.

---

---
title: "Use BPMN pools for organizational boundaries."
impact: MEDIUM
impactDescription: "general best practice"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Use BPMN pools for organizational boundaries.

Each pool represents a distinct participant. Use lanes within pools for roles or departments.

---

---
title: "Use Mermaid flowcharts as a practical approximation."
impact: MEDIUM
impactDescription: "general best practice"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Use Mermaid flowcharts as a practical approximation.

While Mermaid does not natively support DFD or IDEF0 notation, flowchart syntax captures the essential structure and is renderable in documentation platforms.

---

---
title: "Use verb-noun naming for processes."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Use verb-noun naming for processes.

"Validate Order", "Calculate Tax", "Ship Package" — not "Order Validation" or "Tax Module."

---

---
title: "Validate data conservation."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: functional-diagrams, specs, diagramming, data-flow-diagrams-dfd, functional-decomposition, idef0-modeling
---

## Validate data conservation.

All data entering a process must either be output or stored. Data does not appear or disappear inside processes.
