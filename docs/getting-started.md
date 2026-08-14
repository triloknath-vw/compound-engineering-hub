# Getting Started

## Using this hub in VS Code

1. Clone this repository (or add it as a workspace folder).
2. Open it in VS Code — `.vscode/settings.json` already points Copilot Chat at
   `agents/` and `prompts/` in addition to the VS Code defaults.
3. Anything you add under `agents/`, `prompts/`, `skills/`, or
   `.github/instructions/` is picked up automatically (reload the window if it
   doesn't appear immediately).

## Using a plugin in another repository

```bash
# Register this repo as a marketplace (once it's pushed to GitHub)
copilot plugin marketplace add <owner>/compound-engineering-hub

# Browse available plugins
copilot plugin marketplace browse compound-engineering-hub

# Install one
copilot plugin install <plugin-name>@compound-engineering-hub
```

Or, to try a plugin locally before it's pushed anywhere:

```bash
copilot plugin install ./plugins/<plugin-name>
```

## Contributing something new

See [Contributing](contributing.md) for the full checklist. In short: copy the
template in the relevant folder, fill it in, add a row to `MARKETPLACE.md`,
open a PR.
