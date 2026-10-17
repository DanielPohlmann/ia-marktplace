<!-- Cover page. Rendered by build/build-pdf.mjs via the `.cover*` classes in build/style.css.
     This raw HTML block IS the cover — there is no automatic H1→cover conversion. -->
<div class="cover">
  <div class="cover-band"><ORG · SITE — TEAM></div>
  <hr class="cover-rule"/>
  <div class="cover-title">AI Harness Audit</div>
  <div class="cover-sub"><TARGET — one-line subtitle></div>
  <div class="cover-meta">
    <div><span>Prepared by</span><Name><br/><Role, Org></div>
    <div><span>Assisted by</span><e.g. Claude (Opus 4.8)></div>
    <div><span>Date</span><Date></div>
    <div><span>Version</span><X.Y></div>
    <div><span>Method</span>Framework v<X.Y> (8-dimension) + independent clean-context cross-check</div>
    <div><span>Classification</span><span class="cover-class">Confidential — internal</span></div>
  </div>
</div>

<!-- pagebreak -->

## Document Control

| | |
|---|---|
| **Target** | <repo / system + enabled plugins> |
| **Stack** | <stack> |
| **Harness scope** | <project repo + shared plugin repo>; per-user config excluded |
| **Prepared by** | <name, role, org> |
| **Engagement date** | <date> |
| **Framework** | v<X.Y> (`ai-harness-audit` @ <commit>) — the method version this audit ran against |
| **Method** | Independent clean-context cross-check (fresh subagents, assess + adversarial verify) |
| **Base refs** | <repo@ref; plugin@ref> |
| **Prior audit** | none — first audit *(or:* [`<prev-date>-<target>`](../<prev-date>-<target>/<target>-<prev-date>-v<X.Y>.md) — Level <N> · <opinion>*)* |
| **Report version** | v<X.Y> — <Draft / Final> |

## 1. Executive Summary
- Context (1 paragraph)
- Overall posture verdict
- **Overall maturity Level (1–5) + target**, and **Assurance opinion** (Satisfactory / Partial / Unsatisfactory)
- Scorecard table (Dimension · Score · Maturity · one-line)
- Key findings / Top priorities (Impact × Effort)

## 2. Methodology & Scope
- The frame (Agent = Model + Harness)
- Scope (impartial · reproducible · plugin-inclusive · auditor's own setup never a reference)
- Clean-context cross-check
- Dimensions & rubric (reference framework/); walk the **Claude Code surface map**
- **Limitations** — what was NOT assessed (suites not run, output quality, point-in-time, …)

## 3. Architecture Overview
- Diagram of the harness (planes; reproducibility boundary)
- Where each artifact lives (tracked / ignored / plugin / excluded)

## 4. Diagnosis
- Cross-cutting findings (the central tension[s])

## 5. Item-by-Item Review  *(5 C's + maturity + severity-ordered findings with IDs)*
- 5.1 Contract
- 5.2 Skills
- 5.3 Guides
- 5.4 Sensors
- 5.5 Enforcement & Permissions
- 5.6 Memory & State
- 5.7 Improvement Loop
- 5.8 Tooling, Automation & Orchestration  *(MCP · loops · schedules/routines · workflows · headless/CI)*

## 6. Open Questions

## 7. Conclusion & Prioritized Action Plan
- Impact × Effort matrix (Quick Wins / Major Projects / Fill-ins / Reconsider)
- Action register: ID · **Finding** · Action · Impact · Effort · Quadrant · Owner · Target
- Closing assessment

## Appendix A — Inventory (incl. Excluded: per-user / non-reproducible)
## Appendix B — Scoring Rubric (score · severity · maturity · assurance opinion)
## Appendix C — References (criteria basis: audit standards + Claude Code docs)
