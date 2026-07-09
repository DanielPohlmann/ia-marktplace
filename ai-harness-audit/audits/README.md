# Audit ledger

One row per engagement. A re-audit of a target adds a **new** dated row (it never overwrites a prior
one), so each target's history reads top-to-bottom. `Framework` is the method version the audit ran
against (see `../framework/METHODOLOGY.md` changelog); `Report` is that audit's own revision.

| Date | Target | Framework | Overall maturity | Assurance | Report | Rev |
|---|---|---|---|---|---|---|
| 2026-06-24 | `pim` monolith + harness plugins | v1.0 (8-dim) | L2 — Managed (→ L3) | Partial | [md](2026-06-24-pim/pim-2026-06-24-v1.0.md) · [pdf](2026-06-24-pim/pim-2026-06-24-v1.0.pdf) | 1.0 |

> **Future — benchmark comparison.** Today the ledger tracks only overall maturity + opinion. A later
> iteration should capture the **per-dimension scorecard** per audit (a column per dimension, or a
> companion `benchmarks.csv`) so re-audits of the same target — and different targets on the same
> framework version — can be compared dimension-by-dimension, not just at the headline level.
