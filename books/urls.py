from django.urls import path
from . import views

urlpatterns = [

    # BOOKS
    path('', views.index, name='index'),
    path('add/', views.book_create, name='book_create'),
    path('<int:id>/edit/', views.book_update, name='book_update'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),

    # AUTHENTICATION
    path('register/', views.register, name='register'),
    path('logget_out', views.goodbye, name='logged_out'),

    #SPOTIFY
    path(
        "spotify/login/",
        views.spotify_login,
        name="spotify_login"
    ),

    path(
        "spotify/callback/",
        views.spotify_callback,
        name="spotify_callback"
    ),

]