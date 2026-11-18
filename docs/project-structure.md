# 🗂️ Project Structure and File Ownership

> This inventory describes the checked-in repository and source modules inspected during documentation review. It is not a proposed application rewrite.

## 🧭 Repository overview

| Path | Responsibility | Policy |
|---|---|---|
| `.github/` | Issue forms, PR template, Dependabot, GitHub Actions. | Repository support; may enhance. |
| `docs/` | Product, architecture, development, security, quality, operations, and visuals. | Documentation; may enhance. |
| `docs/assets/` | Branding and architecture SVG assets. | Documentation visuals; may add. |
| `docs/templates/` | Reusable engineering templates. | Documentation; may add. |
| `public/` | Static assets served by Vite. | Existing application assets; preserve. |
| `scripts/` | Documentation validation utilities. | Support scripts; may add without changing app behavior. |
| `src/` | React entry point, route modules, styles, and contact data helpers. | **Protected application source. Do not edit.** |
| `index.html` | Vite HTML entry point. | **Protected application file. Do not edit.** |
| `package.json` | npm scripts and dependency declarations. | **Protected configuration. Do not edit.** |
| `package-lock.json` | Exact npm dependency tree. | **Protected configuration. Do not edit.** |
| `vite.config.js` | Vite configuration. | **Protected configuration. Do not edit.** |
| `.eslintrc.cjs` | Existing ESLint configuration. | **Protected configuration. Do not edit.** |
| `.editorconfig`, `.gitattributes`, `.gitignore` | Existing repository/editor conventions. | Preserve unless separately authorized. |

## 🧩 Important application modules

| Path | Responsibility | Evidence |
|---|---|---|
| `src/main.jsx` | Creates browser router and mounts React. | Router registration and React root. |
| `src/contacts.js` | Contact CRUD, search/sort helpers, and localForage persistence. | Imports localForage, match-sorter, and sort-by. |
| `src/routes/root.jsx` | Root layout, contact sidebar, search form, create action. | Root loader/action and rendered layout. |
| `src/routes/index.jsx` | Empty-selection/welcome content. | Index route element. |
| `src/routes/contact.jsx` | Contact detail, favorite action, edit link, delete form. | Contact loader/action and UI. |
| `src/routes/edit.jsx` | Edit form and update action. | Edit loader/action and fields. |
| `src/routes/destroy.jsx` | Delete action and redirect. | Destroy action. |
| `src/error.jsx` | Router error screen. | Configured error element. |
| `src/index.css` | Application styles. | Imported by `src/main.jsx`. |
| `src/contacts2.js` | Additional contact-helper module. | Present in tree; primary router imports `contacts.js`. |

## 🗺️ Route mapping

| URL | Route modules | Data behavior | User outcome |
|---|---|---|---|
| `/` | `root.jsx`, `index.jsx` | Root loader reads query and contacts. | Browse/search contacts or create a record. |
| `/contacts/:contactId` | `contact.jsx` | Loads record by ID, throws 404 when missing. | View and favorite contact. |
| `/contacts/:contactId/edit` | `edit.jsx` | Loads record and saves submitted fields. | Edit contact details. |
| `/contacts/:contactId/destroy` | `destroy.jsx` | Runs router action and redirects. | Delete selected contact. |

These are client-side React Router routes, not remote HTTP API endpoints.

## 🔒 Protected-file policy

Routine repository enhancements may modify documentation, governance files, issue/PR templates, documentation-focused workflows, repository metadata, and validation scripts. They must not modify:

- `src/**`, including components, pages, route modules, styles, and data helpers.
- `public/**` application assets or `index.html`.
- `package.json`, `package-lock.json`, or `vite.config.js`.
- Existing runtime behavior, dependencies, or build configuration.

A source-code issue discovered during review must be documented as a finding and left untouched unless separate explicit authorization is given.

## 🧰 Inventory maintenance procedure

1. Inspect the default branch recursively before every enhancement.
2. Classify each path as application, configuration, documentation, or repository support.
3. Update this file when the actual tracked tree changes.
4. Verify route names against `src/main.jsx` and behavior against current source.
5. Report protected paths as preserved, not as files modified.

## ✅ Review checklist

- [ ] Paths match the current default-branch tree.
- [ ] Important application modules and responsibilities are described.
- [ ] Route inventory matches router registration.
- [ ] Protected files remain unchanged during documentation work.
- [ ] Documentation links resolve.
