#!/usr/bin/env python

import darksky
from ConfigParser import ConfigParser

# Import details from config file to save typing
config = ConfigParser()
config.read('config/config.ini')
api_key = config.get('darksky', 'key')
latitude = config.get('darksky', 'latitude')
longitude = config.get('darksky', 'longitude')

f = darksky.Forecast(api_key, latitude, longitude) # Generates forecast object

# Print the current weather summary in the console
current = f.currently
print(current.summary)

# Print the forecast summary for the next hour in the consol
hourly = f.hourly
print(hourly[1].summary)
