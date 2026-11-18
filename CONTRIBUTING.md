# 🛠️ Contributing to Contact Display

Thank you for considering a contribution. This repository currently contains a React/Vite client-side contact manager. Please read the project documentation before proposing changes.

## 🎯 Contribution boundaries

The application is considered complete for the current maintenance task. Documentation and repository-maintenance contributions are welcome. Do not refactor or rewrite application code as part of a documentation-only change. A separate, explicitly approved request is required for product-code changes.

## 🧭 Before starting

1. Read the [README](README.md).
2. Review [architecture](docs/architecture.md) and [project structure](docs/project-structure.md).
3. Search existing issues and pull requests.
4. For substantial changes, open an issue or discussion first.

## 💻 Local setup

```bash
git clone https://github.com/Brajesh31/Contact-Display.git
cd Contact-Display
npm ci
npm run dev
```

## 🌿 Branch conventions

Use focused branches such as:

- `docs/<topic>` for documentation.
- `chore/<topic>` for repository maintenance.
- `fix/<topic>` only for an approved defect fix.
- `feat/<topic>` only for explicitly authorized product work.

## ✍️ Commit messages

Prefer concise, imperative messages with a conventional prefix:

| Prefix | Use |
|---|---|
| `docs:` | Documentation changes. |
| `chore:` | Repository maintenance. |
| `ci:` | CI workflow changes. |
| `test:` | Test-only changes. |
| `fix:` | Approved bug fixes. |
| `feat:` | Approved new functionality. |

Example: `docs: document local contact storage architecture`.

## 📚 Documentation standards

- Describe behavior confirmed by the current source.
- Use tables for inventories, configuration, and comparisons.
- Include Mermaid source for diagrams and keep labels readable.
- Use relevant emojis in documentation headings, not in syntactically constrained files.
- Use relative links for repository documents.
- Add alt text to images.
- Identify assumptions, unknowns, and limitations explicitly.
- Distinguish implemented functionality from proposals.
- Never invent endpoints, database schemas, metrics, tests, screenshots, or deployment environments.
- Keep examples safe and free of real contact information or credentials.

## 🧪 Validation

For documentation-only changes, run the repository validation scripts when Python is available:

```bash
python scripts/validate_docs.py
python scripts/validate_links.py
python scripts/validate_svg.py
```

For changes to workflows or metadata, validate YAML syntax and review permissions. Do not modify application source, package manifests, lockfiles, Vite configuration, or application styling as part of documentation work.

## 🔍 Pull request checklist

- [ ] The change has a focused purpose.
- [ ] No application/project source file was modified.
- [ ] Existing functional behavior is untouched.
- [ ] Documentation matches actual source.
- [ ] Internal links resolve.
- [ ] Mermaid and SVG assets are valid.
- [ ] No secrets or personal contact data were added.
- [ ] Planned functionality is labeled as planned.
- [ ] Validation results are reported accurately.

## 🤝 Review

Reviews may request evidence, clearer wording, corrected links, or separation of implementation facts from assumptions. A contribution is complete when the change is understandable, accurate, and maintainable.
