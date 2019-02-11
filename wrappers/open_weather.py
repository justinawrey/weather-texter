import requests
import datetime

def unix_to_pst(utc_time):
    dt = datetime.datetime.utcfromtimestamp(utc_time)
    return (dt.strftime("%a %b. %d"), dt.hour)

class OpenWeather:
    def __init__(self):
        self.api_key = ""
    
    def set_api_key(self, key):
        self.api_key = key

    def get_5_day_forecast(self, city, country_code):
        endpoint = "http://api.openweathermap.org/data/2.5/forecast?q={},{}&units=metric&appid={}" \
            .format(city, country_code, self.api_key)
        res = requests.get(endpoint).json()
        forecast = []
        for item in res['list']:
            weather_str = item['weather'][0]['main']
            weather_id = item['weather'][0]['id']
            day, hour = unix_to_pst(item['dt'])
            temp = item['main']['temp']
            if hour == 12:
               forecast.append((weather_id, weather_str, day, temp))
        return forecast
            