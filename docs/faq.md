# ❓ Frequently Asked Questions

## Does the project use MongoDB or Express?

The inspected application uses browser-side localForage. No MongoDB database or Express server is established by the inspected project files.

## Is there a remote REST API?

No public server API contract was found. React Router loaders and actions are in-process browser application functions, not remote endpoints.

## Where are contacts stored?

The contact helper reads and writes the `contacts` key through localForage in the current browser origin/profile.

## Will contacts sync across devices?

No remote synchronization is established by the inspected implementation.

## Can browser data be lost?

Yes. Clearing site/browser storage or using a different browser profile/origin can result in records not being available.

## What Node/npm commands are available?

The inspected package manifest defines `npm run dev`, `npm run build`, `npm run preview`, and `npm run lint`. It does not declare a test script or `npm start`.

## Are UI screenshots available?

The repository contains architecture SVGs. Genuine application UI screenshots have not been captured and verified in this documentation review.

## Is the application WCAG 2.2 AA compliant?

No conformance claim is made. WCAG 2.2 AA is a target for evaluation. See [accessibility guidance](accessibility.md) and [audit criteria](wcag-compliance.md).

## Where do I report a security issue?

Use GitHub's private vulnerability reporting option if enabled for the repository. Do not put exploit details or personal contact data in public issues.
