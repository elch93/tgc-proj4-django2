from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product, Category
from django.contrib import messages
from home.views import index
# Create your views here.


def user_cart(request):
    cart = request.session.get('cart', {})

    context = {
        'cart': cart
    }

    return render(request, 'cart/cart.template.html', context)


def add_to_cart(request, product_id):
    # obtain user's cart from the session
    cart = request.session.get('cart', {})

    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        buying_quantity = request.get('quantity')

        cart[product] = {
            'id': product_id,
            'name': product.name,
            'quantity': buying_quantity,
            'cost': product.price
        }

    else:
        cart[product_id]['quantity'] += buying_quantity

    request.session['cart'] = cart

    messages.success(request, "Product added to cart.")
    return redirect(reverse(index))
