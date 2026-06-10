import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\nWeather Information")
        print("-" * 25)
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s\n")

    except requests.exceptions.HTTPError:
        try:
            error = response.json().get("message", "Unknown error")
            print(f"API Error: {error}")
        except Exception:
            print("Failed to retrieve weather data.")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")


while True:
    city = input("Enter city (q to quit): ")

    if city.lower() == "q":
        break
    else:
        if city:
            get_weather(city)
        else:
            print("Please enter a valid city name.")
                                              
