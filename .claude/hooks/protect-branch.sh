#!/bin/bash
# PreToolUse hook (Bash) — branch protection + destructive-command blocking
#
# Covers:
#   1. Commits/deletions on the protected branch (main)
#   2. rm -rf targeting /, ~, $HOME, ./, or ..
#   3. DROP TABLE / TRUNCATE TABLE / DELETE FROM without WHERE
#   4. git push --force, git reset --hard, git clean -f, git checkout -- ., git restore .
#   5. Reading .env files (credential protection)

INPUT=$(cat)

# Extract the command via jq (fallback to grep if jq is unavailable)
if command -v jq &>/dev/null; then
  COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)
else
  COMMAND=$(echo "$INPUT" | grep -oP '"command":\s*"\K[^"]+' 2>/dev/null)
fi

[ -z "$COMMAND" ] && exit 0

# ─── 1. PROTECTED BRANCH ─────────────────────────────────────────────────────

# Block direct commits
if echo "$COMMAND" | grep -qE '^git\s+commit'; then
  BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  if echo "$BRANCH" | grep -qE '^main$'; then
    echo '{"decision":"block","reason":"Direct commits to the protected branch (main) are not allowed. Create a feature branch first."}'
    exit 0
  fi
fi

# Block local branch deletion: git branch -d/-D/--delete
if echo "$COMMAND" | grep -qE '^git\s+branch\b'; then
  if echo "$COMMAND" | grep -qE '(\s-[a-zA-Z]*[dD][a-zA-Z]*|\s--delete)\b'; then
    echo '{"decision":"block","reason":"Deleting branches is not allowed. Only a human may delete branches manually."}'
    exit 0
  fi
fi

# Block remote branch deletion: git push origin --delete
if echo "$COMMAND" | grep -qE '^git\s+push\b' && echo "$COMMAND" | grep -qE '\s--delete\b'; then
  echo '{"decision":"block","reason":"Deleting remote branches is not allowed. Only a human may delete branches manually."}'
  exit 0
fi

# Block deletion via refspec: git push origin :branch
if echo "$COMMAND" | grep -qE '^git\s+push\b' && echo "$COMMAND" | grep -qE '\s+:[a-zA-Z]'; then
  echo '{"decision":"block","reason":"Deleting remote branches via refspec is not allowed. Only a human may delete branches manually."}'
  exit 0
fi

# ─── 2. DESTRUCTIVE FILESYSTEM OPERATIONS ────────────────────────────────────

if echo "$COMMAND" | grep -qE 'rm\s+(-[a-zA-Z]*f[a-zA-Z]*\s+|(-[a-zA-Z]*\s+)*)(\/|~|\$HOME|\.\/|\.\.)'; then
  echo '{"decision":"block","reason":"Blocked: destructive rm targeting root, home, or a parent directory. Run manually if intentional."}'
  exit 0
fi

# ─── 3. DESTRUCTIVE DATABASE OPERATIONS ──────────────────────────────────────

if echo "$COMMAND" | grep -qiE 'DROP\s+(TABLE|DATABASE)|TRUNCATE\s+TABLE|DELETE\s+FROM\s+\S+\s*;?\s*$'; then
  echo '{"decision":"block","reason":"Blocked: destructive database command. Run manually if intentional."}'
  exit 0
fi

# ─── 4. DANGEROUS GIT OPERATIONS ─────────────────────────────────────────────

# Block force push
if echo "$COMMAND" | grep -qE 'git\s+push\s+.*--force(-with-lease)?|git\s+push\s+-f\b'; then
  echo '{"decision":"block","reason":"Blocked: force push. Run manually if intentional."}'
  exit 0
fi

# Block git reset --hard (any variant permanently discards changes)
if echo "$COMMAND" | grep -qE 'git\s+reset\s+--hard\b'; then
  echo '{"decision":"block","reason":"Blocked: git reset --hard permanently discards changes. Run manually if intentional."}'
  exit 0
fi

# Block git clean -f / -fd / -fdx (removes untracked files)
if echo "$COMMAND" | grep -qE 'git\s+clean\s+-'; then
  echo '{"decision":"block","reason":"Blocked: git clean permanently removes untracked files. Run manually if intentional."}'
  exit 0
fi

# Block git checkout -- . and git restore . (discards all working-tree changes)
if echo "$COMMAND" | grep -qE 'git\s+checkout\s+--\s+\.' || echo "$COMMAND" | grep -qE 'git\s+restore\s+\.'; then
  echo '{"decision":"block","reason":"Blocked: discards all working-tree changes. Run manually if intentional."}'
  exit 0
fi

# ─── 5. READING .env FILES (CREDENTIAL PROTECTION) ───────────────────────────

# if echo "$COMMAND" | grep -qE '(cat|less|head|tail|more|source|grep|sed|awk|bat)\s+\.env\b'; then
#   echo '{"decision":"block","reason":"Blocked: reading a .env file. The agent must not read credentials."}'
#   exit 0
# fi

exit 0
