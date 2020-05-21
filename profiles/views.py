from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
# Create your views here.


@login_required
def index(request):
    # print('here', request.user.username, request.user.email)
    # profile = get_object_or_404(UserProfile, user=request.user)
    # profile_form = UserProfileForm(instance=profile)
    profile_form = UserProfileForm()

    context = {
        'profile_form': profile_form
    }
    return render(request, 'profiles/profile.template.html', context)
