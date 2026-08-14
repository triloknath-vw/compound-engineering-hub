# Plugins

An installable, versioned bundle of one or more agents/skills (and optionally
an MCP server) that other engineers or repositories install with:

```bash
copilot plugin install <plugin-name>@compound-engineering-hub
```

This packaging convention (and the marketplace manifest at
[`../.github/plugin/marketplace.json`](../.github/plugin/marketplace.json))
follows the internal [Copilot Marketplace Guide](../../copilot-marketplace-guide/README.md)
— read `03-building-a-plugin/` and `04-building-a-marketplace/` there for the
full explanation before publishing a real plugin.

## Structure

```text
plugins/<plugin-name>/
├── plugin.json         # manifest: name, description, version, agents/skills paths
├── agents/              # *.agent.md bundled with this plugin
├── skills/               # <skill-name>/SKILL.md bundled with this plugin
└── .mcp.json            # optional — only if the workflow needs an external MCP server
```

Each plugin folder must be **self-contained**: it should not reference files
outside itself, since it gets copied/installed standalone into other
environments.

## Adding a new plugin

1. Copy [`_template-plugin/`](_template-plugin/) to `plugins/<kebab-case-name>/`.
2. Fill in `plugin.json` (`name`, `description`, `version`, `author`, `license`, `keywords`).
3. Add real `agents/*.agent.md` and/or `skills/<name>/SKILL.md` inside the plugin folder.
4. Add a `.mcp.json` only if genuinely needed — see the security guidance in
   `copilot-marketplace-guide/05-enterprise-and-governance/`.
5. Register it in [`../.github/plugin/marketplace.json`](../.github/plugin/marketplace.json)
   under `plugins`, and add a row to [`../MARKETPLACE.md`](../MARKETPLACE.md).
6. Get at least one other engineer to review the manifest and any MCP config
   before merging (principle of least privilege — see the review checklist in
   [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Try a plugin locally

```bash
copilot plugin install ./plugins/<plugin-name>
copilot plugin list
```

Plugin contents are cached at install time — reinstall after editing.
