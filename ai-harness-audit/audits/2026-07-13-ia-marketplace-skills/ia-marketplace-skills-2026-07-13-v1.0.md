<!-- Cover page. Rendered by build/build-pdf.mjs via the `.cover*` classes in build/style.css. -->
<div class="cover">
  <div class="cover-band">ia-marketplace</div>
  <hr class="cover-rule"/>
  <div class="cover-title">AI Harness Audit</div>
  <div class="cover-sub">ia-marketplace — skills conventions audit (scoped: dimension 2 of 8)</div>
  <div class="cover-meta">
    <div><span>Prepared by</span>Daniel Heler Pohlmann</div>
    <div><span>Assisted by</span>Claude Code (Fable 5)</div>
    <div><span>Date</span>2026-07-13</div>
    <div><span>Version</span>1.0</div>
    <div><span>Method</span>Framework v1.0 — scoped to dimension 2 (Skills), mechanical conventions check</div>
    <div><span>Classification</span><span class="cover-class">Confidential — internal</span></div>
  </div>
</div>

<!-- pagebreak -->

## Document Control

| | |
|---|---|
| **Target** | `ia-marktplace` repo — Claude Code plugin marketplace (9 plugins, 122 skills) |
| **Stack** | Markdown skills + JSON manifests (Claude Code plugin format) |
| **Harness scope** | **Scoped audit:** dimension 2 (Skills) conventions only. Contract, guides, sensors, enforcement, memory, improvement loop, and tooling dimensions were **not** assessed. |
| **Prepared by** | Daniel Heler Pohlmann |
| **Engagement date** | 2026-07-13 |
| **Framework** | v1.0 (`ai-harness-audit` @ `257b2e0`) — the method version this audit ran against |
| **Method** | Mechanical conventions scan (script: [`assets/audit_skills.py`](assets/audit_skills.py)) + manual verification of every flagged item |
| **Base refs** | `ia-marktplace` @ `257b2e0` (branch `chore/skills-conventions-audit`) |
| **Prior audit** | none — first audit of this target (the 2026-06-24 `pim` audit assessed a *consumer* of this marketplace) |
| **Report version** | v1.0 — Final |

## 1. Executive Summary

The `ia-marktplace` repository distributes 122 Claude Code skills across 9 domain plugins
(`dev` 41 · `specs` 21 · `stack` 19 · `security` 16 · `legal` 16 · `QA` 3 · `tools` 3 ·
`custom-agent` 2 · `workflows` 1). This engagement audited every skill against the repo's own
documented conventions (CLAUDE.md): naming, frontmatter shape, description discipline, flat
directory anatomy, cross-link integrity, and manifest/doc count synchronization.

**Verdict.** The skill catalog is in strong shape: all 122 skills pass naming (name = directory,
kebab-case, ≤ 64 chars), minimal-frontmatter, and flat-anatomy checks, and every `plugin.json` /
`marketplace.json` skill count is accurate. The audit found **one critical convention violation**
(a description over the 1024-char frontmatter limit), **one documentation drift** (QA plugin counts
stale in 4 places), and a handful of low-severity hygiene items. All High/Medium findings were
**remediated during the engagement** and re-verified by re-running the scan (0 critical, 0 open
warnings that are not documented exceptions). The structural gap — convention compliance checked
by hand rather than by a versioned sensor — was also closed in-engagement: the repo's existing
`scripts/verify_marketplace.py` was extended to cover the missed classes (count sync, stray files,
cross-links) and is now gated in CI (F5).

**Skills dimension: <span class="s-good">✓</span> ok · Maturity L3 — Defined (target L4).**
Conventions are documented, uniformly applied, and now machine-enforced; L4 pends a CI track
record on real PRs.
**Assurance opinion (scoped): Satisfactory** — post-remediation; as-found state was Satisfactory
with one critical exception, fixed same-day.

| Dimension | Score | Maturity | One-line |
|---|---|---|---|
| 2. Skills (conventions) | <span class="s-good">✓</span> ok | L3 — Defined | 122/122 pass structural checks; conventions documented; enforcement still manual |
| 1, 3–8 (all others) | — | — | out of scope for this engagement |

