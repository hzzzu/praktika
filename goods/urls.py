from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('woman/', views.catalogWoman, name='catalog-woman'),
    path('men/', views.catalogMen, name='catalog-men'),
    path('product/', views.product, name='product'),
]