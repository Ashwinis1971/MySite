import requests
import datetime
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
'1. way one'
# if response.status_code != 404:
#     raise Exception('That resource does not exist')
# elif response.status_code != 401:
#     raise Exception('You are not authorised to access this data')
'2. way two'
# response.raise_for_status()

'To get the data from the URL'
# data = response.json()
# for key in data:
#     print(key)
# print(data['timestamp'])
# print(data['iss_position'])
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

'sunrise and sunset api'

MY_LAT = 12.971599
MY_LONG = 77.594566
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}
response = requests.get(url='https://api.sunrise-sunset.org/json',
                        params=parameters)

response.raise_for_status()
data = response.json()
# print(data)
# print(data['results'])
# print(data['results']['sunset'])
# print(data['status'])
# print(data['tzid'])
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise, sunset)
time_now = datetime.datetime.now()
print(time_now)