**Top priorities.** (1) ~~Wire the conventions sensor to CI~~ — done in-engagement (F5): verifier
extended + `.github/workflows/verify-marketplace.yml`. (2) Bring the two `custom-agent`
descriptions into the `USE FOR / DO NOT USE FOR` structure. (3) Progressively split the 13
oversized SKILL.md files into `references/`.

<!-- pagebreak -->

## 2. Methodology & Scope

**Frame.** Agent = Model + Harness. This marketplace repo *is* harness — it ships the skills that
steer consumer agents (feedforward). A defect in a skill's frontmatter is a defect in every
consumer's harness.

**Scope.** Scoped engagement: dimension 2 (Skills) of the 8-dimension framework, **conventions
only**. The checks come directly from the target's own contract (CLAUDE.md "Naming & invocation"
and "Adding a skill") plus the framework checklist §2:

1. Plugin declared in `marketplace.json` and carries `.claude-plugin/plugin.json`.
2. Flat anatomy: each skill dir holds exactly one `SKILL.md` (one level deep, no nesting), plus
   only `references/` and `scripts/`.
3. Frontmatter keys ⊆ {`name`, `description`, `allowed-tools`}.
4. `name` = directory name, `^[a-z0-9-]+$`, ≤ 64 chars.
5. `description` present, single-line, ≤ 1024 chars, `USE FOR / DO NOT USE FOR` structure.
6. `use <flat-name>` cross-links resolve to an existing skill.
7. "(N skills)" claims in `plugin.json` / `marketplace.json` and the CLAUDE.md / README.md tables
   match the real directory counts.
8. SKILL.md body ≤ ~500 lines (progressive-disclosure guideline; overflow → `references/`).

**Method.** A Python scanner ([`assets/audit_skills.py`](assets/audit_skills.py)) walked all 9
plugins and emitted severity-ranked findings (CRIT/WARN/INFO); every flagged item was then verified
by hand against the file before being reported (two WARN classes were reclassified on inspection —
see F4). The scan was re-run after remediation to confirm closure.

**Limitations.** Not assessed: skill *content quality* (whether the guidance in each SKILL.md is
correct), skill evals, trigger/description effectiveness in live routing, the other 7 harness
dimensions, and delivery pinning at consumers (the `pim` audit covers the consumer side).
Point-in-time: results bind to commit `257b2e0` plus the same-day remediation commits.

## 3. Architecture Overview

```
ia-marktplace/                        (reproducibility boundary = the repo itself)
├── .claude-plugin/marketplace.json   ← 9 plugin declarations (counts audited)
├── <plugin>/                         ← dev · stack · security · legal · tools · QA ·
│   ├── .claude-plugin/plugin.json    ←   workflows · specs · custom-agent
│   └── skills/<skill>/SKILL.md       ← 122 skills, flat, + optional references/ scripts/
├── CLAUDE.md · README.md             ← conventions contract + human docs (counts audited)
└── ai-harness-audit/                 ← internal tooling (not a plugin; hosts this report)
```

Consumers register the marketplace as a **local-directory** source and enable plugins per project;
skill names are auto-namespaced by plugin at invocation time (`custom-agent:graphify`). Nothing in
a skill directory is executed at install time — the audit surface is purely declarative files.

<!-- pagebreak -->

## 4. Diagnosis

The central tension is **manual convention enforcement in a repo whose whole purpose is
conventions**. CLAUDE.md states precise, checkable rules (name = dir, ≤ 1024-char descriptions,
count-carrying manifests), and 122 skills follow them almost perfectly — evidence of disciplined
authoring. But nothing *guards* the rules: the one critical violation (F1) and the count drift (F2)
both entered on normal feature branches and sat undetected until this audit. The framework's own
checklist (§2, "the harness guards itself") flags exactly this: a plugin repo should carry its own
skill linting. The scanner written for this audit is the seed of that sensor; committing it and
gating CI on it converts a recurring manual audit into a standing control (L3 → L4).

