# hello-copilot
Introduction to coding with copilot

Short answer: **Yes.** You can use **GitHub Copilot inside GitHub Codespaces**, whether you open the codespace in **VS Code for the Web** (in your browser) or **VS Code desktop**. You just enable Copilot for your account and install/enable the Copilot extension in the codespace. ([GitHub Docs][1])

If that’s good, here’s a **hands-on, copy-paste walkthrough** that takes you from zero → repo → codespace → Copilot-assisted scaffolding → tests → CI.

---

# 🧪 From Zero to Repo with Copilot in Codespaces

## 0) Prereqs

* A GitHub account with **Copilot Free/Pro/Business/Enterprise** enabled for your user/org.
* You’ll be prompted to sign in + enable Copilot the first time in VS Code. ([Visual Studio Code][2])

---

## 1) Create a repo on GitHub

1. Go to GitHub → **New repository**.
2. Name it (e.g., `hello-copilot`), choose **Private** or **Public**.
3. Tick **Add README**; add a **.gitignore** for your language (e.g., Python).
4. Click **Create repository**.

---

## 2) Open in Codespaces

* On the repo page → **Code ▸ Codespaces ▸ Create codespace on main**.
* This launches a cloud dev environment. You can open it in **browser** or **VS Code desktop**. ([GitHub Docs][3])

---

## 3) Enable Copilot in the codespace

* In the codespace (browser or desktop), open the Extensions panel and ensure **GitHub Copilot** (and **Copilot Chat**) are installed and signed in.
* If prompted, click **Set up Copilot** and complete sign-in. ([Visual Studio Code][2])

> Tip: You can also try **Copilot Agent Mode** and **Copilot Workspace** flows if available in your account—they accelerate repo-wide changes and PRs. ([The GitHub Blog][4])

---

## 4) Scaffold your project with Copilot

### A. Create basic structure

In the Explorer, create folders/files (you can also ask Copilot to do this with Agent/Chat if enabled):

```
.
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

### B. Use Copilot to write code

Open `src/app.py` and **describe what you want** at the top:

```python
# Build a minimal FastAPI app with one GET /health endpoint returning {"status": "ok"}.
# Add a second endpoint /sum that accepts two query params (a, b) and returns their sum as JSON.
# Include type hints and docstrings. Keep it simple and production-friendly.
```

Pause typing—Copilot should suggest an implementation. Accept with `Tab` (or the inline accept shortcut shown).

### C. Generate tests

Open `tests/test_app.py` and prompt Copilot:

```python
# Write pytest tests for the FastAPI app in src/app.py
# - test_health() should check {"status": "ok"}
# - test_sum() should check sum of a and b for a couple of cases
# Use TestClient from fastapi
```

Let Copilot draft the tests, then review before saving.

### D. Fill packaging/deps

Open `pyproject.toml` and prompt:

```toml
# Create a minimal pyproject for a FastAPI app using uvicorn and pytest.
# Include fastapi, uvicorn, httpx, pytest as dependencies/dev-deps.
# Use hatchling or setuptools to keep it simple.
```

> If you prefer `requirements.txt`, ask Copilot to create it instead.

---

## 5) Run & iterate (in Codespaces)

Open a terminal in the codespace:

```bash
# install deps
pip install -e .  ||  pip install fastapi uvicorn httpx pytest

# run tests
pytest -q

# run the app (adjust command based on your file)
uvicorn src.app:app --host 0.0.0.0 --port 8000
```

Use the **Ports** panel to open the forwarded port in your browser and test `/health` and `/sum?a=3&b=4`.

If something fails, open **Copilot Chat** and ask:

> “Why is `test_sum` failing? Here’s the error… suggest a fix.”

---

## 6) Add CI with GitHub Actions

Open `.github/workflows/ci.yml` and prompt:

```yaml
# GitHub Actions: on push/pull_request, run Python tests on 3.10–3.12
# steps: checkout, setup-python, install deps, run pytest
```

Commit and push—GitHub will run CI automatically on PRs.

---

## 7) Use Copilot beyond code

* **Generate docstrings**: “Add NumPy-style docstrings to this file.”
* **Refactor**: “Refactor `sum` into a service layer with input validation.”
* **Explain code**: “Explain what this function does and its complexity.”
* **Write README**: “Draft a concise README with install/run/test instructions.”

---

## 8) Commit, PR, and review

* Use **Source Control** to commit changes.
* Create a **pull request**; optionally ask Copilot to summarize diffs or draft the PR description.
* Rinse and repeat: describe → generate → test → commit.

---

### Notes / gotchas

* Copilot suggestions can be **wrong or insecure**—review and test.
* For larger changes, try **Copilot Chat** or **Agent Mode** to plan, edit multiple files, and open a PR. ([Visual Studio Code][5])
* Copilot today is **multi-model** (not just the old “Codex”) and may use models from OpenAI, Anthropic, Google, etc., depending on your Copilot plan and settings. ([The Verge][6])

---

If you want, I can turn this into a **ready-made starter repo** (FastAPI + tests + CI) tailored to your preferences (Python version, package manager, linting, pre-commit hooks, Dockerfile, devcontainer).

[1]: https://docs.github.com/en/codespaces/reference/using-github-copilot-in-github-codespaces?utm_source=chatgpt.com "Using GitHub Copilot in GitHub Codespaces"
[2]: https://code.visualstudio.com/docs/copilot/setup?utm_source=chatgpt.com "Set up GitHub Copilot in VS Code"
[3]: https://docs.github.com/en/codespaces/guides?utm_source=chatgpt.com "Guides for Codespaces"
[4]: https://github.blog/changelog/2025-04-11-vscode-copilot-agent-mode-in-codespaces/?utm_source=chatgpt.com "VSCode Copilot agent mode in Codespaces"
[5]: https://code.visualstudio.com/docs/copilot/getting-started?utm_source=chatgpt.com "Get started with GitHub Copilot in VS Code"
[6]: https://www.theverge.com/2024/10/29/24282544/github-copilot-multi-model-anthropic-google-open-ai-github-spark-announcement?utm_source=chatgpt.com "GitHub Copilot will support models from Anthropic, Google, and OpenAI"

