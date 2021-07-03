# google sheet
# sheety.co
# nutritionix.com

import requests
from datetime import datetime

GENDER = "male"
WEIGHT = 75
HEIGHT = 172
AGE = 27

APP_ID = "4d5d1517"
API_KEY = "889b53db7b20c84b0842f2f8172f5e27"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/7e26797b72574cab74248f115a5e4beb/workoutTracking/workouts"

exercise_text = input('Tell us which exercise you did: ')

headers = {
	"x-app-id": APP_ID,
	"x-app-key": API_KEY,
}

parameters = {
	"query": exercise_text,
	"gender": GENDER,
	"weight_kg": WEIGHT,
	"height_cm": HEIGHT,
	"age": AGE,
}

response = requests.post(url=exercise_endpoint, json = parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
	sheet_inputs = {
		"workout" : {
			"date": today_date,
			"time": now_time,
			"exercise":exercise["name"].title(),
			"duration":exercise["duration_min"],
			"calories":exercise["nf_calories"],
		}
	}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)