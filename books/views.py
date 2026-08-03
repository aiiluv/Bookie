import requests
import base64
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render, redirect, get_object_or_404

from .models import Books, SpotifyToken
from .forms import BooksForm
from .google_books import search_books, get_book

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('index')

    else:

        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })


@login_required
def index(request):

    category = request.GET.get('category')

    books = Books.objects.filter(
        user=request.user
    )

    total_books = books.count()
    unread_books = books.filter(book_category='unread').count()
    read_books = books.filter(book_category='read').count()
    dropped_books = books.filter(book_category='dropped').count()

    if category:

        books = books.filter(
            book_category=category
        )

    for book in books:
        if book.book_genre:
            genres = [g.strip() for g in book.book_genre.split("/")]

            book.display_genre = " / ".join(genres[:3])

    return render(request, 'books/index.html', {
        'books': books,
        'total_books' : total_books,
        'unread_books' : unread_books,
        'read_books' : read_books,
        'dropped_books' : dropped_books
    })

@login_required
def logout_confirm(request):
    return render(request, 'registration/logout_confirm.html')

@login_required
def logout_confirm_2(request):
    return render(request, 'registration/logout_confirm_2.html')

@login_required
def book_create(request):

    if request.method == 'POST':

        form = BooksForm(request.POST)

        if form.is_valid():

            book = form.save(commit=False)

            book.user = request.user

            book.save()

            return redirect('index')

    else:

        form = BooksForm()

    return render(request, 'books/book_form.html', {
        'form': form
    })


@login_required
def book_update(request, id):

    book = get_object_or_404(
        Books,
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        form = BooksForm(
            request.POST,
            instance=book
        )

        if form.is_valid():

            form.save()

            return redirect('index')

    else:

        form = BooksForm(
            instance=book
        )

    return render(request, 'books/book_form.html', {
        'form': form
    })


@login_required
def book_delete(request, id):

    book = get_object_or_404(
        Books,
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        book.delete()

        return redirect('index')

    return render(request, 'books/book_confirm_delete.html', {
        'book': book
    })

def goodbye(request):
    return render(request, 'books/registration/login.html')

@login_required
def book_detail(request, id):
    book = get_object_or_404(
        Books,
        id=id,
        user = request.user
    )

    return render(request, 'books/book_detail.html', {
        'book' : book
    })

@login_required
def book_search(request):

    query = request.GET.get("q", "")

    books = []

    if query:
        books = search_books(query)

    return render(request, "books/search.html", {
        "books": books,
        "query": query,
    })

def book_api_detail(request, book_id):

    book = get_book(book_id)

    if not book:
        return render(request, "books/book_not_found.html")

    return render(request, "books/api_book_detail.html", {
        "book": book
    })

def google_book_detail(request, book_id):

    book = get_book(book_id)

    if not book:
        return render(request, "books/google_book_detail.html", {
            "book": None
        })

    return render(request, "books/google_book_detail.html", {
        "book": book
    })

@login_required
def add_google_book(request, book_id):

    if request.method != "POST":
        return redirect("book_search")

    book = get_book(book_id)

    if not book:
        return redirect("book_search")

    info = book.get("volumeInfo", {})

    title = info.get("title", "Unknown title")

    authors = info.get("authors", [])
    author = ", ".join(authors)

    categories = info.get("categories", [])
    genre = ", ".join(categories)

    description = info.get("description", "")

    image_links = info.get("imageLinks", {})
    cover = image_links.get("thumbnail", "")

    identifiers = info.get("industryIdentifiers", [])

    isbn = ""

    if identifiers:
        isbn = identifiers[0].get("identifier", "")

    Books.objects.create(
        user=request.user,
        book_title=title,
        book_author=author,
        book_genre=genre,
        book_cover=cover,
        description=description,
        isbn=isbn,
        book_category="unread"
    )

    return redirect("index")