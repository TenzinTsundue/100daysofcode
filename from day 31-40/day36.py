# fetching news and stock change between last two day through sms 

import requests
from datetime import date, datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YOUR KEY"
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=YOURKEY

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR KEY"
# https://newsapi.org/v2/everything?q=apple&from=2021-06-30&to=2021-06-30&sortBy=popularity&apiKey=YOURKEY

account_sid = "ACd3c24d52621263c342b84d920551b28d"
auth_token = "YOUR AUTH KEY"

parameter = {
	"function": "TIME_SERIES_DAILY_ADJUSTED",
	"symbol": STOCK,
	"apikey": STOCK_API_KEY,
}

today = date.today()

# for stock price to fetch
stock = requests.get(STOCK_ENDPOINT, params=parameter)
stock_data = stock.json()


def cal_per_diff():
	yesterday_price = float(stock_data["Time Series (Daily)"][str(today - timedelta(days=1))]["4. close"])
	day_before_yesterday_price = float(stock_data["Time Series (Daily)"][str(today - timedelta(days=2))]["4. close"])
	difference = yesterday_price - day_before_yesterday_price
	percentage_difference = difference/day_before_yesterday_price * 100
	if percentage_difference<0:
		return f'🔻{str(round(percentage_difference, 2))}'
	else:
		return f'🔺{str(round(percentage_difference, 2))}'


percentage_difference = cal_per_diff()

# for news to fetch
parameter = {
	"q": "tesla",
	"from": str(today - timedelta(days=2)),
	"to":str(today - timedelta(days=1)),
	"sortBy": "popularity",
	"apiKey": NEWS_API_KEY,

}

news = requests.get(NEWS_ENDPOINT, params=parameter)
news_data = news.json()


def top_three_news():
	news = ""
	for i in range(0,3):
		new = f'{i+1}. {news_data["articles"][i]["title"]}.'
		news = "\n".join([news, new])
	return news


text = top_three_news()

# to send message
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body=f"{STOCK}: {percentage_difference} \nBrief: {text}",
                     from_='+YOUR TWILIO NUMBER',
                     to='+YOUR REGISTERED PHONE NUMBER'
                 )

print(message.status)
