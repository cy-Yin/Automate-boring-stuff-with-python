#! python
# Prints the weather for a location from the command line.

import json, requests, sys

from sklearn.utils import resample

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3" % (location)
response = requests.get(url)
try:
    response.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))

# Load JSON data into a Python variable.
weatherData = json.load(response.text)
# Print weather descriptions.
w = weatherData['list']
print("Current weather in %s: " % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])