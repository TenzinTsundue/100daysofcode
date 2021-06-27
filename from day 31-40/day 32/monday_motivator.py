# sending monday motivator quotes

import smtplib
import datetime as dt
import random

my_email = "yourgmail@gmail.com"
my_password = "yourpassword"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
	with open("quotes.txt") as file:
		data = file.readlines()
		quote = random.choice(data)

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_email, password=my_password)
		connection.sendmail(
			from_addr=my_email, 
			to_addrs="reciever@gmail.com", 
			msg=f"Subject:Monday motivation\n\n{quote}"
		)











