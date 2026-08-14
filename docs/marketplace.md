# Marketplace

There are two catalogs in this repo, serving different audiences:

| | Purpose | Audience | File |
|---|---|---|---|
| Machine manifest | Lets Copilot CLI resolve and install plugins | `copilot plugin` CLI | [`.github/plugin/marketplace.json`](../.github/plugin/marketplace.json) |
| Human catalog | Browsable index of everything published here | Engineers browsing the repo | [`MARKETPLACE.md`](../MARKETPLACE.md) |

## Registering this repo as a marketplace

Once pushed to GitHub:

```bash
copilot plugin marketplace add <owner>/compound-engineering-hub
copilot plugin marketplace browse compound-engineering-hub
copilot plugin install <plugin-name>@compound-engineering-hub
```

## Adding a plugin to the marketplace manifest

Add an entry under `plugins` in
[`.github/plugin/marketplace.json`](../.github/plugin/marketplace.json):

```json
{
  "name": "your-plugin-name",
  "description": "What it standardizes",
  "version": "0.1.0",
  "source": "../../plugins/your-plugin-name"
}
```

Then add a matching row to [`MARKETPLACE.md`](../MARKETPLACE.md) so it's
human-browsable too. Changes to `plugins/**` and `marketplace.json` should go
through the same pull-request review as everything else — that review is the
entire governance model, no extra infrastructure required.
