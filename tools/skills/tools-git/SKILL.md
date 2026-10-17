---
name: tools-git
description: Use when working with Git workflows, history, or hooks. USE FOR: branching strategies (Gitflow, trunk-based), merge vs rebase, conflicts, cherry-pick, bisect, stash, worktrees, lefthook and other hooks, conventional commits, history rewriting, config. DO NOT USE FOR: GitHub/GitLab platform features (PRs, Actions), Git LFS administration, containers (use tools-docker).
---

# Git

## Overview

Git is the universal version control system. Mastering it means understanding not just the commands but the model -- commits are snapshots (not diffs), branches are lightweight pointers to commits, and the staging area (index) separates what you have changed from what you intend to commit. Every operation in Git manipulates this underlying graph of commits, and once you internalize that model, even advanced operations become intuitive.

## Merge vs Rebase

| Aspect | Merge | Rebase |
|--------|-------|--------|
| History | Preserves branch topology with a merge commit | Linear, clean history — as if work happened sequentially |
| Safety | Safe for shared branches | **Dangerous on shared branches** — rewrites commit hashes |
| Conflict resolution | Resolve once at merge time | Potentially resolve at each replayed commit |
| When to use | Merging feature branches into main (public) | Cleaning up local feature branch before merging |
| Command | `git merge feature` | `git rebase main` (from feature branch) |

> **Golden Rule:** Never rebase commits that have been pushed to a shared branch. Rebasing rewrites commit history, and if others have based work on the original commits, you will create divergent histories and cause significant confusion. Rebase is for local cleanup only.

```bash
# Typical rebase workflow (local feature branch)
git switch feature/auth
git fetch origin
git rebase origin/main          # Replay your commits on top of latest main
# Resolve any conflicts at each step
git switch main
git merge feature/auth          # Now it's a clean fast-forward
```

## Best Practices

- **Commit early and often.** Small, focused commits are easier to review, revert, and bisect than large monolithic ones. Each commit should represent a single logical change.
- **Write meaningful commit messages.** The subject line should explain *what* changed and *why* in imperative mood ("Add auth module", not "Added auth module" or "Adding auth module"). Use the body for context when needed.
- **Never force push to shared branches.** Force pushing rewrites history and can destroy teammates' work. Use `--force-with-lease` if you must, and only on your own feature branches.
- **Use .gitignore from day one.** Add it as the first file in any new repository. Include dependencies, build output, secrets, and OS artifacts. Use templates from gitignore.io or GitHub's collection.
- **Learn reflog for recovery.** Reflog is your undo history. Before panicking about a bad rebase or reset, check `git reflog` — the original commits are almost certainly still there.
- **Rebase local branches before merging.** Rebase your feature branch onto the latest `main` before creating a merge or pull request. This results in a clean, linear history and avoids unnecessary merge commits.
- **Sign commits in sensitive repositories.** Use GPG or SSH signing (`git config --global commit.gpgsign true`) for repositories where commit authorship integrity matters.
- **Review diffs before committing.** Always run `git diff --staged` before committing to verify you are committing exactly what you intend. Catching stray debug statements or unrelated changes at this stage saves time.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/everyday-commands.md](references/everyday-commands.md) | Everyday Commands — Starting a Repository, Working with Changes, Branching, Working with Remotes, Inspecting History |
| [references/advanced-operations.md](references/advanced-operations.md) | Advanced Operations — Cherry-Pick, Bisect, Worktrees, Reflog, Interactive Rebase (Local Only) |
| [references/details.md](references/details.md) | Configuration; Branching Strategies; Conflict Resolution; Git Hooks; .gitignore; Conventional Commits |

## References

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book (Official)](https://git-scm.com/book/en/v2)
- [Git GitHub Repository](https://github.com/git/git)

See references/rules.md for the full rule catalog.
