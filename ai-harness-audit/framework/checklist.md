# Audit Checklist — detailed criteria per dimension

Score each dimension **✓✓ strong · ✓ ok · ⚠ weak/blocked · ✗ missing** (see `scoring-rubric.md`).
Tag each fix **`cheap`** (deterministic, do first) or **`deeper`** / **`gated`**.
For the *why* behind every criterion, see `principles.md`.

## Claude Code surface map — walk every surface (don't skip any)

A generic harness model (contract/skills/guides/sensors/enforcement/memory/improvement) silently
misses **Claude-Code-specific surfaces**. Before scoring, confirm each surface below was inspected;
an un-walked surface is a coverage gap, not an implicit pass.

| Surface | Where it lives | Dimension |
|---|---|---|
| Contract | `CLAUDE.md`, `.claude/rules/` | 1 |
| Skills | `.claude/skills/` or plugin | 2 |
| Subagents | `.claude/agents/`, plugin agents | 2 |
| Commands | `.claude/commands/`, plugin commands | 2 |
| Guides / docs | conventions, codebase docs | 3 |
| Tests / linters / CI | test projects, pipelines | 4 |
| Hooks | `.claude/settings.json` hooks | 5 |
| **Permissions** | `permissions.allow/ask/deny` in settings | 5 |
| Memory & state | `MEMORY.md`/`KNOWLEDGE.md`, state files | 6 |
| Improvement loop | lessons, evals, drift | 7 |
| **MCP / external tools** | `.mcp.json` servers | 8 |
| **Loops** | `/loop` recurring tasks | 8 |
| **Schedules / Routines** | `/schedule`, cron tools, `CLAUDE_CODE_DISABLE_CRON` | 8 |
| **Workflows** | Workflow tool, `.claude/workflows/` | 8 |
| **Headless / CI agent** | SDK, GitHub Actions / pipeline agent | 8 |

---

## 1. The Contract — `CLAUDE.md` (and `AGENTS.md`, `.cursor/rules`)

**Criteria**
- Exists at repo root and actually loads (not empty).
- Contains **hard constraints** — explicit *always / never* rules, not vibes.
- **Under ~200 lines.** It is always-on; every line taxes every turn.
- Holds *facts and rules*, not long how-to procedures (those belong in skills/scripts).
- States the build / test / run commands (or points to a one-command script).
- **Smell:** a section that has grown into a multi-step procedure → extract to a skill or `scripts/`.
- **Layering:** when rules grow, split into `.claude/rules/*.md` with `paths` frontmatter —
  *specific overrides general, like CSS specificity.*
