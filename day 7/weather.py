import requests
import json

def fetch_weather(api_key):
    location = input("Enter a location: ")
    response = requests.get(
        f"http://api.weatherstack.com/current?access_key={api_key}&query={location}")
    data = response.json()

    location_data = data.get('location',{})
    current_data = data.get('current' ,{})

    loc = f"Location: {location_data.get('name', 'N/A')}, {location_data.get(
        'region', 'N/A')}, {location_data.get('country', 'N/A')}"
    curr = f"Temperature: {current_data['temperature']}°C \t Condition: {', '.join(current_data['weather_descriptions'])} \t Humidity: {current_data['humidity']} \t Wind Speed: {current_data['wind_speed']}"
    print(loc)
    print(curr)


api_key = "YOUR_API_KEY"
fetch_weather(api_key)
