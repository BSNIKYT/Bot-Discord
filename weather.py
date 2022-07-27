#Code taken from this video  --> https://youtu.be/9P5MY_2i7K8

import datetime as dt
import requests
BASE_weather_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_weather_KEY = "YOUR TOKEN"   # <-----
CITY = "Hrodna"
url = f"{BASE_weather_URL}q={CITY}&appid={API_weather_KEY}"
response = requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

temp_kelvin = response["main"]["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius,feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response["main"]["speed"]
humidity = response["main"]["humidity"]
description = response["main"]["humidity"]
sunrise_time = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunset_time = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])

# /// Your further use of this data is unlimited (Ваше дальнейшее использование этих данных, безгранично) ///
