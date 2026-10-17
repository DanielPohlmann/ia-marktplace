---
name: specs-documentation-rfc
description: Use when proposing a significant technical change for team review. USE FOR: RFC structure, motivation, detailed design, alternatives, risks, review workflow, lightweight vs heavyweight RFCs, RFC vs ADR. DO NOT USE FOR: recording a final decision (use specs-documentation-adr), product requirements (use specs-documentation-prd), business case (use specs-documentation-brd).
---

# RFC (Request for Comments) / Design Documents

## Overview
An RFC (Request for Comments) is a design document that proposes a significant technical change and solicits structured feedback from the team before a decision is made. Unlike an ADR, which records a decision already taken, an RFC is a *proposal* -- it invites discussion, critique, and refinement.

RFCs are the primary mechanism for making large-scale technical decisions collaboratively. They ensure that significant changes are well-thought-out, that alternatives are considered, and that the team has an opportunity to surface concerns before implementation begins.

## When to Write an RFC

Write an RFC when:
- A change affects multiple teams, services, or systems
- The implementation will take more than a few days of effort
- There are multiple viable approaches and the trade-offs are not obvious
- The change introduces new infrastructure, frameworks, or patterns
- You need buy-in from stakeholders outside your immediate team
- The decision is hard to reverse once implemented

Do NOT write an RFC for:
- Small, easily reversible changes
- Bug fixes or minor improvements
- Changes that are already decided by organizational policy
- Decisions that a single engineer can make independently

## Standard RFC Structure

### 1. Metadata
Title, author, status, reviewers, and dates.

### 2. Summary
A concise (1-3 sentence) description of the proposal.

### 3. Motivation
Why is this change needed? What problem does it solve?

### 4. Detailed Design
The core of the RFC -- how the proposed change works.

### 5. Alternatives Considered
Other approaches that were evaluated and why they were not chosen.

### 6. Risks
What could go wrong? What are the unknowns?

### 7. Open Questions
Unresolved issues that need team input.

### 8. Timeline
Estimated implementation schedule.

## Lightweight vs Heavyweight RFC

### Lightweight RFC
For smaller, team-scoped decisions. Shorter template, faster review cycle.

```markdown
# RFC: [Title]
**Author:** [Name] | **Status:** Draft | **Date:** YYYY-MM-DD

## Problem
[2-3 sentences]

## Proposal
[Description of the proposed approach]

## Alternatives
- [Alternative 1]: [Why not]
- [Alternative 2]: [Why not]

## Risks
- [Risk 1]

## Questions
- [Question 1]
```

Best for:
- Single-team decisions
- Technology choices within a service
- Process changes
- Convention adoption

### Heavyweight RFC
For cross-team, high-impact decisions. Full template with detailed design.

Best for:
- Architecture changes affecting multiple services
- New infrastructure or platform decisions
- Breaking changes to public APIs
- Security model changes
- Major technology migrations

### Choosing the Right Weight

| Signal | Lightweight | Heavyweight |
|--------|-------------|-------------|
| Teams affected | 1 | 2+ |
| Reversibility | Days to reverse | Weeks/months to reverse |
| Implementation effort | < 2 weeks | > 2 weeks |
| Risk level | Low-medium | Medium-high |
| Stakeholders | Engineering only | Engineering + product + leadership |

## RFC vs ADR

| Aspect | RFC | ADR |
|--------|-----|-----|
| **Purpose** | Propose a change for discussion | Record a decision that was made |
| **Timing** | Before the decision | At or after the decision |
| **Audience** | Reviewers who will provide feedback | Future developers who need context |
| **Tone** | Proposing ("We could...") | Deciding ("We will...") |
| **Length** | 3-10 pages (detailed design) | 1-2 pages (concise record) |
| **Lifecycle** | Draft -> Review -> Accepted/Rejected | Proposed -> Accepted -> Deprecated/Superseded |
| **Output** | One or more ADRs | The final record |

### Common Workflow
```
RFC (proposal + discussion)
  |
  v
Decision made by team/decision-maker
  |
  v
ADR(s) created to record the decision(s)
  |
  v
Implementation begins
```

An RFC may produce multiple ADRs. For example, an RFC proposing a migration to microservices might result in:
- ADR-0010: Adopt microservices architecture
- ADR-0011: Use Kubernetes for container orchestration
- ADR-0012: Use RabbitMQ for inter-service messaging

## Best Practices

- **Start with the problem, not the solution** -- the Motivation section should clearly explain why the change is needed. If the problem is not compelling, the solution does not matter.
- **Always include "Do Nothing" as an alternative** -- explicitly documenting the cost of inaction gives reviewers a baseline for comparison.
- **Be specific about trade-offs** -- every design decision has trade-offs. Acknowledging them builds trust and invites constructive feedback.
- **Set a review deadline** -- without a deadline, RFCs linger indefinitely. A clear deadline (e.g., 5-10 business days) ensures timely decisions.
- **Designate a decision-maker** -- someone (tech lead, architecture council) must have the authority to make the final call. Consensus is ideal but not always achievable.
- **Address all review comments** -- even if you disagree, explain your reasoning. Unaddressed comments signal that feedback is not valued.
- **Convert accepted RFCs into ADRs** -- the RFC captures the discussion; the ADR captures the decision. Do not skip the ADR step.
- **Keep RFCs scoped** -- an RFC that tries to solve everything at once is harder to review and more likely to be rejected. Break large proposals into focused RFCs.
- **Include a migration strategy** -- proposals that address how to get from here to there are far more likely to be accepted than those that only describe the end state.
- **Use diagrams liberally** -- architecture diagrams, sequence diagrams, and data flow diagrams make proposals easier to understand and review.
- **Write for a skeptical reader** -- assume the reviewer's first reaction is "why should we change what works?" and address that concern proactively.
- **Prototype when possible** -- a working spike alongside the RFC dramatically increases confidence in the proposal.

See references/rules.md for the full rule catalog.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/complete-rfc-template.md](references/complete-rfc-template.md) | Complete RFC Template — Problem Statement, Why Now?, Goals, Non-Goals, Overview, Component Design, … |
| [references/rfc-example-migrate-from-rest-to-graphql.md](references/rfc-example-migrate-from-rest-to-graphql.md) | RFC Example: Migrate from REST to GraphQL — Problem Statement, Why Now?, Goals, Non-Goals, Overview, Schema Design, … |
| [references/details.md](references/details.md) | RFC Workflow; Managing RFCs |
