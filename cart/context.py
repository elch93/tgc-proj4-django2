
def cart_content(request):
    cart = request.session.get('cart', {})
    number_of_items = 0

    for item in cart:
        number_of_items += cart[item]['quantity']

    context = {
        'cart': cart,
        'number_of_items': number_of_items
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
        'cart_summary': cart_summary,
        'subtotal': cart_summary['subtotal'],
        'total': cart_summary['total'],
        'delivery_fee': cart_summary['delivery_fee'],
        'summary': cart_summary['summary']
    }

    return context
