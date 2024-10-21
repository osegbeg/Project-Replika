import smtplib
import datetime as dt
import random
import pandas as pd

from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

#

load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
# recipients = os.getenv("RECIPIENTS").split(",")
#
now = dt.datetime.now()
week_day = now.weekday()
hour = now.hour
month = now.month
day = now.day

# Specify the folder path
folder_path = "./letter_templates"

# Initialize an empty list to store file contents
file_contents = []

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    # Check if file is a text file
    if filename.endswith(".txt"):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)

        # Open and read the file
        with open(file_path, 'r') as file:
            content = file.read()
            # Append file content to the list
            file_contents.append(content)

#
#
# with open("quotes.txt", "r") as quotes:
#     quotes_list = quotes.readlines()
#     random_quote = random.choice(quotes_list)
#
# if hour == 22:
#     msg = MIMEText(random_quote)
#     msg['Subject'] = "Motivated to motivate"
#     msg['From'] = my_email
#     with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
#         for recipient in recipients:
#             msg['To'] = recipient.strip()
#             connection.login(my_email, my_password)
#             connection.sendmail(my_email, recipient.strip(), msg.as_string())

birthday_file = pd.read_csv("birthdays.csv")
birthday_dataframe = pd.DataFrame(birthday_file)
birthday_dict = birthday_dataframe.to_dict(orient="list")

for index, row in birthday_dataframe.iterrows():
    if row['month'] == month and row['day'] == day:
        chosen_file = random.choice(file_contents).replace("[NAME]", row["name"])
        msg = MIMEText(chosen_file)
        msg['Subject'] = "Happy Birthday"
        msg['From'] = my_email
        msg['To'] = row["email"]
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
            connection.login(my_email, my_password)
            connection.sendmail(my_email, row["email"], msg.as_string())




