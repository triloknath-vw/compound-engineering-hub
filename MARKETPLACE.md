# Marketplace Catalog

A human-curated index of everything published in this hub. This is the
browsable counterpart to the machine-readable
[`.github/plugin/marketplace.json`](.github/plugin/marketplace.json) manifest
that Copilot CLI reads for `copilot plugin install`.

> The Agents/Prompts/Skills/Plugins tables below are generated from actual
> repo content by `python scripts/generate_catalog.py` — don't edit them by
> hand, just run the script after adding something new (also runs in CI).

## Agents

<!-- CATALOG:AGENTS:START -->
| Name | Description | Path |
|---|---|---|
| MoM Agent | Generate comprehensive Minutes of Meeting (MoM) from meeting transcripts. Capture discussions, decisions, action items, risks, blockers, dependencies, and… | [`agents/mom.agent.md`](agents/mom.agent.md) |
| Planner | Researches and outlines multi-step plans | [`agents/planner.agent.md`](agents/planner.agent.md) |
<!-- CATALOG:AGENTS:END -->

## Prompts

<!-- CATALOG:PROMPTS:START -->
| Name | Description | Path |
|---|---|---|
| minutes-of-meeting | Generate comprehensive Minutes of Meeting (MoM) from meeting transcripts. Capture discussions, decisions, action items, risks, blockers, dependencies, and… | [`prompts/minutes-of-meeting.prompt.md`](prompts/minutes-of-meeting.prompt.md) |
<!-- CATALOG:PROMPTS:END -->

## Skills

<!-- CATALOG:SKILLS:START -->
| Name | Description | Path |
|---|---|---|
| readme-blueprint-generator | Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot… | [`skills/readme-blueprint-generator/SKILL.md`](skills/readme-blueprint-generator/SKILL.md) |
<!-- CATALOG:SKILLS:END -->

## Plugins

Installable via `copilot plugin install <name>@compound-engineering-hub` once
this repo is registered as a marketplace (`copilot plugin marketplace add
<owner>/compound-engineering-hub`).

<!-- CATALOG:PLUGINS:START -->
_None yet — see [Contributing](contributing.md) for how to add one._
<!-- CATALOG:PLUGINS:END -->

## Instructions

Not yet scanned by `generate_catalog.py` — add a row by hand for now.

| Name | Applies to | Path |
|---|---|---|
| _none yet_ | | |

