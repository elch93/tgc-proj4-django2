from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product, Category
from django.contrib import messages
from django.db.models import Q
from reviews.models import Review
# Create your views here.


def index(request):

    return render(request, 'home/index.template.html')


def view_all(request):
    # sort functionality
    current_sort = 'name'
    current_tag = None

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'alpha':
                current_sort = 'name'
            if sort == 'price':
                current_sort = 'price'
            if 'direction' in request.GET:
                if request.GET['direction'] == 'desc':
                    current_sort = f'-{current_sort}'

        # if user enter a search term on products page
        if 'q' in request.GET:
            userquery = request.GET['q']
            if not userquery:
                # no search term detected
                messages.error(request, 'Please enter a search term')
                return redirect(reverse(index))
            else:
                # case-insensitive search in product name or description
                search = Q(name__icontains=userquery) | Q(
                    description__icontains=userquery) | Q(
                    tags__name__icontains=userquery)
                results = Product.objects.filter(search)

                context = {
                    'products': results,
                }

                return render(request, 'home/view.template.html', context)

    if 'tag' in request.GET:
        if request.GET['tag'] == 'Sale':
            current_tag = request.GET['tag']
            category_selected = 'all'

            all_products = Product.objects.filter(
                tags__name__contains=current_tag).order_by(current_sort)

    if 'category' in request.GET and request.GET['category'] != 'all':
        category_selected = request.GET['category']
        all_products = Product.objects.filter(
            category__name__contains=category_selected).order_by(current_sort)

    if 'category' in request.GET and request.GET['category'] == 'all':
        all_products = Product.objects.all().order_by(current_sort)
        category_selected = 'all'

    context = {
        'products': all_products,
        'current_category': category_selected,
        'current_sort': current_sort,
        'current_tag': current_tag
    }

    return render(request, 'home/view.template.html', context)


def product_details(request, product_id):
    get_product = get_object_or_404(Product, pk=product_id)
    get_reviews = Review.objects.filter(product=get_product)

    context = {
        'product': get_product,
        'product_reviews': get_reviews
    }

    return render(request, 'home/details.template.html', context)
