# -*- coding: utf-8 -*-
"""Skills conventions audit for the ia-marketplace repo.

Checks every plugin/skill against the conventions in CLAUDE.md:
  A1  plugin dir has .claude-plugin/plugin.json and is listed in marketplace.json
  A2  skills/ layout is flat: each skill dir has exactly one SKILL.md, one level deep
  A3  no stray files in skill dir besides SKILL.md, references/, scripts/
  B1  frontmatter parses, keys subset of {name, description, allowed-tools}
  B2  name == directory name, matches ^[a-z0-9-]+$, <= 64 chars
  B3  description present, single line, <= 1024 chars
  B4  description has USE FOR / DO NOT USE FOR structure (warning if missing)
  B5  'use <flat-name>' cross-links in description resolve to an existing skill
  C1  '(N skills)' counts in plugin.json and marketplace.json match reality
  C2  body has ## References section only (no frontmatter references key) - covered by B1
"""
import io, json, os, re, sys

ROOT = r"C:\workspace\Diary\Projeto\ia-marktplace"
PLUGINS = ["dev", "stack", "security", "legal", "tools", "QA", "workflows",
           "specs", "custom-agent"]

findings = []  # (severity, plugin, skill, message)
def add(sev, plugin, skill, msg):
    findings.append((sev, plugin, skill or "-", msg))

def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    fm, keys = m.group(1), {}
    current = None
    for line in fm.splitlines():
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            k, _, v = line.partition(":")
            current = k.strip()
            keys[current] = v.strip().strip('"').strip("'")
        elif current and line.startswith((" ", "\t", "-")):
            keys[current] += " | " + line.strip()
    return keys

mk = json.loads(read(os.path.join(ROOT, ".claude-plugin", "marketplace.json")))
mk_plugins = {p["name"]: p for p in mk["plugins"]}

all_skill_names = set()
skill_meta = {}   # flat name -> (plugin, desc)
plugin_counts = {}

for plugin in PLUGINS:
    pdir = os.path.join(ROOT, plugin)
    pj_path = os.path.join(pdir, ".claude-plugin", "plugin.json")
    if plugin not in mk_plugins:
        add("CRIT", plugin, None, "plugin not declared in marketplace.json")
    if not os.path.isfile(pj_path):
        add("CRIT", plugin, None, "missing .claude-plugin/plugin.json")
        continue
    pj = json.loads(read(pj_path))
    sdir = os.path.join(pdir, "skills")
    skills = sorted(d for d in os.listdir(sdir)
                    if os.path.isdir(os.path.join(sdir, d)))
    plugin_counts[plugin] = len(skills)

    for sk in skills:
        skdir = os.path.join(sdir, sk)
        entries = sorted(os.listdir(skdir))
        if "SKILL.md" not in entries:
            add("CRIT", plugin, sk, "no SKILL.md in skill directory")
            continue
        # A3: stray entries
        for e in entries:
            full = os.path.join(skdir, e)
            if os.path.isdir(full):
                if e not in ("references", "scripts"):
                    add("WARN", plugin, sk, "unexpected subdirectory '%s'" % e)
                # nested SKILL.md?
                for base, _, files in os.walk(full):
                    if "SKILL.md" in files:
                        add("CRIT", plugin, sk, "nested SKILL.md under %s" % e)
            elif e != "SKILL.md":
                add("WARN", plugin, sk, "stray file '%s' in skill dir" % e)

        text = read(os.path.join(skdir, "SKILL.md"))
        fm = parse_frontmatter(text)
        if fm is None:
            add("CRIT", plugin, sk, "SKILL.md has no valid frontmatter block")
            continue
        # B1 keys
        extra = set(fm) - {"name", "description", "allowed-tools"}
        if extra:
            add("WARN", plugin, sk, "extra frontmatter keys: %s" % ", ".join(sorted(extra)))
        # B2 name
        name = fm.get("name", "")
        if name != sk:
            add("CRIT", plugin, sk, "frontmatter name '%s' != directory name" % name)
        if not re.match(r"^[a-z0-9-]+$", name or ""):
            add("CRIT", plugin, sk, "name not kebab-case: '%s'" % name)
        if len(name) > 64:
            add("CRIT", plugin, sk, "name longer than 64 chars (%d)" % len(name))
        all_skill_names.add(name)
        # B3 description
        desc = fm.get("description")
        if not desc:
            add("CRIT", plugin, sk, "missing description in frontmatter")
            desc = ""
        if " | " in desc:
            add("WARN", plugin, sk, "description spans multiple lines")
        if len(desc) > 1024:
            add("CRIT", plugin, sk, "description > 1024 chars (%d)" % len(desc))
        skill_meta[name] = (plugin, desc)
        # body size
        body_lines = text.count("\n")
        if body_lines > 500:
            add("INFO", plugin, sk, "SKILL.md is %d lines (>500 guideline: split into references/)" % body_lines)

    # C1 count claims
    m = re.search(r"\((\d+) skills?\)", pj.get("description", ""))
    claimed = int(m.group(1)) if m else None
    if claimed is not None and claimed != len(skills):
        add("CRIT", plugin, None, "plugin.json claims %d skills, found %d" % (claimed, len(skills)))
    mdesc = mk_plugins.get(plugin, {}).get("description", "")
    m2 = re.search(r"\((\d+) skills?\)", mdesc)
    if m2 and int(m2.group(1)) != len(skills):
        add("CRIT", plugin, None, "marketplace.json claims %s skills, found %d" % (m2.group(1), len(skills)))

