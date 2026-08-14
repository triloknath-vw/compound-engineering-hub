# Instructions

Two layers of custom instructions live in this repo:

1. **Always-on**: [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) —
   applied to every chat request in this workspace.
2. **Scoped**: `.github/instructions/*.instructions.md` — applied when files
   match the `applyTo` glob, or on-demand when the `description` matches the
   current task.

## Adding a scoped instruction

Copy `.github/instructions/templates/instructions.template.md`, rename it to
`<topic>.instructions.md`, and fill in `description` plus either `applyTo` or a
keyword-rich description for on-demand discovery.

Full reference: [VS Code custom instructions docs](https://code.visualstudio.com/docs/copilot/customization/custom-instructions).
