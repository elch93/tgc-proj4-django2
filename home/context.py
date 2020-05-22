from manage_product.models import Category


def show_categories(request):
    all_categories = Category.objects.all()

    context = {
        'categories': all_categories
    }

    return context
