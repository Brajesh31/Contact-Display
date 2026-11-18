# 🗂️ Repository and Project Structure

> **Scope:** documentation of the tracked Contact Display repository. The vendored Bootstrap distribution under `src/css/bootstrap-5.2.3/` is summarized rather than expanded file by file. Application files remain unchanged during documentation-only enhancement.

## 🧭 Repository map

```text
Contact-Display/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   ├── documentation.yml
│   │   └── feature_request.yml
│   ├── workflows/
│   │   ├── documentation-validation.yml
│   │   ├── markdown-link-check.yml
│   │   └── update-readme.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml
├── docs/
│   ├── architecture/
│   │   ├── decisions/
│   │   └── architecture views and Mermaid source
│   ├── assets/
│   │   ├── architecture/
│   │   └── branding/
│   ├── templates/
│   └── product, development, quality, security and operations guides
├── public/
│   └── vite.svg
├── scripts/
│   ├── validate_docs.py
│   ├── validate_links.py
│   └── validate_svg.py
├── src/
│   ├── routes/
│   │   ├── contact.jsx
│   │   ├── destroy.jsx
│   │   ├── edit.jsx
│   │   ├── index.jsx
│   │   └── root.jsx
│   ├── assets/react.svg
│   ├── css/bootstrap-5.2.3/ [vendored framework distribution]
│   ├── App.css
│   ├── App.jsx
│   ├── contacts.js
│   ├── contacts2.js
│   ├── error-page.jsx
│   ├── error.jsx
│   ├── index.css
│   └── main.jsx
├── .editorconfig
├── .eslintrc.cjs
├── .gitattributes
├── .gitignore
├── AUTHORS.md
├── CHANGELOG.md
├── CODEOWNERS
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── SUPPORT.md
├── index.html
├── package-lock.json
├── package.json
└── vite.config.js
```

This is a high-level view of the default branch at the time of audit. Nested vendor files and individual documentation pages are intentionally grouped.

## 🧱 Important directories and responsibilities

| Path | Responsibility | Classification | Maintenance boundary |
|---|---|---|---|
| `.github/ISSUE_TEMPLATE/` | Structured bug, feature, and documentation intake. | GitHub governance | Editable |
| `.github/workflows/` | Repository automation and documentation checks. | Repository automation | Only repository-support workflows may be edited |
| `docs/` | Product, architecture, UI, data, security, and operational knowledge base. | Documentation | Editable |
| `docs/architecture/` | Architecture views, sequence flows, and decision records. | Documentation | Editable |
| `docs/assets/` | Documentation banner and architecture visuals. | Visual assets | Editable |
| `docs/templates/` | Reusable engineering templates. | Documentation | Editable |
| `scripts/` | Python validators for docs, links, and SVG assets. | Repository tooling | Editable when isolated from app behavior |
| `public/` | Static application assets. | Application assets | Preserve |
| `src/routes/` | React Router screens, loaders, and actions. | Application source | **Do not edit** |
| `src/contacts.js` | Active contact CRUD/search/sort helper. | Application source | **Do not edit** |
| `src/contacts2.js` | Alternate data helper not imported by the inspected entry. | Application source | **Do not edit** |
| `src/main.jsx` | React mount and route registration. | Application source | **Do not edit** |
| `src/css/bootstrap-5.2.3/` | Vendored Bootstrap distribution and its upstream documentation/assets. | Vendor/application content | **Do not edit** |
| `src/index.css`, `src/App.css` | Application stylesheets. | Application source | **Do not edit** |
| `index.html` | Vite HTML entry. | Application entry | **Do not edit** |
| `package.json`, `package-lock.json` | npm scripts and exact dependency resolution. | Project configuration | **Do not edit** |
| `vite.config.js`, `.eslintrc.cjs` | Vite and ESLint configuration. | Project configuration | **Do not edit** |

## 🚪 Application entry points

| Entry | Responsibility |
|---|---|
| `index.html` | Provides the HTML document and application mount element. |
| `src/main.jsx` | Creates the browser router and mounts `RouterProvider` under React StrictMode. |
| `src/routes/root.jsx` | Root shell, contact list, search loader, and create action. |
| `src/routes/index.jsx` | Introductory/zero-state content. |
| `src/routes/contact.jsx` | Contact detail screen and favorite action. |
| `src/routes/edit.jsx` | Contact edit form and update action. |
| `src/routes/destroy.jsx` | Delete action and redirect. |
| `src/contacts.js` | Browser persistence and contact operations. |
| `src/error.jsx` | Error UI imported by the router entry. |
| `src/contacts2.js` | Alternate helper present in the repository; not imported by `src/main.jsx` during inspection. |

## 🔀 Routing and data organization

Routes are registered centrally in `src/main.jsx`. Route modules are organized under `src/routes/`. They call the shared `src/contacts.js` helper, which persists the collection under the localForage key `contacts`. The inspected application has no separate `server/`, public API implementation, or database migration directory.

## ⚙️ Configuration and build files

| File | Purpose |
|---|---|
| `package.json` | npm scripts and dependency declarations. |
| `package-lock.json` | Reproducible npm dependency tree. |
| `vite.config.js` | Vite/React build setup. |
| `.eslintrc.cjs` | ESLint configuration. |
| `.editorconfig` | Editor defaults. |
| `.gitattributes` | Git text/binary handling. |
| `.gitignore` | Excluded local and generated files. |
| `index.html` | Vite HTML entry. |
| `dist/` | Default Vite output after build; generated, not a source directory. |

## 🔒 Preservation policy

Repository enhancement may update documentation, governance files, GitHub templates, repository-only automation, and documentation assets. It must not modify application source, application styles, package manifests, lockfiles, runtime dependencies, HTML entry, or build configuration without separate explicit authorization.

Related: [Architecture](architecture.md) · [Page documentation](page-documentation.md) · [Configuration reference](configuration-reference.md) · [Developer guide](developer-guide.md)
