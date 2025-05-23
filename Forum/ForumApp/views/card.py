from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from ForumApp.models import Card,Category
from django.contrib.auth.decorators  import login_required
def getAllCategory():
    card = Card.objects.all()
    return card
@login_required
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
    return render(request, "Card/addCard.html")


def home(request:HttpRequest):
    getCard = getAllCategory()
    return render(request, 'index.html', {'cards': getCard})


# def card_detail(request, pk):
#     card = get_object_or_404(Card, pk=pk)
#     posts = Card.objects.filter(category=card)  # category — це ForeignKey до Card
#     return render(request, 'category/category_detail.html', {'card': card, 'posts': posts})

def card_detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    categories = Category.objects.filter(category=card)
    return render(request, 'ForumApp/card_detail.html', {
        'card': card,
        'categories': categories
    })