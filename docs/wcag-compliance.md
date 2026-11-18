# ♿ Accessibility Target and Conformance Evidence

## 🎯 Target

Use WCAG 2.2 Level AA as a design and evaluation target where applicable. This document does not claim that the application currently conforms.

## 🔍 Required review areas

| Area | Review method | Evidence to record |
|---|---|---|
| Keyboard access | Manual keyboard-only traversal. | Focus order, visible focus, unreachable controls. |
| Semantics | DOM/assistive technology inspection. | Headings, landmarks, labels, button/link semantics. |
| Contrast | Contrast analyzer on real rendered states. | Foreground/background pairs and ratios. |
| Forms | Keyboard and screen-reader testing. | Labels, instructions, errors, required state. |
| Images | Inspect meaningful content images. | Useful alternative text or decorative treatment. |
| Reflow | Zoom and narrow viewport checks. | No unintended horizontal scrolling/clipping. |
| Motion | Reduced-motion preference testing. | Motion behavior and alternatives. |

## 🧪 Audit status

No complete WCAG audit or assistive-technology test was executed in this documentation-only pass. Mark criteria individually after capturing evidence; do not claim blanket conformance from automated scans alone.

## 📋 Review checklist

- [ ] All routes reviewed, including error and empty states.
- [ ] Keyboard order and focus indicators tested.
- [ ] Form labels and validation messages announced correctly.
- [ ] Color contrast measured.
- [ ] Zoom/reflow and responsive states checked.
- [ ] Screen-reader behavior checked on supported combinations.
- [ ] Findings have severity, owner, and follow-up.

Use the [accessibility audit template](templates/accessibility-audit-template.md).