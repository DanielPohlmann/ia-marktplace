<!-- Part of the specs-documentation-rfc skill. Loaded on demand from SKILL.md. -->

# Complete RFC Template

```markdown
# RFC: [Title]

| Field          | Value                                      |
|----------------|--------------------------------------------|
| Author         | [Name]                                     |
| Status         | Draft / In Review / Accepted / Rejected    |
| Created        | YYYY-MM-DD                                 |
| Last Updated   | YYYY-MM-DD                                 |
| Review Deadline| YYYY-MM-DD                                 |
| Reviewers      | [Names]                                    |
| Decision Maker | [Name/Group]                               |
| ADRs Created   | [Links to ADRs, filled in after acceptance]|

## Summary

[1-3 sentences describing the proposal. A reader should understand
the core idea after reading only this section.]

## Motivation

## Problem Statement
[What problem exists today? What pain points are we experiencing?
Include data, metrics, or incidents that illustrate the problem.]

## Why Now?
[Why does this need to be addressed now rather than later?
What is the cost of inaction?]

## Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

## Non-Goals
- [Explicitly state what this RFC does NOT address]
- [Scope boundaries]

## Detailed Design

## Overview
[High-level description of the proposed approach.
Include architecture diagrams where helpful.]

## Component Design

### [Component 1]
[Detailed description of the component, its responsibilities,
interfaces, and behavior.]

### [Component 2]
[Detailed description.]

## API Changes
[New or modified API endpoints, request/response formats,
breaking changes.]

## Data Model Changes
[Schema changes, new tables, migration strategy.]

## Migration Strategy
[How do we get from the current state to the proposed state?
Big-bang vs incremental migration. Feature flags. Data migration.]

## Security Considerations
[Authentication, authorization, data protection implications.]

## Performance Implications
[Expected impact on latency, throughput, resource consumption.
Benchmarks if available.]

## Observability
[Logging, metrics, tracing, alerting changes needed.]

## Testing Strategy
[How will the change be tested? Unit, integration, e2e, load testing.]

## Alternatives Considered

## Alternative 1: [Name]
**Description:** [Brief description of the approach]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Why not chosen:** [Explanation]

## Alternative 2: [Name]
**Description:** [Brief description of the approach]

**Pros:**
- [Pro 1]

**Cons:**
- [Con 1]
- [Con 2]

**Why not chosen:** [Explanation]

## Alternative 3: Do Nothing
**Description:** Maintain the status quo.

**Pros:**
- No development cost or risk

**Cons:**
- [Existing problems persist]
- [Cost of inaction]

**Why not chosen:** [Explanation]

## Risks

| Risk                              | Likelihood | Impact | Mitigation                  |
|-----------------------------------|------------|--------|-----------------------------|
| [Risk 1]                         | High/Med/Low| High/Med/Low | [Mitigation strategy] |
| [Risk 2]                         | High/Med/Low| High/Med/Low | [Mitigation strategy] |
| [Risk 3]                         | High/Med/Low| High/Med/Low | [Mitigation strategy] |

## Open Questions

- [ ] [Question 1 -- what input do you need from reviewers?]
- [ ] [Question 2]
- [ ] [Question 3]

## Timeline

| Phase                  | Duration    | Description                          |
|------------------------|-------------|--------------------------------------|
| RFC Review             | X weeks     | Team review and feedback             |
| Prototype / Spike      | X weeks     | Validate assumptions                 |
| Phase 1: [Description] | X weeks    | [Deliverables]                       |
| Phase 2: [Description] | X weeks    | [Deliverables]                       |
| Migration / Rollout    | X weeks     | [Strategy]                           |
| Post-Launch Review     | X weeks     | Validate success metrics             |

## References

- [Link to related PRD]
- [Link to related TRD]
- [Link to related ADRs]
- [Link to relevant research, benchmarks, or prior art]
```
