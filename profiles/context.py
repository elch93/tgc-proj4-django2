from .models import UserProfile
from django.shortcuts import get_object_or_404


def userprofile(request):
    userinfo = {}
    context = {}

    if request.user.is_authenticated:
        userinfo = get_object_or_404(UserProfile, user=request.user)

        context = {
            'user_email': userinfo.user.email,
            'user_contact': userinfo.contact,
            'user_country': userinfo.country,
            'user_city': userinfo.city,
            'user_postal': userinfo.postal_code,
            'user_s1': userinfo.street_address_1,
            'user_s2': userinfo.street_address_2
        }

    return context
