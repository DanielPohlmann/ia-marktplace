---
name: specs-diagramming-functional-diagrams
description: Use when drawing data flow diagrams, functional decomposition, IDEF0, or BPMN process models. USE FOR: DFD levels, decomposition trees, IDEF0 ICOM, BPMN pools/lanes/gateways, process and input-output analysis. DO NOT USE FOR: OO modeling (use specs-diagramming-uml), containers (use specs-diagramming-c4-diagrams), enterprise architecture (use specs-diagramming-archimate).
---

# Functional Diagrams

## Overview
Functional diagrams describe systems in terms of processes, data flows, and transformations rather than objects or containers. They answer the question "what does the system do with data?" and "how are functions decomposed into sub-functions?"

This skill covers four complementary functional diagramming techniques:
1. **Data Flow Diagrams (DFD)** — Show how data moves through a system
2. **Functional Decomposition** — Break high-level functions into sub-functions
3. **IDEF0** — Model decisions, actions, and activities with inputs, controls, outputs, and mechanisms
4. **BPMN** — Model business processes with standardized notation

## Choosing the Right Functional Diagram

| Diagram Type | Best For | Not Suitable For |
|-------------|----------|-----------------|
| **DFD** | Data transformation analysis, system boundaries, data store identification | Process timing, organizational roles |
| **Functional Decomposition** | Breaking complex systems into manageable pieces, scope definition | Data flow, process sequencing |
| **IDEF0** | Understanding function constraints and resources, manufacturing and engineering processes | Simple workflows, quick communication |
| **BPMN** | Business process documentation, workflow automation, cross-department handoffs | Data modeling, system architecture |

## Best Practices
- **Start at the context level.** Whether using DFD or IDEF0, begin with a single-process context diagram before decomposing. This establishes scope and boundaries.
- **Maintain level consistency.** All processes at the same decomposition level should be at the same granularity. Do not mix high-level and detailed processes on the same diagram.
- **Label every data flow.** Unlabeled arrows are the most common DFD error and make diagrams ambiguous.
- **Limit elements per diagram.** Follow the 3-7 process guideline per decomposition level. More than 7 processes on a single diagram reduces readability.
- **Use verb-noun naming for processes.** "Validate Order", "Calculate Tax", "Ship Package" — not "Order Validation" or "Tax Module."
- **Distinguish between data flow and control flow.** In DFDs, arrows represent data movement. In BPMN, arrows represent sequence flow. Do not mix paradigms on a single diagram.
- **Validate data conservation.** All data entering a process must either be output or stored. Data does not appear or disappear inside processes.
- **Use BPMN pools for organizational boundaries.** Each pool represents a distinct participant. Use lanes within pools for roles or departments.
- **Use Mermaid flowcharts as a practical approximation.** While Mermaid does not natively support DFD or IDEF0 notation, flowchart syntax captures the essential structure and is renderable in documentation platforms.
- **Cross-reference between diagram types.** When using both DFDs and BPMN, ensure process names and data labels are consistent across all diagrams. A process called "Validate Order" in the DFD should have the same name in the BPMN model.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/data-flow-diagrams-dfd.md](references/data-flow-diagrams-dfd.md) | Data Flow Diagrams (DFD) — DFD Elements, DFD Levels, DFD Rules, DFD in Mermaid Syntax |
| [references/functional-decomposition.md](references/functional-decomposition.md) | Functional Decomposition — Decomposition Tree Structure, Decomposition Guidelines, Functional Decomposition in Mermaid |
| [references/idef0-integration-definition-for-function-modeli.md](references/idef0-integration-definition-for-function-modeli.md) | IDEF0 (Integration Definition for Function Modeling) — ICOM Convention, IDEF0 Example: Process Customer Order, IDEF0 Decomposition, IDEF0 Rules, IDEF0 in Mermaid |
| [references/bpmn-business-process-model-and-notation.md](references/bpmn-business-process-model-and-notation.md) | BPMN (Business Process Model and Notation) — Core BPMN Elements, BPMN Example: Order Fulfillment Process, BPMN in Mermaid |
| [references/details.md](references/details.md) | Combining Functional Diagram Types |

## References

- [OMG Business Process Model and Notation (BPMN) Specification](https://www.omg.org/spec/BPMN/)
- [Data-Flow Diagram — Wikipedia](https://en.wikipedia.org/wiki/Data-flow_diagram)

See references/rules.md for the full rule catalog.
