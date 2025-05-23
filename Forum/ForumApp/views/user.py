from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest
from ForumApp.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators  import login_required
from django.contrib import messages
from ForumApp.models.user import User



def custom_404(request, exception):
    return render(request, '404.html', status=404)


def register_user_view(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        nickname = request.POST.get('surname')
        email = request.POST.get('email')
        birthday = request.POST.get("birthday")
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if User.objects.filter(email=email).exists():
            return render(request, "registration/registration.html", {'error':'такое email уже занят'})
        
        if password != confirmPassword:
            return render(request, "registration/registration.html", {
                'error': 'Пароли не совпадают',
                'name': name,
                'nickname': nickname,
                'email': email,
                'birthday': birthday
            })  
        
        newUser = User.objects.create_user(
            name = name,
            nickname = nickname,
            password = password,
            email = email,
            birthday = birthday
        )

        login(request, newUser)
        return redirect('homePage')
    return render(request, "registration/registration.html")

def authorizeUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return render(request, "authorization/login.html", {'error': 'Неверный email или пароль'})
    return render(request, "authorization/login.html")
    


def logout_view(request:HttpRequest):
    logout(request)
    return redirect('homePage')



