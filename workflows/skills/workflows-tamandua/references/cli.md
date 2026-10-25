# Tamandua CLI — operator command catalog

Every command that takes `<run>` accepts a run-id prefix (8 chars is enough).
`workflow status` also accepts a substring of the task text. `logs` and
`logs-tail` also accept `#<run-number>`.

## Install and services

| Command | Purpose |
|---|---|
| `tamandua version` | Confirm the CLI is on `PATH` |
| `node <tamandua-checkout>/dist/cli/cli.js <command>` | Fallback when the `tamandua` symlink is missing (`tamandua source-path` prints the checkout) |
| `tamandua get-ready` | Install bundled workflows and start dashboard + control plane |
| `tamandua status` | Services (dashboard, MCP, control plane), version, run summary, running harness processes |
| `tamandua dashboard start` / `tamandua dashboard status` | Web UI on `http://localhost:3334`; also the daemon that `pause`/`resume` of paused runs talk to |
| `tamandua control-plane status` | Run-scoped scheduler (default port 3339) |
| `tamandua nudge` | Make every scheduled agent poll now. Does not resume paused runs or interrupt in-flight agents |

## Workflows

| Command | Purpose |
|---|---|
| `tamandua workflow list [--json]` | Installed workflows (`--json` → `[{ id, name, description }]`) |
| `tamandua workflow install <id>` / `--all` | Install a bundled workflow and provision its agents |
| `tamandua workflow uninstall <id> [--force]` | Remove one workflow; refuses while it has active runs unless `--force` |

## Start a run

```bash
tamandua workflow run <workflow-id> "<task>" [options]
```

For plan-driven delivery workflows the task is a repository-relative path to a
plan file or a spec file.

| Option | Effect |
|---|---|
| `--worktree-origin-repository <dir>` | Repository to cut the isolated worktree from. Defaults to the current repository |
| `--worktree-origin-ref <ref>` | Branch, tag or SHA checked out in the worktree. Defaults to the current branch. Use the PR's base branch |
| `--context <key=value>` | Repeatable; later wins. Overrides the workflow's `context:` defaults, e.g. `--context base_branch=main`. Keys are lowercase snake_case |
| `--working-directory-for-harness <dir>` | Harness working directory for non-worktree runs. Defaults to the shell's CWD; pass an absolute path |
| `--claude-as-harness` | Claude Code CLI (`claude -p`). Default. Mutually exclusive with `--pi-as-harness` / `--hermes-as-harness` |
| `--no-hurry-please-save-tokens-mode` | Lower polling frequency (15-minute floor). For low-priority background runs |
| `--no-relaunch-upon-rugpull` | Only for merge workflows: do not auto-create a replacement run when the base moved |

The command prints `Run: <id>`, `Workflow: <id>`, `Status: running`.

| Environment variable | Effect |
|---|---|
| `TAMANDUA_CLAUDE_BINARY` | Use a specific `claude` binary (also how test suites inject a scripted fake) |
| `TAMANDUA_NOTIFY_URL` | Webhook for `run.blocked` and `run.pr_opened`. An `ntfy.sh` URL (or `TAMANDUA_NOTIFY_FORMAT=ntfy`) sends ntfy pushes with title, tags, priority and a click-through to the PR; other URLs get the JSON event payload |

## Inspect a run

