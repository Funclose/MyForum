from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='comments')  # Category = пост
    author = models.CharField(max_length=100)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)