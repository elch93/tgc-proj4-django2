from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(max_length=100, blank_label='(select country)', blank=True, null=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    street_address_1 = models.CharField(max_length=80, null=True, blank=True)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username
