# 🖼️ Visual Assets and Screenshot Policy

## 📌 Current checked-in assets

| Asset | Format | Purpose |
|---|---|---|
| [Contact Display banner](branding/contact-display-banner.svg) | SVG | README and project identity. |
| [Application architecture](architecture/contact-display-architecture.svg) | SVG | Browser, router, data helper, and localForage overview. |
| [Contact data flow](architecture/contact-data-flow.svg) | SVG | Contact data read/write path. |
| [Contact sequence](architecture/contact-sequence.svg) | SVG | Route and persistence interaction. |

## 📁 Recommended organization

```text
docs/assets/
├── branding/
├── architecture/
├── workflows/
├── screenshots/
│   ├── desktop/
│   ├── tablet/
│   ├── mobile/
│   ├── features/
│   └── error-states/
├── demos/
└── illustrations/
```

## 📸 Screenshot requirements

- Capture from the real running application and record the tested commit/environment.
- Use synthetic sample contacts only. Never expose real names, phone numbers, notes, or private browser storage.
- Capture desktop/tablet/mobile states only after checking those viewports.
- Add meaningful alt text and descriptive filenames.
- Do not label architecture drawings as screenshots or demo images.
- Do not fabricate screens for features that are not implemented.

## ♿ Accessibility and licensing

Use descriptive alt text in Markdown/HTML. Prefer original SVG assets. Record source and license for any third-party image or icon added. Keep SVGs free of scripts, event handlers, and unreviewed external references.

## ✅ Validation

Run `python scripts/validate_svg.py` to parse SVG XML and check basic title/description elements. Parsing does not establish visual correctness or accessibility conformance.
