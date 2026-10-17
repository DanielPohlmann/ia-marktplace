<!-- Part of the tools-git skill. Loaded on demand from SKILL.md. -->

# Git — details

## Configuration

Set up Git globally after installation. These settings live in `~/.gitconfig`:

```bash
# Identity
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Line endings (critical for cross-platform teams)
git config --global core.autocrlf input    # macOS/Linux
git config --global core.autocrlf true     # Windows

# Default branch name
git config --global init.defaultBranch main

# Pull strategy
git config --global pull.rebase true       # Rebase instead of merge on pull

# Useful aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD --stat"
git config --global alias.unstage "reset HEAD --"
```

Verify your configuration:

```bash
git config --list --show-origin
```

## Branching Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| **Trunk-Based Development** | Short-lived feature branches (hours to a few days), merge to `main` frequently. Often paired with feature flags. | Teams practicing CI/CD, high-velocity delivery |
| **Gitflow** | Long-lived `develop` branch plus `feature/*`, `release/*`, and `hotfix/*` branches. Structured and formal. | Teams with scheduled releases, enterprise projects |
| **GitHub Flow** | Feature branches off `main`, open a PR, code review, merge. Simple and effective. | Small to mid-size teams, continuous deployment |
| **GitLab Flow** | Environment branches (`main` -> `staging` -> `production`). Merges promote code through environments. | Teams needing environment tracking and approvals |

> **Modern default:** Trunk-based development is the recommended approach for most teams today. It reduces merge conflicts, encourages small incremental changes, and aligns with continuous integration and delivery practices.

## Conflict Resolution

When Git cannot automatically merge changes, it marks conflicts in the affected files:

### Step-by-Step

1. **Identify conflicted files:**
   ```bash
   git status    # Lists files with "both modified" status
   ```

2. **Open the file and understand the conflict markers:**
   ```
   <<<<<<< HEAD
   // Your changes on the current branch
   const timeout = 5000;
   =======
   // Their changes from the incoming branch
   const timeout = 10000;
   >>>>>>> feature/update-timeout
   ```

3. **Decide which changes to keep** (yours, theirs, or a combination). Edit the file to the correct final state and remove all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

4. **Stage the resolved file and continue:**
   ```bash
   git add src/config.js
   git commit                            # For merge conflicts
   # or
   git rebase --continue                 # For rebase conflicts
   ```

**Merge tools** can simplify visual conflict resolution:

```bash
git mergetool                            # Launch configured merge tool
git config --global merge.tool vscode    # Set VS Code as merge tool
```

## Git Hooks

Git hooks are scripts that run automatically at specific points in the Git workflow. They live in `.git/hooks/`.

| Hook | Trigger | Common Use |
|------|---------|------------|
| `pre-commit` | Before a commit is created | Linting, formatting, running quick tests |
| `commit-msg` | After commit message is written | Validate conventional commit format |
| `pre-push` | Before push to remote | Run full test suite, check for secrets |
| `prepare-commit-msg` | Before editor opens for message | Insert template, branch name, or ticket number |
| `post-merge` | After a merge completes | Install dependencies, rebuild |
| `pre-rebase` | Before rebase starts | Warn if rebasing published branch |

### Example: pre-commit Hook

```bash
#!/bin/sh
# .git/hooks/pre-commit

# Run linter
npm run lint
if [ $? -ne 0 ]; then
    echo "Linting failed. Fix errors before committing."
    exit 1
fi

# Check for debug statements
if grep -rn "console.log\|debugger\|binding.pry" --include="*.js" --include="*.ts" --include="*.rb" src/; then
    echo "Debug statements found. Remove them before committing."
    exit 1
fi
```

> **Husky** is the standard tool for managing Git hooks in Node.js projects. It lets you define hooks in `package.json` or `.husky/` and ensures all team members run the same hooks.

## .gitignore

The `.gitignore` file tells Git which files and directories to exclude from tracking.

### Pattern Syntax

```gitignore
# Comments start with #
*.log              # Ignore all .log files
!important.log     # But DO track this specific one
/build/            # Ignore build directory at repo root only
**/temp/           # Ignore temp directory at any depth
doc/**/*.pdf       # Ignore PDFs inside doc/ recursively
```

### Common Entries by Platform

```gitignore
# Dependencies
node_modules/
vendor/
.venv/
__pycache__/

# Build output
dist/
build/
bin/
obj/
*.dll
*.exe
*.o

# Environment and secrets
.env
.env.local
*.pem
credentials.json

# OS files
.DS_Store
Thumbs.db
Desktop.ini

# IDE files
.vscode/settings.json
.idea/
*.suo
*.user
*.swp
*~
```

### Global Gitignore

Set a global ignore file for files that should never be tracked on any repo on your machine:

```bash
git config --global core.excludesFile ~/.gitignore_global
```

Add OS-specific junk (`.DS_Store`, `Thumbs.db`) and editor temp files to the global file.

## Conventional Commits

A lightweight convention for writing structured commit messages that can be parsed by tooling:

### Format

```
type(scope): description

[optional body]

[optional footer(s)]
```

### Types

| Type | Purpose |
|------|---------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Formatting, white-space, semicolons (no logic change) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or correcting tests |
| `build` | Changes to build system or external dependencies |
| `ci` | Changes to CI configuration files and scripts |
| `chore` | Maintenance tasks, dependency bumps, tooling |

### Examples

```
feat(auth): add OAuth2 login with Google provider
fix(api): handle null response from payment gateway
docs(readme): add setup instructions for local development
refactor(db): extract connection pooling into separate module
test(auth): add integration tests for token refresh flow
build(deps): bump lodash from 4.17.20 to 4.17.21
ci(github): add CodeQL security scanning workflow
chore: update .gitignore for Python virtual environments
```

> Adding `!` after the type (e.g., `feat!: ...`) or including `BREAKING CHANGE:` in the footer signals a breaking change, which tools like `semantic-release` use to trigger major version bumps.
