import requests
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv



# you can use twilio to send sms instead,
# a bunch of apis to explore at "https://apilist.fun"

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")






parameters = {
    "lat": 6.283023,
    "lon": 5.618527,
    "cnt": 4,
    "appid": os.getenv("WEATHER_API_KEY")
}
# latitude = 6.283023
# longitude = 5.618527

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = (weather_data["list"])


# weather_data = test_data.data
# weather_list = (weather_data["list"])
# print(weather_list)

will_rain = False
for weather in weather_list:
    if (weather["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    msg = MIMEText("it might rain today, please hold an umbrella")
    msg['Subject'] = "Today's Weather"
    msg['From'] = my_email
    msg['To'] = "osegbegoldenjoe1@gmail.com"
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
        connection.login(my_email, my_password)
        connection.sendmail(my_email, msg['To'], msg.as_string())