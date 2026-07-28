from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    # BOOKS
    path('books/', include('books.urls')),

    # LOGIN / LOGOUT
    path('accounts/', include('django.contrib.auth.urls')),

]