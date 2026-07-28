from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback

        fields = [
            'rating',
            'email',
            'message'
        ]

        widgets = {

            'rating': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 5
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Your email (optional)'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Tell us what you think!',
                    'rows': 5
                }
            ),
        }