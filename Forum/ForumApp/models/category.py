from django.db import models
from .card import Card
from django.conf import settings

class Category(models.Model):
    category = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # author = models.CharField(max_length=255)

  