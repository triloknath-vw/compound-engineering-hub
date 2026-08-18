# Prompts

Single-purpose, parameterized task templates in `prompts/*.prompt.md`, invoked
with `/` in chat. Discovered automatically in this workspace via the
`chat.promptFilesLocations` setting.

- Folder: `prompts/`
- Example: `prompts/minutes-of-meeting.prompt.md`
- Full field reference: [VS Code prompt files docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files)

## When to write a prompt instead of an agent

Use a prompt for a single, well-defined, one-off task (e.g. "generate a PR
description", "write unit tests for the selected code"). Use an
[agent](agents.md) when you need a reusable persona with its own tool
restrictions across many tasks.

## Catalog

> Generated from `prompts/*.prompt.md` by `scripts/generate_catalog.py` — do
> not edit by hand, run the script instead.

<!-- CATALOG:PROMPTS:START -->
| Name | Description | Path |
|---|---|---|
| minutes-of-meeting | Generate comprehensive Minutes of Meeting (MoM) from meeting transcripts. Capture discussions, decisions, action items, risks, blockers, dependencies, and… | `prompts/minutes-of-meeting.prompt.md` |
<!-- CATALOG:PROMPTS:END -->

