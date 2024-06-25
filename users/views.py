from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from carts.models import Cart
# from common.mixins import CacheMixin
# from orders.models import Order, OrderItem

from users.forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm
    context = {
        'title': 'IGNIS - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def users_cart(request) -> HttpResponseRedirect:
    return render(request, "users/cart.html", context)

class UserCartView(TemplateView):
    template_name = 'users/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Корзина'
        return context

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