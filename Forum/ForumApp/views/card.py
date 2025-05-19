from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from ForumApp.models import Card

def getAllCategory():
    card = Card.objects.all()
    return card

def createCard(request):
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

def test(request):
    return render(request, '/category/categoryPage')


def home(request:HttpRequest):
    getCard = getAllCategory()
    return render(request, 'index.html', {'cards': getCard})


def category_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    posts = Card.objects.filter(category=card)  # category — це ForeignKey до Card
    return render(request, 'category/category_detail.html', {'card': card, 'posts': posts})