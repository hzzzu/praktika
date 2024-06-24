from django.shortcuts import render

def login(request):
    context = {
        'title': 'IGNIS - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'IGNIS - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'IGNIS - Личный кабинет'
    }
    return render(request, 'users/profile.html', context)


# def logout(request):
#     context = {
#         'title': 'Home - Выход'
#     }
#     return render(request, 'users/logout.html', context)