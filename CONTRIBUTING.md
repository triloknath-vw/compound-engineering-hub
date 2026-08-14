# Contributing

This hub only has value if the conventions stay consistent. Follow these rules
for every new addition.

## Ground rules

- **One template, one copy.** Start from the `templates/` (or `_template*`)
  file in the target folder — don't write frontmatter from memory.
- **Keyword-rich descriptions.** `description` is the discovery surface for
  instructions, agents, prompts, and skills. Write it as "Use when X, Y, Z" with
  the actual trigger words a user or agent would say.
- **One concern per file.** Don't mix, e.g., testing conventions and API design
  in a single instructions file, or two unrelated tasks in one prompt.
- **No secrets, ever.** Nothing in this repo should contain API keys, tokens,
  or credentials — including in `plugins/*/`.mcp.json` examples.

## Adding a new item

| I want to add... | Do this |
|---|---|
| A repo-wide coding rule | Edit [`.github/copilot-instructions.md`](.github/copilot-instructions.md) directly |
| A rule for specific files/tasks | Copy [`.github/instructions/templates/instructions.template.md`](.github/instructions/templates/instructions.template.md) into `.github/instructions/` |
| A specialist persona | Copy [`agents/templates/agent.template.md`](agents/templates/agent.template.md) into `agents/` |
| A one-off task template | Copy [`prompts/templates/prompt.template.md`](prompts/templates/prompt.template.md) into `prompts/` |
| A bundled multi-step workflow | Copy [`skills/_template-skill/`](skills/_template-skill/) into `skills/<your-skill-name>/`, rename `SKILL.md`'s `name` field to match the folder |
| A distributable plugin | Copy [`plugins/_template-plugin/`](plugins/_template-plugin/) into `plugins/<your-plugin-name>/`, update `plugin.json`, then add an entry to [`.github/plugin/marketplace.json`](.github/plugin/marketplace.json) |

## Review checklist (for pull requests)

- [ ] Frontmatter is valid YAML and includes a real `description` (not "helpful agent"/"useful prompt")
- [ ] Folder name matches the `name` field, where applicable (skills, plugins)
- [ ] No secrets or credentials committed
- [ ] If it's a plugin: `plugin.json` `agents`/`skills` paths exist and are non-empty
- [ ] Added to [`MARKETPLACE.md`](MARKETPLACE.md) catalog (and `marketplace.json` if it's a plugin)
- [ ] `python scripts/validate_structure.py` passes locally

## Naming conventions

- Agents: `kebab-case.agent.md`, e.g. `terraform-reviewer.agent.md`
- Prompts: `kebab-case.prompt.md`, e.g. `generate-pr-description.prompt.md`
- Skills: folder `kebab-case/`, file always named `SKILL.md`
- Instructions: `kebab-case.instructions.md`
- Plugins: folder `kebab-case/`, manifest always named `plugin.json`
