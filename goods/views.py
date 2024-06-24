from django.shortcuts import render

def catalogWoman(request):
    context: dict[str, str] = {
        'title': 'IGNIS - Женский каталог',
        'year': '2024',
        }
    return render(request,'goods/catalog-woman.html', context)

def catalogMen(request):
    context: dict[str, str] = {
        'title': 'IGNIS - Мужской каталог',
        'year': '2024',
        }
    return render(request,'goods/catalog-men.html', context)

def product(request):
    context: dict[str, str] = {
        'title': 'IGNIS - Продукт',
        'year': '2024',
        }
    return render(request,'goods/products.html', context)