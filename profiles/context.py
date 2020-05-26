from cart.models import Order
from manage_product.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def order_history(request):
    # retrieve user's order history
    order_history = Order.objects.filter(buyer=request.user)

    item_purchased = {}

    for order in order_history:
        item_array = order.summary.split(',')
        item_array.pop()
        item_purchased[order.id] = []

        for i in item_array:
            details = i.split('-')
            product = get_object_or_404(Product, pk=details[0])

            item = {
                'product_name': product.name,
                'product_price': product.price,
                'size': details[1],
                'quantity': details[2]
            }
            item_purchased[order.id].append(item)
    context = {
        'item_purchased': item_purchased
    }

    return context
