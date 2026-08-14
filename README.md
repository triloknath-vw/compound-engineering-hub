# Compound Engineering Hub

A comprehensive repository of reusable GitHub Copilot configurations — specialized
agents, workflow prompts, custom instructions, agent skills, and installable
plugins — designed to standardize AI-assisted development across teams.

This is a **skeleton**: every category below is wired up and ready to use, but
intentionally ships without example content. Copy a template, fill it in, and
commit.

## What this hub provides

| Category | Folder | What it is |
|---|---|---|
| Custom Instructions | [`.github/copilot-instructions.md`](.github/copilot-instructions.md), [`.github/instructions/`](.github/instructions/) | Always-on and file-scoped guidance that shapes every Copilot chat request |
| Agents | [`agents/`](agents/) | Specialized `.agent.md` personas (tool-restricted, task-focused) usable directly in this repo |
| Prompts | [`prompts/`](prompts/) | Reusable `.prompt.md` slash-command templates for one-off tasks |
| Skills | [`skills/`](skills/) | Bundled, on-demand `SKILL.md` workflows with scripts/templates/references |
| Plugins | [`plugins/`](plugins/) | Installable Copilot CLI plugin bundles (agent + skills + optional MCP, packaged with a `plugin.json`) |
| Marketplace | [`.github/plugin/marketplace.json`](.github/plugin/marketplace.json), [`MARKETPLACE.md`](MARKETPLACE.md) | The machine-readable Copilot CLI marketplace manifest, plus a human-curated catalog page |
| Docs site | [`docs/`](docs/) + [`mkdocs.yml`](mkdocs.yml) | MkDocs source for a browsable documentation site (deployable to GitHub Pages) |
| Automation | [`scripts/`](scripts/), [`.github/workflows/`](.github/workflows/) | Structure validation and docs-deploy CI |

## Repository layout

```text
compound-engineering-hub/
├── .github/
│   ├── copilot-instructions.md      # always-on repo-wide instructions
│   ├── instructions/                # *.instructions.md (file/task scoped)
│   ├── plugin/marketplace.json      # Copilot CLI marketplace manifest
│   └── workflows/                   # CI: validate structure, deploy docs
├── .vscode/
│   └── settings.json                # points VS Code at agents/ and prompts/
├── agents/                          # *.agent.md custom agents
├── prompts/                         # *.prompt.md reusable prompts
├── skills/                          # <skill-name>/SKILL.md agent skills
├── plugins/                         # installable plugin bundles (plugin.json + agents/ + skills/)
├── docs/                            # MkDocs site source
├── scripts/                         # validation & automation scripts
├── MARKETPLACE.md                   # curated, human-readable catalog
├── CONTRIBUTING.md
├── mkdocs.yml
└── requirements-docs.txt
```

## Two ways content gets used

1. **Directly in this workspace** — `agents/`, `prompts/`, `.github/instructions/`
   are picked up automatically by VS Code (see [`.vscode/settings.json`](.vscode/settings.json))
   and `skills/` is picked up by any Copilot surface that supports Agent Skills.
   Add a file, reload the window, done.
2. **Packaged and distributed** — `plugins/<name>/` bundles an agent + skill(s)
   (+ optional MCP server) into a versioned unit that other repos/engineers install
   via `copilot plugin install <name>@compound-engineering-hub`. This is how
   conventions here scale beyond a single repository. See
   [`plugins/README.md`](plugins/README.md) and
   [`.github/plugin/marketplace.json`](.github/plugin/marketplace.json).

## Getting started

1. Pick the category that matches your need (see table above).
2. Copy the template in that folder (`templates/*.template.md`, or
   `_template-skill/`, or `plugins/_template-plugin/`).
3. Rename and fill it in — each template's comments explain every field.
4. Open a pull request. CI validates required frontmatter automatically
   (see [`.github/workflows/validate-customizations.yml`](.github/workflows/validate-customizations.yml)).
5. If it should be installable elsewhere, add an entry to
   [`.github/plugin/marketplace.json`](.github/plugin/marketplace.json).

See [CONTRIBUTING.md](CONTRIBUTING.md) for full conventions, and
[MARKETPLACE.md](MARKETPLACE.md) for the current catalog.

## Documentation site

Full docs (built with MkDocs) live in [`docs/`](docs/). Run locally with:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

The [`deploy-docs`](.github/workflows/deploy-docs.yml) workflow publishes `docs/`
to GitHub Pages on push to `main`.
