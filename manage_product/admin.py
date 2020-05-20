from django.contrib import admin
from .models import Tag, Category, Product
# Register your models here.
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Category)