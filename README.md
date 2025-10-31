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

To publish to GitHub:
- Initialize git (already done locally if you committed), then add a remote and push:

  git remote add origin <your-github-repo-url>
  git push -u origin main

If you want me to add the remote and push for you, provide the GitHub repo URL (HTTPS) or let me know if you'd like me to create the repo using the GitHub CLI (`gh`).