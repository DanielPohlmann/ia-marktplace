---
name: workflows-tamandua
description: Use when operating Tamandua workflow runs from an interactive session — start a run for a plan or spec, check status, tail logs, explain findings, unblock a run. USE FOR: tamandua workflow run/status/resume/findings, logs, blocked vs paused vs failed, gate findings, disputes, fix and token budgets, run worktrees. DO NOT USE FOR: executing one plan in this session (use workflows), writing plans (use superpowers:writing-plans), checkpointed in-session execution (use superpowers:executing-plans).
---

# workflows-tamandua — Operate Tamandua Runs

## Overview

Tamandua is a local orchestrator that drives `claude -p` agents through a YAML
workflow, one step at a time, inside an isolated git worktree. A plan-driven
delivery workflow runs: load plan → implement ⇄ verify → gates (unit, security,
review, e2e, local CI) → pull request. Only the developer agent edits code; every
gate verifies and returns **findings**. A failing gate sends its open findings to a
`fix` step, then re-runs itself.

This skill is for the **human operator's** Claude Code session: start a run, watch
it, explain what it found, and make the decisions the pipeline refuses to make on
its own. The agents inside the run do not need this skill.

**Announce at start:** "Operating Tamandua via workflows-tamandua."

## Before you start

1. `tamandua version` — the CLI is on `PATH`. If not, see `references/cli.md`.
2. `tamandua status` — dashboard, control plane and daemon are up. Paused-run
   resume needs the daemon (`tamandua dashboard start`).
3. `tamandua workflow runs` — nothing else is active against the same repository.
   Delivery workflows run **one plan at a time** (E2E gates boot the app on fixed
   ports and shared containers). Never start a second run in parallel.
4. The target workflow is installed: `tamandua workflow list`. If missing,
   `tamandua workflow install <workflow-id>`.
5. Optional: `TAMANDUA_NOTIFY_URL` (an ntfy topic URL) in the environment of the
   Tamandua services gets a push when a run blocks or opens its PR.

## Start a run

Pass a plan path (one plan) or a spec path (the loader resolves its plans) as the
task. Always use an isolated worktree cut from the branch the PR will target, and
tell the workflow that branch:

```bash
tamandua workflow run <workflow-id> "docs/superpowers/plans/<plan>.md" \
  --worktree-origin-repository <absolute-repo-path> \
  --worktree-origin-ref <base-branch> \
  --context base_branch=<base-branch>
```

`--context key=value` is repeatable and overrides the workflow's context defaults.
Report the 8-char run id from the output. Every other command accepts a run-id
prefix (or, for `status`, a task substring).

## Watch a run

| Need | Command |
|---|---|
| Human-readable step list | `tamandua workflow status <run>` |
| Machine-readable state | `tamandua workflow status <run> --json` → `{ id, status, currentStepId, blockedStep, blockedReason, pausedUntil, tokensSpent, context: { pr? } }` |
| Recent events | `tamandua logs <run>` |
| Follow live | `tamandua logs-tail <run>` (stop it when done; it never exits on its own) |
| Where the code is | `tamandua worktree status <run>` → worktree path, origin ref, SHA |
| Open findings | `tamandua workflow findings <run> --status open [--gate <step-id>]` |

Poll with `status --json`, not by re-reading logs. When the user asks "how is it
going", answer with: run status, current step, tokens spent, count of open
findings by severity, and the PR URL once `context.pr` is set.

## Run states

| Status | Meaning | Who acts | Action |
|---|---|---|---|
| `running` | A step is in flight or queued | Nobody | Watch |
| `paused` | Usage limit hit (`pausedUntil` = reset time) or a human pause (`pausedUntil` = null) | Nobody / Human | Usage limit: wait — the engine resumes the **same step** and never counts it as a retry or round. Human pause: `tamandua workflow resume <run>` |
| `blocked` | A gate exhausted its rounds, the run-wide fix or token budget ran out, a disputed finding was raised again, a read-only violation happened, or a non-code failure (push rejected, `gh` unauthenticated, network) | **Human** | Diagnose, decide, then resume — see below |
| `failed` | A step failed outside the gate loop (e.g. implement retries exhausted per plan) | Human | Read logs, fix cause, `tamandua workflow resume <run>` (re-queues the failed step on the **same run id**) |
| `completed` | PR opened | Human | Review the PR. The pipeline never merges |
| `canceled` | Stopped by `tamandua workflow stop` | — | Start a new run if needed |

