import pyowm
import datetime

from database_ops import dbOperations
from celery import Celery

app = Celery()

@app.task
def fetchData():
    dbHelper = dbOperations("local")
    owm = pyowm.OWM('ffb52b0cdebcf60299c9241d29d1f786')
    cities = {"London":'GB', "Paris":"FR", 'Sofia': 'BG', 'Madrid':'ES', 'Bucharest':'RO'}

    for key,value in cities.iteritems():
        place = key + "," + value
        observation = owm.weather_at_place(place)
        w = observation.get_weather()

        wind = w.get_wind()
        humidity = w.get_humidity()
        temp = w.get_temperature('celsius')
        date = datetime.datetime.today()
        saveData = {'city' : key    ,
                    'date' : date,
                    'humidity' : humidity,
                    'wind' : wind,
                    'temperature' : temp}

        dbHelper.insertData(saveData,"weather_historical_data")

if __name__ == '__main__':
    fetchData()