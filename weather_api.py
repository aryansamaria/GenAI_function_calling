from api_call import call_api
import json

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city_name,*other_det):

    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&aqi=no")
    result = dict()
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "feels_like": data["current"]["feelslike_c"],
            "humidity": data["current"]["humidity"]

        }
        for key,value in weather_info.items():
            if key in other_det:
                result[key] = value
            elif len(other_det) == 0:
                return weather_info
        return result
    else:
        return {"error": f"City '{city_name}' not found or API error."}


if __name__ == "__main__":
    city = "London"
    weather = get_weather(city,"temperature","feels_like")
    print(weather)
