from django.db import models
from users.models import User
from goods.models import Products

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    
    def __str__(self):
        return f'Корзина пользователя {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Корзина')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    
    class Meta:
        db_table = 'cart_item'
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
    
    def __str__(self):
        return f'{self.product.name} - {self.quantity} шт.'