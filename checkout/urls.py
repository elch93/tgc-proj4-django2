from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success', views.checkout_success, name='checkout_success'),
    path('cancelled', views.checkout_cancelled, name='checkout_cancelled'),
    path('payment_completed', views.payment_completed, name='payment_completed'),
]
