# Generated by Django 4.2.13 on 2024-06-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер телефона'),
        ),
    ]
