from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product
# Create your views here.


def index(request):
    return render(request, 'home/index.template.html')


def view_all(request, category_selected):
    all_products = Product.objects.all()

    context = {
        'category_selected': category_selected,
        'products': all_products
    }
    print(category_selected)
    return render(request, 'home/view.template.html', context)
