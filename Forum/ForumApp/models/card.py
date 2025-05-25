from django.db import models

class Card(models.Model):
    card_title = models.CharField(null=False,max_length=40)
    card_description = models.TextField()
                                                     
    card_pathImage = models.ImageField(upload_to='assets/', blank=True, null=True,default='assets/default.jpg')