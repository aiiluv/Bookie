import requests

API_KEY = "AIzaSyDsRtNIo81HYS8OEnK6dtwmLr5J9KvoWps"

url = "https://www.googleapis.com/books/v1/volumes"

params = {
    "q": "Laskar Pelangi",
    "maxResults": 5,
    "key": API_KEY
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())