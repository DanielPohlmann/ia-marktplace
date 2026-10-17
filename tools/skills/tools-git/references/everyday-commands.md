<!-- Part of the tools-git skill. Loaded on demand from SKILL.md. -->

# Everyday Commands

## Starting a Repository

```bash
# Create a new repository
git init my-project
cd my-project

# Clone an existing repository
git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git          # SSH
git clone --depth 1 https://github.com/user/repo.git  # Shallow clone (latest commit only)
```

## Working with Changes

```bash
# Check status of working directory and staging area
git status
git status -s                        # Short format

# View changes
git diff                             # Unstaged changes
git diff --staged                    # Staged changes (about to be committed)
git diff HEAD                        # All changes since last commit

# Stage changes
git add file.txt                     # Stage a specific file
git add src/                         # Stage an entire directory
git add -p                           # Interactively stage hunks (partial file staging)

# Commit
git commit -m "feat: add user authentication"
git commit -am "fix: correct null check"   # Stage tracked files + commit in one step

# Undo changes
git restore file.txt                 # Discard unstaged changes to a file
git restore --staged file.txt        # Unstage a file (keep changes in working directory)

# Stash work in progress
git stash                            # Save current changes
git stash push -m "WIP: auth feature"  # Save with a description
git stash list                       # View all stashes
git stash pop                        # Apply most recent stash and remove it
git stash apply stash@{2}            # Apply a specific stash (keep it in the list)
git stash drop stash@{0}             # Remove a specific stash
git stash clear                      # Remove all stashes
```

## Branching

```bash
# List branches
git branch                           # Local branches
git branch -r                        # Remote branches
git branch -a                        # All branches

# Create and switch
git branch feature/auth              # Create a branch
git switch feature/auth              # Switch to it (modern)
git switch -c feature/auth           # Create and switch in one step
git checkout -b feature/auth         # Older equivalent

# Delete branches
git branch -d feature/auth           # Delete (only if merged)
git branch -D feature/auth           # Force delete (even if not merged)

# Merge
git switch main
git merge feature/auth               # Merge feature into main
git merge --no-ff feature/auth       # Force a merge commit (no fast-forward)

# Rebase
git switch feature/auth
git rebase main                      # Replay feature commits on top of main
```

## Working with Remotes

```bash
# View remotes
git remote -v

# Fetch latest changes (does NOT modify working directory)
git fetch origin
git fetch --all                      # Fetch from all remotes

# Pull (fetch + merge/rebase)
git pull                             # Fetch and merge (or rebase if configured)
git pull --rebase                    # Explicitly rebase on pull

# Push
git push origin main
git push -u origin feature/auth      # Push and set upstream tracking
git push --force-with-lease          # Safe force push (fails if remote has new commits)

# Add a remote
git remote add upstream https://github.com/original/repo.git
```

## Inspecting History

```bash
# Log
git log                              # Full log
git log --oneline                    # Compact one-line format
git log --oneline --graph --all      # Visual branch graph
git log --since="2 weeks ago"        # Time-based filter
git log --author="Alice"             # Filter by author
git log -- path/to/file.txt          # History of a specific file

# Show a specific commit
git show abc1234

# Blame — who changed each line
git blame src/app.py
git blame -L 10,20 src/app.py       # Blame specific line range

# Diff between branches
git diff main..feature/auth
git diff main...feature/auth         # Changes since branch diverged
```
