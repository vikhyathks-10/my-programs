import requests

API_KEY = "YOUR_NEW_API_KEY"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Bangalore,IN",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Response:", response.text)