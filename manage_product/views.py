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
        # create category, tag, product
        if ProductForm(request.POST).is_valid() and 'psubmit' in request.POST:
            pform = ProductForm(request.POST)
            created_item = pform.save(commit=False)
            created_item.creator = request.user
            pform.save()

        elif CategoryForm(request.POST).is_valid() and 'csubmit' in request.POST:
            cform = CategoryForm(request.POST)
            created_item = cform.save(commit=False)
            created_item.creator = request.user
            cform.save()

        elif TagForm(request.POST).is_valid() and 'tsubmit' in request.POST:
            tform = TagForm(request.POST)
            created_item = tform.save(commit=False)
            created_item.creator = request.user
            tform.save()

        return redirect(reverse(index))


@login_required
def delete(request, item_type, item_id):
    if item_type == 'category':
        item = get_object_or_404(Category, pk=item_id)
    if item_type == 'tag':
        item = get_object_or_404(Tag, pk=item_id)
    if item_type == 'product':
        item = get_object_or_404(Product, pk=item_id)

    context = {
        'item': item,
        'item_type': item_type.capitalize()
    }

    # confirmation page
    if request.method == 'GET':
        return render(request, 'manage_product/delete.template.html', context)
    # delete item
    if request.method == 'POST':
        item.delete()
        return redirect(reverse(index))


@login_required
def edit(request, item_type, item_id):
    # return the respective form for edit
    if request.method == 'GET':
        if item_type == 'category':
            item = get_object_or_404(Category, pk=item_id)
            edit_form = CategoryForm(instance=item)

        if item_type == 'tag':
            item = get_object_or_404(Tag, pk=item_id)
            edit_form = TagForm(instance=item)

        if item_type == 'product':
            item = get_object_or_404(Product, pk=item_id)
            edit_form = ProductForm(instance=item)

        context = {
            'form': edit_form,
            'item_type': item_type
        }

        return render(request, 'manage_product/edit.template.html', context)
    # save the edited instance
    if request.method == 'POST':
        if item_type == 'category':
            item = get_object_or_404(Category, pk=item_id)
            edited_form = CategoryForm(request.POST, instance=item)

        elif item_type == 'tag':
            item = get_object_or_404(Tag, pk=item_id)
            edited_form = TagForm(request.POST, instance=item)

        elif item_type == 'product':
            item = get_object_or_404(Product, pk=item_id)
            edited_form = ProductForm(request.POST, instance=item)

        if edited_form.is_valid():
            edited_form.save()
        return redirect(reverse(index))
