---
idea: <slug>
stage: architecture
status: draft
approved_on:
inputs: [01-ideation.md, 02-design.md]
---

# <Idea name> — Technical design

## Summary
<3–5 sentences: what changes and why.>

## Event Storming
- File: <path>
- Hotspots:

## Context map
| Bounded context | New / existing | Aggregates | Owns data |
|---|---|---|---|

```mermaid
flowchart LR
```

## Commands and domain events
| Command | Aggregate | Domain event(s) | Rejected when |
|---|---|---|---|

## Integration events
| Event | Producer | Consumers | Payload fields | Delivery guarantee |
|---|---|---|---|---|

## HTTP API
| Method | Route | Request | Response | Errors |
|---|---|---|---|---|

## Data model
| Table / collection | Owner aggregate | Key fields | Indexes |
|---|---|---|---|

## Patterns
| Force (concrete problem) | Pattern | Simpler alternative rejected, and why | Existing precedent in the code |
|---|---|---|---|

## Diagrams
### C4 — Context
```mermaid
C4Context
```
### C4 — Container
```mermaid
C4Container
```
### Main flow
```mermaid
sequenceDiagram
```

## Decisions (ADRs)
### ADR-1: <title>
- Context:
- Options:
- Decision:
- Consequences:

## Threat model (STRIDE)
| Threat | Flow / data | Mitigation |
|---|---|---|

## Testing strategy
| Level | What | Where |
|---|---|---|

## Critique findings
| Finding | Severity | Resolution |
|---|---|---|

## Open questions

## Change log
| Date | Change |
|---|---|
