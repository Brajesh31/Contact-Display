# 📦 Dependency Security and Supply-Chain Review

## 📌 Current dependency model

The project uses npm with a committed `package-lock.json`. The documented stack includes React, React Router DOM, Vite, localForage, match-sorter, sort-by, and ESLint. This page records a review process, not a claim that every dependency has been audited.

## 🔍 Review requirements

| Check | Evidence | Action |
|---|---|---|
| Known advisories | Dependabot/GitHub advisory alerts and npm audit output. | Triage severity and applicability. |
| Package provenance | Registry/package metadata and maintainer history. | Investigate unexpected ownership or package changes. |
| Lockfile integrity | Reviewed `package-lock.json` diff. | Require explicit approval for dependency changes. |
| License obligations | Declared license metadata and notices. | Review compatibility and preserve required notices. |
| Workflow supply chain | Action references and permissions. | Pin reviewed immutable SHAs where appropriate. |
| Build integrity | CI build record and source commit. | Retain traceable evidence. |

## 🔒 Documentation-only boundary

Do not update packages, regenerate `package-lock.json`, replace package managers, or modify build configuration during documentation enhancement. Dependency remediation must be separately authorized and tested.

## ✅ Review checklist

- [ ] Advisory alerts inspected.
- [ ] Direct and transitive dependency changes reviewed.
- [ ] License and attribution obligations considered.
- [ ] Lockfile remains reproducible.
- [ ] Build/test evidence associated with the reviewed commit.
- [ ] Findings assigned and tracked.

Use the [dependency review template](templates/dependency-review-template.md).