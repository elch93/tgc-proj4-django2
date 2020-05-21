from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, blank=False, null=True)
    country = CountryField(
        max_length=100, blank_label='(select country)', blank=False, null=True)
    city = models.CharField(max_length=40, blank=False, null=True)
    postal_code = models.CharField(max_length=20, blank=False, null=True)
    street_address_1 = models.CharField(max_length=80, blank=False, null=True)
    street_address_2 = models.CharField(max_length=80,  blank=True, null=True)

    def __str__(self):
        return self.user.username

# obtains a signal when User model is created during account registration


@receiver(post_save, sender=User)
def create__user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
