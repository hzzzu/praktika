# Generated by Django 4.2.13 on 2024-06-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_products_color_products_compound_products_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='gender',
            field=models.TextField(blank=True, null=True, verbose_name='Пол'),
        ),
    ]
