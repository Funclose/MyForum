from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from ForumApp.models import User

def custom_404(request, exception):
    return render(request, '404.html', status=404)

#сделать сохранение на странице с введенными данными пользователя
#сделать проверку на уже созданого пользователя
def register_user_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        birthday = request.POST.get("birthday")

        if User.objects.filter(email=email).exists():
            return render(request, "registration/registration.html", {'error':'такое email уже занят'})
        
        if password != confirmPassword:
            return render(request, "registration/registration.html", {'error':'пароли не совпадают'})    

        User.objects.create(
            name = name,
            surname = surname,
            password = password,
            confirmpassword = confirmPassword,
            email = email,
            birthday = birthday
        )
        return redirect('homePage')
    return render(request, "registration/registration.html")

def authorizeUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['user_id'] = user.id  
                return redirect('homePage')
            else:
                return render(request, "authorization/login.html", {'error': 'Неверный пароль'})
        except User.DoesNotExist:
            return render(request, "authorization/login.html", {'error': 'Пользователь c таким email не найден'})
    return render(request, "authorization/login.html")


def checkUserAuthorize(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'index.html', {'user': user})
    return redirect('homePage')



