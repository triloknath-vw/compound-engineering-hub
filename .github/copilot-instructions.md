---
description: "Compound Engineering Hub repository conventions for Copilot"
---

# Compound Engineering Hub — Agent Instructions

This repository is a **catalog and packaging system** for GitHub Copilot
customizations, not an application. When working in this repo:

- Treat `agents/`, `prompts/`, `skills/`, `.github/instructions/` as
  **directly-used** customizations for this workspace (auto-discovered by VS
  Code — see [`.vscode/settings.json`](../.vscode/settings.json)).
- Treat `plugins/` as **distributable bundles**: each plugin folder is
  self-contained (its own `plugin.json`, `agents/`, `skills/`) and must not
  depend on files outside itself, since it gets installed standalone elsewhere.
- Never invent example content unless explicitly asked. `agents/`, `prompts/`,
  and `skills/` now contain real examples to use as structural references;
  `.github/instructions/` and `plugins/` still ship template-only.
- When adding any new agent/prompt/skill file, follow the structure of an
  existing file in that folder. For instructions/plugins, follow the exact
  template in that folder's `templates/` (or `_template*`) subfolder. Either
  way, run `python scripts/generate_catalog.py` afterwards so
  [`MARKETPLACE.md`](../MARKETPLACE.md) and `docs/*.md` reflect it (never edit
  those Catalog tables by hand).
- Keep `description` fields keyword-rich ("Use when...") — that's the only
  signal used for on-demand discovery.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full contribution workflow.
