from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product, Category
from django.contrib import messages
import uuid
from decimal import Decimal
from .models import Order
# Create your views here.


def user_cart(request):
    cart = request.session.get('cart', {})

    subtotal = 0
    delivery_fee = Decimal('10.00')
    total_qty = 0
    summary = []

    for key, item in cart.items():
        line_total = item['quantity']*Decimal(item['unit_cost'])
        subtotal += line_total
        total_qty += item['quantity']
        summary.append({key: item['quantity']})

    if subtotal >= 20:
        delivery_fee = Decimal('0.00')

    total = delivery_fee + subtotal

    cart_summary = request.session.get('cart_summary', {})

    cart_summary = {
        'subtotal': str(subtotal),
        'total': str(total),
        'delivery_fee': str(delivery_fee),
        'summary': summary
    }

    request.session['cart_summary'] = cart_summary

    context = {
        'cart': cart,
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'total': total,
        'total_quantity': total_qty
    }

    return render(request, 'cart/cart.template.html', context)


def add_to_cart(request, product_id):
    if request.method == 'POST':
        # obtain user's cart from the session
        cart = request.session.get('cart', {})
        buying_quantity = int(request.POST['quantity'])

        # if user hasn't added the item to cart OR
        # if user has already added the same item but want a different size
        # create a unique but easily retrievable key in cart
        get_item = get_object_or_404(Product, pk=product_id)
        if get_item.category.name == 'Accessory':
            size = 0
        else:
            size = request.POST['size']

        cart_item_id = str(product_id) + '-' + str(size)

        if cart_item_id not in cart:
            product = get_object_or_404(Product, pk=product_id)
            order_id = str(uuid.uuid4())

            cart[cart_item_id] = {
                'cart_item_id': cart_item_id,
                'order_id': order_id,
                'product_id': product_id,
                'name': product.name,
                'quantity': buying_quantity,
                'size': size,
                'unit_cost': str(product.price),
                'product_image': product.image.cdn_url
            }
            messages.success(
                request, f"{product.name} has been added to your cart.")

        else:
            cart[cart_item_id]['quantity'] += buying_quantity
            messages.success(
                request, f"{cart[cart_item_id]['name']} has been added to your cart.")

        request.session['cart'] = cart

        return redirect(reverse(user_cart))


def delete_from_cart(request, cart_item_id):
    # retrieve cart
    cart = request.session.get('cart', {})

    if cart_item_id in cart:
        messages.success(
            request, f"{cart[cart_item_id]['name']} has been removed from cart.")
        del cart[cart_item_id]

        request.session['cart'] = cart

    return redirect(reverse(user_cart))


def update_from_cart(request, cart_item_id):
    # retrieve cart
    cart = request.session.get('cart', {})
    product_selected = get_object_or_404(
        Product, pk=cart[cart_item_id]['product_id'])

    if request.method == 'GET':

        context = {
            'update_quantity': cart[cart_item_id]['quantity'],
            'update_size': cart[cart_item_id]['size'],
            'product_name': cart[cart_item_id]['name'],
            'product_cost': cart[cart_item_id]['unit_cost'],
            'product_id': cart[cart_item_id]['product_id'],
            'cart_item_id': cart_item_id,
            'product': product_selected
        }

        return render(request, 'cart/update_cart.template.html', context)
    if request.method == 'POST':
        updated_quantity = int(request.POST['quantity'])
        updated_size = 0

        if product_selected.category.name == 'Accessory':
            updated_size = 0
        else:
            updated_size = request.POST['size']

        if cart_item_id in cart:
            cart[cart_item_id]['quantity'] = updated_quantity
            cart[cart_item_id]['size'] = updated_size

            request.session['cart'] = cart
            messages.success(request, 'Item has been updated in the cart.')

        return redirect(reverse(user_cart))
