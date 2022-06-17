import requests
import json
import os
from pprint import pprint
from flask import Flask

app = Flask(__name__)


@app.route('/<lat>/<lon>')
def weather(lat, lon, api_key):
    cle_api = os.environ['API_KEY']
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
        lat, lon, api_key)

    weather_data = requests.get(url).json()

    json_str = json.dumps(weather_data)
    resp = json.loads(json_str)

    # pprint(resp['current'])

    return resp['current']


#latitude = os.environ['LAT']
#longitude = os.environ['LONG']

#weather(latitude, longitude, cle_api)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
