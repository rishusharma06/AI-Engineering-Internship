from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
from models import User
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = os.getenv("API_URL")


@app.get("/users")
def get_users():
    try:
        response = requests.get(API_URL, timeout=10)

        response.raise_for_status()

        data = response.json()

        validated_users = [User(**user) for user in data]

        return validated_users

    except requests.RequestException:
        return {
            "error": "Failed to fetch users from API"
        }

    except Exception:
        return {
            "error": "Something went wrong"
        }