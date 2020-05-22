from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product, Category
from django.contrib import messages
from home.views import index
import uuid
# Create your views here.


def user_cart(request):
    cart = request.session.get('cart', {})

    context = {
        'cart': cart
    }

    return render(request, 'cart/cart.template.html', context)


def add_to_cart(request, product_id):
    if request.method == 'POST':
        # obtain user's cart from the session
        cart = request.session.get('cart', {})
        buying_quantity = int(request.POST['quantity'])
        size = request.POST['size']

        # if user hasn't added the item to cart OR
        # if user has already added the same item but want a different size

        if product_id not in cart:
            product = get_object_or_404(Product, pk=product_id)
            order_id = str(uuid.uuid4())

            cart[product_id] = {
                'order_id': order_id,
                'id': product_id,
                'name': product.name,
                'quantity': buying_quantity,
                'size': size,
                'cost': float(product.price)
            }

        else:
            cart[product_id]['quantity'] += buying_quantity

        request.session['cart'] = cart

        messages.success(request, "Product added to cart.")
        return redirect(reverse(user_cart))


def delete_from_cart(request, product_id):
    # retrieve cart
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]

        request.session['cart'] = cart
        messages.success(request, 'Item removed from cart.')

    return redirect(reverse(user_cart))
