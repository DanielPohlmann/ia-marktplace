# ArchiMate Rules

Best practices and rules for ArchiMate.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use the correct layer. | CRITICAL | [`archimate-use-the-correct-layer.md`](archimate-use-the-correct-layer.md) |
| 2 | Keep viewpoints focused. | HIGH | [`archimate-keep-viewpoints-focused.md`](archimate-keep-viewpoints-focused.md) |
| 3 | Use relationships precisely. | CRITICAL | [`archimate-use-relationships-precisely.md`](archimate-use-relationships-precisely.md) |
| 4 | Color-code by layer. | MEDIUM | [`archimate-color-code-by-layer.md`](archimate-color-code-by-layer.md) |
| 5 | Start with the Layered Viewpoint. | MEDIUM | [`archimate-start-with-the-layered-viewpoint.md`](archimate-start-with-the-layered-viewpoint.md) |
| 6 | Model motivation first. | HIGH | [`archimate-model-motivation-first.md`](archimate-model-motivation-first.md) |
| 7 | Pair with TOGAF. | MEDIUM | [`archimate-pair-with-togaf.md`](archimate-pair-with-togaf.md) |
| 8 | Limit elements per diagram to 15-20. | LOW | [`archimate-limit-elements-per-diagram-to-15-20.md`](archimate-limit-elements-per-diagram-to-15-20.md) |
| 9 | Name elements with precision. | MEDIUM | [`archimate-name-elements-with-precision.md`](archimate-name-elements-with-precision.md) |
| 10 | Version your models. | MEDIUM | [`archimate-version-your-models.md`](archimate-version-your-models.md) |

---

---
title: "Color-code by layer."
impact: MEDIUM
impactDescription: "general best practice"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Color-code by layer.

Follow the standard color convention: yellow for Business, blue for Application, green for Technology. This provides instant visual orientation.

---

---
title: "Keep viewpoints focused."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Keep viewpoints focused.

Each diagram should use a single viewpoint. A Layered Viewpoint can show cross-layer dependencies, but avoid cramming all elements into one diagram.

---

---
title: "Limit elements per diagram to 15-20."
impact: LOW
impactDescription: "recommended but situational"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Limit elements per diagram to 15-20.

Overcrowded diagrams lose communicative value. Split into multiple viewpoints if needed.

---

---
title: "Model motivation first."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Model motivation first.

Before modeling structure, capture stakeholder goals, drivers, and requirements. This ensures architecture decisions are traceable to business rationale.

---

---
title: "Name elements with precision."
impact: MEDIUM
impactDescription: "general best practice"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Name elements with precision.

Use clear, specific names (e.g., "Order Management Service" not "Service 1"). Element names should be self-explanatory.

---

---
title: "Pair with TOGAF."
impact: MEDIUM
impactDescription: "general best practice"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Pair with TOGAF.

ArchiMate provides the notation; TOGAF provides the process. Use ArchiMate diagrams as deliverables within TOGAF ADM phases.

---

---
title: "Start with the Layered Viewpoint."
impact: MEDIUM
impactDescription: "general best practice"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Start with the Layered Viewpoint.

When introducing an architecture to stakeholders, the Layered Viewpoint provides the best overview of how business is supported by applications and technology.

---

---
title: "Use relationships precisely."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Use relationships precisely.

ArchiMate relationships have specific semantics. Do not use "serving" when you mean "realization" — they convey different architectural meaning.

---

---
title: "Use the correct layer."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Use the correct layer.

Do not model application concerns in the Business Layer or vice versa. Cross-layer connections should use serving or realization relationships.

---

---
title: "Version your models."
impact: MEDIUM
impactDescription: "general best practice"
tags: archimate, specs, diagramming, enterprise-architecture-modeling, layered-architecture-visualization, business-application-technology-mapping
---

## Version your models.

Like code, ArchiMate models should be version-controlled. Use tool exports (e.g., Archi Open Exchange format) stored alongside source code.
