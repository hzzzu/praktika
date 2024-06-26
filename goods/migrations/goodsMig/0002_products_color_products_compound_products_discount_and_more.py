# Generated by Django 4.2.13 on 2024-06-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.TextField(blank=True, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='products',
            name='compound',
            field=models.TextField(blank=True, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Скидка в %'),
        ),
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Размер'),
        ),
    ]
