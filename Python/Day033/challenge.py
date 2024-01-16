import requests

MY_LAT = 39.749535
MY_LONG = -8.807683

OMW_ENDPOINT = ""
api_key = "123456"

weather_params = {
    "lat" : MY_LAT,
    "long" : MY_LONG,
    "api": "api_key"
}

response = requests.get("", params=weather_params)
response.json()