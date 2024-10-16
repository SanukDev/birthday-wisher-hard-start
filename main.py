from typing import Dict, Any
import datetime as dt
import pandas as pd
import random
import smtplib

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
data_birthdays = pd.read_csv("birthdays.csv")
data = data_birthdays.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

dic_data = {(x['month'], x['day']): [x['email'], x['name']] for x in data}
print(dic_data)

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
now = dt.datetime.now()
month = now.month
day = now.day
print( month, day)
if (month, day) in dic_data:

    email = dic_data[(month, day)][0]
    name = dic_data[(month, day)][1]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as l_data:
        letter_data = l_data.readlines()
        letter_str = ""
        for x in letter_data:
            letter_str += x
        letter_ready = letter_str.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="samukakaroto123@gmail.com", password="wplk zuyj gapn ntrs")
        connection.sendmail(from_addr="samukakaroto123@gmail.com",
                            to_addrs=email, msg=f"Subject: Happy birthday! \n\n{letter_ready}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



