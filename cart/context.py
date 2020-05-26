
def cart_content(request):
    cart = request.session.get('cart', {})
    context = {
        'cart': cart,
        'number_of_items': len(cart)
    }

    return context


def cart_summary(request):
    cart_summary = request.session.get('cart_summary', {
        'subtotal': float(0),
        'total': float(0),
        'delivery_fee': 'NIL',
        'summary': []
    })

    context = {
        'subtotal': cart_summary['subtotal'],
        'total': cart_summary['total'],
        'delivery_fee': cart_summary['delivery_fee'],
        'summary': cart_summary['summary']
    }

    return context
