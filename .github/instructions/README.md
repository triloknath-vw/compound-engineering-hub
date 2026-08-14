# Instructions (`.instructions.md`)

Always-on guidance lives in [`../copilot-instructions.md`](../copilot-instructions.md).
This folder is for **scoped** instructions — rules that apply only to specific
files (via `applyTo` glob) or specific tasks (via keyword-rich `description`).

## Adding a new instructions file

1. Copy [`templates/instructions.template.md`](templates/instructions.template.md).
2. Rename to `<topic>.instructions.md` (kebab-case).
3. Fill in `description` and either `applyTo` (file-based) or rely on
   description-based on-demand discovery.
4. Keep it to one concern — separate files for testing, styling, API design, etc.

## Discovery

VS Code searches this folder recursively, so you can group instructions in
subfolders, e.g.:

```text
.github/instructions/
  frontend/
    react.instructions.md
  backend/
    api-design.instructions.md
```

Additional search locations are controlled by the `chat.instructionsFilesLocations`
setting in [`../../.vscode/settings.json`](../../.vscode/settings.json).
