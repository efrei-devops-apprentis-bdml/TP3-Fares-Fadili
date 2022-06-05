import requests
import json
import os
from pprint import pprint


def weather(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
        lat, lon, api_key)

    weather_data = requests.get(url).json()

    json_str = json.dumps(weather_data)
    resp = json.loads(json_str)

    pprint(resp['current'])


latitude = os.environ['LAT']
longitude = os.environ['LONG']
cle_api = os.environ['API_KEY']


weather(latitude, longitude, cle_api)
