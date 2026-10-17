---
name: specs-documentation-brd
description: Use when writing a Business Requirements Document to justify a project. USE FOR: business case, objectives, stakeholders, current state, business rules, cost-benefit and ROI, success criteria, risks. DO NOT USE FOR: technical design (use specs-documentation-trd), product features (use specs-documentation-prd), decisions (use specs-documentation-adr).
---

# Business Requirements Document (BRD)

## Overview
A Business Requirements Document (BRD) answers the fundamental question: *"Should we build this, and why?"* It captures the business rationale, objectives, stakeholders, costs, benefits, and success criteria for a proposed initiative. The BRD is typically the first formal document in the requirements lifecycle, written before the PRD and TRD.

The BRD speaks to leadership and business stakeholders in business language, not technical jargon:
```
BRD ("Should we build this?") --> PRD ("What are we building?") --> TRD ("How do we build it?")
```

## Relationship to PRD

```
BRD (Business Requirements)  <-- YOU ARE HERE
 |  Answers: "Should we build this?"
 |  Contains: Business case, ROI, stakeholders, costs, success criteria
 |  Audience: Leadership, finance, business stakeholders
 |
 v
PRD (Product Requirements)
 |  Answers: "What are we building?"
 |  Contains: Features, user stories, acceptance criteria, milestones
 |  Audience: Product, engineering, design
 |
 v
TRD (Technical Requirements)
    Answers: "How do we build it?"
    Contains: Architecture, APIs, data models, deployment
    Audience: Engineering
```

### BRD vs PRD

| Aspect | BRD | PRD |
|--------|-----|-----|
| **Primary question** | Should we build this? | What are we building? |
| **Audience** | Business leadership, finance | Product, engineering, design |
| **Language** | Business language, financials | Product language, user stories |
| **Contains** | ROI, cost-benefit, business rules | Features, UX, acceptance criteria |
| **Approved by** | Business sponsors, finance | Product and engineering leads |
| **When written** | Before PRD (project justification) | After BRD approval (feature definition) |
| **Level of detail** | High-level solution description | Detailed feature requirements |

## Best Practices

- **Lead with the executive summary** -- many decision-makers will only read this section. Make it compelling, concise, and self-contained.
- **Quantify everything possible** -- "improve efficiency" is vague; "reduce average ticket resolution time from 4 hours to 15 minutes" is actionable.
- **Always include a "Do Nothing" alternative** -- explicitly documenting the cost of inaction strengthens the case for investment.
- **Separate business requirements from product requirements** -- the BRD should not contain UI mockups, user stories, or technical specifications. Those belong in the PRD and TRD.
- **Identify all stakeholders early** -- missed stakeholders cause late-stage scope changes and delays. Use a RACI matrix to clarify roles.
- **Be honest about risks** -- underplaying risks erodes trust. Present risks with realistic assessments and credible mitigation plans.
- **Validate assumptions explicitly** -- every cost-benefit calculation rests on assumptions. Document them so they can be challenged and verified.
- **Use a consistent format** -- a standardized BRD template ensures nothing is overlooked and makes documents comparable across initiatives.
- **Get formal sign-off** -- the BRD is a commitment. Require signatures from the business sponsor, finance, and IT leadership before proceeding to PRD.
- **Keep it business-focused** -- resist the temptation to include technical details. If someone asks "how will it work?", point them to the TRD.
- **Review with finance** -- the cost-benefit analysis should be validated by someone with financial expertise, not just the project team.
- **Plan for post-launch measurement** -- define how and when success criteria will be measured. A BRD without a measurement plan is a wish list.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/complete-brd-template.md](references/complete-brd-template.md) | Complete BRD Template — Alignment with Strategic Goals, Stakeholder Matrix, RACI Matrix, Current Process, Pain Points, Current Costs, … |
| [references/details.md](references/details.md) | Standard BRD Structure; BRD Example: Customer Self-Service Portal |

## References

- [Business Requirements — Wikipedia](https://en.wikipedia.org/wiki/Business_requirements)

See references/rules.md for the full rule catalog.
