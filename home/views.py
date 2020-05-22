from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product, Category
from django.contrib import messages
from django.db.models import Q
# Create your views here.

all_categories = Category.objects.all()


def index(request):
    # search
    if request.GET:
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
                    'categories': all_categories
                }

                return render(request, 'home/view.template.html', context)

    context = {
        'categories': all_categories
    }

    return render(request, 'home/index.template.html', context)


def view_all(request):
    # sort functionality
    current_sort = 'name'
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
                    'categories': all_categories
                }

                return render(request, 'home/view.template.html', context)

    if 'category' in request.GET and request.GET['category'] != 'all':
        category_selected = request.GET['category']
        all_products = Product.objects.filter(
            category__name__contains=category_selected).order_by(current_sort)

    else:
        all_products = Product.objects.all().order_by(current_sort)
        category_selected = request.GET['category']

    context = {
        'categories': all_categories,
        'products': all_products,
        'current_category': category_selected,
        'current_sort': current_sort
    }

    return render(request, 'home/view.template.html', context)


def product_details(request, product_id):
    # if user enter a search term on products page
    if request.GET:
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
                    'categories': all_categories
                }

                return render(request, 'home/view.template.html', context)

    get_product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': get_product
    }

    return render(request, 'home/details.template.html', context)
