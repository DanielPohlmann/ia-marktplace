#!/bin/bash
# Stop hook — verifies marketplace conventions before completing a task
#
# Runs `python scripts/verify_marketplace.py` (the same check CI runs) whenever
# a change touches marketplace content: skills, plugin manifests, the
# marketplace manifest, or the count-bearing root docs. Blocks completion on
# error; passes through untouched otherwise.

INPUT=$(cat)

# Avoid an infinite loop: if this hook already blocked and Claude fixed +
# retried, let it through.
STOP_ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active // false' 2>/dev/null)
if [ "$STOP_ACTIVE" = "true" ]; then
  exit 0
fi

# Detect modified files (staged + unstaged + untracked with content)
MODIFIED_FILES=$(git status --short 2>/dev/null | awk '{print $NF}')

# Nothing modified — nothing to verify
if [ -z "$MODIFIED_FILES" ]; then
  exit 0
fi

# Only run the validator if a marketplace-relevant path changed
if ! echo "$MODIFIED_FILES" | grep -qE '(^|/)skills/|\.claude-plugin/|^scripts/verify_marketplace\.py$|^CLAUDE\.md$|^README\.md$'; then
  exit 0
fi

if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null; then
  echo '{"additionalContext": "WARNING: no python/python3 found on PATH. Verify manually: python scripts/verify_marketplace.py"}'
  exit 0
fi

PYTHON=$(command -v python3 || command -v python)

OUTPUT=$("$PYTHON" scripts/verify_marketplace.py 2>&1)
if [ $? -ne 0 ]; then
  echo "{\"decision\": \"block\", \"reason\": \"scripts/verify_marketplace.py failed. Fix the errors below before completing the task:\n\n${OUTPUT}\"}"
  exit 2
fi

exit 0
