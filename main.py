

from twilio.rest import Client
from datetime import datetime

import pandas
import random

account_sid='**********'
auth_token='***********'

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=contents,
        from_='+1 985 531 1090',
        to='*************'
    )
    print(message.status)


