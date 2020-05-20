from django import forms
from .models import Category, Product, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tagname',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'creator', 'category', 'tags',)
