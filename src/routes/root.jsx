import {
  getContacts,
  createContact,
  getContact,
  updateContact,
} from "../contacts";
import {
  Outlet,
  NavLink,
  Link,
  useLoaderData,
  Form,
  redirect,
  useNavigation,
  useSubmit,
} from "react-router-dom";
import { useEffect } from "react";

export async function action() {
  const contact = await createContact();
  return redirect(`contacts/${contact.id}/edit`);
}

export async function loader({ request }) {
  // hussain card will always exist
  await createhussainCard();

  const url = new URL(request.url);
  const q = url.searchParams.get("q");
  const contacts = await getContacts(q);
  return { contacts, q };
}

async function createBrajeshCard() {
  // check local forage for micahel Id
  let hussainIdStorage = localStorage.getItem("hussainIdStorage");
  let hussainExists = await getContact(hussainIdStorage);

  // if null create card
  if (!hussainExists) {
    console.log("creating card");
    const hussainContactCard = await createContact();
    const hussainInfo = {
      first: "Brajesh",
      last: "Kumar",
      avatar: `https://placekitten.com/200/200?image=${
        Math.floor(Math.random() * 16) + 1
      }`,
      website: "www.github.com/Brajesh31/",
      number: "078-033-8261",
      notes: "No need to login. Create a contact. Saved to your Local Storage!",
      favorite: true,
    };
    await updateContact(BrajeshContactCard.id, hussainInfo);
    localStorage.setItem("hBrajeshIdStorage", hussainContactCard.id);
  }
  return hussainExists;
}

export default function Root() {
  const { contacts, q } = useLoaderData();
  const navigation = useNavigation();
  const submit = useSubmit();
  const searching =
    navigation.location &&
    new URLSearchParams(navigation.location.search).has("q");

  useEffect(() => {
    document.getElementById("q").value = q;
  }, [q]);

  useEffect(() => {
    createhussainCard();
  }, []);

  return (
    <>
      <div id="sidebar">
        <h1>
          <Link to="/">React Router Contacts</Link>
        </h1>
        <div>
          <Form id="search-form" role="search">
            <input
              id="q"
              className={searching ? "loading" : ""}
              aria-label="Aria Label Search Contacts"
              placeholder="Search Contact"
              type="search"
              autoComplete="off"
              name="q"
              defaultValue={q}
              onChange={(event) => {
                const isFirstSearch = q == null;
                submit(event.currentTarget.form, {
                  replace: !isFirstSearch,
                });
              }}
            />
            <div id="search-spinner" aria-hidden hidden={!searching} />
            <div className="sr-only" aria-live="polite"></div>
          </Form>
          <Form method="post">
            <button type="submit">New</button>
          </Form>
        </div>

        <nav>
          {contacts.length ? (
            <ul>
              {contacts.map((contact) => (
                <li key={contact.id}>
                  <NavLink
                    to={`contacts/${contact.id}`}
                    className={({ isActive, isPending }) =>
                      isActive ? "active" : isPending ? "pending" : ""
                    }
                  >
                    {contact.first || contact.last ? (
                      <>
                        {contact.first} {contact.last}
                      </>
                    ) : (
                      <i>No Name</i>
                    )}{" "}
                    {contact.favorite && <span>★</span>}
                  </NavLink>
                </li>
              ))}
            </ul>
          ) : (
            <p>
              <i>No contacts</i>
            </p>
          )}
        </nav>
      </div>
      <div
        id="detail"
        className={navigation.state === "loading" ? "loading" : ""}
      >
        <Outlet />
      </div>
    </>
  );
}
