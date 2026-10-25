# Troubleshooting Tamandua runs

| Symptom | Likely cause | Action |
|---|---|---|
| `tamandua: command not found` | Symlink missing from `PATH` | `node <checkout>/dist/cli/cli.js version`; reinstall with `./install` from the checkout |
| `node:sqlite` error | Not running real Node.js ≥ 22 | Use Node 22+, not a wrapper |
| `resume` of a paused run fails with daemon unreachable | Dashboard daemon down | `tamandua dashboard start`, then resume |
| Run stays `running`, `currentStepId` unchanged, no new events for a long time | Agents not polling, or a long gate (E2E, mutation testing) | `tamandua logs <run>` for the last event; `tamandua status` for running harness processes; `tamandua nudge` if nothing is running |
| Run `paused` again right after resume | Usage limit not reset yet | Wait for the reset time (`pausedUntil` in `status --json`, also in the logs). Auto-resume is done by the control-plane reconciler, so the control plane must be up (`tamandua status`). After 5 consecutive pauses without progress (`MAX_CONSECUTIVE_RATE_LIMIT_PAUSES`) the step is handled as a failure |
| Same finding `repeated` across rounds | The developer agent misunderstands the finding | Read the code, fix manually in the worktree, commit, resume |
| Findings flip between two gates (security fix breaks review, review fix breaks security) | Conflicting rules | Human decision on which rule wins; fix manually; consider documenting the exception in the rule source |
| `blocked` on a disputed finding | Gate and developer disagree | Explain both sides (see `findings-contract.md` → Dispute rule); wait for the user |
| Same disputed finding blocks again right after resume | Resumed without changing the worktree; no CLI switch accepts a dispute | Adjust the gate's rule/config or the code in the worktree, commit, then resume |
| `blocked` with `gate/read-only-violation` | A verifier tried to write | Check the step's logs for which tool it used; the change is in `<git-common-dir>/tamandua-quarantine/`, never deleted |
| `blocked` at `pr` with no findings | Push rejected, `gh` not authenticated, network | `gh auth status`; check remote access; resume. Never `--no-verify` |
| `blocked` at `pr` with a `gate/pre-push` finding | The pre-push hook failed on a commit made after the last local-CI gate | Normal loop; if it blocked, the round budget ran out — fix manually, or resume (a bare resume grants the gate a fresh `max_rounds`; `--max-rounds <n>` sets the cap of every gate for the rest of the run) |
| E2E gate fails on port already in use | Another run, or a leftover app process, holds the ports | Make sure only one run is active (`tamandua workflow runs`); stop leftover processes; resume |
| `failed` at `implement` | Plan retries exhausted (per plan) | Read the verify feedback in the logs and fix the cause. `resume` re-queues the failed step and all later steps, but does not reset stories: if the plan loop is exhausted (failed stories, none pending) it fails again with "Loop has failed stories and no pending stories". Known engine limitation: start a new run with the remaining plan. `resume` works for a failed single step |
| Worktree missing after a run | Removed by `worktree remove`, `worktree prune` or `workflow delete` (the default cleanup policy is `keep`) | `tamandua worktree list`; the PR branch still has the commits |
| Disk filling with worktrees | Old completed runs | `tamandua worktree prune --completed --older-than 7d` |
| No push notification when a run blocks | `TAMANDUA_NOTIFY_URL` was not exported in the shell that ran `tamandua workflow run`; the URL is captured per run at start and never updated | Export it (e.g. an `ntfy.sh` topic URL) and start a new run; the current run keeps what it captured. The env var wins over the workflow's `notifications.url` |

## Information to collect before asking the user

1. `tamandua workflow status <run> --json` (`blockedStep`, `blockedReason`, `tokensSpent`)
2. `tamandua workflow findings <run> --gate <blockedStep>` (no `--status`: a blocking finding is usually `repeated` or `disputed`, not `open`)
3. The last 50 events: `tamandua logs <run>`
4. Worktree path and HEAD: `tamandua worktree status <run>`
