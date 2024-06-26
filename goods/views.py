from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Products

def catalogWoman(request, category_slug=None):
    categories = Categories.objects.all()
    goods = Products.objects.filter(gender="Жен")
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        goods = goods.filter(category=category)
    context = {
        'title': 'IGNIS - Женский каталог',
        'year': '2024',
        'categories': categories,
        'goods': goods,
    }
    return render(request, 'goods/catalog-woman.html', context)

def catalogMen(request, category_slug=None):
    categories = Categories.objects.all()
    goods = Products.objects.filter(gender="Муж")
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        goods = goods.filter(category=category)
    context = {
        'title': 'IGNIS - Мужской каталог',
        'year': '2024',
        'categories': categories,
        'goods': goods,
    }
    return render(request, 'goods/catalog-men.html', context)

def product(request):
    context = {
        'title': 'IGNIS - Продукт',
        'year': '2024',
    }
    return render(request, 'goods/products.html', context)
