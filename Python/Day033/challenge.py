import requests

MY_LAT = 39.749535
MY_LONG = -8.807683

OMW_ENDPOINT = "api_name"
api_key = "api_key"

weather_params = {
    "lat" : MY_LAT,
    "long" : MY_LONG,
    "api": "api_key",
    "cnt": 4
}

response = requests.get(OMW_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0][id])
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring umbrella")