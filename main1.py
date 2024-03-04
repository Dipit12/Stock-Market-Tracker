# stock api
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key = os.environ.get("STOCK_API")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key
}

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'


response = requests.get(url = "https://www.alphavantage.co/query?",params=parameters)
data = response.json()
"""
print(data)


high_price = data["Time Series (Daily)"]["2024-03-01"]["2. high"]
low_price = data["Time Series (Daily)"]["2024-03-01"]["3. low"]
open_price = data["Time Series (Daily)"]["2024-03-01"]["1. open"]
close_price = data["Time Series (Daily)"]["2024-03-01"]["4. close"]

print(high_price)
print(low_price)
print(open_price)
print(close_price)

opening_closing_diff = abs(float(close_price)-float(open_price))
max_diff = abs(float(high_price)-float(low_price))
print(opening_closing_diff)
print(max_diff)
"""

data_list = [value for (key,value) in data.items()]
yesterday_list =data_list[1]
print(data_list)
print(yesterday_list)

yesterday_closing_price = yesterday_list["4. close"]
day_before_yesterday = data_list[2]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(int(yesterday_closing_price) - int(day_before_yesterday_closing_price))
print(difference)

diff_percentage =(difference/int(yesterday_closing_price)) * 100

# news api


news_api_key =os.environ.get("NEWS_API")
#url = "https://newsapi.org/v2/everything?"

if diff_percentage >=3:

    news_params ={
        "q":COMPANY_NAME,
        "apikey":news_api_key,
        }
    new_response = requests.get(url = "https://newsapi.org/v2/everything?",params=news_params)
    articles = new_response.json()["articles"]
    #print(articles)

    three_articles = articles[:3]
    #content = three_articles[0]['title']['description']
    print(three_articles)


    # sms api using twilio
    from twilio.rest import Client
    acc_sid = "ACa78b12c08781dc142129e26c20725dbb"
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(acc_sid,auth_token)
    formatted_article=[f'Headline: {article["title"]}. \nBrief: {article["description"]}' for article in three_articles]

    for article in formatted_article:
        message = client.messages \
            .create(
                messaging_service_sid='MG9752274e9e519418a7406176694466fa',
                body= formatted_article,
                from_="+19377300622",
                to="+918368355407"


             )

        print(message.status)