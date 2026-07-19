# Harness Maturity Model

A 5-level capability scale (adapted from CMMI) for rating an agent harness overall and per
dimension. It answers "where is this harness on the curve, and what's the next level?" — a more
professional framing than a pass/fail and a natural companion to the per-dimension score.

| Level | Name | What it looks like for an agent harness |
|-------|------|------------------------------------------|
| **1** | **Initial** | Ad hoc. Maybe a `CLAUDE.md`; little/no enforcement or sensors. Quality depends on the model and the individual. |
| **2** | **Managed** | Basic controls exist — a contract, some hooks, tests that run — but they are **inconsistent, narrowly scoped, or partly wired**, and largely reactive. |
| **3** | **Defined** | Controls are documented, consistent, and **version-controlled**; shared skills/standards; sensors run in CI; guards cover the primary paths. Reproducible across the team. |
| **4** | **Quantitatively Managed** | Coverage and quality are **measured**; evals/metrics gate changes; delivery is pinned/deterministic; drift is monitored. |
| **5** | **Optimizing** | The harness **improves itself**: a wired learning loop, continuous drift/eval, proactive hardening. |

## How to use it

- Assign each dimension a level from its evidence; assign an **overall** level (usually the
  *weakest load-bearing* dimension drags it down — a dormant learning loop caps the whole at L1–L2
  for self-improvement even if other dimensions are L3).
- State a **target** level and the 1–2 moves that unlock it. Maturity is a roadmap, not a grade.
- Maturity complements the per-dimension ✓✓/✓/⚠/✗ score: the score says "how good now," the level
  says "how repeatable/embedded."

*Source: Capability Maturity Model / CMMI (SEI, Carnegie Mellon) — levels 1 Initial, 2 Managed,
3 Defined, 4 Quantitatively Managed, 5 Optimizing.*
