# Principles — the reasoning behind the checks

Cite these when explaining a finding, so the report teaches, not just grades.

## Harness Engineering (the frame)

**Agent = Model + Harness.** The model is one box; everything around it is the harness — the
part you build. Guides steer **before** the agent acts (feedforward); sensors check **after**
(feedback). *Feedback-only repeats mistakes; feedforward-only never proves it worked* — you need both.

A control is a guide or a sensor by **when it runs, not which tool**: a linter pre-commit
*guides*; post-edit it *senses*. Controls are also **computational** (fast, deterministic —
tests, linters, type-checkers) or **inferential** (LLM-as-judge, review agents — slower,
probabilistic) → **start cheap**. **"Keep quality left"**: cheap controls early, expensive ones
in CI. Three regulation categories: **maintainability**, **architecture fitness** (fitness
functions / structural tests), **behaviour** (the hardest). The harness is an **ongoing
engineering practice** — whenever an issue recurs, improve a guide or sensor so it can't recur
(the steering loop).

*— Birgitta Böckeler, "Harness Engineering", https://martinfowler.com/articles/harness-engineering.html*

## Contract & rules

`CLAUDE.md` is the always-on **contract**: short (**< ~200 lines**), hard *always/never*
constraints, **facts not how-to**. As rules grow, **layer** them (`.claude/rules/` common +
per-language; *"specific overrides general — like CSS specificity"*). **Rules tell WHAT; skills
tell HOW.** A rule is only hard if a **hook** blocks it (prose is a request); **protect configs**
so the agent can't weaken a check to pass. Every reference in the contract must resolve in the
checkout it ships in — a dangling pointer costs the agent a wasted, confused turn every time.

*— ECC, https://github.com/affaan-m/ECC*

## Skill quality & anatomy

`description` = **WHEN to use** (third person, triggers), not what it does. **Progressive
disclosure**: a lean `SKILL.md` orchestrator + `references/` (the dominant supporting folder
across the most-installed skills); keep the **checklist inline**. Match degrees of freedom to
fragility (narrow bridge = exact steps; open field = direction). Be concise — only encode what
the model can't guess. Build **evals first**; iterate with the Claude-A-writes / Claude-B-uses loop.

*— Anthropic Agent Skills best practices (platform.claude.com/docs/.../agent-skills/best-practices).*

## When to use what (right tool for the job)

wrong-twice → **CLAUDE.md** · same prompt/playbook → **skill** (`/command`) · floods context →
**subagent** · every-time-no-judgment → **hook** · reach external system → **MCP** · another repo
needs it → **plugin**.

*— Claude Code docs, https://code.claude.com/docs/en/features-overview*

## Governance of the harness itself

The harness is software, and like software it needs a **review path and an owner**. When the
artifacts that *steer the agent* (skills, lessons, the contract) live in a different review lane
than the *application code*, mixing them in one change request breaks both reviews. Decide
explicitly: where do harness artifacts live, who reviews them, and how does an improvement
captured mid-task reach that lane without polluting a code change. An improvement loop whose
storage location contradicts the org's review model will silently never run.

## The full expert setup (what "good" looks like)

A mature harness is layered: **Contract · Skills · Guides · Sensors · Memory · State ·
Improvement loop.** Build the contract + one skill first; the rest is the same move — *notice a
gap, encode it.* Memory survives context resets; state tracks long tasks; the improvement loop
makes the setup get better when it fails.

## Proof it matters

Stripe's coding agents merge 1,300+ PRs/week, ~70% accepted unmodified — not because the model
got smarter, because the **harness** did (sandboxes, permissions, checks, clean context). A good
harness directs human input to where it matters most, rather than eliminating it.
