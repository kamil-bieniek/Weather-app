import requests
import json
from pprint import pprint
import webbrowser
#import key

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

    more = input(
        "Do you want see more about your town weather ?  Y/N  ").upper()

    if(more == "Y"):
        link = "https://www.google.com/search?client=opera-gx&q=pogoda+rzeszow&sourceid=opera&ie=UTF-8&oe=UTF-8"
        webbrowser.open_new_tab(link)
    else:
        print("if not then see you later")
