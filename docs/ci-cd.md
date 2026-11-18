# 🔁 CI/CD

## Existing workflow
The repository already contains `.github/workflows/update-readme.yml`, which runs on push, schedule, and manual dispatch and writes a timestamp to README. This existing workflow was preserved.

## Documentation workflows
Additional workflows validate documentation-only paths and run with read-only contents permission. They do not install or change application dependencies or edit application source.

Review actual workflow run results before describing CI as healthy. Use least privilege and review action versions periodically.
