from django import forms
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'book_title',
            'book_genre',
            'book_category'
        ]