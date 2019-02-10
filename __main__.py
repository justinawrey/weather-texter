import os
import sys
import time

import schedule
import requests
from .wrappers.open_weather import OpenWeather
from .wrappers.twilio import Twilio

def get_api_keys():
    return (os.environ.get(item) for item in ('open_weather_api_key', 'twilio_api_key'))

def main():
    # Check that api keys are set via environment
    open_weather_api_key, twilio_api_key = get_api_keys()
    if not (open_weather_api_key and twilio_api_key):
        print("missing api keys")
        sys.exit()

    # Set up OpenWeather wrapper
    weather = OpenWeather() 
    weather.set_api_key(open_weather_api_key)

    # Set up Twilio wrapper and register recipients to receive weather updates
    twilio = Twilio()
    twilio.set_api_key(twilio_api_key)
    twilio.register_recipient("+16048457579")

    # Define the cron job to be ran
    def send_forecast():
        forecast = weather.get_5_day_forecast("vancouver", "ca")
        twilio.send_data(forecast)

    # Set up cron to perform job every day at 8 AM
    schedule.every().day.at("08:00").do(send_forecast)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()