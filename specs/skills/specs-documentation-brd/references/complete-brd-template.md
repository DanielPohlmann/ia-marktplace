<!-- Part of the specs-documentation-brd skill. Loaded on demand from SKILL.md. -->

# Complete BRD Template

```markdown
# BRD: [Initiative Name]

| Field            | Value                          |
|------------------|--------------------------------|
| Author           | [Name]                         |
| Status           | Draft / In Review / Approved   |
| Created          | YYYY-MM-DD                     |
| Last Updated     | YYYY-MM-DD                     |
| Business Sponsor | [Name, Title]                  |
| Department       | [Department]                   |
| Reviewers        | [Names]                        |
| Approvers        | [Names]                        |

## 1. Executive Summary

[1-2 paragraphs summarizing the business need, proposed solution at a high
level, expected benefits, estimated investment, and timeline. This section
should be self-contained for executive readers who may not read further.]

## 2. Business Objectives

| ID    | Objective                              | Measurable Target           |
|-------|----------------------------------------|-----------------------------|
| BO-1  | [Objective 1]                         | [Quantified target]         |
| BO-2  | [Objective 2]                         | [Quantified target]         |
| BO-3  | [Objective 3]                         | [Quantified target]         |

## Alignment with Strategic Goals
[How this initiative aligns with the organization's strategic plan,
OKRs, or annual priorities.]

## 3. Stakeholders

## Stakeholder Matrix

| Stakeholder       | Role           | Interest Level | Influence | Involvement          |
|-------------------|----------------|----------------|-----------|----------------------|
| [Name/Group]      | Business Sponsor| High          | High      | Approval authority   |
| [Name/Group]      | End User       | High           | Medium    | Requirements input   |
| [Name/Group]      | IT Operations  | Medium         | Medium    | Technical feasibility|
| [Name/Group]      | Finance        | Medium         | High      | Budget approval      |
| [Name/Group]      | Legal/Compliance| Low           | High      | Regulatory sign-off  |

## RACI Matrix

| Activity               | Sponsor | Product | Engineering | QA   | Legal |
|------------------------|---------|---------|-------------|------|-------|
| Requirements approval  | A       | R       | C           | I    | C     |
| Budget approval        | A       | I       | I           | I    | I     |
| Technical design       | I       | C       | R           | C    | I     |
| User acceptance testing| I       | A       | C           | R    | I     |
| Go-live decision       | A       | R       | C           | C    | C     |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

## 4. Current State Analysis

## Current Process
[Describe the existing process, workflow, or system. Include a
process flow diagram if helpful.]

## Pain Points

| # | Pain Point                           | Impact                        | Affected Users |
|---|--------------------------------------|-------------------------------|----------------|
| 1 | [Pain point 1]                      | [Business impact]             | [Count/group]  |
| 2 | [Pain point 2]                      | [Business impact]             | [Count/group]  |
| 3 | [Pain point 3]                      | [Business impact]             | [Count/group]  |

## Current Costs
[Annual cost of the current process/system including labor, licensing,
maintenance, opportunity cost, and cost of errors or inefficiency.]

## 5. Proposed Solution

## Solution Overview
[High-level description of the proposed solution. Focus on capabilities
and business value, not technical implementation.]

## In Scope
- [Capability 1]
- [Capability 2]
- [Capability 3]

## Out of Scope
- [Excluded item 1 -- rationale]
- [Excluded item 2 -- rationale]

## Alternatives Considered

| Alternative          | Pros                    | Cons                      | Why Not Selected          |
|----------------------|-------------------------|---------------------------|---------------------------|
| Do Nothing           | No cost                 | Pain points persist       | Unacceptable status quo   |
| [Alternative 1]     | [Pros]                  | [Cons]                    | [Reason]                  |
| [Alternative 2]     | [Pros]                  | [Cons]                    | [Reason]                  |
| **Recommended**      | [Pros]                  | [Cons]                    | **Best fit for objectives**|

## 6. Business Rules

| ID    | Rule                                                  | Source              |
|-------|-------------------------------------------------------|---------------------|
| BR-1  | [Business rule 1]                                    | [Policy/regulation] |
| BR-2  | [Business rule 2]                                    | [Policy/regulation] |
| BR-3  | [Business rule 3]                                    | [Policy/regulation] |

## Regulatory and Compliance Requirements
[GDPR, HIPAA, SOX, PCI-DSS, industry-specific regulations that
constrain the solution.]

## 7. Cost-Benefit Analysis

## Investment Required

| Category              | One-Time Cost | Annual Cost | Notes                    |
|-----------------------|---------------|-------------|--------------------------|
| Software/Licensing    | $XX,XXX       | $XX,XXX     |                          |
| Development           | $XX,XXX       | --          | [Duration]               |
| Infrastructure        | $XX,XXX       | $XX,XXX     |                          |
| Training              | $XX,XXX       | $X,XXX      |                          |
| Change Management     | $XX,XXX       | --          |                          |
| **Total**             | **$XXX,XXX**  | **$XX,XXX** |                          |

## Expected Benefits

| Benefit               | Annual Value  | Type          | Realization Timeline     |
|-----------------------|---------------|---------------|--------------------------|
| [Benefit 1]          | $XX,XXX       | Cost saving   | [When]                   |
| [Benefit 2]          | $XX,XXX       | Revenue gain  | [When]                   |
| [Benefit 3]          | Qualitative   | Risk reduction| [When]                   |
| **Total Annual**      | **$XXX,XXX**  |               |                          |

## ROI Summary

| Metric                         | Value         |
|--------------------------------|---------------|
| Total Investment (3-year)      | $XXX,XXX      |
| Total Benefits (3-year)        | $XXX,XXX      |
| Net Present Value (NPV)        | $XXX,XXX      |
| Return on Investment (ROI)     | XX%           |
| Payback Period                  | X months      |
| Break-Even Point                | YYYY-MM       |

## 8. Success Criteria

| ID    | Criterion                              | Target          | Measurement         | Timeline      |
|-------|----------------------------------------|-----------------|---------------------|---------------|
| SC-1  | [Success criterion 1]                 | [Target value]  | [How measured]      | [When]        |
| SC-2  | [Success criterion 2]                 | [Target value]  | [How measured]      | [When]        |
| SC-3  | [Success criterion 3]                 | [Target value]  | [How measured]      | [When]        |

## 9. Timeline

## Major Phases

| Phase                  | Duration      | Start        | End          | Key Deliverables         |
|------------------------|---------------|--------------|--------------|--------------------------|
| Discovery & Planning   | X weeks       | YYYY-MM-DD   | YYYY-MM-DD   | PRD, TRD approved        |
| Design                 | X weeks       | YYYY-MM-DD   | YYYY-MM-DD   | UX designs, API specs    |
| Development            | X weeks       | YYYY-MM-DD   | YYYY-MM-DD   | Working software         |
| Testing & QA           | X weeks       | YYYY-MM-DD   | YYYY-MM-DD   | Test reports, sign-off   |
| Deployment & Rollout   | X weeks       | YYYY-MM-DD   | YYYY-MM-DD   | Production launch        |
| Post-Launch Review     | X weeks       | YYYY-MM-DD   | YYYY-MM-DD   | Success metrics report   |

## Key Milestones

| Milestone              | Target Date  | Decision Gate?  |
|------------------------|--------------|-----------------|
| BRD Approved           | YYYY-MM-DD   | Yes             |
| PRD Approved           | YYYY-MM-DD   | Yes             |
| Design Complete        | YYYY-MM-DD   | No              |
| Development Complete   | YYYY-MM-DD   | No              |
| UAT Complete           | YYYY-MM-DD   | Yes             |
| Go-Live                | YYYY-MM-DD   | Yes             |

## 10. Risks and Assumptions

## Risks

| ID   | Risk                    | Likelihood | Impact | Mitigation                      | Owner      |
|------|-------------------------|------------|--------|---------------------------------|------------|
| R-1  | [Risk 1]               | High/Med/Low| High/Med/Low | [Mitigation strategy]    | [Name]     |
| R-2  | [Risk 2]               | High/Med/Low| High/Med/Low | [Mitigation strategy]    | [Name]     |
| R-3  | [Risk 3]               | High/Med/Low| High/Med/Low | [Mitigation strategy]    | [Name]     |

## Assumptions

| ID   | Assumption                                              | Impact if Invalid            |
|------|---------------------------------------------------------|------------------------------|
| A-1  | [Assumption 1]                                         | [Consequence]                |
| A-2  | [Assumption 2]                                         | [Consequence]                |
| A-3  | [Assumption 3]                                         | [Consequence]                |

## Constraints
- [Constraint 1: budget, timeline, regulatory, organizational]
- [Constraint 2]
- [Constraint 3]

## 11. Approval

| Role              | Name          | Signature     | Date         |
|-------------------|---------------|---------------|--------------|
| Business Sponsor  | [Name]        |               |              |
| Finance           | [Name]        |               |              |
| IT Leadership     | [Name]        |               |              |
| Legal/Compliance  | [Name]        |               |              |

## Appendix

## A. Glossary
[Business terms and acronyms used in this document.]

## B. Supporting Data
[Market research, survey results, analytics data, competitive analysis.]

## C. Related Documents
- PRD: [link, if already started]
- Strategic Plan: [link]
- Competitive Analysis: [link]
```
