# Agents (`.agent.md`)

Specialist personas with restricted tools and a focused system prompt, usable
directly in this workspace (discovered via `chat.agentFilesLocations` in
[`../.vscode/settings.json`](../.vscode/settings.json)).

## Adding a new agent

1. Copy [`templates/agent.template.md`](templates/agent.template.md).
2. Rename to `<kebab-case-name>.agent.md` and drop it directly in this folder.
3. Fill in `description` (keyword-rich — this is how the agent picker and
   subagent delegation find it), `tools` (minimal set needed), and the body
   persona/constraints/approach.
4. Add a row to [`../MARKETPLACE.md`](../MARKETPLACE.md).

## When to use an agent vs. a prompt vs. a skill

- **Agent**: needs its own tool restrictions or persona, reusable across many tasks.
- **Prompt**: a single, parameterized, one-off task.
- **Skill**: a multi-step workflow that bundles scripts/templates/reference docs.

## Packaging an agent for distribution

If an agent should be installable in *other* repositories (not just used here),
don't leave it only in this folder — bundle it into a
[plugin](../plugins/README.md) instead, so it ships with its supporting skills
and any MCP servers it needs.
