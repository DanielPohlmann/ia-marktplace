#!/bin/bash
# PostToolUse hook (Grep|Bash) — detects truncated tool results
#
# Claude Code truncates tool results > 50K chars to a 2KB preview.
# The agent gets a warning but doesn't always act on it.
# This hook injects an explicit context note to force the correct follow-up.

INPUT=$(cat)

TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)

# Extract the tool response (string or object)
TOOL_RESPONSE=$(echo "$INPUT" | jq -r '
  if (.tool_response | type) == "string" then .tool_response
  elif (.tool_response | type) == "object" then (.tool_response | tostring)
  else empty
  end
' 2>/dev/null)

# Detect the truncation marker
if echo "$TOOL_RESPONSE" | grep -q "Output too large"; then
  echo '{"additionalContext": "WARNING: the tool result was truncated to a 2KB preview. The full output was saved to disk. Read the full file at the given path before acting on these results, or re-run with a narrower scope (specific directory, more precise pattern)."}'
  exit 0
fi

exit 0
