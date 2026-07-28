from django.db import models

# Create your models here.
class Feedback(models. Model):
    rating = models.IntegerField()
    email = models.EmailField(
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.rating}/5 - {self.email}"