import { useEffect, useState } from "react";
import Card from "./components/Card";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/users")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch users");
        }

        return response.json();
      })
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const filteredUsers = users.filter((user) =>
    user.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h1 className="title">Public API Explorer</h1>

      <p className="subtitle">
        Search and explore users fetched from a public API
      </p>

      <div className="search-box">
        <input
          type="text"
          placeholder="Search users..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      {loading && <h2 className="message">Loading...</h2>}

      {error && <h2 className="message error">{error}</h2>}

      {!loading && !error && filteredUsers.length === 0 && (
        <h2 className="message">No users found</h2>
      )}

      <div className="grid">
        {filteredUsers.map((user) => (
          <Card
            key={user.id}
            name={user.name}
            email={user.email}
            company={user.company.name}
            website={user.website}
          />
        ))}
      </div>
    </div>
  );
}

export default App;