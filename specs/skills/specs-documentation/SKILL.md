---
name: specs-documentation
description: Use only when choosing which specification document type fits. USE FOR: PRD vs TRD vs BRD vs ADR vs RFC, documentation strategy, combining written and executable specs. DO NOT USE FOR: writing a specific document (use the matching specs-documentation-* skill, e.g. specs-documentation-prd, specs-documentation-adr), diagrams (use specs-diagramming).
---

# Documentation & Requirements

## Overview
Software specifications capture the "what" and "why" before implementation addresses the "how." Well-structured requirements documents, architecture decisions, and executable specs reduce ambiguity, align stakeholders, and create verifiable acceptance criteria.

## Document Types

### Requirements Documents
| Type | Audience | Focus |
|------|----------|-------|
| **PRD** (Product Requirements) | Product + Engineering | Features, user stories, success metrics |
| **TRD** (Technical Requirements) | Engineering | Architecture, APIs, data models, constraints |
| **BRD** (Business Requirements) | Business + Leadership | ROI, market need, business objectives |

### Architecture Documents
| Type | Audience | Focus |
|------|----------|-------|
| **ADR** (Architecture Decision Record) | Engineering | Single decision with context and consequences |
| **RFC** (Request for Comments) | Engineering + Stakeholders | Proposed change seeking feedback |

### Executable Specifications
| Type | Audience | Focus |
|------|----------|-------|
| **Gherkin** (Given/When/Then) | QA + Product + Engineering | Acceptance criteria as executable tests |
| **Gauge** (Markdown specs) | QA + Engineering | Free-form test specifications in Markdown |

## Document Flow

```
Business Need
    │
    ▼
  BRD ──► "Should we build this?"
    │
    ▼
  PRD ──► "What are we building?"
    │
    ├──► ADR ──► "Why did we choose X over Y?"
    │
    ▼
  TRD ──► "How do we build it?"
    │
    ├──► RFC ──► "Proposing approach Z for feedback"
    │
    ▼
  Gherkin / Gauge ──► "How do we verify it works?"
    │
    ▼
  Implementation + Automated Tests
```

## Best Practices
- Write the PRD before the TRD — define what you're building before deciding how to build it.
- Use ADRs for every significant architecture decision — they're short, structured, and invaluable for future developers.
- Make specifications executable where possible — Gherkin and Gauge connect written specs directly to automated tests.
- Keep documents close to the code in the same repository so they evolve together.
- Use lightweight templates rather than heavyweight processes — a short, focused ADR beats a 50-page design doc nobody reads.
- Review specs before implementation, not after — specifications are cheapest to change when they're still text.

## References

- [Architectural Decision Records](https://adr.github.io/)
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)

See references/rules.md for the full rule catalog.
