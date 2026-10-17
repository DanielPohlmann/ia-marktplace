# AI Harness Audit

A reusable framework for auditing the **agent harness** of a repository — everything
wrapped around the model (contract, skills, guides, sensors, hooks, memory) — and producing
a professional PDF report.

> **Agent = Model + Harness.** The model is fixed; the harness is what you engineer.
> Guides steer *before* the agent acts (feedforward); sensors check *after* (feedback).
> A good audit measures both.

## Layout

```
ai-harness-audit/
├── README.md                  ← this file
├── framework/                 ← the reusable method (version-controlled, repo-agnostic)
│   ├── METHODOLOGY.md         ← how an audit is run, the 8 dimensions, the frame
│   ├── checklist.md           ← detailed per-dimension criteria (the "what to look for")
│   ├── principles.md          ← the "why" behind each criterion, with sources
│   ├── scoring-rubric.md      ← the ✓✓ / ✓ / ⚠ / ✗ scale, severity + maturity
│   ├── prioritization.md      ← 5 C's findings, severity, Impact×Effort matrix, owners
│   ├── maturity-model.md      ← CMMI-style 1–5 harness maturity levels
│   ├── item-template.md       ← the consistent per-dimension item structure (5 C's)
│   └── TEMPLATE.md            ← blank report skeleton to copy per engagement
├── build/                     ← Markdown → HTML → PDF pipeline
│   ├── package.json
│   ├── build-pdf.mjs
│   └── style.css
└── audits/                    ← one folder per engagement
    ├── README.md              ← ledger: one row per audit (date · target · framework · maturity)
    └── YYYY-MM-DD-<target>/                 ← folder is date-first (sorts chronologically)
        ├── <target>-YYYY-MM-DD-v<ver>.md    ← the audit (source of truth); file is target-first + version
        ├── <target>-YYYY-MM-DD-v<ver>.pdf   ← generated deliverable (same basename)
        └── assets/
```

Filenames carry **target · date · version** (e.g. `pim-2026-06-24-v1.0.pdf`) so a deliverable shared
outside its folder still identifies itself. `<ver>` is the **report version**; a re-issue of the same
audit (errata/addendum) is a new file `…-v1.1.…` beside the old one, never an in-place overwrite.

## Running a new audit

1. Copy `framework/TEMPLATE.md` to `audits/<date>-<target>/<target>-<date>-v1.0.md`.
2. Inventory the target harness (see `framework/METHODOLOGY.md` §Scan).
3. Score each dimension against `framework/scoring-rubric.md`; fill every section.
4. Build the PDF (below).

## Versioning

Two independent version axes — don't conflate them:

- **Framework version** (the *method*) — dimensions, checklist, rubric. Single source of truth is the
  changelog at the bottom of `framework/METHODOLOGY.md` (currently **v1.0**). Every report pins the
  version + commit it ran against, so a jump in a target's maturity isn't confused with a change in
  the ruler. Bump it when criteria change.
- **Report version** (a single audit's *revision*) — the `Version` on the cover. Bump on re-issue of
  the **same** engagement (errata, addendum). Independent per audit.

**Re-auditing the same target** — a re-audit is a **new dated folder** `audits/YYYY-MM-DD-<target>/`
(same `<target>` slug; date-first keeps them ordered), not an edit of the old one. In the new report's
Document Control, link the previous folder as the **Prior audit** baseline, and add a row to the
ledger in [`audits/README.md`](audits/README.md).

## Building the PDF

One-time:

```bash
cd build
npm install
```

Per report:

```bash
cd build
node build-pdf.mjs ../audits/2026-06-24-pim/pim-2026-06-24-v1.0.md
# → writes the .pdf (and .html) with the same basename, next to the source
```

Requires Node 18+ and a local Chrome or Edge (auto-detected by `build-pdf.mjs`).
No Chromium download — it drives the installed browser via `puppeteer-core`.

## Markdown conventions for clean PDFs

- The cover page is a raw **`<div class="cover">…</div>`** block at the top of the report
  (`html: true` is on). Copy the skeleton from `framework/TEMPLATE.md`; the `.cover*` classes
  live in `build/style.css`. There is no automatic H1→cover conversion — a plain `# H1`
  renders as an ordinary heading.
- `<!-- pagebreak -->` forces a page break.
- Status glyphs can be color-coded with inline spans: `<span class="s-good">✓</span>`,
  `s-strong`, `s-warn`, `s-bad`. Effort chips: `<span class="tag tag-cheap">cheap</span>`,
  `tag-deeper`, `tag-gated`.
