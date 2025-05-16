from django.db import models

class Category(models.Model):
    category_title = models.CharField(null=False,max_length=40)
    category_description =  models.TextField()
                                                     #дописать путь к файлу
    category_pathImage = models.ImageField(upload_to='assets/', blank=True, null=True)

    # def getAllCategory():
    #     allCategory = 