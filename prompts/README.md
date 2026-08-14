# Prompts (`.prompt.md`)

Reusable, single-focus task templates invoked with `/` in chat, usable directly
in this workspace (discovered via `chat.promptFilesLocations` in
[`../.vscode/settings.json`](../.vscode/settings.json)).

## Adding a new prompt

1. Copy [`templates/prompt.template.md`](templates/prompt.template.md).
2. Rename to `<kebab-case-name>.prompt.md` and drop it directly in this folder.
3. Fill in `description` and the task body. Keep it to **one** well-defined task
   — don't chain "generate and test and deploy" into a single prompt.
4. Add a row to [`../MARKETPLACE.md`](../MARKETPLACE.md).

## When to use a prompt vs. an agent vs. a skill

- **Prompt**: a single, parameterized, one-off task (e.g. "generate a PR description").
- **Agent**: a reusable persona with its own tool restrictions.
- **Skill**: a multi-step workflow bundling scripts/templates/reference docs.
