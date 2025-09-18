# hello-copilot
Introduction to coding with copilot

This repo shows how you can use **GitHub Copilot inside GitHub Codespaces**, whether you open the codespace in **VS Code for the Web** (in your browser) or **VS Code desktop**. You just enable Copilot for your account and install/enable the Copilot extension in the codespace. ([GitHub Docs][1])

If that’s good, here’s a **hands-on, copy-paste walkthrough** that takes you from zero → repo → codespace → Copilot-assisted scaffolding → tests → CI.

This repository was made by following the instructions below.

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

> **Note:** PR stands for "pull request"—a request to merge changes from one branch into another, commonly used for code review and collaboration in GitHub repositories.

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

References

[1]: https://docs.github.com/en/codespaces/reference/using-github-copilot-in-github-codespaces?utm_source=chatgpt.com "Using GitHub Copilot in GitHub Codespaces"
[2]: https://code.visualstudio.com/docs/copilot/setup?utm_source=chatgpt.com "Set up GitHub Copilot in VS Code"
[3]: https://docs.github.com/en/codespaces/guides?utm_source=chatgpt.com "Guides for Codespaces"
[4]: https://github.blog/changelog/2025-04-11-vscode-copilot-agent-mode-in-codespaces/?utm_source=chatgpt.com "VSCode Copilot agent mode in Codespaces"
[5]: https://code.visualstudio.com/docs/copilot/getting-started?utm_source=chatgpt.com "Get started with GitHub Copilot in VS Code"
[6]: https://www.theverge.com/2024/10/29/24282544/github-copilot-multi-model-anthropic-google-open-ai-github-spark-announcement?utm_source=chatgpt.com "GitHub Copilot will support models from Anthropic, Google, and OpenAI"

# Instructions for running the program made by this repo

## What does this program do?

This project is a minimal FastAPI web application with two endpoints:

- `GET /health`: Returns a JSON health check `{ "status": "ok" }`.
- `GET /sum?a=1&b=2`: Accepts two query parameters (`a`, `b`) and returns their sum as JSON, e.g. `{ "sum": 3 }`.
- `GET /`: Root endpoint with a welcome message and endpoint info.

## How to use

### Install dependencies
You can install dependencies using pip:

```bash
pip install .[dev]
```

### Run the FastAPI app
Start the server with:

```bash
uvicorn src.app:app --host 0.0.0.0 --port 8000
```

### Example commands

- Health check:
    ```bash
    curl http://localhost:8000/health
    # Response: {"status": "ok"}
    ```

- Sum endpoint:
    ```bash
    curl "http://localhost:8000/sum?a=5&b=7"
    # Response: {"sum": 12}
    ```

- Root endpoint:
    ```bash
    curl http://localhost:8000/
    # Response: {"message": "Welcome to hello-copilot FastAPI app!", "endpoints": "/health, /sum?a=1&b=2"}
    ```

### Run tests
To run the tests:


```bash
PYTHONPATH=src pytest -q
```

---

## FAQ

### How do I know if I am signed into Copilot?
You will see your GitHub username or avatar in the Copilot extension panel in VS Code. If not signed in, Copilot will prompt you to sign in when you try to use it.

### How do I activate Copilot Agent Mode?
Open the Copilot Chat panel and look for the "Agent Mode" toggle or button. If available, enable it to let Copilot make repo-wide changes and open PRs automatically.

### How do I activate Copilot Workspace Mode?
In VS Code, open the Copilot panel and look for "Workspace Mode". This mode allows Copilot to operate across multiple files and plan larger changes.

### In the chat setting, under the wheel icon, describe the purpose and example usages of each of the settings:
- **Prompt files**: Files containing prompts or instructions for Copilot. Use to guide Copilot's code generation or refactoring.
- **Instructions**: Custom instructions for Copilot's behavior, such as coding style or architectural guidelines.
- **Tool sets**: Select which tools Copilot can use (e.g., file editing, running tests, refactoring).
- **Modes**: Choose between modes like Chat, Agent, or Workspace for different levels of automation and scope.
- **MCP servers**: Model Context Protocol servers that provide advanced context and automation for Copilot.
- **Generate Instructions**: Automatically create instructions for Copilot based on your project or files.
- **Chat settings**: Configure how Copilot Chat behaves, such as verbosity, context window, or model selection.

### Why are prompts entered into files not automatically followed as suggested in the instructions?
Copilot does not automatically execute instructions found in files. You need to enter coding suggestions or prompts into the chat for Copilot to act on them. For example, after adding comments to `src/app.py`, you must ask Copilot in chat to implement them.

### What is a FastAPI application?
FastAPI is a modern, high-performance Python web framework for building APIs and web applications. It is designed for speed, automatic validation, and easy integration with Python type hints.

**Example use:**
You can use FastAPI to build REST APIs, microservices, or backend services for web and mobile apps. For example, you might create an API for a todo list app, a machine learning model serving endpoint, or a health check service for infrastructure.

### What is uvicorn?
Uvicorn is a lightning-fast ASGI server for Python web apps, commonly used to run FastAPI applications in development and production.

### What is ci.yml?
`ci.yml` is a GitHub Actions workflow file that defines automated CI (Continuous Integration) steps, such as installing dependencies and running tests on every push or pull request.

### What is a service layer?
A service layer is a part of your application that contains business logic, separate from web/API routes. It helps organize code, improve testability, and keep endpoints clean.

### Where can I find a list of design patterns to prompt repository layouts?
You can find lists of software design patterns and project structures in resources such as:
- The book "Design Patterns: Elements of Reusable Object-Oriented Software" by Gamma et al. (the "Gang of Four")
- The "Awesome Design Patterns" GitHub repository: https://github.com/DovAmir/awesome-design-patterns
- The "Awesome Project Structure" GitHub repository: https://github.com/alexeygrigorev/project-structure-patterns
- Documentation for specific frameworks (e.g., Django, FastAPI, React) often includes recommended layouts
- Online articles and tutorials about software architecture and repository organization

You can use these resources to prompt Copilot or other tools to scaffold repositories using different design patterns or best practices.