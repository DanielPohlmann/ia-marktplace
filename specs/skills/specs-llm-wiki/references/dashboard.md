# Wiki Dashboard (Self-Contained HTML)

Generate a standalone HTML dashboard that visualizes the llm-wiki. Zero external dependencies — all wiki data is embedded as JSON in a `<script>` tag.

## When to Generate

- User asks to "visualize the wiki", "create a dashboard", or "see the knowledge graph"
- After a significant ingest (5+ new pages) — offer to regenerate
- After wiki initialization — include dashboard as part of setup

## Architecture

Single HTML file with three layers:

1. **CSS** — Dark theme (GitHub-dark inspired), responsive flexbox layout, CSS variables for colors
2. **HTML** — Sidebar + main content area, empty `<script id="wiki-data">` tag as injection point
3. **JS** — Simple markdown renderer, wikilink navigation, dashboard view with stats/timeline/graph

## Build Process

### Phase 1: Write HTML skeleton

Write the complete HTML with CSS and JS to `$WIKI/dashboard.html`. The JS references `WIKI_DATA` global which will be injected in Phase 2.

Key JS functions needed:
- `md2html(md)` — inline markdown-to-HTML (headings, bold, code, wikilinks, tables, lists)
- `extractLinks(md)` — extract `[[wikilinks]]` from body
- `parseFM(content)` — extract YAML frontmatter + body
- `findPage(slug)` — resolve wikilink slug to page data
- `WIKI.navigate(id)` — page router (dashboard, transcript, entity, concept)
- `WIKI.renderDashboard()` — overview view with stats cards, meeting timeline, SVG knowledge graph

### Phase 2: Inject wiki data

Use a Python script (via `terminal`) to:
1. Walk `$WIKI` directory, read all `.md` files (skip SCHEMA.md, log.md)
2. Parse frontmatter from each
3. Build `{pages: {...}, transcripts: {...}}` JSON
4. Replace the empty `<script id="wiki-data">` tag with `<script>var WIKI_DATA = {...};</script>`

```python
import json, os, re

WIKI = os.environ.get("WIKI_PATH") or os.path.join(os.getcwd(), "wiki")
pages = {}
transcripts = {}

for root, dirs, files in os.walk(WIKI):
    for f in files:
        if not f.endswith('.md'): continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, WIKI)
        with open(path) as fh:
            content = fh.read()
        # Parse frontmatter + body
        fm, body = parse_fm(content)
        if 'raw/transcripts/' in rel:
            transcripts[rel] = {'fm': fm, 'body': body}
        elif rel not in ('SCHEMA.md', 'log.md'):
            pages[rel] = {'fm': fm, 'body': body}

wiki_data = json.dumps({'pages': pages, 'transcripts': transcripts}, ensure_ascii=False)

with open(f'{WIKI}/dashboard.html') as f:
    html = f.read()
html = html.replace(
    '<script id="wiki-data" type="application/json"></script>',
    f'<script id="wiki-data" type="application/json">var WIKI_DATA = {wiki_data};</script>'
)
with open(f'{WIKI}/dashboard.html', 'w') as f:
    f.write(html)
```

## Dashboard Views

### Overview (default)
- **Stats cards** — page count, entity count, concept count, meeting count
- **Meeting timeline** — vertical timeline from transcripts sorted by date
- **Knowledge graph** — SVG with colored nodes (green=entity, blue=concept), edges for wikilinks, clickable nodes

### Entity / Concept pages
- Rendered markdown body
- Tags bar below header
- Cross-references section at bottom (outbound wikilinks as clickable pills)
- Sources section (links to raw transcripts)

### Meeting transcripts
- Rendered markdown body
- Source metadata in header

### Page not found
- Friendly empty state for broken wikilinks

## Design Decisions

- **Self-contained** — no CDN, no npm, no build step. Open from `file://` or serve static.
- **Dark theme** — GitHub-dark palette: `#0d1117` bg, `#e6edf3` text, `#58a6ff` accent
- **CSS variables** — all colors in `:root`, easy to retheme
- **Simple markdown renderer** — ~60 lines of JS, handles the wiki's markdown subset (headings, bold, code, wikilinks, tables, lists, blockquotes)
- **Wikilink navigation** — `[[page-name]]` rendered as clickable spans, resolved against page slugs
- **SVG graph** — positioned on a grid (5 columns), edges from wikilink extraction, height scales with node count

## Pitfalls

- **Run the build script through the `Bash` tool** — save the Python above to a file and run it with `python`. Use plain `open()` for reading files during the build.
- **Python f-string escaping** — `{{` and `}}` in CSS/JS conflict with Python f-string/format. Write the HTML skeleton with the `Write` tool (no escaping issues), then inject the data via the Python script.
- **Frontmatter parsing** — handle both string and array values (`tags: [a, b]` vs `tags: a`)
- **File size** — dashboard grows with wiki content. At 10 pages + 3 transcripts, ~42KB is typical. For 100+ pages, consider lazy-loading or pagination.
- **Wikilink edge cases** — slugs are lowercase-hyphenated. The `findPage()` function must normalize accordingly.
