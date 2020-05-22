from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_cart, name='view_cart'),
    path('add/<product_id>', views.add_to_cart, name='add_to_cart'),
    path('delete/<product_id>', views.delete_from_cart, name='delete_from_cart'),
    path('update/<product_id>', views.update_from_cart, name='update_from_cart'),
]
