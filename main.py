from datetime import datetime
import os
import dotenv
import requests

dotenv.load_dotenv()

APP_ID = os.getenv("REACT_APP_APP_ID")
APP_KEY = os.getenv("REACT_APP_APP_KEY")
EXERCISE_ENDPOINT = os.getenv("REACT_APP_EXERCISE_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("REACT_APP_SHEETY_ENDPOINT")

nutri_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

authenticate = ("bee8498", "jsdkfjighdifjhsklfjsdkl")

workout = input("Tell me which exercise you did:: ")

parameters = {
    "query": workout,
    "gender": "male",
    "weight_kg": 78.5,
    "height_cm": 170.64,
    "age": 24,
}

nutri_response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=nutri_header)
data = nutri_response.json()
# print(data)

today_date = datetime.now().strftime("%d/%m/%Y")
# print(today_date)
now_time = datetime.now().strftime("%X")
# print(now_time)

for exercise in data["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, auth=authenticate)
    print(sheet_response.text)
