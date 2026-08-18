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

1. Create a `<kebab-case-skill-name>/` folder with a `SKILL.md` inside — use
   [`readme-blueprint-generator/SKILL.md`](readme-blueprint-generator/SKILL.md)
   as a reference for structure and frontmatter.
2. Set `name` to match the folder name exactly, and write a keyword-rich
   `description`.
3. Add a row to [`../MARKETPLACE.md`](../MARKETPLACE.md).

## Packaging a skill for distribution

If a skill should be installable in *other* repositories, bundle it into a
[plugin](../plugins/README.md) alongside any agent that uses it, rather than
expecting other repos to copy this folder by hand.
