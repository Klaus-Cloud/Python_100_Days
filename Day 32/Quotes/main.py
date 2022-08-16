import smtplib
import datetime as dt
import random as rnd



my_gmail = "klauspertest@gmail.com"
my_yahoo = "klauspertest@yahoo.com"
my_password = "Red1blau@mensa"
my_password_app_gmail = "snhouegtmzmmbspc"
my_password_app_yahoo = ""

with open("quotes.txt", "r") as file:
    quote_data = file.readlines()

now = dt.datetime.now()

if now.weekday() == 1:
    with smtplib. SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_gmail, password=my_password_app_gmail)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=my_yahoo,
                            msg=f"Subject:Happy Birthday\n\n{rnd.choice(quote_data)}"
                            )







