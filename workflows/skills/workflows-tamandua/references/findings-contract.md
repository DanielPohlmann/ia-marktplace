# Findings contract

Gates never edit code. They report findings; the engine stores them and hands the
open ones to the `fix` step. This is the contract every gate and the `fix` step
follow — use it to read `tamandua workflow findings` output and to explain why a
run looped or blocked.

## Verifier output (agent gates)

A verifier ends its reply with a status line and, when it found problems, one
`FINDINGS_JSON:` line holding a JSON array on a single line:

```
STATUS: retry
FINDINGS_JSON: [{"rule":"arch/cross-module-import","severity":"blocking","file":"src/Orders/Application/PlaceOrderHandler.cs","line":42,"symbol":"PlaceOrderHandler","evidence":"uses Billing.Domain.Invoice","expected":"reference by id or consume an integration event"}]
```

| Field | Required | Meaning |
|---|---|---|
| `rule` | yes | Stable identifier: a review-rule id, `semgrep/<id>`, `stryker/survived-mutant`, `gate/<step-id>` |
| `severity` | yes | `blocking`, `major` or `minor` |
| `file` | yes | Repository-relative path. The engine **drops** an agent finding without one |
| `evidence` | yes | What was observed (code excerpt, scanner message, test output) |
| `line` | no | Line at the time of the round. Informational only |
| `symbol` | no | Class/function/member the finding is about. Part of the fingerprint |
| `expected` | no | What would satisfy the rule |

`STATUS: done` with no `FINDINGS_JSON`, or with only `minor` findings, passes the
gate.

## Severities

| Severity | Triggers `fix` | Ends up |
|---|---|---|
| `blocking` | Yes | Must be resolved (or the run blocks) |
| `major` | Yes | Must be resolved (or the run blocks) |
| `minor` | Never | Listed under "Observations" in the PR body |

## Engine findings

Findings the engine synthesizes itself use `file: "."` (repository root):

- A bash gate that exits non-zero without printing its own `FINDINGS_JSON:` becomes
  **one** finding: `rule: gate/<step-id>`, `severity: blocking`, `evidence` = last
  200 lines of combined output. Gate scripts wrapping JSON-producing tools
  (Semgrep, gitleaks, Stryker) print a `FINDINGS_JSON:` line so each result is a
  separate finding with a real file.
- `gate/read-only-violation`: a verification, analysis, testing or scanning agent
  changed the worktree. The engine discarded the change (`git status --porcelain`
  check after the step) and blocks the run.
- `gate/pre-push`: the pre-push hook failed during the `pr` step.

When a bash gate fails, its verifier agent (if any) does not run; the run goes
straight to `fix`.

## Stored findings (`tamandua workflow findings --json`)

An array of objects:

| Field | Meaning |
|---|---|
| `runId` | Run the finding belongs to |
| `gate` | Gate step id that raised it (e.g. `gate-review`) |
| `fingerprint` | Stable id — see below. `RESOLVED` and `DISPUTED_JSON` refer to it |
| `severity` | `blocking`, `major`, `minor` |
| `status` | `open`, `resolved`, `disputed`, `repeated` |
| `round` | Gate round in which it was last raised |
| `rule`, `file`, `line`, `symbol`, `evidence`, `expected` | As reported (see above) |
| `disputeReason` | The developer agent's reason, when it disputed the finding |

**Fingerprint** = hash of `gate + rule + file + symbol`. Line numbers are excluded
because edits move them. The same problem raised in a later round is the same
finding, not a new one.

| Status | Meaning |
|---|---|
| `open` | Raised and not yet resolved — goes to the next `fix` |
| `resolved` | `fix` claimed it and the gate did not raise it again |
| `disputed` | `fix` rejected it with a `disputeReason` |
| `repeated` | Raised again in a later round after `fix` claimed it resolved — the fix did not work |

A growing count of `repeated` findings means the developer agent is not
converging; that is the signal to fix manually instead of raising `--max-rounds`.

## `fix` input and output

`fix` receives only the open `blocking`/`major` findings of the gate that invoked
it plus the plan paths. It replies:

```
STATUS: done
RESOLVED: ["<fingerprint>", "<fingerprint>"]
DISPUTED_JSON: [{"fingerprint":"<fingerprint>","reason":"false positive: input already validated in OrderValidator"}]
```

`fix` rules: never disable a check, skip or delete a test, lower a threshold or
suppress a warning to pass; fix the root cause; run the affected unit tests before
replying.

## Dispute rule

The developer agent may dispute a finding with a reason. If the gate raises a
**disputed** finding again, the run becomes `blocked` immediately: disagreement
between agents is a human decision.

There is no command that accepts a dispute. Resuming without a change re-runs the
gate, which raises the finding again and blocks again. The human resolves it in the
worktree:

- **Developer is right (false positive):** change what the gate reads — a rule
  exception or scanner suppression with a written reason, a corrected rule source,
  corrected test data — commit, resume.
- **Gate is right:** fix the code, commit, resume.

When explaining a dispute, show side by side: the gate's `evidence` and
`expected`, the `disputeReason`, and the code at `file` in the worktree.

## Re-review scope

From round 2 on, a review gate reviews only commits made since its previous round
(`git diff <last-reviewed-sha>..HEAD`) and receives its earlier findings; it must
not repeat a resolved one. A finding about code untouched since round 1 that
appears only in round 3 is therefore suspicious — mention it.
