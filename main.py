import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv('.env')
# Parameters for the API
parameters = {
    "lat": os.environ.get("LAT"),
    "lon": os.environ.get("LONG"),
    "appid": os.environ.get("APPID"),
    "exclude": "current,minutely,daily"
}

# Getting the data from the weather API
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]

is_raining = False

# Checks if it is going to rain in the next 12 hours, which occurs when id < 700 as shown the weather API docs
for hour in range(0, 12):
    id_weather = data[hour]["weather"][0]["id"]
    if id_weather < 700:
        is_raining = True

# If it is going to rain, it will email notify me by email
if is_raining:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("yashcode.wiz1@gmail.com", os.environ.get("EMAIL_PASS"))
    connection.sendmail(from_addr="yashcode.wiz1@gmail.com", to_addrs="kumar.yashrana1718@gmail.com",
                        msg="Subject: Rain coming!\n\nIt's going to rain today. Please take an umbrella!")
    connection.close()
