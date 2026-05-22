# Public API Explorer

A simple full-stack application built using **FastAPI (Python)** and **React + Vite**.  
The app fetches user data from a public API, validates it using Pydantic, and displays it on the frontend with search functionality.

---

# Features

## Backend
- Fetches data from a public API using `requests`
- Uses `Pydantic` for response validation
- Loads API URL from `.env`
- Handles API/network errors gracefully
- Built with FastAPI

## Frontend
- Displays users as reusable cards
- Live search/filter functionality
- Loading and error states
- Built using React + Vite
- Uses `useState` and `useEffect`

---

# Project Structure

```txt
yourname-week1/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Card.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   └── package.json
│
└── README.md
```

---

# Technologies Used

## Backend
- Python
- FastAPI
- Requests
- Pydantic
- Python-dotenv

## Frontend
- React
- Vite
- JavaScript
- CSS

---

# Public API Used

```txt
https://jsonplaceholder.typicode.com/users
```

---


# How the App Works

1. FastAPI fetches user data from the public API.
2. Data is validated using Pydantic models.
3. React frontend fetches data from FastAPI backend.
4. Users are displayed using reusable `<Card />` components.
5. Search box filters users dynamically.

---

# Features

- Search users by name
- Loading state while fetching data
- Error handling for failed API requests
- Responsive card layout

---

# Example API Response

```json
{
  "id": 1,
  "name": "Leanne Graham",
  "email": "leanne@example.com"
}
```

---

# Reusable Component Used

```jsx
<Card />
```

Used with `.map()` to display all users dynamically.

---

# React Hooks Used

## useState
Used for:
- users
- loading
- error
- search input

## useEffect
Used to fetch API data when component loads.

---

# Future Improvements

- Add dark mode
- Add pagination
- Add sorting
- Add user details page
- Add responsive navbar

---

# Author

Rishu Sharma
