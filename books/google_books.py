import requests
from django.conf import settings

def get_book(book_id):

    url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"

    params = {
        "key": settings.GOOGLE_BOOKS_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    return response.json()

def search_books(query):

    url = "https://www.googleapis.com/books/v1/volumes"

    params = {
        "q": query,
        "maxResults": 20,
        "key": settings.GOOGLE_BOOKS_API_KEY,
    }

    response = requests.get(url, params=params)

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("ERROR:", response.text)
        return []

    data = response.json()

    return data.get("items", [])

def get_book(book_id):

    url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"

    params = {
        "key": settings.GOOGLE_BOOKS_API_KEY,
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    return response.json()