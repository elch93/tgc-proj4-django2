from .models import Order


class OrderForm():
    class Meta:
        model = Order
        fields = ('buyer', 'total', 'summary')
