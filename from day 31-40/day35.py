# API Authentication
# www.openweathermap.org
# API link: https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={hourly},daily&appid={API key}

# Rain alert

import requests
import os   # for this app to work on pythonanywhere
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient   # for this app to work on pythonanywhere

# Open Weather Map keys
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

# Twilio Keys
account_sid = "ACd3c24d52621263c342b84d920551b28d"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
	"lat": 52.52,
	"lon": 13.40,
	"exclude": "current,minutely,daily",
	"appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()

# print(weather_data["hourly"][0]["weather"][0]["id"])

for i in range(0,12):
	weather_code = int(weather_data["hourly"][i]["weather"][0]["id"])
	if weather_code < 700:
		proxy_client = TwilioHttpClient()   # for this app to work on pythonanywhere
		proxy_client.session.proxies = {'https': os.environ['https_proxy']}   # for this app to work on pythonanywhere
		client = Client(account_sid, auth_token, http_client=proxy_client)   # updated for this app to work on pythonanywhere

		message = client.messages \
		                .create(
		                     body="It's going to rain today. Remember to bring an umbrella☔",
		                     from_='+15106741159',
		                     to='{your registered phone number}'
		                 )
		print(message.status)
	break

