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
        'gender': "Женщинам",
        'gender_url': 'goods:catalog-woman'
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
        'gender': "Мужчинам",
        'gender_url': 'goods:catalog-man'
    }
    return render(request, 'goods/catalog-men.html', context)

def product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    gender_text = 'Женщинам' if product.gender == 'Жен' else 'Мужчинам'
    context = {
        'title': 'IGNIS - Продукт',
        'year': '2024',
        'product': product,
        'gender': gender_text
    }
    return render(request, 'goods/product.html', context)
