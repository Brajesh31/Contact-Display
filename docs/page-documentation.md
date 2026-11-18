# 🖥️ Page, Route, and Interaction Documentation

This guide describes the client-side route structure found in the React Router configuration and route modules. It is based on static source inspection, not browser-based QA.

## 🗺️ Route inventory

| Route | Screen | Source | Data loading | User actions |
|---|---|---|---|---|
| `/` | Contact list and index/empty-selection state | `src/routes/root.jsx`, `src/routes/index.jsx` | Root loader reads `q` and the contact collection. | Search, create, select contact. |
| `/contacts/:contactId` | Contact details | `src/routes/contact.jsx` | Contact loader reads selected record and throws 404 if missing. | Favorite, edit, delete. |
| `/contacts/:contactId/edit` | Contact editor | `src/routes/edit.jsx` | Edit loader reads selected record. | Edit fields, save, cancel. |
| `/contacts/:contactId/destroy` | Destructive action route | `src/routes/destroy.jsx` | No loader registered. | Delete action then redirect to `/`. |

## 1. 📇 Root layout and contact list

**Implementation:** `src/routes/root.jsx`

| Element | Observed behavior | Notes |
|---|---|---|
| Sidebar title | Link to `/`. | Visible text currently says “React Router Contacts”. |
| Search | Form submits `q` as input changes. | Data helper matches first and last names. |
| New contact | Posts to root action. | Creates record and redirects to edit route. |
| Contact navigation | Lists records as links. | Shows first/last name or “No Name”; favorite star. |
| Detail outlet | Renders matching nested route. | Loading class follows router navigation state. |
| Empty collection | Displays “No contacts”. | Distinct from index/empty-selection content. |

### 🔄 Root workflow

```mermaid
flowchart TD
  A["Open root route"] --> B["Root loader"]
  B --> C["Read q query parameter"]
  C --> D["Load contacts through localForage"]
  D --> E{"Query present?"}
  E -->|"Yes"| F["Match first and last names"]
  E -->|"No"| G["Use complete collection"]
  F --> H["Sort and render sidebar"]
  G --> H
  H --> I{"User action"}
  I -->|"Search"| B
  I -->|"New"| J["Create record"]
  J --> K["Redirect to edit route"]
  I -->|"Select"| L["Open contact details"]
```

## 2. 👤 Contact details

**Implementation:** `src/routes/contact.jsx`

| Element | Behavior |
|---|---|
| Avatar | Renders stored avatar URL when available. |
| Name | Shows first/last name or “No Name”. |
| Favorite | Fetcher form submits inverse favorite value. |
| Website | Creates an external link by prefixing `https://` to stored text. |
| Phone | Displays stored number when present. |
| Notes | Displays free-form notes when present. |
| Edit | Navigates to relative `edit` route. |
| Delete | Submits to relative `destroy` route after browser confirmation. |

### ⭐ Favorite sequence

```mermaid
sequenceDiagram
  participant U as User
  participant F as Fetcher form
  participant A as Contact action
  participant H as updateContact helper
  participant S as localForage
  U->>F: Click favorite button
  F->>A: Submit form data
  A->>H: Update favorite boolean
  H->>S: Persist contacts collection
  S-->>H: Complete write
  H-->>F: Return updated record
```

## 3. ✏️ Edit contact

**Implementation:** `src/routes/edit.jsx`

| Field | Form name | Input | Notes |
|---|---|---|---|
| First name | `first` | Text | Optional in current markup. |
| Last name | `last` | Text | Optional in current markup. |
| Phone | `number` | Telephone | Pattern: three digits, hyphen, three digits, hyphen, four digits. |
| Website | `website` | Text | Stored as text. |
| Avatar URL | `avatar` | Text | Fallback image URL generated when empty. |
| Notes | `notes` | Textarea | Free-form text. |

Save submits to the edit action and redirects to the detail route. Cancel uses browser history navigation.

## 4. 🗑️ Delete workflow

**Implementation:** `src/routes/contact.jsx`, `src/routes/destroy.jsx`

```mermaid
flowchart TD
  A["User selects Delete"] --> B["Browser confirmation"]
  B -->|"Cancel"| C["Prevent form submission"]
  B -->|"Confirm"| D["Submit destroy route action"]
  D --> E["deleteContact helper"]
  E --> F["Write collection to localForage"]
  F --> G["Redirect to root"]
```

The destroy route is a browser-side router action, not an HTTP DELETE endpoint.

## 5. ⚠️ Error and fallback states

| Scenario | Source behavior | Evidence level |
|---|---|---|
| Unknown contact ID | Contact loader throws a 404 response. | Static source review. |
| Unexpected route error | Configured error element renders `src/error.jsx`. | Static source review. |
| Delete cancelled | Form submission is prevented by confirmation handler. | Static source review. |
| Empty collection | Root route renders “No contacts”. | Static source review. |
| Missing avatar | Avatar image receives a null source. | Static source review; browser appearance not captured. |

## 6. 📱 Responsive behavior

The checked-in styles determine breakpoints and responsive layout. Do not claim responsive testing based on source inspection alone.

| Viewport | Verification needed | Current evidence |
|---|---|---|
| Desktop | Sidebar, detail panel, navigation, forms. | Not runtime-verified in this pass. |
| Tablet | Layout transition, overflow, touch targets. | Not runtime-verified in this pass. |
| Mobile | Navigation, form usability, wrapping, scrolling. | Not runtime-verified in this pass. |
| Zoom/text scaling | Reflow and clipping. | Not runtime-verified in this pass. |

## 7. 📸 Screenshot evidence

No genuine application screenshots are claimed here. Capture screenshots from the running application using synthetic test records and place them in `docs/assets/screenshots/`. Never expose actual names, phone numbers, notes, or private contact data.

## 🔎 Related documentation

- [Feature inventory](features.md)
- [Navigation structure](navigation-structure.md)
- [Component inventory](component-library.md)
- [Known issues](known-issues.md)
- [Accessibility review](accessibility.md)
