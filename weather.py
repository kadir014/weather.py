#                       Weather.py
#            Kadir Aksoy - 2020 - Licensed MIT
#          https://github.com/kadir014/weather.py

import requests
import json


#IMPORTANT: You should change API keys written below with your own keys, because
#           these keys will hit the request limit so easily once I publish this
#           project on GitHub and people will use these keys by default.


#WeatherAPI  https://www.weatherapi.com
class WAPI:
    base_url = "http://api.weatherapi.com/v1"
    key = "c6acac8187f3470db39115311201209"

#OpenWeatherMap  https://openweathermap.org
class OWM:
    base_url = "http://api.openweathermap.org/data/2.5"
    key = "5d91b4d0414a1469ccd429e3fc2352c9"


#Kelvin to Celsius
def k2c(kelvin): return kelvin - 273.15

#Celsius to Kelvin
def c2k(celsius): return celsius + 273.15

#Fahrenheit to Celsius
def f2c(fahrenheit): return (fahrenheit - 32) * 5/9

#Celsius to Fahrenheit
def c2f(celsius): return (celsius * 9/5) + 32

#Kelvin to Fahrenheit
def k2f(kelvin): return ((kelvin - 273.15) * 9/5) + 32

#Fahrenheit to Kelvin
def f2k(fahrenheit): return ((fahrenheit - 32) * 5/9) + 273.15


class Weather:
    #TODO: User should be able to search by region/state name, country name and lat/lon
    def __init__(self, city):
        self.city = city.lower().capitalize()
        self.update()

    def __repr__(self):
        return f"<weather.Weather(city={self.city}, temp={self.temp}*C)>"

    def update(self):
        data_wapi = json.loads(requests.get(f"{WAPI.base_url}/current.json?key={WAPI.key}&q={self.city}").content)
        data_owm  = json.loads(requests.get(f"{OWM.base_url}/weather?q={self.city}&appid={OWM.key}").content)

        self._owm_id = data_owm["sys"]["id"]

        #Geogrophic information
        self.country =        data_wapi["location"]["country"]
        self.lat =            data_wapi["location"]["lat"]
        self.lon =            data_wapi["location"]["lat"]
        self.timezone_name =  data_wapi["location"]["tz_id"]
        self.timezone =       f'UTC+{int(float(data_owm["timezone"])/3600)}'

        #Temperature information
        self.temp =           k2c(data_owm["main"]["temp"])
        self.temp_min =       k2c(data_owm["main"]["temp_min"])
        self.temp_max =       k2c(data_owm["main"]["temp_max"])
        self.temp_feelslike = data_wapi["current"]["feelslike_c"]

        #General information
        self.humidity =       data_owm["main"]["humidity"]
        self.visibility =     data_owm["visibility"]
        self.pressure =       data_owm["main"]["pressure"]
        self.uv =             data_wapi["current"]["uv"]

        #Wind information
        self.wind_speed =     data_owm["wind"]["speed"]
        self.wind_degree =    data_owm["wind"]["deg"]
        self.wind_dir =       data_wapi["current"]["wind_dir"]
        self.gust_speed =     float(data_wapi["current"]["gust_kph"]) / 3.6

        #Cloud information
        self.cloudliness =    data_owm["clouds"]["all"]
        self.state_wapi =     data_wapi["current"]["condition"]["text"]
        self.state_owm =      f'{data_owm["weather"][0]["main"]}, {data_owm["weather"][0]["description"]}'

        #TODO: Rain, snow and better timezone support
        #TODO: Dictionary key checking
