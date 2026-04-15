# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import requests
import smtplib
import os

api_key = os.environ.get("API_KEY")
MY_LAT = os.environ.get("MY_LAT")
MY_LON = os.environ.get("MY_LON")

# Email credentials
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: It's raining today! \n\n Bring an umbrella.")
