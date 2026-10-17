---
name: specs-diagramming-togaf
description: Use when applying TOGAF to enterprise architecture work. USE FOR: ADM phases and deliverables, architecture repository, enterprise continuum, content metamodel, governance, capability planning. DO NOT USE FOR: element notation (use specs-diagramming-archimate), container diagrams (use specs-diagramming-c4-diagrams), general diagrams (use specs-diagramming-mermaidjs).
---

# TOGAF - The Open Group Architecture Framework

## Overview
TOGAF is an enterprise architecture framework that provides a structured approach for designing, planning, implementing, and governing enterprise information technology architecture. It is maintained by The Open Group and is the most widely adopted enterprise architecture framework globally.

TOGAF's core is the **Architecture Development Method (ADM)** — an iterative cycle of phases that transforms business requirements into architecture deliverables.

## Best Practices
- **Iterate, don't waterfall.** The ADM is explicitly iterative. Complete a lightweight pass through all phases before deep-diving into any single phase.
- **Tailor the ADM.** TOGAF is a framework, not a methodology. Adapt the depth and formality of each phase to your organization's maturity and project scope.
- **Maintain the Architecture Repository.** Treat architecture outputs as living assets. Keep the repository current with baseline and target descriptions.
- **Use the Enterprise Continuum.** Classify reusable architecture assets along the continuum so teams can find and leverage existing patterns before inventing new ones.
- **Align with ArchiMate for notation.** TOGAF defines what to produce; ArchiMate defines how to model it visually. Use ArchiMate as the modeling language for TOGAF deliverables.
- **Engage stakeholders early.** Phase A exists specifically to secure buy-in. Do not skip stakeholder identification and concern mapping.
- **Define Architecture Principles before modeling.** Principles in the Preliminary Phase guide all subsequent architecture decisions and serve as tie-breakers.
- **Trace requirements continuously.** Requirements Management is not a phase you pass through once — it runs throughout every ADM cycle.
- **Use gap analysis rigorously.** In Phases B, C, and D, the gap between baseline and target drives the roadmap in Phase E. Incomplete gap analysis leads to incomplete migration plans.
- **Govern the implementation.** Phase G ensures that the actual implementation conforms to the architecture. Without governance, architectures become shelfware.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/architecture-development-method-adm.md](references/architecture-development-method-adm.md) | Architecture Development Method (ADM) — Preliminary Phase, Phase A: Architecture Vision, Phase B: Business Architecture, Phase C: Information Systems Architecture, Phase D: Technology Architecture, Phase E: Opportunities and Solutions, … |
| [references/togaf-content-metamodel.md](references/togaf-content-metamodel.md) | TOGAF Content Metamodel — Core Content Metamodel Entities, Key Metamodel Relationships, Extensions to the Core Metamodel |
| [references/details.md](references/details.md) | Architecture Repository; Enterprise Continuum; Key Deliverables Summary |

## References

- [TOGAF — The Open Group](https://www.opengroup.org/togaf)
- [TOGAF Standard — Digital Edition](https://pubs.opengroup.org/togaf-standard/)

See references/rules.md for the full rule catalog.
