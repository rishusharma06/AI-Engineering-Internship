import requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time

load_dotenv()

def fetch_weather():
    url = os.getenv("API_KEY")
    params = {
        "latitude": float(os.getenv("LATITUDE")),
        "longitude": float(os.getenv("LONGITUDE")),
        "current_weather": True
    }
    max_retries = 3
    wait_seconds = 2

    for attempt in range(1, max_retries+1):
        try:
            print(f"Attemp {attempt} of {max_retries}...")
            response = requests.get(url, params = params,timeout = 5)
            if response.status_code == 200:
                print("Success")
                return response.json()
            elif response.status_code == 429:  #rate limited
                print(f"Rate limited! Waiting {wait_seconds} seconds...")
                time.sleep(wait_seconds)
                wait_seconds *= 2  # double wait each time
            
            else:
                print(f"Error: {response.status_code}")
                return None
        
        except requests.exceptions.ConnectionError:
            print(f"No internet connection. Waiting {wait_seconds}s...")
            time.sleep(wait_seconds)
            
        except requests.exceptions.Timeout:
            print(f"Request timed out. Waiting {wait_seconds}s...")
            time.sleep(wait_seconds)
    
    print("All attempts failed!")
    return None
   

class CurrentWeather(BaseModel):
    temperature: float
    windspeed: float
    winddirection: int
    is_day: int
    weathercode: int


def save_report(weather):
    with open("weather_report.txt", "w") as f:
        f.write("=== Weather Report ===\n")
        f.write(f"Temperature   : {weather.temperature}°C\n")
        f.write(f"Wind Speed    : {weather.windspeed} km/h\n")
        f.write(f"Wind Direction: {weather.winddirection}°\n")
        f.write(f"Is Daytime    : {'Yes' if weather.is_day else 'No'}\n")
    print("Report saved to weather_report.txt")


data = fetch_weather()

if data:
    weather = CurrentWeather(**data["current_weather"])
    print(f"Temperature  : {weather.temperature}°C")
    print(f"Wind Speed   : {weather.windspeed} km/h")
    print(f"Wind Direction: {weather.winddirection}°")
    print(f"Is Daytime   : {'Yes' if weather.is_day else 'No'}")
    save_report(weather) 