# weather_prediction

This program checks if it is going to rain in the next 12 hours, if so it sends a warning email.
The program requests the weather API (https://api.openweathermap.org/data/2.5/onecall) and checks the JSON data returned for any potential rain. It uses the SMPT library to send emails.
This script can be uploaded to Pythonanywhere to be run every day so that you will be notified if any rain is coming!
