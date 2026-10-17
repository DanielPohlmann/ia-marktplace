# Scoring Rubric

## Per-dimension scale

| Glyph | Label | Meaning |
|-------|-------|---------|
| ✓✓ | **strong** | Mature and correct; a model others could copy. Keep doing it. |
| ✓ | **ok** | Present and working, with clear room to improve. |
| ⚠ | **weak / blocked** | Exists but unreliable, partial, or blocked by an unresolved decision. |
| ✗ | **missing** | Absent where it materially matters. |

Score the *effective* state, accounting for where artifacts live (a capability delivered by a
plugin still counts even if the local repo folder is empty).

## Finding tags

| Tag | Meaning |
|-----|---------|
| `cheap` | Deterministic, low-risk, low-effort. Usually a config/file/hook edit. Do first. |
| `deeper` | Real engineering effort (new scripts, structural tests, refactors). |
| `gated` | Blocked on a governance/ownership decision before it can be actioned. |

## Severity (per finding)

Rate and order findings worst-first: **Critical** (a relied-on guarantee is void in normal use, or
secret exposure) · **High** (primary path unprotected/unverified) · **Medium** (real gap, limited
blast radius) · **Low** (hygiene/polish). Severity = impact × likelihood. See `prioritization.md`.

## Maturity (per dimension + overall)

Assign a CMMI-style level 1–5 (Initial / Managed / Defined / Quantitatively Managed / Optimizing) —
see `maturity-model.md`. The ✓✓/✓/⚠/✗ score says "how good now"; the level says "how repeatable".
**Always give a one-line rationale** for each level (why L3 not L2), so the rating is defensible.

## Assurance opinion (overall)

Close with one overall opinion on a defined scale, with a one-line basis:

| Opinion | Meaning |
|---------|---------|
| **Satisfactory** | Controls are effective; only minor gaps. |
| **Partial** | Meaningful risk reduction, but relied-on guarantees are bypassable or unverified. |
| **Unsatisfactory** | Key controls absent or ineffective. |

## Output ordering

1. Prioritize the action plan by **Impact × Effort** (Quick Wins → Major Projects → Fill-ins); see
   `prioritization.md`. Effort alone is not a priority.
2. Every corrective action carries an **owner** and a **target window**.
3. Separate **code-repo-legitimate** fixes from **governance-gated** ones.
4. Be honest: if a dimension is thin, say so plainly and give the first three steps.