# B4/B5 second pass: USE FOR structure + cross-links
for name, (plugin, desc) in sorted(skill_meta.items()):
    has_use = "USE FOR" in desc
    has_dont = "DO NOT USE FOR" in desc
    if not (has_use and has_dont):
        add("INFO", plugin, name, "description lacks USE FOR/DO NOT USE FOR structure")
    for ref in re.findall(r"use ([a-z0-9]+(?:-[a-z0-9]+)+)", desc):
        if ref not in all_skill_names and ref != name:
            add("WARN", plugin, name, "cross-link 'use %s' does not resolve to an existing skill" % ref)

# CLAUDE.md / README.md table counts
def check_doc(path, label):
    txt = read(os.path.join(ROOT, path))
    for plugin, n in plugin_counts.items():
        pat = re.compile(r"`?%s`?\*{0,2}\s*\|[^|]*\|?\s*" % re.escape(plugin))
        for line in txt.splitlines():
            if re.match(r"^\|\s*\*{0,2}`?%s`?\*{0,2}\s*\|" % re.escape(plugin), line.strip()):
                nums = re.findall(r"\|\s*(\d+)\s*\|", line)
                if nums and int(nums[0]) != n:
                    add("WARN", plugin, None, "%s table says %s skills, found %d" % (label, nums[0], n))

check_doc("CLAUDE.md", "CLAUDE.md")
check_doc("README.md", "README.md")

# report
order = {"CRIT": 0, "WARN": 1, "INFO": 2}
findings.sort(key=lambda f: (order[f[0]], f[1], f[2]))
total = sum(plugin_counts.values())
print("Plugins: %d | Skills: %d | %s" % (len(plugin_counts), total,
      " ".join("%s=%d" % kv for kv in sorted(plugin_counts.items()))))
print("Findings: %d (CRIT=%d WARN=%d INFO=%d)" % (
    len(findings),
    sum(1 for f in findings if f[0] == "CRIT"),
    sum(1 for f in findings if f[0] == "WARN"),
    sum(1 for f in findings if f[0] == "INFO")))
print()
for sev, plugin, sk, msg in findings:
    print("%-4s %-12s %-42s %s" % (sev, plugin, sk, msg))
