# Scripts

Automation for this repository (not for the plugins it publishes).

## `validate_structure.py`

Validates that every real (non-template) agent, prompt, instruction, skill,
and plugin has required frontmatter/manifest fields, and that skill/plugin
folder names match their `name` field. Run before opening a PR:

```bash
python scripts/validate_structure.py
```

Also runs automatically in CI via
[`.github/workflows/validate-customizations.yml`](../.github/workflows/validate-customizations.yml).

No dependencies beyond the Python standard library.
