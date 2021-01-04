import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import requests

USER_AGENT = {'User-agent': 'Mozilla/5.0'}

class ColdAlert():
    def __init__(self):
        lat = 52.229676
        lon = 21.012229
        api_key = self.get_api_key().strip()
        url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,hourly,minutely&appid={api_key}"
        self.raw_data = requests.get(url, headers=USER_AGENT).content
        self.log = {}

    def get_api_key(self):
        with open(os.path.join(sys.path[0],'weather_api_key')) as file_object:
            api_key = file_object.read()
            return api_key

    def alert(self):
        data = json.loads(self.raw_data)
        min_temp_today = round(data['daily'][0]['temp']['min']-273,1)
        self.log['temperatura'] = min_temp_today
        if min_temp_today < 10:
            self.log['alert'] = True
            alert = f'Będzie dziś zimno! {min_temp_today}'
        else:
            self.log['alert'] = False
            alert = None

        return alert

