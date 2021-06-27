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
