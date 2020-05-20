from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Tag
from .forms import ProductForm, CategoryForm, TagForm
# Create your views here.


@login_required
def index(request):
    category_form = CategoryForm()
    tag_form = TagForm()
    product_form = ProductForm()

    context = {
        'cform': category_form,
        'tform': tag_form,
        'pform': product_form
    }

    return render(request, 'manage_product/manage.template.html', context)
