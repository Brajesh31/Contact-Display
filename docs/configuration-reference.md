# ⚙️ Configuration Reference

| File | Purpose | Current finding |
|---|---|---|
| `package.json` | npm metadata, scripts and dependencies. | Existing root manifest; preserved. |
| `package-lock.json` | Dependency resolution lock. | Existing npm lockfile; preserved. |
| `vite.config.js` | Vite React plugin setup. | No custom server port visible. |
| `.eslintrc.cjs` | ESLint rules. | Existing config; preserved. |
| `.gitignore` | Local/build artifacts. | Existing file; preserved. |
| `index.html` | HTML app entry. | Existing file; preserved. |
| `.editorconfig` | Editor defaults. | Added for repository consistency. |
| `.gitattributes` | Git text/binary handling. | Added for repository consistency. |

## Environment
No project-specific application environment variable was established from the inspected source. Do not add dummy `MONGO_URI`, `PORT`, or backend credentials to environment examples.
