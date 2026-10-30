---
name: product-ideation
description: Use when turning a raw business or feature idea into an approved idea brief through an interactive brainstorm, before any spec, design or architecture. USE FOR: problem framing, jobs-to-be-done, personas, value proposition, competitor scan, hypotheses, success metrics, risk flags. DO NOT USE FOR: PRDs or specs (use specs-documentation-prd), screens and flows (use product:product-design), technical design (use product:product-architecture).
---

# product-ideation — Stage 1: Business Idea Brainstorm

**Announce at start:** "Using product-ideation for `<slug>`."

## Hard gate

This stage produces an idea brief, not a spec. No requirement lists, screens, APIs, data models or code. Write only `docs/product/<slug>/01-ideation.md`.

## Process

1. **Context.** Read the product context: the path under a `Product context` heading in `CLAUDE.md`, else `README.md`. If neither describes the product, ask for a one-paragraph summary.
2. **Artifact.** Create it from `references/ideation-template.md` with `status: draft`.
3. **Research in background.** Dispatch `product:product-market-researcher` with the one-sentence idea, target audience and market/country. Keep interviewing while it runs.
4. **Interview, one question per message**, multiple choice when possible:
   - Who has the problem, and at which moment of their day?
   - What do they do today instead?
   - What does it cost them (time, money, risk)?
   - Why now?
   - What would make this a success in 90 days?
5. **Frame.** Use these when installed; otherwise apply the framework directly:
   - problem → `problem-framing-canvas:problem-framing-canvas`, `problem-statement:problem-statement`
   - user → `jobs-to-be-done:jobs-to-be-done`, `proto-persona:proto-persona`
   - value → `positioning-statement:positioning-statement`, `press-release:press-release`
   - market → `tam-sam-som-calculator:tam-sam-som-calculator`
   - facilitation → `product-management:product-brainstorming`
6. **Diverge, then converge.** Present 3 distinct value bets (not UI variants), each with its riskiest assumption. The user picks or merges.
7. **Hypotheses.** "We believe <change> for <persona> will result in <outcome>. We will know when <metric> reaches <target> by <date>." (`lean-ux-canvas:lean-ux-canvas`, `epic-hypothesis:epic-hypothesis`). Suggest the cheapest validation (`pol-probe:pol-probe`).
8. **Merge research** into Competitors and Market, sources inline.
9. **Risk scan.** Flag legal/compliance topics (personal data, payments, health, minors, user content) and point at `legal:legal`. Flag, do not solve.
10. **Self-review.** Every section filled or "Unknown — <how we would find out>". At most one paragraph of solution per option.
11. **Approval.** Set `status: in-review` and ask: "Approve the idea brief so we can move to design?" Follow the gate rules of `product:product`.

## Pitfalls

- Jumping to features — ask which job each one serves.
- Treating research as truth — keep source and date on every claim.
- Several questions in one message.

## Detailed reference

| File | Contents |
|---|---|
| `references/ideation-template.md` | Skeleton of `01-ideation.md` |
