import asyncio
import aiohttp
from dotenv import load_dotenv 

load_dotenv() #load secretes after reading the .env file

async def fetch_weather_async(city_name, latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                temp = data["current_weather"]["temperature"]
                print(f"{city_name}: {temp}°C")
                return data
            else:
                print(f"{city_name} failed: {response.status}")
                return None

async def fetch_all_cities():
    cities = [
        ("Delhi",     28.6,  77.2),
        ("Mumbai",    19.07, 72.87),
        ("Bangalore", 12.97, 77.59)
    ]
    tasks = [fetch_weather_async(name, lat, lon) for name, lat, lon in cities]
    results = await asyncio.gather(*tasks)
    return results

asyncio.run(fetch_all_cities())