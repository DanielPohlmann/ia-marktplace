<!-- Part of the specs-documentation-brd skill. Loaded on demand from SKILL.md. -->

# Business Requirements Document (BRD) — details

## Standard BRD Structure

### 1. Executive Summary
A concise overview (1-2 paragraphs) of the business need, proposed solution, and expected outcomes. This section should stand alone -- a reader should understand the essence of the proposal after reading only this section.

### 2. Business Objectives
Specific, measurable business goals the initiative aims to achieve.

### 3. Stakeholders
All individuals and groups affected by or involved in the initiative.

### 4. Current State Analysis
Description of the existing situation, pain points, and limitations.

### 5. Proposed Solution (High-Level)
Overview of the recommended approach without technical implementation details.

### 6. Business Rules
Policies, regulations, and organizational rules that govern the solution.

### 7. Cost-Benefit Analysis
Financial justification including investment required and expected returns.

### 8. Success Criteria
Measurable outcomes that determine whether the initiative achieved its goals.

### 9. Timeline
Major phases and milestones with estimated durations.

### 10. Risks and Assumptions
Known risks with mitigation strategies and assumptions that underpin the analysis.

## BRD Example: Customer Self-Service Portal

```markdown
# BRD: Customer Self-Service Portal

| Field            | Value                    |
|------------------|--------------------------|
| Author           | Maria Business           |
| Status           | In Review                |
| Business Sponsor | VP of Customer Success   |

## 1. Executive Summary

Customer support costs have increased 35% year-over-year while
satisfaction scores have declined from 4.2 to 3.6. Analysis shows
that 62% of support tickets are routine requests (password resets,
billing inquiries, order status) that customers could resolve
independently. We propose a self-service portal that would reduce
ticket volume by 40%, save $1.2M annually in support costs, and
improve customer satisfaction by enabling 24/7 instant resolution.
Estimated investment: $450K over 6 months with a 4.5-month payback.

## 2. Business Objectives

| ID   | Objective                                | Target              |
|------|------------------------------------------|---------------------|
| BO-1 | Reduce support ticket volume             | -40% within 6 months|
| BO-2 | Reduce annual support costs              | -$1.2M              |
| BO-3 | Improve customer satisfaction (CSAT)     | 3.6 -> 4.3          |
| BO-4 | Enable 24/7 customer self-service        | 99.9% availability  |
```