| Command | Output |
|---|---|
| `tamandua workflow runs` | Every run: status, workflow, tokens |
| `tamandua workflow status <query>` | Run, workflow, task, status, tokens, workspace mode, and one line per step: `[done   ]`, `[running]`, `[failed ]`, `[pending]` + agent role |
| `tamandua workflow status <query> --json` | `{ "id", "status", "currentStepId", "blockedStep", "blockedReason", "pausedUntil", "tokensSpent", "context": { "pr"? } }` — `status` ∈ `running`, `paused`, `blocked`, `completed`, `failed`, `canceled`; `blockedStep`/`blockedReason` are `null` unless blocked; `pausedUntil` is the usage-limit reset time of a rate-limit pause (the engine resumes by itself) and `null` for a human pause (needs `resume`); `context.pr` is the PR URL once the `pr` step ran |
| `tamandua workflow findings <query> [--json] [--status <s>] [--gate <step-id>]` | Findings recorded for the run. `--status` ∈ `open`, `resolved`, `disputed`, `repeated`; `--gate` filters by gate step id. Text: one line per finding (`[status] severity gate rule file:line fingerprint evidence`). `--json`: array of finding objects (fields in `findings-contract.md`) |
| `tamandua logs [<lines> \| <run> \| #<n>]` | Last 50 global events, or the run's events |
| `tamandua logs-tail [<lines> \| <run> \| #<n>]` | Follow events live. Never exits by itself — run it in the background or stop it |
| `tamandua worktree list` | Every managed worktree: run id, status, cleanup policy, path |
| `tamandua worktree status <run>` | Origin repo, origin ref, origin SHA, original branch, worktree path, cleanup policy |

Polling loop for scripts:

```bash
while :; do
  s=$(tamandua workflow status "$RUN" --json | node -e 'process.stdin.on("data",d=>console.log(JSON.parse(d).status))')
  case "$s" in completed|failed|blocked|canceled) break ;; esac
  sleep 60
done
```

## Resume and budgets

```bash
tamandua workflow resume <run> [--max-rounds <n>] [--max-fix-rounds <n>] [--max-tokens <n>]
```

| Run status | Effect |
|---|---|
| `blocked` | Re-queues `blockedStep` (a gate, `fix` or `pr`) on the current worktree HEAD, resets that step's fix-round counter, keeps the findings history, and applies any budget flags |
| `paused` | Budget flags are stored first; then the daemon resumes agent polling on the same step (daemon must be up) |
| `failed` | Budget flags are stored first; then the failed step is re-queued on the **same run id** |
| `running` | Only stores the budget flags (`Updated budgets for run <id>.`) |
| `completed`, `canceled` | Cannot be resumed |

| Flag | Budget | Workflow default | On exhaustion |
|---|---|---|---|
| `--max-rounds <n>` | Fix rounds each gate may send | 3 (`on_fail.max_rounds`) | `blocked` |
| `--max-fix-rounds <n>` | Fix rounds across all gates of the run | 8 (`budgets.max_fix_rounds`) | `blocked` |
| `--max-tokens <n>` | Token budget for the run (compare with `tokensSpent`) | unset (`budgets.max_tokens`) | `blocked` before the next step |

Values must be positive integers. `implement` retries per plan (4) are not a
resume flag; exhausting them fails the run.

Resuming a block caused by a **disputed** finding without changing anything in the
worktree blocks again: there is no CLI switch that accepts a dispute.

## Other run controls

| Command | Applies to | Effect |
|---|---|---|
| `tamandua workflow pause <run> [--drain]` | `running` | Pause; `--drain` lets in-flight sessions finish first |
| `tamandua workflow pause-all [--drain]` / `resume-all` | all `running` / all `paused` | Bulk pause/resume. `resume-all` does not touch failed or blocked runs |
| `tamandua workflow stop <run>` | `running` | Cancel (`canceled`). Agents notice on their next poll |
| `tamandua workflow delete <run> [--force]` | any | Permanently delete the run, its steps, findings and managed worktree. `--force` cancels an active run first. Irreversible — confirm with the user |
| `tamandua worktree remove <run> [--force]` | worktree | Delete a worktree and its tracking entry |
| `tamandua worktree prune --completed --older-than <7d\|24h\|30m>` | worktrees | Remove worktrees of completed/canceled runs older than the duration |

## Help

Every command prints its own usage with `--help`, e.g.
`tamandua workflow findings --help`. When this catalog and `--help` disagree,
`--help` wins — it ships with the installed version.
