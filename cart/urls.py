from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/<product_id>', views.add_to_cart, name='add_to_cart'),
]
