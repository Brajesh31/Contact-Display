# 🗂️ Project Structure and File Ownership

This inventory describes the actual repository and modules inspected during the documentation review. It is not a proposed application rewrite.

## 🧭 Repository overview

| Path | Responsibility | Editing boundary |
|---|---|---|
| `.github/` | Issue forms, PR template, Dependabot, GitHub Actions. | Repository support, may enhance. |
| `docs/` | Product, architecture, development, security, quality, operations, visuals. | Documentation, may enhance. |
| `docs/assets/` | Project banner and architecture SVGs. | Documentation visuals, may add. |
| `docs/templates/` | Reusable engineering templates. | Documentation, may add. |
| `public/` | Static assets served by Vite. | Existing application assets, preserve. |
| `scripts/` | Documentation validation utilities. | Support tooling, may add without altering app behavior. |
| `src/` | React entry point, route modules, styles, contact helpers. | **Protected application source, do not edit.** |
| `index.html` | Vite HTML entry point. | **Protected application file, do not edit.** |
| `package.json` | npm scripts and dependency declarations. | **Protected configuration, do not edit.** |
| `package-lock.json` | Exact npm dependency tree. | **Protected configuration, do not edit.** |
| `vite.config.js` | Vite configuration. | **Protected configuration, do not edit.** |
| `.eslintrc.cjs` | Existing ESLint configuration. | **Protected configuration, do not edit.** |
| `.editorconfig`, `.gitattributes`, `.gitignore` | Existing repository/editor conventions. | Preserve unless separately authorized. |

## 🧩 Important application modules

| File | Responsibility |
|---|---|
| `src/main.jsx` | Creates the browser router and mounts React. |
| `src/contacts.js` | Contact CRUD, search/sort helpers, and localForage persistence. |
| `src/routes/root.jsx` | Root layout, contact sidebar, search form, and create action. |
| `src/routes/index.jsx` | Index/empty-selection content. |
| `src/routes/contact.jsx` | Contact details, favorite action, edit link, and delete form. |
| `src/routes/edit.jsx` | Contact edit form and update action. |
| `src/routes/destroy.jsx` | Delete action and redirect. |
| `src/error.jsx` | Router error UI. |
| `src/index.css` | Application styles imported by the entry point. |
| `src/contacts2.js` | Additional helper present in the tree; main router imports `contacts.js`. |

## 🗺️ Route mapping

| URL | Route modules | Data behavior | User outcome |
|---|---|---|---|
| `/` | `root.jsx`, `index.jsx` | Root loader reads search query and contacts. | Browse/search or create a record. |
| `/contacts/:contactId` | `contact.jsx` | Loads by ID and throws 404 if missing. | View and favorite a contact. |
| `/contacts/:contactId/edit` | `edit.jsx` | Loads and updates contact fields. | Edit and save a contact. |
| `/contacts/:contactId/destroy` | `destroy.jsx` | Runs a router action and redirects. | Delete selected contact. |

These are client-side React Router routes, not remote HTTP API endpoints.

## 🔒 Protected-file policy

Routine enhancement may modify documentation, governance files, issue/PR templates, documentation-focused workflows, repository metadata, and validation scripts. It must not modify `src/**`, `public/**` application assets, `index.html`, `package.json`, `package-lock.json`, `vite.config.js`, existing runtime behavior, dependencies, or build configuration. A source issue must be recorded as a finding and left untouched unless separately authorized.

## 🧰 Inventory maintenance

1. Inspect the default branch recursively before each enhancement.
2. Classify paths as application, configuration, documentation, or repository support.
3. Update this inventory when the tracked tree changes.
4. Verify routes against `src/main.jsx` and behavior against current source.
5. Report protected paths as preserved, not modified.

## ✅ Review checklist

- [ ] Tree and important file names match the default branch.
- [ ] Important modules and responsibilities are described.
- [ ] Routes match router registration.
- [ ] Protected files remain unchanged.
- [ ] Documentation links resolve.
