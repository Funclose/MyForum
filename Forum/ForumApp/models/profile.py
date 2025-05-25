from django.db import models
from django.conf import settings 
# from ForumApp.models.user import User
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    profile_avatar = models.ImageField(upload_to='assets/profile_img/', blank=True, null=True,default='assets/profile_img/default_img.jpg')

    def __str__(self):
        return self.nickname