# Skills (`SKILL.md`)

Bundled, on-demand workflows with scripts, templates, and reference docs that
agents load progressively (name + description first, full body only when
relevant). See [VS Code Agent Skills docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills).

## Structure

```text
skills/<skill-name>/
├── SKILL.md           # Required — name field must match the folder name
├── scripts/           # Executable code (optional)
├── references/        # Docs loaded only as needed (optional)
└── assets/            # Templates, boilerplate (optional)
```

## Adding a new skill

1. Copy the [`_template-skill/`](_template-skill/) folder.
2. Rename the folder to `<kebab-case-skill-name>/`.
3. In `SKILL.md`, set `name` to match the new folder name exactly, write a
   keyword-rich `description`, remove `user-invocable: false` /
   `disable-model-invocation: true` (those two lines only keep the *template*
   inert), and replace the body with real step-by-step procedures.
4. Add a row to [`../MARKETPLACE.md`](../MARKETPLACE.md).

## Packaging a skill for distribution

If a skill should be installable in *other* repositories, bundle it into a
[plugin](../plugins/README.md) alongside any agent that uses it, rather than
expecting other repos to copy this folder by hand.
