# 🗺️ Page, Route, and Interaction Documentation

This inventory is based on the route tree registered in `src/main.jsx` and its route modules. These are browser-side React Router routes, not server endpoints.

## 🧭 Route inventory

| URL pattern | Screen/action | Module | Loader | Action | Navigation |
|---|---|---|---|---|---|
| `/` | Root shell and contact list | `src/routes/root.jsx` with index child | `rootLoader` | `rootAction` | Contact selection opens details; New redirects to edit. |
| `/` index | Initial/introductory state | `src/routes/index.jsx` | Parent loader data | None | Rendered in root outlet when no contact child is selected. |
| `/contacts/:contactId` | Contact detail | `src/routes/contact.jsx` | `contactLoader` | `contactAction` | Edit opens editor; Delete submits destroy action. |
| `/contacts/:contactId/edit` | Edit form | `src/routes/edit.jsx` | `editLoader` | `editAction` | Save redirects to detail; Cancel navigates backward in history. |
| `/contacts/:contactId/destroy` | Delete action route | `src/routes/destroy.jsx` | None | `destroyAction` | Removes selected record and redirects to root. |

The index child is an index route and therefore shares the `/` pathname.

## 🏠 Root shell and contact list

**Module:** `src/routes/root.jsx`

| UI element | Behavior | Data / state |
|---|---|---|
| App title link | Navigates to root. | React Router Link |
| Search field | Submits `q` as a URL query parameter. | `rootLoader` reads query and calls `getContacts(q)`. |
| Search indicator | Reflects pending router navigation containing `q`. | `useNavigation()` |
| New button | Submits the parent route action. | `createContact()`, then redirect to edit. |
| Contact list | Displays records returned by loader. | `contacts` loader data |
| Contact link | Opens the selected record. | `contacts/:contactId` |
| Favorite marker | Shows a star when `favorite` is truthy. | Contact record |
| Detail outlet | Hosts index/detail/edit child route. | React Router `Outlet` |
| Empty state | Displays when the returned contact list is empty. | `contacts.length` |

**Source-review caveat:** the root route contains inconsistent references to `createhussainCard`, while the visible local helper is named `createBrajeshCard`; that helper also contains inconsistent identifiers. This potential initialization defect is recorded in [Known issues](known-issues.md). It is not changed in this documentation-only task.

## 🏡 Index / initial state

**Module:** `src/routes/index.jsx`

The index element renders a short author/date statement and introductory text describing the project as a React Router demo. It appears in the detail outlet when no contact child screen is selected.

## 👁️ Contact details

**Module:** `src/routes/contact.jsx`

| Element | Behavior |
|---|---|
| Avatar | Renders the record avatar URL when provided. |
| Name | Displays first/last name or a “No Name” fallback. |
| Favorite control | Submits the inverse favorite value through a fetcher form. |
| Website | Renders an HTTPS-prefixed link when a website value exists. |
| Phone number | Displays stored number when present. |
| Notes | Displays stored notes when present. |
| Edit | Opens relative `edit` route. |
| Delete | Calls browser `confirm()`; canceled submission is prevented. |

The loader looks up the route parameter and throws a 404 Response when no record exists. The action converts submitted favorite text into a boolean and invokes the update helper.

## ✏️ Contact editor

**Module:** `src/routes/edit.jsx`

| Field | Form name | Input behavior |
|---|---|---|
| First name | `first` | Text input; default value from record. |
| Last name | `last` | Text input; default value from record. |
| Phone | `number` | Telephone input, max length 12, pattern `[0-9]{3}-[0-9]{3}-[0-9]{4}`. |
| Website | `website` | Text input. |
| Avatar URL | `avatar` | Text input; current value or generated default URL. |
| Notes | `notes` | Textarea. |

The edit action converts FormData into an object, calls `updateContact`, and redirects to the detail route. Cancel invokes `navigate(-1)`, which depends on browser history.

## 🗑️ Delete action

**Module:** `src/routes/destroy.jsx`

The detail form submits to the relative `destroy` action route. The confirmation dialog runs before submission. After confirmation, the action calls `deleteContact(contactId)` and redirects to `/`. This is a client-router action, not a public HTTP DELETE endpoint.

## ⚠️ Error and exceptional states

| Condition | Source behavior | Verification state |
|---|---|---|
| Unknown contact ID | Detail loader throws a 404 Response. | Runtime test not recorded. |
| Router exception | Root/nested routes configure ErrorPage. | Runtime test not recorded. |
| Delete canceled | Browser confirmation prevents submission. | Runtime test not recorded. |
| Empty list | Root shell displays “No contacts”. | Root initialization concerns may interfere. |
| Missing collection | `getContacts` defaults missing value to an empty array. Other helpers make stronger assumptions. | Static source observation. |
| External URL unavailable | Avatar/link may fail outside app control. | No external-resource test recorded. |

## 📱 Responsive behavior

Responsive behavior must be assessed from the actual stylesheet and browser screenshots at representative viewport widths. No mobile/tablet conformance is claimed here. See [Responsive design](responsive-design.md).

## 🧪 Route verification matrix

| ID | Scenario | Expected outcome | Status |
|---|---|---|---|
| R-01 | Open `/` | Root shell and list/empty state render. | Not run |
| R-02 | Search with `?q=...` | Matching names appear. | Not run |
| R-03 | Submit New | New record is created and editor opens. | Not run |
| R-04 | Open existing contact | Detail fields render. | Not run |
| R-05 | Open unknown ID | 404 error boundary renders. | Not run |
| R-06 | Toggle favorite | Star state updates and persists. | Not run |
| R-07 | Save edit form | Detail screen reflects updates. | Not run |
| R-08 | Cancel edit | Browser history navigation occurs. | Not run |
| R-09 | Cancel delete | No delete submission occurs. | Not run |
| R-10 | Confirm delete | Record removed and root opens. | Not run |

These are test cases, not passing results.

Related: [Navigation](navigation-structure.md) · [Component inventory](component-library.md) · [Features](features.md) · [Testing](testing.md)
