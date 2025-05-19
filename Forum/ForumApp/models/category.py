from django.db import models
from .card import Card

class Category(models.Model):
    category = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='posts')
    author = models.CharField(max_length=100)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

  