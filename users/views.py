from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('main:index'))
            else:
                form.add_error(None, 'Неправильное имя пользователя или пароль')
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'IGNIS - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'IGNIS - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)



def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'IGNIS - Личный кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))