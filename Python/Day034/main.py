import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "2YM45CWVV1Q0DJ1C"
NEWS_API_KEY = "29c96b5c42594b10b87553006c19cf34"

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


response_trade = requests.get(STOCK_ENDPOINT,params=stock_params)
response_trade.raise_for_status()
data_trade = response_trade.json()["Time Series (Daily)"]

data_trade_list = [value for (key, value) in data_trade.items()]

#Yesterday closing price and data
yesterday_data = data_trade_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Day before yesterday closing price and data
before_yesterday_data = data_trade_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]
print(before_yesterday_closing_price)

#Calculate the difference between yesterday and the day before
diference = abs(float(before_yesterday_closing_price) - float(before_yesterday_closing_price))
diference_perc = (diference/float(yesterday_closing_price))*100
if abs(diference_perc) > 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response_news.json()["articles"]
    three_art = articles[:3]

    formatted_articles = [f"{STOCK_NAME }: {article['title']}. \nBrief: {article['description']} " for article in three_art]
    print(formatted_articles)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 