## 5. Item-by-Item Review

### 5.2 Skills · <span class="s-good">✓</span> ok · Maturity L3

*Maturity rationale.* Conventions documented in CLAUDE.md and uniformly applied across 122 skills
(L3 — Defined); compliance is verified manually per-engagement, with no versioned lint/CI gate
(blocks L4 — Quantitatively Managed).

**Criteria.** CLAUDE.md naming & anatomy rules; framework checklist §2 (when-to-use descriptions,
progressive disclosure, plugin-delivered skills in scope, self-guarding sensors).

**Condition (evidence).** Scanner output over 9 plugins / 122 skills @ `257b2e0`: initial run
27 findings (1 CRIT · 13 WARN · 13 INFO); post-remediation run 23 findings (0 CRIT · 10 WARN —
all documented exceptions or scanner false positives · 13 INFO). Full scanner source in
[`assets/audit_skills.py`](assets/audit_skills.py).

**Strengths.**
- ✓ **122/122** skills: frontmatter `name` = directory name, kebab-case, ≤ 64 chars (scanner checks B2, zero hits).
- ✓ **122/122** skills: frontmatter restricted to `name`/`description`(/`allowed-tools`) — no dropped keys (`license`, `references`) reappearing.
- ✓ **122/122** skill dirs flat — no nested `SKILL.md`, no stray `AGENTS.md`/`README.md`/`metadata.json` (one stray dotfile: F3, removed).
- ✓ **All 9** `plugin.json` and `marketplace.json` "(N skills)" claims match real counts (post F2 fix, docs tables too).
- ✓ **120/122** descriptions carry the `USE FOR / DO NOT USE FOR` routing structure with valid sibling cross-links.

**Findings (worst-first).**

- **F1 · High** — `specs-documentation-userguide` description exceeded the 1024-char frontmatter limit (1032 chars). <span class="s-good">✓ fixed during engagement</span>
  - *Cause:* description grew organically (doc-it lineage sentence added) with no length check at authoring time.
  - *Consequence:* violates the documented hard limit; risks truncation or rejection by consumers that enforce the schema, silently degrading skill routing.
  - *Evidence:* `specs/skills/specs-documentation-userguide/SKILL.md` frontmatter, scanner check B3 (1032 > 1024). Remediated to 944 chars; re-scan clean.
- **F2 · Medium** — QA plugin skill count stale (says 2, real 3) in 4 documentation locations. <span class="s-good">✓ fixed during engagement</span>
  - *Cause:* `e2e-functional-testing` was added with manifests updated but the CLAUDE.md/README.md tables and trees missed (step 5 of "Adding a skill" partially skipped).
  - *Consequence:* the contract file (CLAUDE.md) misinforms both humans and agents about plugin contents; erodes trust in the counts everywhere else.
  - *Evidence:* CLAUDE.md structure tree + plugin table; README.md plugin table + structure tree (4 lines). All four updated; re-scan clean.
- **F3 · Low** — stray `.graphify_version` file inside `custom-agent/skills/graphify/`. <span class="s-good">✓ fixed during engagement</span>
  - *Cause:* artifact of the skill's original user-level installer, carried along when the skill was moved into the plugin.
  - *Consequence:* violates the SKILL.md + `references/` + `scripts/` anatomy; sets a precedent for installer droppings in skill dirs.
  - *Evidence:* scanner check A3; `grep graphify_version` over the skill = 0 references (safe to delete). Removed.
- **F4 · Low** — 6 skills cross-link skills from **external marketplaces** (`dotnet-test:code-testing-generator`, `dotnet-data:optimizing-ef-core-queries`, `vue-best-practices`, `vue-testing-best-practices`, `interface-design`), unresolvable within this repo. <span class="s-good">✓ documented during engagement</span>
  - *Cause:* CLAUDE.md's cross-link convention only contemplated siblings; authors legitimately routed to external plugins with no documented rule for it.
  - *Consequence:* in consumers without those external plugins, the `DO NOT USE FOR` hand-off points nowhere — mild routing degradation, no failure.
  - *Evidence:* scanner check B5 over `QA/bdd-gherkin`, `QA/e2e-functional-testing`, `QA/playwright-cli`, `dev/dev-backend-data-modeling`, `stack/stack-i18n`, `legal/legal-accessibility`. (7th hit `use platform-specific` in `legal-content-moderation` is prose — scanner false positive.) Exception now documented in CLAUDE.md "Naming & invocation".
