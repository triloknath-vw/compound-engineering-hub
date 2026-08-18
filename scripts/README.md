# Scripts

Automation for this repository (not for the plugins it publishes).

## `validate_structure.py`

Validates that every real (non-template) agent, prompt, instruction, skill,
and plugin has required frontmatter/manifest fields, and that skill/plugin
folder names match their `name` field. Run before opening a PR:

```bash
python scripts/validate_structure.py
```

## `generate_catalog.py`

Regenerates the "Catalog" tables in `docs/agents.md`, `docs/prompts.md`,
`docs/skills.md`, `docs/plugins.md`, and `MARKETPLACE.md` by scanning the
actual `agents/`, `prompts/`, `skills/`, and `plugins/` folders — so the docs
always list whatever agents/prompts/skills/plugins actually exist, with no
manual bookkeeping. Run after adding or editing any of those:

```bash
python scripts/generate_catalog.py          # rewrite the catalog sections
python scripts/generate_catalog.py --check  # exit 1 if docs are stale (used in CI)
```

## `_catalog.py`

Shared scanning/parsing helpers used by both scripts above (not run directly).

Both `validate_structure.py` and `generate_catalog.py` run automatically in CI
via [`.github/workflows/validate-customizations.yml`](../.github/workflows/validate-customizations.yml).

No dependencies beyond the Python standard library.
