<!-- Part of the specs-llm-wiki skill. Loaded on demand from SKILL.md. -->

# Working with the Wiki

## Searching

Use Claude Code's own search tools against the wiki directory:

- **By content** — `Grep` pattern `"transformer"`, path `<WIKI>`, glob `*.md`
- **By filename** — `Glob` pattern `<WIKI>/**/*.md`
- **By tag** — `Grep` pattern `"tags:.*alignment"`, path `<WIKI>`, glob `*.md`
- **Recent activity** — `Read` `<WIKI>/log.md` (last ~20 lines via `offset`/`limit`)

## Bulk Ingest

When ingesting multiple sources at once, batch the updates:
1. Read all sources first
2. Identify all entities and concepts across all sources
3. Check existing pages for all of them (one search pass, not N)
4. Create/update pages in one pass (avoids redundant updates)
5. Update index.md once at the end
6. Write a single log entry covering the batch

## Archiving

When content is fully superseded or the domain scope changes:
1. Create `_archive/` directory if it doesn't exist
2. Move the page to `_archive/` with its original path (e.g., `_archive/entities/old-page.md`)
3. Remove from `index.md`
4. Update any pages that linked to it — replace wikilink with plain text + "(archived)"
5. Log the archive action

## Obsidian Integration

The wiki directory works as an Obsidian vault out of the box:
- `[[wikilinks]]` render as clickable links
- Graph View visualizes the knowledge network
- YAML frontmatter powers Dataview queries
- The `raw/assets/` folder holds images referenced via `![[image.png]]`

For best results:
- Set Obsidian's attachment folder to `raw/assets/`
- Enable "Wikilinks" in Obsidian settings (usually on by default)
- Install Dataview plugin for queries like `TABLE tags FROM "entities" WHERE contains(tags, "company")`

If using the Obsidian skill alongside this one, set `OBSIDIAN_VAULT_PATH` to the
same directory as the wiki path.

## Obsidian Headless (optional — Linux servers only)

> Not applicable on Windows or macOS desktops. Skip unless the wiki lives on a
> headless Linux server that must sync to Obsidian on another device.

On a headless Linux machine, `obsidian-headless` (`npm install -g obsidian-headless`,
Node.js 22+) syncs the vault via Obsidian Sync without a GUI: `ob login`, then
`ob sync-create-remote`, `ob sync-setup --vault <id>`, and `ob sync --continuous`.
Run it in the background with a systemd user service and `loginctl enable-linger`
so it survives logout. This lets an agent write to the wiki on a server while you
browse the same vault in Obsidian on your laptop/phone.

## Dashboard Generation

Generate a self-contained HTML dashboard at `<WIKI>/dashboard.html` for visual browsing.
Full build instructions in `references/dashboard.md`.

The dashboard provides:
- **Sidebar navigation** — entities, concepts, and meeting transcripts with date badges
- **Overview** — stats cards, meeting timeline, SVG knowledge graph with clickable nodes
- **Page rendering** — inline markdown-to-HTML with clickable `[[wikilinks]]`
- **Cross-references** — outbound links and source references on every page
- **Zero dependencies** — single HTML file, opens from `file://` or any static server

Generate after wiki initialization or significant ingests (5+ new pages).
