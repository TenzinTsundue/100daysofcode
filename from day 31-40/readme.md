> 24 June 2021 | Day 31

created flash card app to learn french

Technology use
- tkinter
- pandas

<img src="https://user-images.githubusercontent.com/40035716/123389560-a346f500-d5b7-11eb-952f-083e826f744c.PNG" width="300">
<img src="https://user-images.githubusercontent.com/40035716/123389568-a3df8b80-d5b7-11eb-9dc9-f93eabc79bce.PNG" width="300">

> 26 June 2021 | Day 32

sending email using smtplib and datetime module

```python
# only work after modefying the security of your mail accout

import smtplib

my_email = "yourgmail@gmail.com"
my_password = "yourpassword"

with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=my_email, password=my_password)
	connection.sendmail(
		from_addr=my_email, 
		to_addrs="reciever@gmail.com", 
		msg="Subject:First test\n\nThis is the body of my email"
	)
```

```python
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()   # 0 Monday, 1 Tuesday...6 Sunduy

data_of_birth = dt.datetime(year=1995, month=7, day=16, hour=10)
print(data_of_birth)
```

> 28 June 2021 | Day 33

**API: Application Programming Interface**

Is a set of commands, functions, protocols, and objects that programmers can user to create a software or interact with an external system

Response Codes (HTTP status code)
- 1xx: Information
- 2xx: Success
- 3xx: Redirectrion
- 4xx: Client Error
- 5xx: Server Error

```python
print(response.status_code)
response.raise_for_status()
```

Some api accept API parameter 

> 29 June 2021 | Day 34

Type hint and arrow

```python
age: int
name: str 
.
.
.
age= "string"   # will show warning/error
```

```python


def police_check(age: int) -> bool:   # This function is expected to return boolen (Type hint)
	if age>18:
		can_drive = True
	else:
		can_drive = False
	return can_drive
  # return "A string"    # will show warning and error 
```

Quizzer app using API and GUI

<img src="https://user-images.githubusercontent.com/40035716/123772653-a6a8ec00-d8e9-11eb-8281-fb092c46f0af.PNG" width=300>

> 30 June 2021 | Day 35

API keys, Authentication, Enviroment Variables and sending SMS

Enviroment Variable
- convenience
- security

```bash
$ env
$ export OWM_API_KEY=d99573693fd6195ac4ecnottherealone
$ export TWILIO_AUTH_TOKEN=d99573693fd6195ac4enottherealone
```

> 1 July 2021 | Day 36

Create an app to get specific stock price change bewtween last two days and check news related to that stock company and share the detail through a sms.

what we use:
- for stockpice: https://www.alphavantage.co/query
- for news: https://newsapi.org/v2/everything
- for sms: twilio

> 2 July 2021 | Day 37

Advance Authentication Requests
- GET requests.get()
- POST requests.post()
- PUT requests.put()   # update
- DELETE requests.delete()

Pixela - habit tracker like github daily activity tracker

