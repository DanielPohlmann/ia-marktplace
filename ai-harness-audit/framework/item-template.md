# Per-item template

Use this exact structure for every dimension in §5, so items are consistent and comparable. It
delivers the **5 C's** (see `prioritization.md`) — don't just *claim* them. Cite evidence, not inference.

```markdown
### 5.x <Dimension> · <✓✓ strong | ✓ ok | ⚠ weak | ✗ missing> · Maturity L<1–5>

*Maturity rationale.* <one line: why this level, e.g. "documented & version-controlled (L3) but not
measured (no coverage gates)">

**Criteria.** <the checklist criteria evaluated, one clause each>

**Condition (evidence).** <what was observed — files / paths / line refs / command output>

**Strengths.**
- ✓ <present and working — cite evidence>

**Findings (worst-first).** Each finding has a stable **ID** (for traceability into the action plan):

- **F<n> · [Critical|High|Med|Low]** <title>
  - *Cause:* <root cause — why it is this way, not a restated symptom>
  - *Consequence:* <impact if unaddressed — the basis for its priority>
  - *Evidence:* <path / line / command output>

**Corrective actions.** (carry into the §7 Impact×Effort register)

| Finding | Action | Impact | Effort | Owner |
|---------|--------|--------|--------|-------|
| F<n> | <fix that addresses the cause> | H/M/L | cheap/deeper/gated | <role> |
```

Rules:
- **Deliver every C.** Each finding states **Cause** and **Consequence** explicitly — not just a
  condition. If you can't state a consequence, it isn't a finding worth listing.
- **Order findings worst-first** by severity (Critical→Low).
- **Finding IDs are stable and unique** (F1, F2 …) and every action references the finding it fixes —
  this is the traceability the action plan relies on.
- **Strengths and findings both cite evidence** — no unsupported praise or criticism.
- A capability that exists only in an external/non-pinned dependency or in personal config is a
  finding ("not reproducible from the repository"), scored accordingly.
- Recommendations carry **Impact + Effort + Owner** so they slot straight into the Impact×Effort plan.
- Add the per-dimension **maturity level + rationale** (see `maturity-model.md`).
- Do not vary the section order between items.
