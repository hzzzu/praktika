from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from goods.models import Products
from .models import Cart, CartItem

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'title': 'IGNIS - Корзина',
        'cart': cart
    }
    return render(request, 'carts/carts.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('carts:cart_detail')

@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('carts:cart_detail')
