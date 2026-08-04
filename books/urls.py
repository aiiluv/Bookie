from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('more-bookie/', views.more_bookie, name='more_bookie'),
    path('add/', views.book_create, name='book_create'),

    # GOOGLE BOOKS
    path('search/', views.book_search, name='book_search'),

    path(
        'search/<str:book_id>/',
        views.google_book_detail,
        name='google_book_detail'
    ),

    path(
        'search/<str:book_id>/add/',
        views.add_google_book,
        name='add_google_book'
    ),

    path('<int:id>/edit/', views.book_update, name='book_update'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),
    path('<int:id>/', views.book_detail, name='book_detail'),

    path('register/', views.register, name='register'),
    path('logout-confirm/', views.logout_confirm, name='logout_confirm'),
    path('logout-confirm-2/', views.logout_confirm_2, name='logout_confirm_2'),
]