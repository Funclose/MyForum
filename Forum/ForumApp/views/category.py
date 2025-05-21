from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from ForumApp.models import Category, Card,Comment

def getAllCategory():
    categories = Category.objects.all()
    return categories


def createCategory(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        text = request.POST.get("text")
        likes = request.POST.get("likes")
        dataCreate = request.POST.get("dataCreate")

        Category.objects.create(
            author = author,
            text = text,
            created_at = dataCreate,
            likes = 0
        )
        return redirect("homePage")
    return render(request, "category/addCategory.html")

def add_post(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            Category.objects.create(
                author=author,
                text=text,
                category=card
            )
            return redirect('categoryPage', pk=pk)  

    return render(request, 'category/add_post.html', {'card': card})
    


def removeCategory(request, pk):
    if request.method == "POST":
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect("homePage")
    return render(request, 'index.html', {'category': getAllCategory})



def category_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method =='POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            Category.objects.create(
                author = author,
                text =text,
                category = card
            )
            return redirect('categoryPage', pk=pk) 
    posts = Category.objects.filter(category=card)  
    return render(request, 'category/categoryPage.html', {'card': card, 'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Category, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
            return redirect('post_detail', pk=pk)

    return render(request, 'category/post_detail.html', {'post': post, 'comments': comments})