Never treat `paused` as an error, and never resume a `blocked` run without a
decision — resuming unchanged reproduces the same block.

## Explain findings

Run `tamandua workflow findings <run> --status open --json` and present a table:
gate, severity, rule, `file:line`, evidence (one line), expected. Group by gate;
`blocking` before `major`; mention `minor` only as a count (they go to the PR body
as observations and never trigger `fix`). A finding with `file: "."` was raised
by the engine itself (failed bash gate, read-only violation), not by a verifier.

For each finding, say in one sentence **why** it matters and whether it looks like
a real defect, a false positive, or a disagreement between agents. Read the cited
file in the worktree (`tamandua worktree status <run>` gives the path) before
judging — never judge from the evidence string alone. Fields, statuses (`open`,
`resolved`, `disputed`, `repeated`), `disputeReason` and fingerprints are in
`references/findings-contract.md`.

## Unblock a run

First establish **why** it blocked: `tamandua workflow status <run> --json` gives
`blockedStep` (the gate, `fix` or `pr`) and `blockedReason`; then read the open
findings of that gate (`--gate <blockedStep>`) and the last events. Present the
options below to the user and wait for a decision — the block exists precisely
because the pipeline must not decide alone.

| Block cause | Options |
|---|---|
| Gate rounds exhausted, finding keeps coming back | **Fix manually** (procedure below), or **raise the budget**: `tamandua workflow resume <run> --max-rounds <n>` if the last rounds show real progress |
| Disputed finding raised again | Resuming alone blocks again — there is no way to accept a dispute from the CLI. **Side with the developer**: adjust the gate's input in the worktree (rule exception or scanner suppression with a written reason, corrected test data). **Side with the gate**: fix the code. Either way, commit in the worktree, then resume |
| Run-wide fix budget spent | `resume --max-fix-rounds <n>`, or fix manually; if fixes oscillate (resolved → repeated), fix manually |
| Token budget spent | `resume --max-tokens <n>` (current spend is `tokensSpent`) |
| `gate/read-only-violation` | A verifier changed the worktree; the engine quarantined the change under `<git-common-dir>/tamandua-quarantine/<run>/<step-db-id>/` (never deleted) and restored the baseline — a moved HEAD is not reverted. Inspect the step's logs; resume once the cause is addressed |
| Non-code failure (push rejected, `gh` auth, network) | Fix the environment (`gh auth status`, remote access), then resume. No code change |

Resuming a blocked run re-queues `blockedStep` on the current worktree HEAD,
resets that step's round counter and keeps the findings history. Budget flags can
be combined with any resume.

### Manual fix procedure

1. `tamandua worktree status <run>` → `cd` into the worktree path.
2. Edit, run the affected tests, and commit there on the run's branch. Never push —
   the `pr` step pushes.
3. `tamandua workflow resume <run>`. The gate runs again on the new HEAD and marks
   fixed findings `resolved`.

### Rules for every unblock

- Never disable a check, skip or delete a test, lower a threshold, or suppress a
  warning **just to pass**. A suppression is acceptable only when the user agrees
  the finding is a false positive, and it carries a reason in the code or config.
- Record the decision in the commit message (`fix: resolve <rule> in <file> (operator decision: …)`).
- Raising a budget is the user's decision, not yours. Propose it with the evidence
  (rounds, findings trend, tokens), then wait.

## Pitfalls

- **Base branch mismatch.** `--worktree-origin-ref` and `--context base_branch=`
  must name the same branch, or the PR diff includes unrelated commits.
- **Editing the origin checkout instead of the worktree.** Worktree runs never read
  your main checkout after start.
- **Pushing manually from the worktree.** It bypasses the `pr` step and the
  pre-push stamp logic.
- **Deleting a blocked run to "start clean".** You lose the findings history that
  explains the block. Resume instead; delete only when abandoning the work.
- **Reading `[failed ]` steps as fatal.** Inside a gate loop a failed gate is
  normal; only the run status matters.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/cli.md](references/cli.md) | Full command catalog: run options and `--context`, status JSON, findings filters and JSON shape, resume semantics and budget flags, logs, worktrees, services, notifications |
| [references/findings-contract.md](references/findings-contract.md) | `FINDINGS_JSON`, `RESOLVED`, `DISPUTED_JSON` formats; severities; stored finding fields; fingerprints; statuses; dispute rule; engine findings |
| [references/troubleshooting.md](references/troubleshooting.md) | Symptom → cause → action table: daemon down, stuck `running`, repeated findings, oscillating fixes, rate-limit loops, worktree conflicts |
