"""Regenerate the catalog tables in docs/*.md and MARKETPLACE.md from actual repo content.

Scans agents/, prompts/, skills/, plugins/ (via `_catalog.py`) and writes a
markdown table between `<!-- CATALOG:<SECTION>:START -->` / `:END` markers in
each target file, so the docs always reflect what's actually in the repo
instead of relying on someone remembering to update them by hand.

Usage:
    python scripts/generate_catalog.py          # rewrite the catalog sections
    python scripts/generate_catalog.py --check  # exit 1 if a rewrite would change anything (CI)
"""
from __future__ import annotations

import re
import sys

from _catalog import REPO_ROOT, CatalogItem, list_agents, list_plugins, list_prompts, list_skills

EMPTY_NOTE = "_None yet — see [Contributing](contributing.md) for how to add one._"
MAX_DESCRIPTION_LENGTH = 160


def truncate(text: str, limit: int = MAX_DESCRIPTION_LENGTH) -> str:
    text = " ".join(text.split())  # collapse newlines/whitespace so the table row stays one line
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + "…"


def build_table(items: list[CatalogItem], *, columns: tuple[str, ...], as_link: bool) -> str:
    if not items:
        return EMPTY_NOTE
    header = "| " + " | ".join(columns) + " |\n" + "|" + "|".join(["---"] * len(columns)) + "|"
    rows = []
    for item in items:
        posix_path = item.path.as_posix()
        path_cell = f"[`{posix_path}`]({posix_path})" if as_link else f"`{posix_path}`"
        description = truncate(item.description) if item.description else "_(no description)_"
        cells = [item.name, description, path_cell]
        if "Version" in columns:
            cells.insert(2, item.version or "_(unset)_")
        rows.append("| " + " | ".join(cells) + " |")
    return header + "\n" + "\n".join(rows)


def splice(text: str, section: str, content: str) -> str:
    start = f"<!-- CATALOG:{section}:START -->"
    end = f"<!-- CATALOG:{section}:END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise ValueError(f"Markers {start} / {end} not found")
    return pattern.sub(f"{start}\n{content}\n{end}", text)


def update_file(path, sections: dict[str, str]) -> bool:
    """Returns True if the file's content changed."""
    original = path.read_text(encoding="utf-8")
    updated = original
    for section, content in sections.items():
        updated = splice(updated, section, content)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    check_only = "--check" in sys.argv

    agents = list_agents()
    prompts = list_prompts()
    skills = list_skills()
    plugins = list_plugins()

    docs_targets = {
        REPO_ROOT / "docs" / "agents.md": {
            "AGENTS": build_table(agents, columns=("Name", "Description", "Path"), as_link=False)
        },
        REPO_ROOT / "docs" / "prompts.md": {
            "PROMPTS": build_table(prompts, columns=("Name", "Description", "Path"), as_link=False)
        },
        REPO_ROOT / "docs" / "skills.md": {
            "SKILLS": build_table(skills, columns=("Name", "Description", "Path"), as_link=False)
        },
        REPO_ROOT / "docs" / "plugins.md": {
            "PLUGINS": build_table(
                plugins, columns=("Name", "Description", "Version", "Path"), as_link=False
            )
        },
        REPO_ROOT / "MARKETPLACE.md": {
            "AGENTS": build_table(agents, columns=("Name", "Description", "Path"), as_link=True),
            "PROMPTS": build_table(prompts, columns=("Name", "Description", "Path"), as_link=True),
            "SKILLS": build_table(skills, columns=("Name", "Description", "Path"), as_link=True),
            "PLUGINS": build_table(
                plugins, columns=("Name", "Description", "Version", "Path"), as_link=True
            ),
        },
    }

    changed = []
    for path, sections in docs_targets.items():
        if check_only:
            original = path.read_text(encoding="utf-8")
            updated = original
            for section, content in sections.items():
                updated = splice(updated, section, content)
            if updated != original:
                changed.append(path.relative_to(REPO_ROOT))
        elif update_file(path, sections):
            changed.append(path.relative_to(REPO_ROOT))

    if check_only:
        if changed:
            print("Catalog is out of date. Run `python scripts/generate_catalog.py` to fix:")
            for path in changed:
                print(f"  - {path}")
            return 1
        print("Catalog is up to date.")
        return 0

    if changed:
        print("Updated catalog in:")
        for path in changed:
            print(f"  - {path}")
    else:
        print("Catalog already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
