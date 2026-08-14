"""Validate frontmatter and manifests for agents, prompts, skills, instructions, and plugins.

Skips anything under a `templates/` folder or named `_template*`, since those
are intentionally-inert starter files, not real content.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def is_template_path(path: Path) -> bool:
    return any(part == "templates" or part.startswith("_template") for part in path.parts)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Minimal parser for simple `key: value` YAML frontmatter (no nesting)."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    fields: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_markdown_files(folder: Path, suffix: str, required: tuple[str, ...]) -> list[str]:
    errors: list[str] = []
    if not folder.exists():
        return errors
    for path in sorted(folder.rglob(f"*{suffix}")):
        if is_template_path(path.relative_to(REPO_ROOT)):
            continue
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter(text)
        rel = path.relative_to(REPO_ROOT)
        if fields is None:
            errors.append(f"{rel}: missing YAML frontmatter (must start with '---')")
            continue
        for field in required:
            if not fields.get(field):
                errors.append(f"{rel}: missing required frontmatter field '{field}'")
    return errors


def check_skills(folder: Path) -> list[str]:
    errors: list[str] = []
    if not folder.exists():
        return errors
    for skill_dir in sorted(p for p in folder.iterdir() if p.is_dir()):
        if is_template_path(skill_dir.relative_to(REPO_ROOT)):
            continue
        skill_md = skill_dir / "SKILL.md"
        rel = skill_dir.relative_to(REPO_ROOT)
        if not skill_md.exists():
            errors.append(f"{rel}: missing SKILL.md")
            continue
        fields = parse_frontmatter(skill_md.read_text(encoding="utf-8")) or {}
        if not fields.get("description"):
            errors.append(f"{rel}/SKILL.md: missing required frontmatter field 'description'")
        name = fields.get("name")
        if name and name != skill_dir.name:
            errors.append(f"{rel}/SKILL.md: name '{name}' does not match folder name '{skill_dir.name}'")

    return errors


def check_plugins(folder: Path) -> list[str]:
    errors: list[str] = []
    if not folder.exists():
        return errors
    for plugin_dir in sorted(p for p in folder.iterdir() if p.is_dir()):
        if is_template_path(plugin_dir.relative_to(REPO_ROOT)):
            continue
        manifest = plugin_dir / "plugin.json"
        rel = plugin_dir.relative_to(REPO_ROOT)
        if not manifest.exists():
            errors.append(f"{rel}: missing plugin.json")
            continue
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}/plugin.json: invalid JSON ({exc})")
            continue
        name = data.get("name")
        if not name:
            errors.append(f"{rel}/plugin.json: missing required field 'name'")
        elif name != plugin_dir.name:
            errors.append(f"{rel}/plugin.json: name '{name}' does not match folder name '{plugin_dir.name}'")
        for path_field in ("agents", "skills"):
            declared = data.get(path_field)
            if declared and not (plugin_dir / declared).exists():
                errors.append(f"{rel}/plugin.json: '{path_field}' path '{declared}' does not exist")
    return errors


def check_marketplace_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return errors
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.relative_to(REPO_ROOT)}: invalid JSON ({exc})"]
    for entry in data.get("plugins", []):
        if not entry.get("name") or not entry.get("source"):
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: plugin entry {entry!r} missing 'name' or 'source'"
            )
    return errors


def main() -> int:
    errors: list[str] = []
    errors += check_markdown_files(REPO_ROOT / "agents", ".agent.md", ("description",))
    errors += check_markdown_files(REPO_ROOT / "prompts", ".prompt.md", ("description",))
    errors += check_markdown_files(
        REPO_ROOT / ".github" / "instructions", ".instructions.md", ("description",)
    )
    errors += check_skills(REPO_ROOT / "skills")
    errors += check_plugins(REPO_ROOT / "plugins")
    errors += check_marketplace_manifest(REPO_ROOT / ".github" / "plugin" / "marketplace.json")

    if errors:
        print("Validation failed:\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("All agents, prompts, instructions, skills, and plugins are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
