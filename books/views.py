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

    return render(request, 'books/index.html', {
        'books': books,
        'total_books' : total_books,
        'unread_books' : unread_books,
        'read_books' : read_books,
        'dropped_books' : dropped_books
    })


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

@login_required
def spotify_login(request):
    scope = "user-read-currently-playing user-read-playback-state"

    auth_url = (
        "https://accounts.spotify.com/authorize"
        f"?client_id={settings.SPOTIFY_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={settings.SPOTIFY_REDIRECT_URI}"
        f"&scope={scope.replace(' ', '%20')}"
    )

    return redirect(auth_url)

@login_required
def spotify_callback(request):
    code = request.GET.get("code")

    if not code:
        return JsonResponse({
            "error": "Spotify authorization failed"
        })

    client_credentials = (
        f"{settings.SPOTIFY_CLIENT_ID}:"
        f"{settings.SPOTIFY_CLIENT_SECRET}"
    )

    encoded_credentials = base64.b64encode(
        client_credentials.encode()
    ).decode()

    token_response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        },
        headers={
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )

    token_data = token_response.json()

    if "access_token" not in token_data:
        return JsonResponse(token_data)

    access_token = token_data["access_token"]
    refresh_token = token_data["refresh_token"]
    expires_in = token_data["expires_in"]

    expires_at = timezone.now() + timedelta(
        seconds=expires_in
    )

    SpotifyToken.objects.update_or_create(
        user=request.user,
        defaults={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": expires_at,
        }
    )

    return redirect("index")

def goodbye(request):
    return render(request, 'books/registration/logged_out.html')