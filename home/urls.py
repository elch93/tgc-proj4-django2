from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('products/', views.view_all, name='view_products'),
    path('products/details/<product_id>', views.product_details, name='product_details'),
]
