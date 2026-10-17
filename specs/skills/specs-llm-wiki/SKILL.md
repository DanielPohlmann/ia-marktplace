---
name: specs-llm-wiki
description: Use when building or maintaining a persistent interlinked markdown knowledge base (Karpathy's LLM Wiki pattern). USE FOR: creating or resuming a wiki, ingesting articles/papers/transcripts, cross-linking and deduplicating pages, lint and health checks, about-me page, dashboards, Obsidian. DO NOT USE FOR: a single decision record (use specs-documentation-adr), code knowledge graphs (use graphify), diagrams (use specs-diagramming).
---

# Karpathy's LLM Wiki

Build and maintain a persistent, compounding knowledge base as interlinked markdown files.
Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki
compiles knowledge once and keeps it current. Cross-references are already there.
Contradictions have already been flagged. Synthesis reflects everything ingested.

**Division of labor:** The human curates sources and directs analysis. The agent
summarizes, cross-references, files, and maintains consistency.

## When This Skill Activates

Use this skill when the user:
- Asks to create, build, or start a wiki or knowledge base
- Asks to ingest, add, or process a source into their wiki
- Asks to ingest meeting notes from Gmail (Gemini "Anotações") — see `references/gemini-meeting-ingest.md`
- Asks to visualize, dashboard, or browse the wiki — see `references/dashboard.md`
- Asks a question and an existing wiki is present at the configured path
- Asks to lint, audit, or health-check their wiki
- Asks to build, update, or improve their `about-me.md` persona page — see `references/about-me.md` and Core Operation 3
- References their wiki, knowledge base, or "notes" in a research context

## Wiki Location

**Location:** Set via the `WIKI_PATH` environment variable. If unset, ask the user
or default to a `wiki/` directory at the repo root.

```powershell
# Windows / PowerShell
$WIKI = if ($env:WIKI_PATH) { $env:WIKI_PATH } else { "$PWD\wiki" }
```

```bash
# macOS / Linux / Git Bash
WIKI="${WIKI_PATH:-$PWD/wiki}"
```

The wiki is just a directory of markdown files — open it in Obsidian, VS Code, or
any editor. No database, no special tooling required. Read and write it with the
standard file tools (`Read`, `Write`, `Edit`, `Grep`, `Glob`); no external CLI needed.

## Resuming an Existing Wiki (CRITICAL — do this every session)

When the user has an existing wiki, **always orient yourself before doing anything**:

① **Read `SCHEMA.md`** — understand the domain, conventions, and tag taxonomy.
② **Read `index.md`** — learn what pages exist and their summaries.
③ **Scan recent `log.md`** — read the last 20-30 entries to understand recent activity.

Orientation reads at session start (use the `Read` tool):
- `Read` `<WIKI>/SCHEMA.md`
- `Read` `<WIKI>/index.md`
- `Read` `<WIKI>/log.md` (last ~30 lines — use the `offset`/`limit` args)

Only after orientation should you ingest, query, or lint. This prevents:
- Creating duplicate pages for entities that already exist
- Missing cross-references to existing content
- Contradicting the schema's conventions
- Repeating work already logged

For large wikis (100+ pages), also run a quick `Grep` for the topic
at hand before creating anything new.

## Pitfalls

- **Never modify files in `raw/`** — sources are immutable. Corrections go in wiki pages.
- **Computing the raw `sha256`.** When saving raw source frontmatter, the `sha256` is computed over the body (everything after the second `---`). Run a Python one-liner through the `Bash` tool:
  ```bash
  python -c "import hashlib,sys; c=open(sys.argv[1],encoding='utf-8').read(); p=c.split('---',2); b=p[2] if len(p)>2 else c; print(hashlib.sha256(b.encode()).hexdigest())" path/to/raw/file.md
  ```
  Then patch the frontmatter with the computed hash. (On Windows the same command works from Git Bash or PowerShell.)
- **Always orient first** — read SCHEMA + index + recent log before any operation in a new session.
  Skipping this causes duplicates and missed cross-references.
- **Always update index.md and log.md** — skipping this makes the wiki degrade. These are the
  navigational backbone.
- **Don't create pages for passing mentions** — follow the Page Thresholds in SCHEMA.md. A name
  appearing once in a footnote doesn't warrant an entity page.
- **Don't create pages without cross-references** — isolated pages are invisible. Every page must
  link to at least 2 other pages.
- **Frontmatter is required** — it enables search, filtering, and staleness detection.
- **Tags must come from the taxonomy** — freeform tags decay into noise. Add new tags to SCHEMA.md
  first, then use them.
- **Keep pages scannable** — a wiki page should be readable in 30 seconds. Split pages over
  200 lines. Move detailed analysis to dedicated deep-dive pages.
- **Ask before mass-updating** — if an ingest would touch 10+ existing pages, confirm
  the scope with the user first.
- **Rotate the log** — when log.md exceeds 500 entries, rename it `log-YYYY.md` and start fresh.
  The agent should check log size during lint.
- **Handle contradictions explicitly** — don't silently overwrite. Note both claims with dates,
  mark in frontmatter, flag for user review.

## Related Tools

[llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler) is a Node.js CLI that
compiles sources into a concept wiki with the same Karpathy inspiration. It's Obsidian-compatible,
so users who want a scheduled/CLI-driven compile pipeline can point it at the same vault this
skill maintains. Trade-offs: it owns page generation (replaces the agent's judgment on page
creation) and is tuned for small corpora. Use this skill when you want agent-in-the-loop curation;
use llmwiki when you want batch compile of a source directory.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/initializing-a-new-wiki.md](references/initializing-a-new-wiki.md) | Initializing a New Wiki — SCHEMA.md Template, raw/ Frontmatter, index.md Template, log.md Template |
| [references/core-operations.md](references/core-operations.md) | Core Operations — 1. Ingest, 2. Query, 3. Build / Update About Me, 4. Lint |
| [references/working-with-the-wiki.md](references/working-with-the-wiki.md) | Working with the Wiki — Searching, Bulk Ingest, Archiving, Obsidian Integration, Obsidian Headless (optional — Linux servers only), Dashboard Generation |
| [references/details.md](references/details.md) | Architecture: Three Layers |
