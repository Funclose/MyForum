from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from ForumApp.models import Category

def getAllCategory():
    categories = Category.objects.all()
    return categories

def home(request:HttpRequest):
    getCategories = getAllCategory()
    return render(request, 'index.html', {'category': getCategories})

def createCategory(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        Category.objects.create(
            category_title = title,
            category_description = description,
            category_pathImage = image
        )
        return redirect("homePage")
    return render(request, "category/addCategory.html")
    


def removeCategory(request, pk):
    if request.method == "POST":
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect("homePage")
    return render(request, 'index.html', {'category': getAllCategory})


