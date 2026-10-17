# Design: `bdd-gherkin` skill (QA plugin)

**Date:** 2026-07-08
**Repo:** `ia-marktplace` (Claude Code skills marketplace)
**Branch:** `feat/qa-bdd-gherkin-skill`

## Goal

Add a single skill, `bdd-gherkin`, to the `QA` plugin that guides authoring of
Gherkin/Cucumber `.feature` files for LinkDaily: turning business requirements
into `Given/When/Then` specifications written in the domain's ubiquitous
language.

## Source analysis

Two references were evaluated:

| Source | Nature | Strong on | Weak on |
|---|---|---|---|
| `angelo-v/opencode-playground` `bdd-gherkin/SKILL.md` | A working Claude/opencode skill | BDD philosophy, generation *workflow* (ask-first), Given/When/Then discipline, single-focused scenarios, data tables, doc strings, tips, validation checklist | Concrete formatting standards, file naming, review checklist beyond generation |
| `AutomationPanda/gherkin-guidelines-for-ai` `gherkin-guidelines.md` | A rules "context contract" | Formatting standards, `.feature`/kebab-case, indentation, line length, blank-line rules, step limits, strict ordering, prohibitions, anti-pattern checklist, template | Generation workflow, BDD philosophy |

**Decision: merge both into one skill.** They are complementary — one is
*how to think and work*, the other is *the rulebook + template*. Picking one
loses half the value. angelo-v provides the skeleton and workflow;
AutomationPanda supplies the formatting standards, prohibitions, and checklist.

## Conflict reconciliation — the `When`-step rule

- angelo-v: **exactly one** `When` step per scenario.
- AutomationPanda template: allows `When … And <continued action>`.

**Resolution (approved):** *one behavior / one logical action per scenario;
prefer a single `When`, allowing an `And` under it only when one action
genuinely spans two steps.* Keeps angelo-v's discipline without contradicting
AutomationPanda's template.

## Skill file

**Path:** `QA/skills/bdd-gherkin/SKILL.md` — one self-contained file (template
and checklist inline; no `references/` split).

**Naming:** `bdd-gherkin` — unprefixed, matching the sibling `playwright-cli`
(the QA plugin does not use a `qa-` prefix). Directory name equals frontmatter
`name`.

**Frontmatter:** only `name` + `description` (repo convention — no `license`,
`compatibility`, or `metadata` keys). angelo-v's dropped source URLs move to a
`## References` body section.

**Description (single line, USE FOR / DO NOT USE FOR, LinkDaily-flavored):**
Triggers on Gherkin / Cucumber / BDD / acceptance-criteria / feature-file
requests. `DO NOT USE FOR` cross-links siblings by flat name: running/executing
tests or writing step-definition/automation glue (`use playwright-cli`), .NET
test generation (`use dotnet-test:code-testing-generator`), Vue component tests
(`use vue-testing-best-practices`).

**Positioning:** `bdd-gherkin` *authors the specification* (`.feature` files);
`playwright-cli` and `dotnet-test` *execute* it.

### Section plan

1. What this skill does / When to use — angelo-v framing.
2. Core principles — domain-driven ubiquitous language (LinkDaily terms:
   professional, client, appointment, take-rate, `AppointmentBooked`),
   single-focused scenarios by default, declarative "what not how".
3. Feature structure & Given/When/Then rules — angelo-v discipline + the
   reconciled `When` rule.
4. Formatting standards (AutomationPanda) — `.feature` + kebab-case, one
   Feature/file, 2-space indent, < 120 chars, blank-line rules, no comments.
5. Scenario structure rules (AutomationPanda) — behavior-focused title,
   < 10 steps, strict Given→When→Then, no repeated phases, no `Or` keyword,
   state-over-navigation, observable `Then`, concrete realistic data (no
   `foo`/`bar`), no automation mechanics / SQL / HTTP leakage.
6. Data tables & doc strings — angelo-v (horizontal for record sets, vertical
   for one entity's fields).
7. Scenario Outlines — sparingly; only genuine input variation.
8. Tags & Background — minimal tags; liberal Background; one Background/Feature.
9. Clarifying-questions workflow — angelo-v ask-first flow.
10. Standard feature file template (inline, LinkDaily example).
11. Anti-patterns (both merged) — Do/Don't pairs, LinkDaily-flavored.
12. Validation checklist (both merged, deduped).
13. References — the two source URLs.

## Registration updates (all in `ia-marktplace`)

1. `QA/skills/bdd-gherkin/SKILL.md` — new file.
2. `QA/.claude-plugin/plugin.json` — extend `description` to mention BDD/Gherkin.
3. `.claude-plugin/marketplace.json` — extend QA plugin `description`.
4. `CLAUDE.md` — plugin table QA row `1 → 2` skills; structure comment.
5. `README.md` — QA section mentions `bdd-gherkin`.
6. Validate with `scripts/verify_marketplace.py`.

## Out of scope

- `linkdaily/CLAUDE.md` skills table update — deferred to a separate follow-up
  in the consuming repo (approved).

## Success criteria

- `bdd-gherkin/SKILL.md` exists, frontmatter is `name` + `description` only,
  description follows USE FOR / DO NOT USE FOR.
- Skill merges both sources faithfully with the reconciled `When` rule.
- Examples use LinkDaily ubiquitous language.
- `verify_marketplace.py` passes; all registration files updated consistently.
