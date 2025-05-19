from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from ForumApp.models import Category, Card

def getAllCategory():
    categories = Category.objects.all()
    return categories

# def home(request:HttpRequest):
#     getCategories = getAllCategory()
#     return render(request, 'index.html', {'category': getCategories})

def createCategory(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        Card.objects.create(
            card_title = title,
            card_description = description,
            card_pathImage = image
        )

       
        return redirect("homePage")
    return render(request, "category/addCategory.html")
    


def removeCategory(request, pk):
    if request.method == "POST":
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect("homePage")
    return render(request, 'index.html', {'category': getAllCategory})



def category_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    posts = Category.objects.filter(category=card)  # category — це ForeignKey до Card
    return render(request, 'category/category_detail.html', {'card': card, 'posts': posts})


# def createCategory(request):
#     if request.method == 'POST':
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         image = request.FILES.get("image")

#         Category.objects.create(
#             category_title = title,
#             category_description = description,
#             category_pathImage = image
#         )

#         Category.objects.create(
#             category_title = title,
#             category_description = description,
#             category_pathImage = image
#         )
#         return redirect("homePage")
#     return render(request, "category/addCategory.html")
    