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

    all_categories = Category.objects.all()
    all_tags = Tag.objects.all()
    all_products = Product.objects.all()

    print(all_products)

    context = {
        'cform': category_form,
        'tform': tag_form,
        'pform': product_form,
        'categories': all_categories,
        'tags': all_tags,
        'products': all_products
    }
    if request.method == 'GET':
        return render(request, 'manage_product/manage.template.html', context)

    if request.method == 'POST':
        print(request.POST.get('tsubmit'))
        if CategoryForm(request.POST).is_valid() and request.POST.get('csubmit'):
            cform = CategoryForm(request.POST)
            cform.save()

        if TagForm(request.POST).is_valid() and request.POST.get('tsubmit'):
            tform = TagForm(request.POST)
            tform.save()

        if ProductForm(request.POST).is_valid():
            pform = ProductForm(request.POST)
            pform.save()

        return redirect(reverse(index))
