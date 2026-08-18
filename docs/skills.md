# Skills

Bundled, on-demand workflows defined in `skills/<skill-name>/SKILL.md`, with
optional `scripts/`, `references/`, and `assets/` subfolders. Agents load only
the `name` + `description` up front, and the full body when relevant.

- Folder: `skills/`
- Example: `skills/readme-blueprint-generator/SKILL.md`
- Full field reference: [VS Code Agent Skills docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

## Rules

- The `name` field in `SKILL.md` **must** match the containing folder name.
- Keep `SKILL.md` under ~500 lines — move detail into `references/`.
- Keep resource references one level deep from `SKILL.md`.

## Catalog

> Generated from `skills/*/SKILL.md` by `scripts/generate_catalog.py` — do not
> edit by hand, run the script instead.

<!-- CATALOG:SKILLS:START -->
| Name | Description | Path |
|---|---|---|
| readme-blueprint-generator | Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot… | `skills/readme-blueprint-generator/SKILL.md` |
| llm-pitfall-resolver | Detects and resolves common LLM pitfalls in generated text, such as hallucinations, contradictions, and inconsistencies. Provides suggestions for improving clarity, accuracy, and coherence… | `skills/llm-pitfall-resolver/SKILL.md` |
<!-- CATALOG:SKILLS:END -->
