from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from .forms import ReviewForm
from manage_product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required
def review(request, product_id):
    # create review form
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=product_id)

        review_form = ReviewForm()

        context = {
            'review_form': review_form,
            'product': product
        }

        return render(request, 'reviews/review.template.html', context)

    # create review
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        product_reviewed = get_object_or_404(Product, pk=product_id)
        if review_form.is_valid():
            temp_review = review_form.save(commit=False)
            temp_review.owner = request.user
            temp_review.product = product_reviewed
            temp_review.save()
            messages.success(
                request, f'Review for {product_reviewed.name} has been saved.')

            return redirect('/products/details/' + str(product_id))
