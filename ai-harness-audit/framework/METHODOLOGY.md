# Audit Methodology

> **Framework version 1.0.** The version of *the method* (dimensions, checklist, rubric). Every
> audit pins the version it ran against — see the Changelog at the bottom. Bump on any material
> change to dimensions/criteria/rubric. Distinct from a *report's* own revision (the cover `Version`).

## The frame — Agent = Model + Harness

The model is one fixed box; everything around it is the **harness**, the part you engineer.
Controls in the harness are either:

- **Guides (feedforward)** — steer *before* the agent acts: the contract, conventions, skills,
  architecture notes. *Feedforward-only never proves it worked.*
- **Sensors (feedback)** — check *after* the agent acts: tests, linters, type-checkers, CI,
  review agents. *Feedback-only repeats the same mistake until something catches it.*

A control is a guide or a sensor by **when it runs**, not which tool it is (a linter pre-commit
*guides*; the same linter post-edit *senses*). Controls are also **computational** (fast,
deterministic — tests, linters, type-checks) or **inferential** (slower, probabilistic —
LLM-as-judge, review agents). **Start cheap:** prefer computational controls first.

*Source: Birgitta Böckeler, "Harness Engineering", martinfowler.com.*

## The eight dimensions

| # | Dimension | Question it answers |
|---|-----------|---------------------|
| 1 | **Contract** | Is there a lean, always-on set of hard rules (CLAUDE.md)? |
| 2 | **Skills** | Is repeated expertise captured, with WHEN-to-use descriptions? |
| 3 | **Guides** (feedforward) | Are conventions, specs, and architecture documented to steer *before*? |
| 4 | **Sensors** (feedback) | Do tests/linters/CI catch problems *after*, cheaply and deterministically? |
| 5 | **Enforcement & Permissions** | Are hard guarantees actual hooks **and** a `permissions` allow/ask/deny posture — scoped to the path that matters? |
| 6 | **Memory & State** | Does knowledge survive context resets; is long-task progress tracked? |
| 7 | **Improvement loop** | When the agent fails, does the harness get better (fail → encode → never again)? |
| 8 | **Tooling, Automation & Orchestration** | Are MCP/external tools least-privilege & pinned; are loops, schedules/routines, workflows, and any headless/CI agent assessed (and guarded)? |

Walk the full **Claude Code surface map** in `checklist.md` before scoring — an un-walked surface
(MCP, permissions, schedules, workflows, CI agent) is a coverage gap, not an implicit pass.

## Scope — reproducibility & impartiality

An audit must be **reproducible** (another auditor reaches the same conclusions from the same
artifacts) and **impartial** (conclusions rest on observable evidence, not on the auditor's
recollection or on verbal/organizational context). Three rules follow:

1. **Assess only what is observable in the repository and its declared dependencies.** Per-user,
   non-shared configuration is **out of scope** because it is not reproducible across the team:
   - personal/local settings (e.g. `settings.local.json`),
   - personal memory stores and work-notes held in a user profile,
   - anything created at runtime in one developer's environment but not committed.

   List excluded items explicitly in the inventory ("Excluded — personal / non-reproducible") so
   the audit is transparent about its boundary; do not score against them.

   **The auditor's own setup is never a reference.** Assess the *client's* harness from the client's
   shared, version-controlled repositories at a cited commit — never from what happens to be
   installed, enabled, or remembered on the **auditor's** machine. Do not treat the auditor's local
   plugin install, personal memory, work-notes, or machine config as evidence or as a baseline for
   "what good looks like". When reading a dependency, attribute findings to the shared repo at a
   commit, not to "what's installed locally". If a fact can only be seen on the auditor's machine,
   it is not an audit fact.

2. **Cite evidence, never inference.** Every finding references a file, path, line, or command
   output. Organizational context the auditor happens to know (who reviews what, team conventions
   not written down) is **not** an audit fact — if it matters, record it separately as
   *"unverified context, excluded from scoring"* or raise it as an open question, never as a basis
   for a score.

