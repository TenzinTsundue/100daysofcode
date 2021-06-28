# Buiding a bot to notify you when ISS is over your head during a night through email

# api for iss location: http://api.open-notify.org/iss-now.json
# api for sunset and sunrise: https://api.sunrise-sunset.org/json

import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 51.507351
MY_LNG = -0.127758
MY_EMAIL = "yourgmail@gmail.com"
MY_PASSWORD = "yourpassword!"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_logitude = float(data["iss_position"]["longitude"])

    # Your position is within +-5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_logitude <=MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT, 
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr = MY_EMAIL,
                to_addrs= MY_EMAIL,
                msg="Subject:ISS Spotted\n\nCheck the sky, ISS is above you."
            )