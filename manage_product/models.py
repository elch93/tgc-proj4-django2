from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = ImageField(blank=True, manual_crop="", null=True)
    description = models.TextField(blank=True)
    date_posted = models.DateTimeField(blank=False, auto_now_add=True)

    def __str__(self):
        return self.name
