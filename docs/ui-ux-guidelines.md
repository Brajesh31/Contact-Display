# 🎨 UI/UX Guidelines

The app uses a two-region interface: a sidebar with search/contact navigation and a detail outlet. React Router handles navigation and form submissions.

| Element | Interaction |
|---|---|
| Sidebar title link | Returns to root. |
| Contact link | Opens selected contact route. |
| Search field | Submits query while typing. |
| New button | Submits root action to create a record. |
| Favorite star | Submits favorite state through a fetcher form. |
| Edit button | Opens edit route. |
| Save button | Submits edit form. |
| Cancel button | Navigates back in history. |
| Delete button | Requests browser confirmation before submission. |

Review responsive behavior, keyboard focus, validation feedback, destructive-action clarity, and loading/error/empty states. This guide does not change the UI implementation.
