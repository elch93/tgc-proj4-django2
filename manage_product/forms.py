from django import forms
from .models import Category, Product, Tag
from pyuploadcare.dj.forms import ImageField


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class ProductForm(forms.ModelForm):
    image = ImageField(label="", required=False)

    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'tags', 'image',)
