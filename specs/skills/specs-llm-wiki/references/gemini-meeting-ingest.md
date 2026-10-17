# Gemini Meeting Notes Ingestion

How to ingest Google Meet meeting notes ("Anotações do Gemini") from Gmail into the wiki.

> **Prerequisite:** this workflow needs a Gmail MCP server connected to the session
> (one that exposes a Gmail search/fetch tool). The tool calls below (`search_gmail_messages`)
> are illustrative — substitute the actual tool names your Gmail MCP provides. If no
> Gmail MCP is available, skip this reference and ingest transcripts manually via paste
> or `Read` of an exported file.

## Source Pattern

Gemini meeting notes arrive as emails from `gemini-notes@google.com` with subject `[Externo] Anotações: "<meeting-name>" em <date>`.

Each email contains:
- Meeting summary (AI-generated, may contain errors)
- Topic sections with key discussion points
- Suggested next steps with owner assignments
- Link to full meeting document on Google Docs

## Ingestion Workflow

### 1. Search Gmail for meeting notes

Use multiple search queries for coverage:

```
# Primary: Portuguese "Anotações" (Gemini's default language for pt-BR orgs)
search_gmail_messages(query="Anotações", page_size=20)

# Secondary: English fallback
search_gmail_messages(query="Gemini meeting notes", page_size=20)

# Date-filtered (Gmail search syntax)
search_gmail_messages(query="after:YYYY/MM/DD Anotações", page_size=20)
```

Paginate with `page_token` to go further back if needed.

### 2. Filter by date window

Message IDs are roughly chronological (higher hex = more recent). Batch-fetch with `get_gmail_messages_content_batch` using `format="full"` and `body_format="text"`.

Discard:
- Calendar declines/rejections (they contain "Anotações do Gemini" link but aren't notes)
- Marketing/newsletter emails
- Meetings older than the target window

### 3. Save raw transcripts

Save each meeting as `raw/transcripts/<slug>-YYYY-MM-DD.md` with frontmatter:

```yaml
---
source_url: https://mail.google.com/mail/u/0/#all/<message-id>
ingested: YYYY-MM-DD
sha256: <hex>
---
```

Compute sha256 over the body (below the closing `---`), not the frontmatter.

Format the body as structured markdown:
- `#` title with meeting name and date
- Source attribution line
- `## Resumo` section
- Topic sections from the email
- `## Próximas etapas` with owner-action list

### 4. Skip cancelled meetings

Meetings cancelled due to conflicts produce notes that say "Reunião cancelada" — skip these, they contain no domain knowledge.

### 5. Create wiki pages

Follow the standard ingest flow from the parent skill. For meeting notes specifically:
- Entity pages for squads/teams that appear across multiple meetings
- Concept pages for technical topics, decisions, and initiatives
- Action items go in tables on the relevant concept/entity page

### 6. Bulk efficiency

When ingesting multiple meetings at once:
- Read all raw transcripts first
- Identify entities and concepts across ALL sources
- Create/update pages in one pass
- Update index.md and log.md once at the end

## Pitfalls

- **Message ID chronology is approximate** — confirm dates from email subjects/headers, not just ID position
- **Gemini notes contain AI-generated errors** — always note the auto-generation caveat; mark confidence `medium` on single-source claims
- **Calendar invitation emails contain "Anotações do Gemini" links** — these are NOT meeting notes, skip them
- **Portuguese/English mixing** — some meetings generate notes in English even in pt-BR orgs; check the language note at the top of the email
- **Google Meet vs Gemini sender** — meeting notes can come from both `gemini-notes@google.com` and `meetings-noreply@google.com`; search by subject keyword "Anotações" not by sender
