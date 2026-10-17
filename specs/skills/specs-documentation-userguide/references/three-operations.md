<!-- Part of the specs-documentation-userguide skill. Loaded on demand from SKILL.md. -->

# Three Operations

Invoke by intent — the user says "generate the user guide", "update the docs", or
"audit the docs".

## 1. Generate

Produce customer-facing docs from scratch (or for a feature area that has none).

① **Discover features from the codebase.** Map code artifacts to user-visible
capabilities (see *Feature Discovery* below). Group by what the customer perceives as
a feature area, NOT by module or service boundary.

② **Cross-check against existing specs.** Read any PRDs (`specs-documentation-prd`
output), READMEs, and `docs/` already present — they carry the intended user value and
naming. Prefer product names the team already uses.

③ **Decide the page set.** One page per feature area a customer would look up. Don't
mirror the code structure — a single customer feature ("Online booking page") may span
several modules.

④ **Write each page** using the template below, in the customer's language. Every
sentence describes something the user does, sees, or receives.

⑤ **Build navigation.** Write/refresh `docs/user-guide/index.md` (or `README.md` in the
docs root) with a table of contents grouped by theme, and a one-line summary per page.

⑥ **Report** every file created, and list features you found in code but intentionally
did NOT document (internal-only, admin-only, not yet shipped) so the user can confirm.

## 2. Update

Sync already-published docs after the product changed.

① **Read the existing docs** and the recent diff / changed areas.
② **Detect drift** — new capabilities not yet documented, changed behavior, renamed or
removed features.
③ **Patch minimally** — edit the affected pages, preserve the existing voice and
structure, bump any "last updated" line. Don't rewrite pages wholesale.
④ **Report** each page changed and why, in one line each.

## 3. Audit

Health-check the docs against the code — the doc-it "stale reference" pass, adapted.

① **Removed features:** doc pages describing capabilities no longer present in the code
(endpoint gone, route deleted, module removed) → flag as **stale**.
② **Undocumented features:** shipped, customer-visible capabilities with no page → flag
as **gap**.
③ **Voice leaks:** pages that mention internal names (module/class/endpoint/event/table),
stack detail, or engineer jargon → flag as **voice**.
④ **Broken cross-links** between doc pages and missing images/assets.
⑤ **Staleness:** pages whose behavior no longer matches current code paths.
⑥ **Report** grouped by severity: stale (describes something gone) > gap (missing) >
voice > broken links > minor staleness. Give the file path and the concrete fix for
each. Don't auto-edit during an audit unless asked — report first.