3. **Shared, version-controlled dependencies are in scope.** A plugin/marketplace repo that
   supplies skills, commands, or agents **is part of the harness** — assess its *committed content*
   directly (skill quality, anatomy, descriptions, its own tests/CI/versioning), exactly as you
   assess the primary repo. Do **not** treat it as an opaque black box. The **reproducibility of its
   delivery** (is it version-pinned? released with tags? or does the consumer track a moving `main`
   via auto-update?) is itself a *finding*, not a reason to exclude the dependency. Only
   **per-user, non-shared** configuration is out of scope (rule 1).

## Consistent item template

Score every dimension using the **same** structure, so reports are comparable. See
`item-template.md`. Each item records the **5 C's** — *Criteria · Condition (evidence) · Cause ·
Consequence · Corrective action* — plus a **maturity level + one-line rationale**, severity-ordered
findings, and recommendations carrying **Impact + Effort + Owner** and a **Finding ID** for
traceability.

## Assurance opinion (overall)

Close with a single overall opinion on a defined scale — **Satisfactory** (controls are effective;
only minor gaps) · **Partial** (meaningful risk reduction, but relied-on guarantees are bypassable or
unverified) · **Unsatisfactory** (key controls absent or ineffective). State the basis in one line.

## Limitations

State explicitly what was **not** assessed (e.g. test suites not executed, skill *output quality* not
evaluated, point-in-time snapshot, dynamic/runtime behaviour). Manage expectations; don't imply
coverage you didn't deliver.

## Process

1. **Scan (read, don't guess).** Inventory the contract, skills, hooks, settings, MCP config,
   sensors (test/lint/CI), memory and state files. Note for each artifact **where it lives**
   (code repo vs plugin vs personal) and whether it is **tracked / gitignored**.
2. **Evaluate.** Score each dimension against the detailed criteria in `checklist.md`, using the
   rubric in `scoring-rubric.md`. Read `principles.md` for the *why* behind each criterion and cite
   it in findings. Tag every fix `cheap` (deterministic, do first), `deeper`, or `gated`.
3. **Report.** Architecture overview → diagnosis → item-by-item review (good *and* bad) →
   prioritized action plan. Write findings with the **5 C's**, rate **severity** worst-first, assign
   a **maturity level** per dimension + overall, and prioritize actions by **Impact × Effort** with
   an owner and target per action — see `prioritization.md` and `maturity-model.md`. Effort alone is
   not a priority.
4. **Deliver & re-audit.** The harness is an ongoing practice, not a one-time config — re-run
   when the setup materially changes. A re-audit of the same target is a **new dated folder**
   `audits/YYYY-MM-DD-<target>/` (same `<target>` slug; date-first keeps them ordered). In its
   Document Control, fill the **`Prior audit`** row with a link to the previous folder and its
   overall maturity/opinion — that prior report is the baseline. Add one row to the ledger in
   `audits/README.md`. Pin the framework version you ran against (below), so a jump in maturity
   isn't confused with a change in the ruler.

## Principles used as judgment criteria

- **Guides + sensors, before + after.** Flag feedforward-only and feedback-only setups.
- **A rule is only hard if a hook blocks it.** Prose is a request; a `PreToolUse` hook is enforcement.
- **Keep the contract lean** (< ~200 lines). How-to belongs in skills/scripts, not the contract.
- **Right tool for the job.** Always-rule → contract; repeated playbook → skill; side-task noise
  → subagent; every-time-no-judgment → hook; external system → MCP; cross-repo reuse → plugin.
- **Start cheap.** Fast deterministic controls before slow inferential ones.
- **Never weaken a check to make something pass.**

## Framework changelog

Semantic-ish: bump **minor** for new/changed criteria or rubric; **major** for a re-scoped dimension
set that breaks comparability with prior audits. Report revisions are tracked separately, per audit.

- **1.0** (2026-06) — Initial release. 8 dimensions (Contract · Skills · Guides · Sensors ·
  Enforcement & Permissions · Memory & State · Improvement Loop · Tooling/Automation/Orchestration),
  ✓✓/✓/⚠/✗ rubric, severity + CMMI-style 1–5 maturity, 5 C's item structure, Impact×Effort plan.
  First run: `audits/2026-06-24-pim`.
