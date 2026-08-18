# Plugins

A plugin is a versioned, installable bundle of one or more agents/skills (and
optionally an MCP server), packaged with a `plugin.json` manifest. This is how
conventions in this hub scale to other repositories: instead of copying an
`agents/` folder by hand, wrap it in a plugin and let engineers run

```bash
copilot plugin install <plugin-name>@compound-engineering-hub
```

- Folder: `plugins/<plugin-name>/`
- Template: `plugins/_template-plugin/`
- Background reading: the internal
  [Copilot Marketplace Guide](../../copilot-marketplace-guide/README.md),
  specifically `03-building-a-plugin/` and `05-enterprise-and-governance/`
  (security review checklist).

## `plugin.json` fields

| Field | Required | Purpose |
|---|---|---|
| `name` | Yes | Must match the folder name |
| `description` | Recommended | What workflow this plugin standardizes |
| `version` | Recommended | Semantic version, bump on every change |
| `author` | Recommended | Who owns/maintains it |
| `agents` / `skills` | Recommended | Relative paths to the bundled content |

See [Marketplace](marketplace.md) for how plugins get registered and discovered.

## Catalog

> Generated from `plugins/*/plugin.json` by `scripts/generate_catalog.py` — do
> not edit by hand, run the script instead.

<!-- CATALOG:PLUGINS:START -->
_None yet — see [Contributing](contributing.md) for how to add one._
<!-- CATALOG:PLUGINS:END -->
