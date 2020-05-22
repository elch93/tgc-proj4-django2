from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Order:
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    summary = models.TextField(blank=True)
