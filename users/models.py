from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')
    town = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name='Улица')
    house = models.CharField(max_length=50, blank=True, null=True, verbose_name='Дом')
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username