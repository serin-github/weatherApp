import sys
import requests

api_key = '3c51f3d4d735c48ea1ba59379ded775b'
# user_input = input("Enter city: ")
user_input = sys.argv[1]

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")

    # sample testing git

    # again git test

    # sample fork