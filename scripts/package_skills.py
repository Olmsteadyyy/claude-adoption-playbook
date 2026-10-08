"""Check every Skill in skills/ and build upload-ready zips.

Usage:
    python scripts/package_skills.py           # check, then write zips to dist/
    python scripts/package_skills.py --check   # check only (used by CI)

Checks, per the Claude help center's custom Skill requirements:
  - SKILL.md starts with YAML frontmatter holding name and description
  - name is 64 characters or fewer and matches the folder name
  - description is 200 characters or fewer
Each zip has the Skill folder as its root, which is what the Claude apps expect.
"""

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            fields[key.strip()] = value.strip()
    return fields


def check(folder):
    problems = []
    skill_file = folder / "SKILL.md"
    if not skill_file.exists():
        return ["no SKILL.md"]
    fields = frontmatter(skill_file.read_text(encoding="utf-8"))
    if fields is None:
        return ["SKILL.md does not start with YAML frontmatter"]
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        problems.append("missing name")
    elif len(name) > 64:
        problems.append(f"name is {len(name)} characters (max 64)")
    elif name != folder.name:
        problems.append(f"name '{name}' does not match folder '{folder.name}'")
    if not description:
        problems.append("missing description")
    elif len(description) > 200:
        problems.append(f"description is {len(description)} characters (max 200)")
    return problems


def package(folder):
    DIST.mkdir(exist_ok=True)
    target = DIST / f"{folder.name}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                archive.write(path, Path(folder.name) / path.relative_to(folder))
    return target


def main():
    check_only = "--check" in sys.argv
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    failed = False
    for folder in folders:
        problems = check(folder)
        if problems:
            failed = True
            print(f"FAIL  {folder.name}: {'; '.join(problems)}")
        elif check_only:
            print(f"ok    {folder.name}")
        else:
            print(f"ok    {folder.name} -> {package(folder).relative_to(ROOT)}")
    if failed:
        sys.exit(1)
    print(f"\n{len(folders)} Skills checked.")


if __name__ == "__main__":
    main()
