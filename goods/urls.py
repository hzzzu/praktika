from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('woman/', views.catalogWoman, name='catalog-woman'),
    path('woman/<slug:category_slug>/', views.catalogWoman, name='catalog-woman-category'),
    path('men/', views.catalogMen, name='catalog-men'),
    path('men/<slug:category_slug>/', views.catalogMen, name='catalog-men-category'),
    path('product/', views.product, name='product'),
    path('product/<int:product_id>', views.product, name='product'),
]
