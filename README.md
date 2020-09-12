# weather.py 🌧️
weather.py is a little module created to access weather information about any given city. Module uses [WeatherAPI](https://www.weatherapi.com) and [OpenWeatherMap](https://openweathermap.org) to perform gathering information so **you should change default API keys with your own keys** in the source code to use this module freely in your own projects.

## Usage
```py
from weather import Weather

istanbul = Weather("istanbul")

print(istanbul.temp_feelslike)
print(istanbul.wind_speed)
...
```

## Reference
| Attribute | Unit | Description |
|-----|-----|-----|
| city | | City name |
| country | | Country name |
| lat | | Latitude in decimal degree |
| lon | | Longitude in decimal degree |
| timezone | UTC | Timezone of the city |
| timezone_name | | Region name of the city's timezone |
| temp | °C | Temperature |
| temp_min | °C | Minimm temperature |
| temp_max | °C | Maximum temperature |
| temp_feelslike | °C | Human perception of weather |
| humidity | % | Humidity as percentage |
| visibility | m | Visibility as meters |
| pressure | mB | Atmospheric pressure as millibars |
| uv | | UV index |
| wind_speed | m/s | Wind speed |
| wind_degree | ° | Wind direction in degrees |
| wind_dir | | Wind direction as 16 point compass |
| gust_speed | m/s | Wind gust speed |
| cloudliness | % | Cloudliness as percentage |
| state_wapi | | Weather state description provided by WeatherAPI |
| state_owm | | Weather state description provided by OpenWeatherMap |

## Extras
Some functions are provided in the module to do conversions between temperature units
- `k2c()` → Kelvin to Celsius
- `k2f()` → Kelvin to Fahrenheit
- `c2k()` → Celsius to Kelvin
- `c2f()` → Celsius to Fahrenheit
- `f2c()` → Fahrenheit to Celsius
- `f2k()` → Fahrenheit to Kelvin

## Todo
- [ ] Users should be able to search any region/state, country and latitude, longitude
- [ ] Module should be able to get information about raining and snowing
- [ ] Support asynchronous requests

## License
[MIT](LICENSE) © Kadir Aksoy
