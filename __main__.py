import os
import sys

from .wrappers.open_weather import OpenWeather
from .wrappers.twilio import Twilio

def get_api_keys():
    keys = ()
    for item in ('open_weather_api_key', 'twilio_api_key'):
        key = os.environ.get(item)
        if key:
           keys += (key,)
        else:
            print("missing enviroment variable: {}".format(item))
            sys.exit()
    
    return keys

def main():
    open_weather_api_key, twilio_api_key = get_api_keys()

    # Set up OpenWeather wrapper
    weather = OpenWeather() 
    weather.set_api_key(open_weather_api_key)

    # Set up Twilio wrapper
    twilio = Twilio()
    twilio.set_api_key(twilio_api_key)


if __name__ == '__main__':
    main()