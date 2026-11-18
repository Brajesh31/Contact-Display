# 📦 Dependency Overview

## 🧰 Runtime dependencies

| Package | Role observed in source/manifest |
|---|---|
| `react` | UI component rendering. |
| `react-dom` | Mount React into browser DOM. |
| `react-router-dom` | Browser routing, loaders, actions, forms, and navigation. |
| `localforage` | Browser storage abstraction. |
| `match-sorter` | Search/matching contact names. |
| `sort-by` | Sort contact records. |

## 🛠️ Development dependencies

| Package | Role |
|---|---|
| `vite` | Development server and production bundler. |
| `@vitejs/plugin-react` | React integration for Vite. |
| `eslint` | Static linting. |
| `eslint-plugin-react` | React lint rules. |
| `eslint-plugin-react-hooks` | Hooks lint rules. |
| `eslint-plugin-react-refresh` | React refresh lint rules. |
| `@types/react`, `@types/react-dom` | React type declarations. |

Exact version ranges are in `package.json`; resolved versions are in `package-lock.json`. Do not manually duplicate version claims here after package updates. Dependency changes are outside a documentation-only task unless separately authorized.
