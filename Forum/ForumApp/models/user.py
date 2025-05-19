from django.db import models


class User(models.Model):
    name = models.CharField(null=False, max_length=30)
    surname = models.CharField(null=False, max_length=30)
    password = models.TextField(null=True, max_length=60, default='355565')
    confirmpassword = models.TextField(null=True,  max_length=60,  default='355565')
    email = models.EmailField(null=False)
    birthday = models.DateField(null=True)



