---
name: specs-documentation-prd
description: Use when writing a Product Requirements Document that defines what to build and why. USE FOR: problem statement, goals/non-goals, user stories, success metrics, functional and non-functional requirements, milestones, MoSCoW, RICE. DO NOT USE FOR: implementation design (use specs-documentation-trd), business case (use specs-documentation-brd), executable criteria (use specs-documentation-gherkin).
---

# Product Requirements Document (PRD)

## Overview
A Product Requirements Document (PRD) defines *what* a product or feature should do and *why* it matters, without prescribing *how* to build it. It aligns product, engineering, design, and business stakeholders around a shared understanding of the problem, the proposed solution, success criteria, and scope boundaries.

The PRD sits between the BRD (business justification) and the TRD (technical design):
```
BRD ("Should we build this?") --> PRD ("What are we building?") --> TRD ("How do we build it?")
```

## Relationship to Other Documents

```
BRD (Business Requirements)
 |  Answers: "Should we build this? What is the business case?"
 |  Audience: Leadership, business stakeholders
 |
 v
PRD (Product Requirements)  <-- YOU ARE HERE
 |  Answers: "What are we building? For whom? What does success look like?"
 |  Audience: Product, engineering, design
 |
 +---> ADR (Architecture Decision Records)
 |     Records: "Why did we choose X over Y?"
 |
 v
TRD (Technical Requirements)
 |  Answers: "How do we build it? What are the technical constraints?"
 |  Audience: Engineering
 |
 v
Gherkin / Gauge (Executable Specs)
    Answers: "How do we verify it works?"
    Audience: QA, engineering, product
```

## Best Practices

- **Start with the problem, not the solution** -- clearly articulate the user pain point before proposing any feature.
- **Be specific about non-goals** -- explicitly stating what you will *not* build prevents scope creep and misaligned expectations.
- **Make success metrics measurable** -- "improve user experience" is not a metric. "Reduce checkout abandonment rate from 68% to 45%" is.
- **Write user stories from the user's perspective** -- avoid implementation language like "the system shall" in favor of "as a user, I want."
- **Include acceptance criteria for every user story** -- without testable criteria, it is impossible to know when a story is done.
- **Prioritize ruthlessly** -- use MoSCoW or RICE to force trade-off decisions early. Not everything can be "Must Have."
- **Keep the PRD living** -- update the document as requirements evolve. A stale PRD is worse than no PRD because it actively misleads.
- **Separate functional from non-functional requirements** -- performance, security, and scalability constraints deserve explicit attention.
- **Link to related documents** -- reference the BRD for business context, ADRs for architectural decisions, and the TRD for technical design.
- **Resolve open questions before development starts** -- open questions that linger into implementation cause rework and delays.
- **Review with all stakeholders** -- engineering, design, QA, and product should all review and approve the PRD before implementation begins.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/complete-prd-template.md](references/complete-prd-template.md) | Complete PRD Template — Persona: [Persona Name], Persona: [Persona Name], FR-1: [Requirement Name], FR-2: [Requirement Name], NFR-1: Performance, NFR-2: Security, … |
| [references/writing-good-user-stories.md](references/writing-good-user-stories.md) | Writing Good User Stories — The Standard Format, INVEST Criteria for User Stories, Good vs Poor User Stories, Acceptance Criteria Formats |
| [references/prioritization-frameworks.md](references/prioritization-frameworks.md) | Prioritization Frameworks — MoSCoW Method, Must Have, Should Have, Could Have, Won't Have (this release), RICE Scoring |
| [references/details.md](references/details.md) | Standard PRD Structure |

## References

- [Product Requirements Document — Wikipedia](https://en.wikipedia.org/wiki/Product_requirements_document)

See references/rules.md for the full rule catalog.
