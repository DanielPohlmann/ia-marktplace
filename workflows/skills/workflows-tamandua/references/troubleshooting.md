# Troubleshooting Tamandua runs

| Symptom | Likely cause | Action |
|---|---|---|
| `tamandua: command not found` | Symlink missing from `PATH` | `node <checkout>/dist/cli/cli.js version`; reinstall with `./install` from the checkout |
| `node:sqlite` error | Not running real Node.js ≥ 22 | Use Node 22+, not a wrapper |
| `resume` of a paused run fails with daemon unreachable | Dashboard daemon down | `tamandua dashboard start`, then resume |
| Run stays `running`, `currentStepId` unchanged, no new events for a long time | Agents not polling, or a long gate (E2E, mutation testing) | `tamandua logs <run>` for the last event; `tamandua status` for running harness processes; `tamandua nudge` if nothing is running |
| Run `paused` again right after resume | Usage limit not reset yet | Wait for the reset time (`pausedUntil` in `status --json`, also in the logs); the engine resumes on its own |
| Same finding `repeated` across rounds | The developer agent misunderstands the finding | Read the code, fix manually in the worktree, commit, resume |
| Findings flip between two gates (security fix breaks review, review fix breaks security) | Conflicting rules | Human decision on which rule wins; fix manually; consider documenting the exception in the rule source |
| `blocked` on a disputed finding | Gate and developer disagree | Explain both sides (see `findings-contract.md` → Dispute rule); wait for the user |
| Same disputed finding blocks again right after resume | Resumed without changing the worktree; no CLI switch accepts a dispute | Adjust the gate's rule/config or the code in the worktree, commit, then resume |
| `blocked` with `gate/read-only-violation` | A verifier tried to write | Check the step's logs for which tool it used; the change is in `<git-common-dir>/tamandua-quarantine/`, never deleted |
| `blocked` at `pr` with no findings | Push rejected, `gh` not authenticated, network | `gh auth status`; check remote access; resume. Never `--no-verify` |
| `blocked` at `pr` with a `gate/pre-push` finding | The pre-push hook failed on a commit made after the last local-CI gate | Normal loop; if it blocked, the round budget ran out — fix manually or `resume --max-rounds <n>` |
| E2E gate fails on port already in use | Another run, or a leftover app process, holds the ports | Make sure only one run is active (`tamandua workflow runs`); stop leftover processes; resume |
| `failed` at `implement` | Plan retries exhausted (per plan) | Read the verify feedback in the logs; fix the plan or the code; `tamandua workflow resume <run>` (new run id) |
| Worktree missing after a run | Cleanup policy removed it on completion | `tamandua worktree list`; the PR branch still has the commits |
| Disk filling with worktrees | Old completed runs | `tamandua worktree prune --completed --older-than 7d` |
| No push notification when a run blocks | `TAMANDUA_NOTIFY_URL` not set in the environment of the Tamandua services | Set it (e.g. an `ntfy.sh` topic URL) and restart the dashboard/control plane |

## Information to collect before asking the user

1. `tamandua workflow status <run> --json` (`blockedStep`, `blockedReason`, `tokensSpent`)
2. `tamandua workflow findings <run> --status open --gate <blockedStep>`
3. The last 50 events: `tamandua logs <run>`
4. Worktree path and HEAD: `tamandua worktree status <run>`
