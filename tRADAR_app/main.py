import os

import requests
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "BTC"
COIN_NAME = "Bitcoin"
coin_parameters = {
    "function":"DIGITAL_CURRENCY_DAILY",
    "symbol":"BTC",
    "market":"USD",
    "apikey": os.getenv("ALPHAVANTAGE_API_KEY")
}

news_parameters = {
    "pageSize":"5",
    "q":"bitcoin",
    "apiKey": os.getenv("NEWS_API_KEY")
}

COIN_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(COIN_ENDPOINT, params=coin_parameters)
response.raise_for_status()
coin_data = response.json()
# print(coin_data)
# coin_test = test_data.coin_data

daily = coin_data["Time Series (Digital Currency Daily)"]
# for key,value in daily.items():
#     new_dict = {key:value}
#     coin_list.append(new_dict)

coin_list = [{"date":value} for key,value in daily.items()]

yesterday_coin_value = float((coin_list[0]["date"]["4. close"]))
day_before_yesterday_coin_value = float((coin_list[0]["date"]["1. open"]))
print(abs(yesterday_coin_value - day_before_yesterday_coin_value))
if yesterday_coin_value > day_before_yesterday_coin_value:
    print("Gains🔼")
elif yesterday_coin_value < day_before_yesterday_coin_value:
    print ("Loss🔻")
else:
    print ("same as yesterday")

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
daily_news = news_response.json()

# daily_news = test_news.news
articles = daily_news["articles"]
description = [article["description"] for article in articles]
print(description)
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

