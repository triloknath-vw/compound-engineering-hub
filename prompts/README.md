# Prompts (`.prompt.md`)

Reusable, single-focus task templates invoked with `/` in chat, usable directly
in this workspace (discovered via `chat.promptFilesLocations` in
[`../.vscode/settings.json`](../.vscode/settings.json)).

## Adding a new prompt

1. Create `<kebab-case-name>.prompt.md` directly in this folder — use
   [`minutes-of-meeting.prompt.md`](minutes-of-meeting.prompt.md) as a
   reference for structure and frontmatter.
2. Fill in `description` and the task body. Keep it to **one** well-defined task
   — don't chain "generate and test and deploy" into a single prompt.
3. Add a row to [`../MARKETPLACE.md`](../MARKETPLACE.md).

## When to use a prompt vs. an agent vs. a skill

- **Prompt**: a single, parameterized, one-off task (e.g. "generate a PR description").
- **Agent**: a reusable persona with its own tool restrictions.
- **Skill**: a multi-step workflow bundling scripts/templates/reference docs.
