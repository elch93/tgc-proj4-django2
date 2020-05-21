from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ( 'contact', 'country', 'city', 'postal_code', 'street_address_1', 'street_address_2')
