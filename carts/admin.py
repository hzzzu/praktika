from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user') 
    list_filter = ('user',)
    inlines = [CartItemInline]

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    list_filter = ('product',)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
