from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product
from django.contrib import messages
from django.conf import settings
import stripe
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from profiles.views import profile
from cart.views import user_cart
from cart.models import Order
# Create your views here.

endpoint_secret = 'whsec_sXxoLf6gxEaOuWY3RD4uRXYvl3D4ezCs'


def handle_checkout_session(session):
    print(session)


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if len(cart) == 0:
        messages.error(request, 'Your cart is empty.')
        return redirect(reverse(user_cart))

    line_items = []
    grand_total = 0
    final_delivery_cost = 0

    for id, item in cart.items():
        x = id.split('-')
        product_object = get_object_or_404(Product, pk=x[0])
        grand_total += product_object.price*item['quantity']
        line_items.append({
            'name': product_object.name,
            'amount': int(product_object.price * 100),
            'currency': 'sgd',
            'quantity': item['quantity']
        })

    if grand_total >= 20:
        final_delivery_cost = 0
    else:
        final_delivery_cost = 10

    # add in delivery cost order line
    line_items.append({
        'name': 'Delivery Fee',
        'amount': int(final_delivery_cost * 100),
        'currency': 'sgd',
        'quantity': 1
    })

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=domain + reverse(checkout_success),
        cancel_url=domain + reverse(checkout_cancelled)
    )

    context = {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    }

    return render(request, 'checkout/checkout.template.html', context)


def checkout_success(request):
    cart_summary = request.session.get('cart_summary')
    # record transaction and display in profile
    record_order = Order.objects.create(
        buyer=request.user,
        total=float(cart_summary['total']),
        subtotal=float(cart_summary['subtotal']),
        delivery_cost=float(cart_summary['delivery_fee'])
    )

    request.session['cart'] = {}
    request.session['cart_summary'] = {
        'subtotal': 0,
        'total': 0,
        'delivery_fee': 'NIL',
        'summary': []
    }

    messages.success(request, 'Payment successfully made.')
    return redirect(reverse(profile))


def checkout_cancelled(request):
    messages.success(request, 'Payment cancelled.')
    return redirect(reverse(user_cart))


@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(status=400)

    # handle checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # fulfill purchase
        handle_checkout_session(session)

    return HttpResponse(status=200)
