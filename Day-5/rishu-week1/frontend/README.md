# Public API Explorer

A simple full-stack app built using FastAPI and React + Vite that fetches users from a public API and displays them with search functionality.

---

# Project Structure

```txt
yourname-week1/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Card.jsx
│   │   ├── App.jsx
│   │   └── App.css
│
└── README.md
```

---

# Features

- Fetch data from public API
- Backend validation using Pydantic
- Search/filter users
- Loading and error states
- Reusable React Card component
- Clean folder structure

---

# Backend Setup

## Go to backend

```bash
cd backend
```

## Create virtual environment

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create `.env`

```env
API_URL=https://jsonplaceholder.typicode.com/users
```

## Run backend

```bash
uvicorn app:app --reload
```

Backend runs at:

```txt
http://127.0.0.1:8000/users
```

---

# Frontend Setup

## Go to frontend

```bash
cd frontend
```

## Install dependencies

```bash
npm install
```

## Run frontend

```bash
npm run dev
```

Frontend runs at:

```txt
http://localhost:5173
```

---

# Technologies Used

## Backend
- Python
- FastAPI
- Requests
- Pydantic
- python-dotenv

## Frontend
- React
- Vite
- JavaScript
- CSS

---

# React Concepts Used

- useState
- useEffect
- Conditional Rendering
- Reusable Components
- map()
- filter()

---

# API Used

```txt
https://jsonplaceholder.typicode.com/users
```

---

# Author
Rishu Sharma