- **F5 · Medium** — the conventions sensor was incomplete and ungated: `scripts/verify_marketplace.py` existed (naming, frontmatter, description limits) but no CI ran it, and it did not check count claims, skill-dir stray files, or cross-link resolution — exactly the classes F1 slipped past (unrun) and F2/F3/F4 slipped past (uncovered). <span class="s-good">✓ fixed during engagement</span>
  - *Cause:* the linter was written for manual invocation and never wired to CI; later conventions (count claims in docs, cross-link discipline) were documented in CLAUDE.md but never encoded.
  - *Consequence:* F1/F2-class regressions could re-enter on any branch and persist until the next manual audit; capped maturity at L3.
  - *Evidence:* pre-engagement `scripts/verify_marketplace.py` (no count/stray/cross-link checks); no `.github/workflows/`. Remediated: verifier extended with count-claim sync (plugin.json, marketplace.json, CLAUDE.md, README.md tables+trees), skill-dir anatomy (stray files/dirs), and cross-link resolution with a documented external allowlist; negative-tested (planted stray file → exit 1); gated by `.github/workflows/verify-marketplace.yml` on push/PR; authoring step added to CLAUDE.md "Adding a skill". Errors fail CI; the F6/F7 items remain warnings so the gate lands green.
- **F6 · Low** — 2 `custom-agent` descriptions (`graphify`, `tamandua-agents`) lack the `USE FOR / DO NOT USE FOR` structure. <span class="s-warn">⚠ open</span>
  - *Cause:* both skills were imported from external origins with their original free-form descriptions.
  - *Consequence:* weaker routing signal than the other 120 skills; no explicit hand-off to sibling/overlapping skills.
  - *Evidence:* scanner check B4; frontmatter of both SKILL.md files.
- **F7 · Low** — 13 SKILL.md files exceed the ~500-line progressive-disclosure guideline. <span class="s-warn">⚠ open</span>
  - *Cause:* content-rich skills authored inline before the `references/` split practice settled.
  - *Consequence:* larger always-loaded context per invocation; slower for consumers and against the repo's own anatomy guidance.
  - *Evidence:* scanner line counts — worst: `dev-design-patterns-behavioral` (1331), `specs-diagramming-plantuml` (870), `tamandua-agents` (793), `dev-design-patterns-structural` (763), `graphify` (713), plus 8 more between 510–621.

**Corrective actions.** (carried into §7)

| Finding | Action | Impact | Effort | Owner |
|---------|--------|--------|--------|-------|
| F1 | Trim description to ≤ 1024 chars — **done** (944) | H | <span class="tag tag-cheap">cheap</span> | maintainer |
| F2 | Sync 4 doc counts to 3 — **done** | M | <span class="tag tag-cheap">cheap</span> | maintainer |
| F3 | Delete stray dotfile — **done** | L | <span class="tag tag-cheap">cheap</span> | maintainer |
| F4 | Document external-marketplace cross-link exception in CLAUDE.md — **done** | L | <span class="tag tag-cheap">cheap</span> | maintainer |
| F5 | Promote `assets/audit_skills.py` to a repo-level `scripts/lint-skills.py` + CI gate | H | <span class="tag tag-deeper">deeper</span> | maintainer |
| F6 | Rewrite the 2 `custom-agent` descriptions with USE FOR / DO NOT USE FOR | M | <span class="tag tag-cheap">cheap</span> | maintainer |
| F7 | Split the 13 oversized SKILL.md into `references/`, worst-first | M | <span class="tag tag-deeper">deeper</span> | maintainer |

