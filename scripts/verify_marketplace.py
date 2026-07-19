#!/usr/bin/env python3
"""Validate the ia-marketplace: marketplace.json, plugin manifests, and every
flat skill (<plugin>/skills/<name>/SKILL.md). Exit 0 when clean, 1 on errors.

Errors block a valid marketplace load. Warnings are quality/convention nits
(triggering structure, oversized SKILL.md) that don't break loading.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9-]+$")
FORBIDDEN_KEYS = ("license", "compatibility", "references", "metadata")
FORBIDDEN_FILES = ("AGENTS.md", "README.md", "metadata.json")
ALLOWED_KEYS = {"name", "description", "allowed-tools"}
ALLOWED_SKILL_DIRS = {"references", "scripts"}
# `use <name>` cross-links in descriptions must resolve to a sibling skill.
# Namespaced refs (`plugin:skill`) point at external marketplaces and are
# allowed as-is (see CLAUDE.md "Naming & invocation"); these bare names are
# known external skills; NON_LINKS are prose that merely looks like a link.
XLINK_RE = re.compile(r"use ([a-z0-9]+(?:[-:][a-z0-9]+)+)")
EXTERNAL_BARE_XLINKS = {
    "vue-best-practices",
    "vue-testing-best-practices",
    "interface-design",
}
NON_LINKS = {"platform-specific"}
COUNT_RE = re.compile(r"\((\d+) skills?\)")


def split_frontmatter(text):
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        return None
    return parts[1]


def scalar(fm, key):
    m = re.search(rf"(?m)^{key}:[ \t]*(.*)$", fm)
    return m.group(1) if m else None


def top_level_keys(fm):
    return re.findall(r"(?m)^([A-Za-z0-9_-]+):", fm)


def doc_count_claims(text, plugin):
    """Yield every skill-count claim for `plugin` in a CLAUDE.md/README.md:
    table rows (first numeric cell) and structure-tree lines '(N skills)'/'(N)'."""
    table_re = re.compile(
        r"^\|\s*\*{0,2}`?%s`?\*{0,2}\s*\|" % re.escape(plugin))
    tree_re = re.compile(
        r"[├└]──\s*%s/.*\((\d+)(?:\s*skills?)?\)" % re.escape(plugin))
    for line in text.splitlines():
        if table_re.match(line.strip()):
            cells = [c.strip() for c in line.split("|")]
            for c in cells:
                if c.isdigit():
                    yield int(c), line.strip()
                    break
        m = tree_re.search(line)
        if m:
            yield int(m.group(1)), line.strip()


def main():
    errors, warnings = [], []
    names = defaultdict(list)
    descs = {}          # flat skill name -> (tag, description)
    plugin_counts = {}  # plugin name -> real skill count

    # --- marketplace.json ---
    mkt_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not mkt_path.exists():
        print("FATAL: .claude-plugin/marketplace.json missing")
        return 1
    mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
    declared = {p["name"]: p for p in mkt.get("plugins", [])}

    # --- per plugin ---
    total_skills = 0
    pj_descs = {}
    for pname, p in declared.items():
        src = (ROOT / p["source"]).resolve()
        if not src.is_dir():
            errors.append(f"plugin '{pname}': source '{p['source']}' missing")
            continue
        manifest = src / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            errors.append(f"plugin '{pname}': no .claude-plugin/plugin.json")
        else:
            mj = json.loads(manifest.read_text(encoding="utf-8"))
            if mj.get("name") != pname:
                errors.append(
                    f"plugin '{pname}': plugin.json name '{mj.get('name')}' != marketplace name"
                )
            pj_descs[pname] = mj.get("description", "")
        skills_dir = src / "skills"
        if not skills_dir.is_dir():
            errors.append(f"plugin '{pname}': no skills/ dir")
            continue

        # forbidden files anywhere under this plugin's skills
        for f in skills_dir.rglob("*"):
            if f.is_file() and f.name in FORBIDDEN_FILES:
                errors.append(f"forbidden file: {f.relative_to(ROOT).as_posix()}")

        plugin_counts[pname] = 0
        for skill_md in skills_dir.rglob("SKILL.md"):
            rel = skill_md.relative_to(skills_dir)
            tag = f"{pname}/{rel.parts[0] if rel.parts else '?'}"
            if len(rel.parts) != 2:
                errors.append(f"SKILL.md not at depth 1: {pname}/skills/{rel.as_posix()}")
                continue
            total_skills += 1
            plugin_counts[pname] += 1
            d = rel.parts[0]

            # skill dir anatomy: SKILL.md + references/ + scripts/ only
            for entry in skill_md.parent.iterdir():
                if entry.is_dir() and entry.name not in ALLOWED_SKILL_DIRS:
                    errors.append(f"{tag}: unexpected subdirectory '{entry.name}/'")
                elif entry.is_file() and entry.name != "SKILL.md":
                    errors.append(f"{tag}: stray file '{entry.name}' in skill dir")
            body = skill_md.read_text(encoding="utf-8")
            fm = split_frontmatter(body)
            if fm is None:
                errors.append(f"{tag}: missing/invalid frontmatter")
                continue

            name = scalar(fm, "name")
            if name is None:
                errors.append(f"{tag}: no name")
            else:
                name = name.strip().strip('"').strip("'")
                names[name].append(tag)
                if name != d:
                    errors.append(f"{tag}: name '{name}' != dir name '{d}'")
                if not NAME_RE.match(name):
                    errors.append(f"{tag}: name '{name}' not ^[a-z0-9-]+$")
                if len(name) > 64:
                    errors.append(f"{tag}: name > 64 chars")

            desc = scalar(fm, "description")
            if desc is None:
                errors.append(f"{tag}: no description")
            else:
                dstrip = desc.strip()
                if dstrip in ("", "|", ">", "|-", ">-", "|+", ">+"):
                    errors.append(f"{tag}: multi-line/block description")
                elif len(desc) > 1024:
                    errors.append(f"{tag}: description > 1024 chars ({len(desc)})")
                else:
                    if "USE FOR" not in desc:
                        warnings.append(f"{tag}: description has no 'USE FOR' cue")
                    if "DO NOT USE FOR" not in desc:
                        warnings.append(f"{tag}: description has no 'DO NOT USE FOR' cue")
                if name:
                    descs[name] = (tag, desc.strip().strip('"').strip("'"))


            for k in top_level_keys(fm):
                if k in FORBIDDEN_KEYS:
                    errors.append(f"{tag}: forbidden frontmatter key '{k}'")
                elif k not in ALLOWED_KEYS:
                    warnings.append(f"{tag}: unexpected frontmatter key '{k}'")

            nlines = body.count("\n") + 1
            if nlines > 500:
                warnings.append(f"{tag}: SKILL.md {nlines} lines (>500)")

    for n, tags in names.items():
        if len(tags) > 1:
            errors.append(f"duplicate skill name '{n}': {tags}")

    # --- '(N skills)' claims must match real counts ---
    for pname, real in plugin_counts.items():
        for label, text in (
            ("plugin.json", pj_descs.get(pname, "")),
            ("marketplace.json", declared[pname].get("description", "")),
        ):
            m = COUNT_RE.search(text)
            if m and int(m.group(1)) != real:
                errors.append(
                    f"plugin '{pname}': {label} claims {m.group(1)} skills, found {real}"
                )
        for doc in ("CLAUDE.md", "README.md"):
            path = ROOT / doc
            if not path.exists():
                continue
            for claimed, line in doc_count_claims(
                path.read_text(encoding="utf-8"), pname
            ):
                if claimed != real:
                    errors.append(
                        f"plugin '{pname}': {doc} claims {claimed} skills, "
                        f"found {real} — '{line[:60]}'"
                    )

    # --- cross-links in descriptions resolve to a sibling or known external ---
    for name, (tag, desc) in sorted(descs.items()):
        for ref in XLINK_RE.findall(desc):
            if ref == name or ref in names or ref in NON_LINKS:
                continue
            if ":" in ref or ref in EXTERNAL_BARE_XLINKS:
                continue  # external marketplace — allowed, see CLAUDE.md
            errors.append(
                f"{tag}: cross-link 'use {ref}' resolves to no skill "
                f"(rename it, or allowlist it if external)"
            )

    print(f"Plugins declared: {len(declared)} | Skills found: {total_skills}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in sorted(warnings):
            print("  ~", w)
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in sorted(errors):
            print("  -", e)
        print("\nverify-marketplace FAILED")
        return 1
    print("\nverify-marketplace OK — marketplace is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
