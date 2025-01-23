import requests
import json

def fetch_api(url):
    data = requests.get(url)
    return data.json()

url = 'https://jsonplaceholder.typicode.com/todos'
api = fetch_api(url)
print(api)