- **Provenance:** every path/reference in the contract must resolve in the checkout it ships in
  (no dangling `../` pointers to repos/docs that aren't present).

**Fixes:** scaffold a 6-line Must-always / Must-never contract `cheap`; move how-to into a skill
`deeper`; split language/dir rules into `.claude/rules/` `deeper`; remove/guard dangling refs `cheap`.

---

## 2. Skills — `.claude/skills/` (local or plugin-delivered)

**Criteria**
- At least one skill captures a repeated expertise (explained twice → it should exist).
- Each `description` says **WHEN to use** (third person, triggers/symptoms) — NOT what it does.
- Names are gerund / verb-first, lowercase-hyphen; no "claude"/"anthropic".
- No duplicated/overlapping descriptions (the model can't pick the right one).
- **Robust anatomy** for non-trivial skills (progressive disclosure): lean `SKILL.md`
  orchestrator + `references/` (dominant supporting folder) + `scripts/` (deterministic steps),
  `templates/`, `rules/` as needed. **Keep the checklist inline** in SKILL.md.
- SKILL.md body roughly < 500 lines (split into `references/` past that).
- **Degrees of freedom match fragility:** narrow/fragile task → exact steps; open task → direction.
- **Plugin-delivered skills are in scope — assess their content.** If expertise ships via a
  shared plugin/marketplace repo, that repo is part of the harness: read and score its skills on the
  same criteria (descriptions, anatomy, evals/CI, versioning). Do not treat it as a black box.
- **Reproducible, pinned delivery.** Separately assess *how* the skills reach the agent. A consumer
  that enables a marketplace with **auto-update and no version pin** tracks a moving target — two
  developers (or two days) may run different harness logic. Flag unpinned/auto-update delivery and
  the absence of release tags as a **determinism gap**, even when the skills themselves are excellent.
- **The harness guards itself.** The plugin repo should have its *own* sensors — skill linting,
  description/index checks, evals — that actually run (registered CI, not just defined YAML), and
  ideally cover more than one flagship skill.

**Fixes:** rewrite a what-it-does description into when-to-use `cheap`; split a monolith SKILL.md
into `references/` `deeper`; move exact/repeatable steps into `scripts/` `deeper`.

---

## 3. Guides — feedforward (steer *before*)

**Criteria**
- Conventions / style documented (in CLAUDE.md or `rules/`).
- Specs or task docs exist for non-trivial work.
- Architecture notes the agent can actually follow.
- Domain glossary where the domain language is non-obvious.
- The guides are **reachable from where the agent starts** (linked from the contract, not orphaned).
- **No contract drift** — the contract must not reference a **deprecated tool/convention** (e.g. an
  abandoned workspace-planning layout). A pointer to a dead convention is worse than no pointer: it
  sends the agent chasing artifacts that no longer exist.
- **Generated docs belong in an outputs directory, not the contract.** Codebase scans / cross-repo
  maps produced by tooling are *outputs* — keep them in the designated (often gitignored) AI-artifacts
  directory, not hand-committed and not referenced from the contract via paths that can rot.

**Fixes:** add a short conventions block `cheap`; add an architecture note `deeper`.

---

## 4. Sensors — feedback (check *after*)

**Criteria**
- Tests exist and run with **one command**.
- Linter + formatter configured; type-checker (if a typed language).
- CI runs the checks (`.github/workflows/`, Azure Pipelines, etc.) — recognise *all* CI systems,
  not just GitHub Actions.
- **Computational present, not only inferential** — fast deterministic controls before slow ones.
  *Start cheap.*
- **Shift-left ("keep quality left")** — cheap controls pre-commit / before the agent acts;
  expensive ones (mutation testing, deep review) post-integration in CI.
- **Coverage across the three regulation categories:**
  - *Maintainability* — style, complexity, duplication, coverage.
  - *Architecture fitness* — fitness functions / structural tests (ArchUnit, dep-cruiser,
    layer tests) enforcing module boundaries.
  - *Behaviour / correctness* — the hardest; don't blindly trust AI-generated tests.
- **Agent-friendly output** — error/CI messages tell the agent *how to fix it*
  ("a positive kind of prompt injection").
- **Sensors don't fire on noise** — a sensor that triggers on generated/uncommitted artifacts
  every run trains the agent to ignore it.
- **Balance** — not feedforward-only (rules, never verified) nor feedback-only (checks, no guidance).

**Fixes:** state the lint/test command in CLAUDE.md `cheap`; wrap a one-command runner `deeper`;
make a key error message instruct the fix `cheap`; add structural tests for module boundaries
`deeper`; add a CI workflow `deeper`.

---

## 5. Enforcement & Permissions — hooks + the permission model

**Criteria — hooks**
- `PreToolUse` hook(s) for hard guarantees — block destructive git/SQL/filesystem ops, lint-on-edit.
- Guardrails are **hooks, not just prose** ("a rule is only hard if a hook blocks it").
- **Scope covers the path that matters** — a guard matched on `Bash` only is bypassable via
  `Edit`/`Write`/`MultiEdit`/`Read`; match the tools the risk actually flows through.
- **No dead enforcement** — commented-out / disabled guards are documented, not silently rotting.
- **Hooks are correct** — they don't false-positive/loop, and they use the current decision idiom
  (`hookSpecificOutput.permissionDecision: allow|deny|ask`), not only legacy `decision:block`.

**Criteria — permissions (Claude Code's primary guardrail)**
- A **`permissions` posture exists** in `settings.json` (not left fully default).
- **`deny` protects secrets and configs by path** — `Read(./.env*)`, `Read(./secrets/**)`,
  `Edit(.claude/**)`, lint/test configs — so the agent can't read secrets or weaken its own checks.
- **`allow`** covers common safe ops (fewer prompts); **`ask`** gates the risky-but-sometimes-needed.
- **Org-level enforcement** — critical rules live in **managed settings**
  (`allowManagedPermissionRulesOnly`) so user/project scopes can't override them; remember `deny`
  beats `allow` and rules **merge** across scopes.
- **Config-protection** — the agent cannot quietly weaken a linter/formatter/test config (via `deny`
  or a hook).

**Fixes:** add `permissions.deny` for secrets/configs `cheap`; re-enable a disabled guard `cheap`;
broaden a `Bash`-only hook to `Edit|Write` `deeper`; move critical rules to managed settings `deeper`.

---

## 6. Memory & State

**Criteria** *(only **shared, repository-level** memory/state is in scope — personal memory stores
held in a user profile are out of scope as non-reproducible; see METHODOLOGY §Scope)*
- **Shared memory** — durable decisions/progress committed to the repo (`MEMORY.md`/`KNOWLEDGE.md`,
  decision logs, ADRs) that survive context resets *for the whole team*.
- **State** — long-task progress tracked in a committed `STATE.md`/progress file (plan mode +
  artifact); guards against "starts too much / stops too early / loses context between sessions".
- **Secrets never land in memory.**
- Bonus: `SessionStart` / `PreCompact` hooks save & restore state across compaction.

**Fixes:** add a `MEMORY.md` the agent reads/writes `cheap`; add a progress/STATE file for long work `cheap`.

---

## 7. Improvement loop — does the harness get better?

**Criteria**
- A **ritual to encode fixes**: when the agent fails, the gap becomes a CLAUDE.md rule, a new
  skill, or a hook (*fail → fix the file → never again*).
- The loop has a **defined storage location and review path** that does not conflict with how the
  org reviews changes (e.g. harness changes vs code changes).
- Skills have **evals** (scenarios that prove they work) — or at least the author tests them
  (Claude-A writes / Claude-B uses).
- **Drift monitoring** — recurring checks for dead code, stale tests, dependency vulns *outside*
  the change lifecycle.
- The harness is treated as an **ongoing engineering practice**, not a one-time config.

**Fixes:** add a "learnings"/decisions log the agent updates after mistakes `cheap`; resolve the
storage/review-path conflict `gated`; add 2–3 eval scenarios for a key skill `deeper`;
schedule a drift scan `deeper`.

---

## 8. Tooling, Automation & Orchestration

The agent's reach beyond a single interactive session — external tools and scheduled/orchestrated runs.

**Criteria — external tools (MCP)**
- `.mcp.json` servers are **inventoried and justified** — each one is needed.
- **Least privilege** — servers expose only the scope required; write/admin access is intentional.
- **Pinned, not `@latest`** — `npx … @latest` server commands are the same non-determinism /
  supply-chain risk as an unpinned plugin; pin versions.
- Auth/secrets for servers are handled safely (not hard-coded, not world-readable).

**Criteria — automation & orchestration**
- **Scheduled work** (`/schedule` routines / cron) — recurring checks (drift scans, dependency
  audits, PR triage) that run *outside* the change lifecycle exist where valuable; or their absence is
  a conscious choice, not an oversight. (`CLAUDE_CODE_DISABLE_CRON` state noted.)
- **Workflows** (`.claude/workflows/`, Workflow tool) — repeatable multi-agent orchestrations are
  captured as artifacts, not improvised each time, where the team runs them.
- **Loops** (`/loop`) — recurring in-session automation used deliberately, not as a busy-wait.
- **Headless / CI agent** — if an autonomous agent runs in CI (SDK / GitHub Actions / pipeline),
  it has the same guardrails as interactive sessions (permissions, hooks); if not, note the gap.
- **Don't recommend what you didn't assess** — e.g. never recommend "scheduled drift monitoring"
  without first assessing whether scheduling is configured or available.

**Fixes:** pin MCP server versions `cheap`; add a scheduled drift/dep-audit routine `deeper`;
capture a repeated orchestration as a saved workflow `deeper`; bring the CI agent under the same
permissions/hooks `deeper`.

---

## Right tool for the job — flag misplacements

| If the repo… | it should use… |
|---|---|
| has "always do X" rules | CLAUDE.md |
| repeats a prompt / playbook | a skill (`/command`) |
| floods context with side-task output | a subagent |
| needs something every time, no judgment | a hook |
| needs to reach an external system | MCP |
| shares the same setup across repos | a plugin |

*Source: Claude Code docs — features-overview.*