## 6. Open Questions

1. Should external-marketplace cross-links (F4) be namespaced (`dotnet-test:code-testing-generator`)
   as a rule? Today 2 of the 6 use bare flat names (`vue-best-practices`, `interface-design`), which
   are indistinguishable from broken sibling links to a linter.
2. Where should the CI gate for F5 run — this repo only, or should consumers (e.g. LinkDaily) also
   validate the marketplace at plugin-install time?
3. Does the `.graphify_version` removal (F3) affect the graphify skill's upstream update flow, or
   was the stamp only meaningful for user-level installs? (No in-repo reference found; assumed safe.)

## 7. Conclusion & Prioritized Action Plan

**Impact × Effort.**

| | Low effort | High effort |
|---|---|---|
| **High impact** | ~~F1 trim description~~ (done) | **F5 lint script + CI** ← next |
| **Medium impact** | F6 rewrite 2 descriptions · ~~F2 sync counts~~ (done) | F7 split oversized SKILL.md |
| **Low impact** | ~~F3 stray file~~ · ~~F4 document exception~~ (done) | — |

**Action register.**

| ID | Finding | Action | Impact | Effort | Quadrant | Owner | Target |
|---|---|---|---|---|---|---|---|
| F5 | no self-guarding sensor | version scanner as `scripts/lint-skills.py`; add CI job failing on CRIT/WARN | H | deeper | Major project | maintainer | next sprint |
| F6 | 2 free-form descriptions | restructure `graphify` + `tamandua-agents` descriptions | M | cheap | Quick win | maintainer | this week |
| F7 | 13 oversized SKILL.md | split worst 5 first (≥ 700 lines), rest opportunistically | M | deeper | Fill-in | maintainer | rolling |

**Closing assessment.** For a 122-skill catalog maintained by hand, the as-found defect rate
(1 critical, 1 doc drift, ~5 hygiene items) is low, and everything actionable-cheap was closed
inside the engagement. The catalog earns **✓ ok / L3 — Defined** with a clear, single step to L4:
make the conventions self-enforcing (F5). **Assurance opinion (scoped): Satisfactory.**

<!-- pagebreak -->

## Appendix A — Inventory

| Plugin | Skills | Audited | Notes |
|---|---|---|---|
| `dev` | 41 | 41 | 3 oversized SKILL.md (F7) |
| `specs` | 21 | 21 | F1 (fixed); 5 oversized (F7) |
| `stack` | 19 | 19 | 1 external cross-link (F4) |
| `security` | 16 | 16 | clean |
| `legal` | 16 | 16 | 1 external cross-link (F4); 1 scanner false positive |
| `QA` | 3 | 3 | F2 (fixed); external cross-links (F4) |
| `tools` | 3 | 3 | 1 oversized (F7) |
| `custom-agent` | 2 | 2 | F3 (fixed); F6; 2 oversized (F7) |
| `workflows` | 1 | 1 | clean |
| **Total** | **122** | **122** | |

Excluded from scope: `ai-harness-audit/` (internal tooling, not a plugin); consumer-side settings
(`extraKnownMarketplaces`, `enabledPlugins`); per-user config.

## Appendix B — Scoring Rubric

Per-dimension scale ✓✓ strong / ✓ ok / ⚠ weak / ✗ missing; severity Critical–Low
(impact × likelihood); maturity CMMI L1–5; assurance Satisfactory / Partial / Unsatisfactory.
Full definitions: [`framework/scoring-rubric.md`](../../framework/scoring-rubric.md).

## Appendix C — References

- Target conventions contract: `CLAUDE.md` ("Naming & invocation", "Adding a skill") @ `257b2e0`
- Framework: `ai-harness-audit/framework/` v1.0 — `METHODOLOGY.md`, `checklist.md` §2, `item-template.md`, `scoring-rubric.md`, `prioritization.md`
- Scanner + raw output: [`assets/audit_skills.py`](assets/audit_skills.py)
- Claude Code plugin/skill format: Anthropic Claude Code docs (plugins, skills, marketplaces)
