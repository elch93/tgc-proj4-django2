from django.db import models
from django.contrib.auth.models import User
from manage_product.models import Product
# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.title
