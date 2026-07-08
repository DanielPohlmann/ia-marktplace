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


def main():
    errors, warnings = [], []
    names = defaultdict(list)

    # --- marketplace.json ---
    mkt_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not mkt_path.exists():
        print("FATAL: .claude-plugin/marketplace.json missing")
        return 1
    mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
    declared = {p["name"]: p for p in mkt.get("plugins", [])}

    # --- per plugin ---
    total_skills = 0
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
        skills_dir = src / "skills"
        if not skills_dir.is_dir():
            errors.append(f"plugin '{pname}': no skills/ dir")
            continue

        # forbidden files anywhere under this plugin's skills
        for f in skills_dir.rglob("*"):
            if f.is_file() and f.name in FORBIDDEN_FILES:
                errors.append(f"forbidden file: {f.relative_to(ROOT).as_posix()}")

        for skill_md in skills_dir.rglob("SKILL.md"):
            rel = skill_md.relative_to(skills_dir)
            tag = f"{pname}/{rel.parts[0] if rel.parts else '?'}"
            if len(rel.parts) != 2:
                errors.append(f"SKILL.md not at depth 1: {pname}/skills/{rel.as_posix()}")
                continue
            total_skills += 1
            d = rel.parts[0]
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
