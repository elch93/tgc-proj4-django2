

def cart_content(request):
    cart = request.session.get('cart', {})
    context = {
        'cart': cart,
        'number_of_items': len(cart)
    }

    return context
