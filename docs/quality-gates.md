# 🧪 Documentation and Repository Quality Gates

## 🎯 Purpose

Define repeatable gates for repository documentation and supporting automation. These gates do not replace application tests or a production readiness review.

## ✅ Current documentation checks

| Gate | Command/workflow | What it establishes | What it does not establish |
|---|---|---|---|
| Required docs | `python scripts/validate_docs.py` | Required documentation paths exist and are non-empty. | Technical accuracy or runtime behavior. |
| Local links | `python scripts/validate_links.py` | Repository-owned Markdown relative links resolve, excluding vendored `src/` and `public/` content. | External URL availability. |
| SVG parsing | `python scripts/validate_svg.py` | SVG XML parses and basic metadata/content checks pass. | Visual quality or WCAG conformance. |
| CI orchestration | `.github/workflows/docs-validation.yml` | Runs the above checks on configured documentation changes. | Application lint/build or browser tests. |

## 🚦 Merge/release checklist

- [ ] README claims reflect current source.
- [ ] New/updated docs are linked from the documentation hub.
- [ ] Route and data diagrams match the actual app.
- [ ] Local links pass.
- [ ] SVG XML and metadata checks pass.
- [ ] Templates contain no real contact data or secrets.
- [ ] Application source and protected configuration remain unchanged for docs-only work.
- [ ] CI result is inspected, not inferred from workflow creation.

## 📊 Evidence policy

Record the commit SHA, workflow run URL, check outcome, and any skipped checks. Never convert “not run” into “passed”.

## 🔗 Related

[Testing strategy](test-strategy.md) · [CI/CD](ci-cd.md) · [Known issues](known-issues.md)