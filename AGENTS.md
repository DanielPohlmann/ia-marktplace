# AGENTS.md — ia-marketplace

Agent contributor guide for this marketplace repo. For structure, plugin layout,
naming, and the full "add a skill" workflow, see [`CLAUDE.md`](CLAUDE.md) — this
file only covers the invariants that must hold for the marketplace to load.

## Invariants (don't break these)

1. **One `SKILL.md` per skill, one level deep.** Every skill is
   `<plugin>/skills/<skill-name>/SKILL.md`. Claude Code does not discover nested
   skills — never add a subdirectory that itself contains a `SKILL.md`.
2. **`name` == directory name.** The SKILL.md `name:` frontmatter must exactly
   match its directory name (kebab-case, `^[a-z0-9-]+$`, ≤ 64 chars) and keep its
   domain prefix.
3. **Single-line `description`.** ≤ 1024 chars, no block scalars. Keep the
   `USE FOR` / `DO NOT USE FOR` structure; `DO NOT USE FOR` cross-links siblings
   by their flat name.
4. **Frontmatter is `name` + `description` only** (plus `allowed-tools` when
   needed). No `license`, `compatibility`, or `references` keys.
5. **No `AGENTS.md` / `README.md` / `metadata.json` inside a skill directory.**
6. **Every plugin has a manifest.** `<plugin>/.claude-plugin/plugin.json` with at
   least a `name`, and a matching entry in `.claude-plugin/marketplace.json`
   whose `source` is the relative path to the plugin root.

## When you add or remove a plugin

- Create/delete `<plugin>/.claude-plugin/plugin.json` **and** update the
  `plugins` array in `.claude-plugin/marketplace.json`.
- Update the plugin tables in `CLAUDE.md` and `README.md`, and the skill counts.
- Add a `CHANGELOG.md` entry.

## When you add or remove a skill

- Update the skill count in `marketplace.json` (plugin description),
  `CLAUDE.md`, and `README.md`.
- If a consuming project references the skill by name (e.g. LinkDaily's
  `CLAUDE.md` tables), update it there too — invocations use the
  `<plugin>:<skill>` namespaced form.
