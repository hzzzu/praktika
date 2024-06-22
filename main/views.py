from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'IGNIS - Главная',
        'sale': '-70% НА КОЛЛЕКЦИЮ VITTORIA VICCI',
        'year': '2024',
        }
    return render(request, 'main/index.html', context)

def login(request):
    return render(request, 'main/login.html')