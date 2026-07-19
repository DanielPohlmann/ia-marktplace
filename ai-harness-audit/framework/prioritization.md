# Findings, Severity & Prioritization

How findings are written, rated, and ordered so the audit is **actionable**, not just descriptive.
Grounded in standard audit/advisory practice (see Sources).

## 1. Finding structure — the 5 C's

Every finding is written so management can act without re-interpretation. Use the **5 C's**:

| C | What it states |
|---|----------------|
| **Criteria** | The standard the harness is expected to meet (the dimension's checklist item). |
| **Condition** | What was actually observed, with evidence (path / line / command output). |
| **Cause** | The underlying reason (root cause), not a restated symptom. |
| **Consequence** | The impact if unaddressed — wasted turns, bypassable guard, non-determinism, etc. *This is what lets a reader judge priority.* |
| **Corrective action** | A specific fix, with an **owner**, an **effort**, and an **impact** (see below). |

*Source: IIA / chartered-audit "5 C's of audit findings".*

## 2. Severity scale (impact × likelihood)

Rate each finding's severity; order findings **worst-first** within each dimension.

| Severity | Meaning (harness context) |
|----------|---------------------------|
| **Critical** | A guarantee is void in normal use (e.g. a guard the team relies on is fully bypassable), or data/secret exposure. Fix immediately. |
| **High** | A control is materially undermined or a primary path is unprotected/unverified; likely to bite in routine work. |
| **Medium** | A real gap with a workaround or limited blast radius; should be scheduled. |
| **Low** | Hygiene / polish; low likelihood or low impact. |

*Source: risk-matrix practice (likelihood × impact); audit 3-/4-tier rating models.*

## 3. Prioritization — Impact × Effort (not effort alone)

Effort alone is not a priority. Plot every corrective action on a 2×2 of **Impact** (value if done)
against **Effort** (cost to do). The quadrant *is* the priority.

```
                 LOW EFFORT            HIGH EFFORT
              ┌─────────────────────┬─────────────────────┐
   HIGH       │   QUICK WINS        │   MAJOR PROJECTS     │
   IMPACT     │   do first (wave 1) │   plan & phase       │
              ├─────────────────────┼─────────────────────┤
   LOW        │   FILL-INS          │   RECONSIDER         │
   IMPACT     │   when time allows  │   avoid / question   │
              └─────────────────────┴─────────────────────┘
```

- **Quick Wins** (high impact, low effort) — the wave-1 backbone; target the cheapest high-impact set first.
- **Major Projects** (high impact, high effort) — real value but phase them; give each a target window.
- **Fill-ins** (low impact, low effort) — batch opportunistically.
- **Reconsider** (low impact, high effort) — challenge whether to do at all.

Rate **Impact** H/M/L by how much it reduces the worst consequences (§2); rate **Effort**
cheap/deeper/gated (deterministic edit / real engineering / blocked on a decision). Decision-gated
items are placed by their *post-decision* impact and flagged `gated`.

*Source: Impact-Effort matrix / Action Priority Matrix (consulting practice).*

## 4. Every action carries an owner and a target

A corrective action without an owner and a timeline is a wish. Each row in the action plan has:
**ID · Action · Impact · Effort · Quadrant · Owner · Target window.** Order by quadrant
(Quick Wins → Major Projects → Fill-ins), then by impact.

## Sources

- IIA / chartered-audit — *5 C's of audit findings* (criteria, condition, cause, consequence, corrective action).
- Impact-Effort / Action Priority Matrix — consulting prioritization (quick wins / major projects / fill-ins / reconsider).
- Risk-matrix practice — severity = likelihood × impact; 3-/4-tier rating, worst-first ordering.
