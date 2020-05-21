from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('products/<category_selected>', views.view_all, name='view_products')
]
