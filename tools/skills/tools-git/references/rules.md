# Git Rules

Best practices and rules for Git.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Commit early and often. | MEDIUM | [`git-commit-early-and-often.md`](git-commit-early-and-often.md) |
| 2 | Write meaningful commit messages. | MEDIUM | [`git-write-meaningful-commit-messages.md`](git-write-meaningful-commit-messages.md) |
| 3 | Never force push to shared branches. | CRITICAL | [`git-never-force-push-to-shared-branches.md`](git-never-force-push-to-shared-branches.md) |
| 4 | Use .gitignore from day one. | CRITICAL | [`git-use-gitignore-from-day-one.md`](git-use-gitignore-from-day-one.md) |
| 5 | Learn reflog for recovery. | MEDIUM | [`git-learn-reflog-for-recovery.md`](git-learn-reflog-for-recovery.md) |
| 6 | Rebase local branches before merging. | HIGH | [`git-rebase-local-branches-before-merging.md`](git-rebase-local-branches-before-merging.md) |
| 7 | Sign commits in sensitive repositories. | MEDIUM | [`git-sign-commits-in-sensitive-repositories.md`](git-sign-commits-in-sensitive-repositories.md) |
| 8 | Review diffs before committing. | CRITICAL | [`git-review-diffs-before-committing.md`](git-review-diffs-before-committing.md) |

---

---
title: "Commit early and often."
impact: MEDIUM
impactDescription: "general best practice"
tags: git, tools, version-control, branching
---

## Commit early and often.

Small, focused commits are easier to review, revert, and bisect than large monolithic ones. Each commit should represent a single logical change.

---

---
title: "Learn reflog for recovery."
impact: MEDIUM
impactDescription: "general best practice"
tags: git, tools, version-control, branching
---

## Learn reflog for recovery.

Reflog is your undo history. Before panicking about a bad rebase or reset, check `git reflog` — the original commits are almost certainly still there.

---

---
title: "Never force push to shared branches."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: git, tools, version-control, branching
---

## Never force push to shared branches.

Force pushing rewrites history and can destroy teammates' work. Use `--force-with-lease` if you must, and only on your own feature branches.

---

---
title: "Rebase local branches before merging."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: git, tools, version-control, branching
---

## Rebase local branches before merging.

Rebase your feature branch onto the latest `main` before creating a merge or pull request. This results in a clean, linear history and avoids unnecessary merge commits.

---

---
title: "Review diffs before committing."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: git, tools, version-control, branching
---

## Review diffs before committing.

Always run `git diff --staged` before committing to verify you are committing exactly what you intend. Catching stray debug statements or unrelated changes at this stage saves time.

---

---
title: "Sign commits in sensitive repositories."
impact: MEDIUM
impactDescription: "general best practice"
tags: git, tools, version-control, branching
---

## Sign commits in sensitive repositories.

Use GPG or SSH signing (`git config --global commit.gpgsign true`) for repositories where commit authorship integrity matters.

---

---
title: "Use .gitignore from day one."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: git, tools, version-control, branching
---

## Use .gitignore from day one.

Add it as the first file in any new repository. Include dependencies, build output, secrets, and OS artifacts. Use templates from gitignore.io or GitHub's collection.

---

---
title: "Write meaningful commit messages."
impact: MEDIUM
impactDescription: "general best practice"
tags: git, tools, version-control, branching
---

## Write meaningful commit messages.

The subject line should explain *what* changed and *why* in imperative mood ("Add auth module", not "Added auth module" or "Adding auth module"). Use the body for context when needed.
