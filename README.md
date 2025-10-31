# moodmeal

Small project (moodmeal) in this folder. Contains Python code and helper scripts.

Repository contents:
- `app.py` — main application entry (existing file)
- `moodmeal.plx`, `extract_ingredients.plx` — supporting scripts
- `index.html` — frontend
- `uploads/` — user uploads (ignored by .gitignore)

How to use locally:
1. Create a virtual environment: `python -m venv .venv`
2. Activate it and install dependencies (if any).
3. Run `python app.py` to start (project-specific instructions may vary).

Environment / secrets

- Set your Anthropic key in your environment instead of committing it to source.
  For example (PowerShell):

  $env:ANTHROPIC_API_KEY = "sk-..."
