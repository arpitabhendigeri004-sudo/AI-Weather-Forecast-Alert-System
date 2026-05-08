from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

app = FastAPI()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Home Route
@app.get("/")
def home():
    return {
        "message": "Weather Forecast API Running Successfully"
    }


# Weather Route
@app.get("/weather/{city}")
def get_weather(city: str):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get("message")
            }

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        alerts = []

        if temperature > 35:
            alerts.append("High Temperature Alert")

        if humidity > 85:
            alerts.append("High Humidity Alert")

        if wind_speed > 10:
            alerts.append("Strong Wind Alert")

        if "rain" in weather.lower():
            alerts.append("Rain Alert")

        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather,
            "wind_speed": wind_speed,
            "alerts": alerts
        }

    except Exception as e:
        return {
            "error": str(e)
        }