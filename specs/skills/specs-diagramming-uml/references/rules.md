# UML Rules

Best practices and rules for UML.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Choose the right diagram for the audience. | MEDIUM | [`uml-choose-the-right-diagram-for-the-audience.md`](uml-choose-the-right-diagram-for-the-audience.md) |
| 2 | Do not model everything. | CRITICAL | [`uml-do-not-model-everything.md`](uml-do-not-model-everything.md) |
| 3 | Keep diagrams focused. | MEDIUM | [`uml-keep-diagrams-focused.md`](uml-keep-diagrams-focused.md) |
| 4 | Use consistent naming. | MEDIUM | [`uml-use-consistent-naming.md`](uml-use-consistent-naming.md) |
| 5 | Show multiplicity on all associations. | MEDIUM | [`uml-show-multiplicity-on-all-associations.md`](uml-show-multiplicity-on-all-associations.md) |
| 6 | Distinguish aggregation from composition. | MEDIUM | [`uml-distinguish-aggregation-from-composition.md`](uml-distinguish-aggregation-from-composition.md) |
| 7 | Use stereotypes sparingly. | CRITICAL | [`uml-use-stereotypes-sparingly.md`](uml-use-stereotypes-sparingly.md) |
| 8 | Combine structural and behavioral diagrams. | MEDIUM | [`uml-combine-structural-and-behavioral-diagrams.md`](uml-combine-structural-and-behavioral-diagrams.md) |
| 9 | Use packages to manage complexity. | MEDIUM | [`uml-use-packages-to-manage-complexity.md`](uml-use-packages-to-manage-complexity.md) |
| 10 | Validate against code. | HIGH | [`uml-validate-against-code.md`](uml-validate-against-code.md) |
| 11 | Prefer text-based tools. | LOW | [`uml-prefer-text-based-tools.md`](uml-prefer-text-based-tools.md) |

---

---
title: "Choose the right diagram for the audience."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Choose the right diagram for the audience.

Use case diagrams for stakeholders, class diagrams for developers, deployment diagrams for operations.

---

---
title: "Combine structural and behavioral diagrams."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Combine structural and behavioral diagrams.

A class diagram shows what exists; a sequence diagram shows how it behaves. Together they tell the full story.

---

---
title: "Distinguish aggregation from composition."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Distinguish aggregation from composition.

Use composition (filled diamond) when the part cannot exist without the whole; use aggregation (open diamond) when it can.

---

---
title: "Do not model everything."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Do not model everything.

UML is a communication tool, not a code generation specification. Model only what adds clarity.

---

---
title: "Keep diagrams focused."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Keep diagrams focused.

One diagram, one concern. A class diagram should not try to show every class in the system.

---

---
title: "Prefer text-based tools."
impact: LOW
impactDescription: "recommended but situational"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Prefer text-based tools.

Use Mermaid, PlantUML, or D2 to write UML diagrams as code so they can be version-controlled and reviewed in pull requests.

---

---
title: "Show multiplicity on all associations."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Show multiplicity on all associations.

Omitted multiplicity is ambiguous and forces readers to guess.

---

---
title: "Use consistent naming."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Use consistent naming.

Class names in PascalCase, operations in camelCase, constants in UPPER_CASE.

---

---
title: "Use packages to manage complexity."
impact: MEDIUM
impactDescription: "general best practice"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Use packages to manage complexity.

For systems with many classes, organize them into packages first, then detail individual packages.

---

---
title: "Use stereotypes sparingly."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Use stereotypes sparingly.

Only add stereotypes that convey meaning your audience needs. Do not decorate every element.

---

---
title: "Validate against code."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: uml, specs, diagramming, class-diagrams, sequence-diagrams, activity-diagrams
---

## Validate against code.

If your UML diverges from the actual code, the diagrams become misleading. Keep them synchronized or clearly label them as aspirational.
