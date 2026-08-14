# Template Plugin

Copy this whole folder to `plugins/<your-plugin-name>/` and:

1. Update `plugin.json` — `name` must match the new folder name.
2. Replace the placeholder files in `agents/` and `skills/` with real content
   (use the templates in [`../../agents/templates/`](../../agents/templates/)
   and [`../../skills/_template-skill/`](../../skills/_template-skill/) as a
   starting point — copy them in here, don't reference them by path, since a
   plugin must be self-contained).
3. Delete this README's instructions and write real usage docs for the plugin.
4. Add a `.mcp.json` at this level only if the plugin genuinely needs an
   external MCP server.
5. Register the plugin in
   [`../../.github/plugin/marketplace.json`](../../.github/plugin/marketplace.json).
