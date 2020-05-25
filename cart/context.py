

def cart_content(request):
    cart = request.session.get('cart', {})
    context = {
        'cart': cart,
        'number_of_items': len(cart),
        'subtotal': cart['subtotal'],
        'total': cart['total'],
        'delivery_fee': cart['delivery_fee'],
        'summary': cart['summary']
    }

    return context
