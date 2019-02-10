import requests
import pprint
import datetime

def unix_to_pst(utc_time):
    dt = datetime.datetime.utcfromtimestamp(utc_time)
    return (dt.day, dt.hour)

def get_art(weather_id):
    if weather_id >= 801:
        return 'Clouds'
    elif weather_id >= 800:
        return  'Clear' 
    elif weather_id >= 700:
        return 'Mist'
    elif weather_id >= 600:
        return 'Snow'
    elif weather_id >= 500:
        return 'Rain'
    elif weather_id >= 300:
        return 'Drizzle'
    elif weather_id >= 200:
        return 'Thunderstorm'

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
            day, hour = unix_to_pst(item['dt'])
            temp = item['main']['temp']
            weather = item['weather'][0]['main']
            weather_id = item['weather'][0]['id']
            if hour == 12:
               forecast.append({'day': day, 'temp': temp, 'weather': weather, 'art': get_art(int(weather_id))})
        return forecast
            