# Compound Engineering Hub

A comprehensive, standardized way to package GitHub Copilot **agents,
prompts, instructions, skills, and plugins** across teams.

This site documents the conventions used in this repository. The repository
itself is a **skeleton**: every category is wired up and ready, but ships
without example content — see [Getting Started](getting-started.md).

## Categories

- [Agents](agents.md) — specialist personas (`.agent.md`)
- [Prompts](prompts.md) — reusable task templates (`.prompt.md`)
- [Instructions](instructions.md) — always-on and file-scoped guidance (`.instructions.md`)
- [Skills](skills.md) — bundled, on-demand workflows (`SKILL.md`)
- [Plugins](plugins.md) — installable, distributable bundles (`plugin.json`)
- [Marketplace](marketplace.md) — how discovery and installation work across repos

## Why both a "hub" and a "marketplace"?

- The **hub** (`agents/`, `prompts/`, `skills/`, `.github/instructions/`) is for
  customizations used directly in *this* workspace by anyone with it open in
  VS Code.
- The **marketplace** (`plugins/` + `.github/plugin/marketplace.json`) is for
  customizations meant to be installed into *other* repositories via the
  Copilot CLI plugin system.

See [Contributing](contributing.md) for how to add to either.
