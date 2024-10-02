import requests
import os
from datetime import datetime

user_api=os.getenv['current_weather_data']
location=input("Enter the city name: ")


complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link=requests.get(complete_api_link)
api_data=api_link.json()


temp_city=((api_data['main']['temp']) - 273.15)
hmdt=api_data['main']['humidity']
weather_desc=api_data['weather'][0]['description']
wind_speed=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_speed ,'kmph')