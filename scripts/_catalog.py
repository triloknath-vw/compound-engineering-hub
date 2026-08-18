"""Shared scanning helpers for agents/prompts/skills/plugins in this repo.

Used by both `validate_structure.py` (frontmatter/manifest checks) and
`generate_catalog.py` (docs/MARKETPLACE.md catalog tables), so the two stay
consistent about what counts as "real" content vs. a template.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
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


@dataclass
class CatalogItem:
    name: str
    description: str
    path: Path  # relative to REPO_ROOT
    version: str = ""


def _iter_real_markdown_files(folder: Path, suffix: str):
    if not folder.exists():
        return
    for path in sorted(folder.rglob(f"*{suffix}")):
        rel = path.relative_to(REPO_ROOT)
        if is_template_path(rel):
            continue
        yield path, rel


def list_agents() -> list[CatalogItem]:
    items = []
    for path, rel in _iter_real_markdown_files(REPO_ROOT / "agents", ".agent.md"):
        fields = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
        fallback_name = path.name.removesuffix(".agent.md")
        items.append(CatalogItem(fields.get("name", fallback_name), fields.get("description", ""), rel))
    return items


def list_prompts() -> list[CatalogItem]:
    items = []
    for path, rel in _iter_real_markdown_files(REPO_ROOT / "prompts", ".prompt.md"):
        fields = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
        fallback_name = path.name.removesuffix(".prompt.md")
        items.append(CatalogItem(fields.get("name", fallback_name), fields.get("description", ""), rel))
    return items


def list_skills() -> list[CatalogItem]:
    items = []
    folder = REPO_ROOT / "skills"
    if not folder.exists():
        return items
    for skill_dir in sorted(p for p in folder.iterdir() if p.is_dir()):
        rel = skill_dir.relative_to(REPO_ROOT)
        if is_template_path(rel):
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        fields = parse_frontmatter(skill_md.read_text(encoding="utf-8")) or {}
        items.append(
            CatalogItem(fields.get("name", skill_dir.name), fields.get("description", ""), rel / "SKILL.md")
        )
    return items


def list_plugins() -> list[CatalogItem]:
    items = []
    folder = REPO_ROOT / "plugins"
    if not folder.exists():
        return items
    for plugin_dir in sorted(p for p in folder.iterdir() if p.is_dir()):
        rel = plugin_dir.relative_to(REPO_ROOT)
        if is_template_path(rel):
            continue
        manifest = plugin_dir / "plugin.json"
        if not manifest.exists():
            continue
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        items.append(
            CatalogItem(
                data.get("name", plugin_dir.name),
                data.get("description", ""),
                rel / "plugin.json",
                version=data.get("version", ""),
            )
        )
    return items
