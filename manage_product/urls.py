from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='manage_home'),
    path('delete/<item_type>/<item_id>', views.delete, name='delete')
]
