from config import *
import pyowm                                                              # weather
from datetime import datetime

def weather_start(bot, update):
    update.message.reply_text('Hi! I can determine current weather at city.')


def weather_help(bot, update):
    update.message.reply_text('Just type, for example, /weather Minsk')


def weather(bot, update, args):
    if args == []:
        update.message.reply_text('Enter the city. For example.\n/weather Minsk')
    else:
        owm = pyowm.OWM(owm_api_key)
        text_location = "".join(str(x) for x in args)
        observation = owm.weather_at_place(text_location)
        w = observation.get_weather()
        humidity = w.get_humidity()
        wind = w.get_wind()
        temp = w.get_temperature('celsius')
        convert_temp = temp.get('temp')
        convert_wind = wind.get('speed')
        convert_humidity = humidity
        text = ""
        text = text + "Weather status is " + w.get_status()
        text = text + "\nWeather detailed status is " + w.get_detailed_status()
        text = text + "\nReference time:\n" \
        + datetime.fromtimestamp(w.get_reference_time()).strftime('%d %B %Y %H:%M:%S')
        text = text + "\nTemperature:".ljust(25) + str(convert_temp) + " celsius"
        text = text + "\nWind speed:".ljust(26) + str(convert_wind) + "m/s"
        text = text + "\nHumidity:".ljust(29) + str(convert_humidity) + "%"
        update.message.reply_text(text)

