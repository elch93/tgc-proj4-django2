from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from .forms import ReviewForm
from manage_product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required
def review(request, product_id):
    if request.method == 'GET':
        review_form = ReviewForm()

        context = {
            'review_form': review_form
        }

        return render(request, 'reviews/review.template.html', context)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.owner = request.user
            review_form.product = get_object_or_404(Product, pk=product_id)
            review_form.save()
            messages.success(
                request, f'Review for {review_form.product.name} has been saved.')

            return redirect(reverse(review))
