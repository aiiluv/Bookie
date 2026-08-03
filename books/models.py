from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Books(models.Model):

#     CATEGORY_CHOICES = [
#         ('unread', 'unread'),
#         ('read', 'read'),
#         ('dropped', 'dropped')
#     ]

#     #setiap buku dimiliki oleh satu user
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     book_cover = models.FileField(upload_to='', null=True)
#     book_title = models.CharField(max_length=100)
#     book_genre = models.CharField(max_length=100)
#     book_category = models.CharField(
#         max_length=20,
#         choices=CATEGORY_CHOICES,
#         default='unread'
#     )

class Books(models.Model):
    CATEGORY_CHOICES = [
        ('unread', 'unread'),
        ('read', 'read'),
        ('dropped', 'dropped')
    ]

    #setiap buku dimiliki oleh satu user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200, blank=True)
    book_genre = models.CharField(max_length=300)
    book_category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='unread'
    )

    book_cover = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    isbn = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.book_title

class SpotifyToken(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    access_token = models.TextField()
    refresh_token = models.TextField()
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} Spotify"