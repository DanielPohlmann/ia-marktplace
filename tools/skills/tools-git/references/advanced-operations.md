<!-- Part of the tools-git skill. Loaded on demand from SKILL.md. -->

# Advanced Operations

## Cherry-Pick

Apply specific commits from one branch to another without merging the entire branch:

```bash
git cherry-pick abc1234                  # Apply a single commit
git cherry-pick abc1234 def5678          # Apply multiple commits
git cherry-pick abc1234 --no-commit      # Apply changes but don't commit (stage only)
```

## Bisect

Binary search to find the commit that introduced a bug:

```bash
git bisect start
git bisect bad                           # Current commit is broken
git bisect good v1.0.0                   # This tag/commit was known good

# Git checks out a midpoint commit. Test it, then:
git bisect good                          # If this commit works
git bisect bad                           # If this commit is broken

# Repeat until Git identifies the first bad commit
# When done:
git bisect reset                         # Return to original branch
```

Automate bisect with a test script:

```bash
git bisect start HEAD v1.0.0
git bisect run ./test-script.sh          # Script exits 0 for good, 1 for bad
```

## Worktrees

Work on multiple branches simultaneously without stashing or switching:

```bash
# Create a new worktree for a branch
git worktree add ../hotfix-branch hotfix/urgent-fix

# List all worktrees
git worktree list

# Remove a worktree when done
git worktree remove ../hotfix-branch
```

## Reflog

The reflog records every change to HEAD. It is your safety net for recovering "lost" commits:

```bash
# View reflog
git reflog

# Recover a "lost" commit after a bad reset or rebase
git reflog
# Find the commit hash you want to return to
git reset --hard abc1234

# Recover a deleted branch
git reflog
git branch recovered-branch abc1234
```

> The reflog keeps entries for approximately 90 days by default. If you made a mistake, you almost certainly can recover from it.

## Interactive Rebase (Local Only)

Squash, reorder, edit, or drop commits before pushing:

```bash
# Rebase the last 4 commits interactively
git rebase -i HEAD~4
```

In the editor, change `pick` to:
- `squash` (or `s`) — combine with previous commit
- `reword` (or `r`) — change commit message
- `edit` (or `e`) — pause to amend the commit
- `drop` (or `d`) — remove the commit entirely

> Only use interactive rebase on commits that have **not** been pushed to a shared branch.
