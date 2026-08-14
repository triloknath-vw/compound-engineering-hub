# Skills

Bundled, on-demand workflows defined in `skills/<skill-name>/SKILL.md`, with
optional `scripts/`, `references/`, and `assets/` subfolders. Agents load only
the `name` + `description` up front, and the full body when relevant.

- Folder: `skills/`
- Template: `skills/_template-skill/` (inert — `user-invocable: false` and
  `disable-model-invocation: true` until you rename and clean it up)
- Full field reference: [VS Code Agent Skills docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

## Rules

- The `name` field in `SKILL.md` **must** match the containing folder name.
- Keep `SKILL.md` under ~500 lines — move detail into `references/`.
- Keep resource references one level deep from `SKILL.md`.
