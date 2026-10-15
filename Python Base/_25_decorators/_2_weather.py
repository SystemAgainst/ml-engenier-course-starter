import requests
from requests.exceptions import RequestException
import time
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f'Failed to get data. Retry in {seconds} seconds')
                time.sleep(seconds)
        return func(*args, **kwargs)

    return wrapper_retry
        

@retry
def get_weather_by_hours_for_day_from_api(
    *,
    date: str,
    city: str,
) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}"

    response = (requests.get(url)).json()
    weather_by_days = response['days']
    weather_by_hours = weather_by_days[0]['hours']
    return weather_by_hours


def fahrenheit_to_celsium(*, fahrenheit_temperature: float) -> int:
    return round((fahrenheit_temperature - 32) * 5 / 9)


def get_dangerous_hours(*, weather_by_hours: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hours:
        uvindex = weather['uvindex']
        time = weather['datetime']
        celsius_temperature = fahrenheit_to_celsium(fahrenheit_temperature=weather['temp'])

        if uvindex >= 3:
            dangerous_hours.append({'time': time, 'uvindex': uvindex, 'temperature': celsius_temperature})

    return dangerous_hours
    

date = "2026-10-14"
city = "London,UK"
weather_by_hours = get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hours=weather_by_hours)
print(dangerous_hours)
