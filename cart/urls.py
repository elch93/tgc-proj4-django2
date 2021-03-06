from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_cart, name='view_cart'),
    path('add/<product_id>', views.add_to_cart, name='add_to_cart'),
    path('delete/<cart_item_id>', views.delete_from_cart, name='delete_from_cart'),
    path('update/<cart_item_id>', views.update_from_cart, name='update_from_cart'),
]
