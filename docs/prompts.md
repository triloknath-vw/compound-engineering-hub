# Prompts

Single-purpose, parameterized task templates in `prompts/*.prompt.md`, invoked
with `/` in chat. Discovered automatically in this workspace via the
`chat.promptFilesLocations` setting.

- Folder: `prompts/`
- Template: `prompts/templates/prompt.template.md`
- Full field reference: [VS Code prompt files docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files)

## When to write a prompt instead of an agent

Use a prompt for a single, well-defined, one-off task (e.g. "generate a PR
description", "write unit tests for the selected code"). Use an
[agent](agents.md) when you need a reusable persona with its own tool
restrictions across many tasks.
