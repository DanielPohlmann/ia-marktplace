---
name: workflows
description: Use when given a plan path from docs/superpowers/plans/ to execute end-to-end. This skill is the agent-side half of a two-part automation system — the orchestrator half is ./scripts/planlist-runner.js, which spawns Claude Code, injects `/workflows <plan_path>` via stdin, and monitors stdout for the [PLANO_CONCLUIDO] signal emitted by this skill. Together they form a fully automated plan queue: planlist-runner.js owns the CSV state (planlist.csv) and rate-limit handling; this skill owns branch isolation, plan execution, commit/push/PR, and signal emission. USE FOR: executing any plan file end-to-end (branch setup → implement → commit → push → PR → signal), automated plan queue runs, "run/execute/process a plan" requests DO NOT USE FOR: authoring or drafting plans (use superpowers:writing-plans), brainstorming implementation approaches (use superpowers:brainstorming), interactive step-by-step execution with human checkpoints (use superpowers:executing-plans)
---

# workflows — Plan Execution Orchestrator

## Overview

Receives a plan file path, executes it end-to-end on an isolated feature branch, and always emits a `[PLANO_CONCLUIDO]` signal at the end — even when errors occur.

**Announce at start:** "Executing loop skill for `<plan_path>`."

---

## Context — Why this skill must never stop

This skill is called by an orchestrator script (`planlist-runner.js`) that injects prompts via stdin and monitors stdout for `[PLANO_CONCLUIDO]`. If the agent stops or asks a question without emitting the signal, the orchestrator **hangs forever** waiting. There is no human at the keyboard during automated runs.

This means:
- Never pause to ask for clarification.
- Never block on an unresolvable error.
- Always reach Phase 4 and emit the signal — capture any errors in the PR and `update-plan.js`, and move on.

---

## Input

The plan path is passed as the argument to this skill:

```
docs/superpowers/plans/2026-05-27-example-create-file.md
```

---

## Phase 1 — Branch Setup

### 1.1 Ensure you start from `develop`

Starting from `develop` guarantees the feature branch contains the latest shared code and the PR diff is clean.

```bash
git branch --show-current
```

If the current branch is **not** `develop`:

```bash
git checkout develop
git pull origin develop
```

### 1.2 Extract the feature branch name

Strip the `YYYY-MM-DD-` date prefix and `.md` extension from the plan filename:

| Plan file | Branch name |
|-----------|-------------|
| `2026-05-27-example-create-file.md` | `example-create-file` |
| `2026-06-01-add-payment-gateway.md` | `add-payment-gateway` |

### 1.3 Create (or reuse) the feature branch

```bash
git checkout -b <slug>
```

If the branch already exists (e.g., retrying a failed run):

```bash
git checkout <slug>
```

All subsequent changes happen on this branch. Never commit to `develop`.

---

## Phase 2 — Execute the Plan

**REQUIRED SUB-SKILL:** Use `superpowers:executing-plans` with the plan path received as input.

If `executing-plans` encounters a blocker it cannot resolve — missing dependency, failing test, ambiguous instruction — **do not stop**. Capture the error description in a variable (`$ERROR_DESCRIPTION`) and proceed to Phase 3 with `error=1`. Stopping here would hang the orchestrator.

---

## Phase 3 — Commit, Push, and Open PR

### 3.1 Check for uncommitted changes

```bash
git status
```

### 3.2 Commit if needed

If uncommitted changes exist AND the plan did not already commit them, stage only the files that were changed (avoid `git add -A` to prevent accidentally including `.env` or large binaries):

```bash
git status --short            # review what changed
git add <each changed file>   # stage explicitly
git commit -m "feat: execute plan <slug>"
```

If the plan already committed everything — skip.

### 3.3 Push with hook error handling

The project uses Lefthook to enforce format, build, and test gates on push.

```bash
git push -u origin <slug>
```

**If the push hook fails:**

1. Read the full error output to understand what failed (lint, build, test).
2. Fix the root cause in the affected files.
3. Stage only the fixed files and commit:
   ```bash
   git add <affected files>
   git commit -m "fix: resolve hook validation errors"
   ```
4. Re-attempt push.

Retry up to **3 times** — more than that usually means a structural problem the agent cannot auto-fix. After 3 failed attempts, capture the hook error as `$ERROR_DESCRIPTION` and continue.

