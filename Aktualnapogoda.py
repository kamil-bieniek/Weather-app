import requests
import json
from pprint import pprint
import webbrowser

def now_weather(questions):
    temp = round(int(questions["main"]["temp"]) - 273.15, 1)
    print("now it is", temp,  "degrees Celsius in :", questions["name"])

city = str(input("select the city where you want to see the temperature : "))

params = {
    "q": city,
    "appid": "7bdb71dbed4c18d7cff757f1fa321702"
}

r = requests.get("https://api.openweathermap.org/data/2.5/weather?",params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    # pprint(questions)
    now_weather(questions)


