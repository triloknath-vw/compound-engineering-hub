# Agents

Specialist personas defined in `agents/*.agent.md`, with restricted tools and a
focused system prompt. Discovered automatically in this workspace via the
`chat.agentFilesLocations` setting.

- Folder: [`agents/`](https://github.com/) <!-- update link once repo is pushed -->
- Examples: `agents/mom.agent.md`, `agents/planner.agent.md`
- Full field reference: [VS Code custom agents docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

## Frontmatter fields

| Field | Required | Purpose |
|---|---|---|
| `description` | Yes | Discovery signal for the agent picker and subagent delegation |
| `tools` | No | Minimal set of tool aliases/MCP tools this agent needs |
| `model` | No | Preferred model, with optional fallback array |
| `user-invocable` | No | Show in the agent picker (default `true`) |
| `disable-model-invocation` | No | Prevent use as a subagent (default `false`) |

See [Contributing](contributing.md) for the step-by-step process to add one.

## Catalog

> Generated from `agents/*.agent.md` by `scripts/generate_catalog.py` — do not
> edit by hand, run the script instead.

<!-- CATALOG:AGENTS:START -->
| Name | Description | Path |
|---|---|---|
| MoM Agent | Generate comprehensive Minutes of Meeting (MoM) from meeting transcripts. Capture discussions, decisions, action items, risks, blockers, dependencies, and… | `agents/mom.agent.md` |
| Planner | Researches and outlines multi-step plans | `agents/planner.agent.md` |
<!-- CATALOG:AGENTS:END -->
