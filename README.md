# Dark Sky Python

Python wrapper for the Dark Sky Weather API. This should provide a lightweight library which is feature-complete with the API. Forked from [https://github.com/ratorx/dark-sky-python](https://github.com/ratorx/dark-sky-python), which has since been archived and was broken.

![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby-oneline.png)

Find your latitude and longitude [here](https://www.latlong.net/).

## Simple Usage
```python
import darksky

API_KEY = 'ADD-HERE'
LAT = ADD-HERE
LON = ADD-HERE

f = darksky.Forecast(API_KEY, LAT, LON) # Generates forecast object
```

From here, you can access all the data provided in the response.

Eg.
```python
current = f.currently
print(current.summary)
```

Eg. to get the forecast in 1 hour:
```python
hourly = f.hourly
print(hourly[1].summary)
```
