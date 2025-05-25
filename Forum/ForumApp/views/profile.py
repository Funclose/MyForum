from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def profilePage(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        birthday = request.POST.get('birthday')
        password = request.POST.get('password')

        user.name = name
        user.birthday = birthday
        if password:
            user.set_password(password)
            update_session_auth_hash(request, user) 

            profile.nickname = nickname
            # if avatar:
            #     profile.avatar = avatar

            user.save()
            profile.save()
            messages.success(request, 'Данные успешно обновлены!')
            return redirect('profile')

    return render(request, 'profile/user_profile.html', {
        'user': request.user,
        'profile': request.user.profile,
    })