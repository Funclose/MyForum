from django.shortcuts import render
from django.http import HttpRequest
from ForumApp.models import Category



def home(request:HttpRequest):
    getCategories = Category.objects.all()
    return render(request, 'index.html', {'category': getCategories})

# def getAllCategory():
#     categories = Category.objects.all()
#     return categories()

