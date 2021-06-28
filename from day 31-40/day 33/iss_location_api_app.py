# ISS location api
# api link: http://api.open-notify.org/iss-now.json 
# link: https://www.latlong.net/

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)   # Will get a response code
response.raise_for_status()

data = response.json()

latitude = data["iss_position"]["latitude"]
logitude = data["iss_position"]["longitude"]

iss_position = (latitude, logitude)

print(iss_position)