### 3.4 Open the PR (or update an existing one)

Check if a PR already exists for this branch:

```bash
EXISTING_PR_URL=$(gh pr list --head <slug> --state open --json url --jq '.[0].url' 2>/dev/null)
```

**If no PR exists** (`$EXISTING_PR_URL` is empty), create one and capture the URL directly from `gh pr create` stdout:

```bash
BODY_FILE=$(mktemp /tmp/pr-body-XXXXXX.txt)

printf 'Automated execution of plan: %s\n' "<plan_path>" > "$BODY_FILE"

if [ -n "$ERROR_DESCRIPTION" ]; then
  printf '\n## ⚠️ Execution Error\n\nThe automated runner encountered an error and could not complete all steps.\n\n**Error:**\n%s\n\nManual review required before merging.\n' \
    "$ERROR_DESCRIPTION" >> "$BODY_FILE"
fi

PR_URL=$(gh pr create \
  --title "feat: <slug>" \
  --body-file "$BODY_FILE" \
  --base develop \
  --head <slug>)

rm -f "$BODY_FILE"
```

> `gh pr create` prints the new PR URL to stdout — that is the value assigned to `$PR_URL`.

**If a PR already exists**, reuse its URL. If there were errors, append the error block:

```bash
PR_URL="$EXISTING_PR_URL"

if [ -n "$ERROR_DESCRIPTION" ]; then
  EXISTING_BODY=$(gh pr view "$PR_URL" --json body --jq '.body')
  UPDATED_FILE=$(mktemp /tmp/pr-body-XXXXXX.txt)

  printf '%s\n\n## ⚠️ Execution Error\n\n%s\n' \
    "$EXISTING_BODY" "$ERROR_DESCRIPTION" > "$UPDATED_FILE"

  gh pr edit "$PR_URL" --body-file "$UPDATED_FILE"
  rm -f "$UPDATED_FILE"
fi
```

---

## Phase 4 — Finalize

### 4.1 Emit the completion signal

The orchestrator script (`planlist-runner.js`) watches stdout for this line to advance the queue and update `planlist.csv`. Print it as the **very last line of output** — success or failure, no exceptions.

**Format:**

```
<plan_path> [PLANO_CONCLUIDO] error=<0|1> pr=<pr_url>
```

| Field | Value |
|-------|-------|
| `<plan_path>` | Exact plan path received as input |
| `error` | `0` = completed without errors; `1` = errors occurred |
| `<pr_url>` | PR URL from Phase 3.4, or empty string if PR creation failed |

Examples:

```
# Success
docs/superpowers/plans/2026-05-27-example-create-file.md [PLANO_CONCLUIDO] error=0 pr=https://github.com/org/repo/pull/42

# With errors
docs/superpowers/plans/2026-05-27-example-create-file.md [PLANO_CONCLUIDO] error=1 pr=https://github.com/org/repo/pull/42

# With errors and no PR URL
docs/superpowers/plans/2026-05-27-example-create-file.md [PLANO_CONCLUIDO] error=1 pr=
```

**Do not call `update-plan.js` here.** CSV state is managed exclusively by the orchestrator — it reads the fields from this signal and calls `update-plan.js` itself. The skill's only responsibility is to emit the signal with accurate `error` and `pr` values.

---

## Error Handling Reference

| Situation | Action |
|-----------|--------|
| Plan step fails or instruction unclear | Skip step, capture error, continue |
| `executing-plans` blocks on a blocker | Capture error, skip to Phase 3 with `error=1` |
| No uncommitted changes after plan | Skip commit step |
| Push hook fails (attempt 1–3) | Fix root cause and retry |
| Push hook fails (attempt 4+) | Capture as error, continue to Phase 3.4 |
| PR creation fails | Capture as error, continue without `$PR_URL` |
| Any unrecoverable situation | Open PR with error comment → emit signal with `error=1` |

---

## Execution Flow

```
Receive <plan_path>
  └─► git checkout develop (if not already there)
        └─► git checkout -b <slug>
              └─► superpowers:executing-plans
                    └─► git add + commit (if uncommitted changes remain)
                          └─► git push (fix hooks up to 3x on failure)
                                └─► gh pr create / edit (with error block if needed)
                                      └─► print <plan_path> [PLANO_CONCLUIDO] error=<0|1> pr=<url>
```
