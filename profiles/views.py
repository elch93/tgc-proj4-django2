from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from home.views import index
# Create your views here.


@login_required
def profile(request):
    if request.method == 'GET':
        profile = get_object_or_404(UserProfile, user=request.user)
        profile_form = UserProfileForm(instance=profile)

        context = {
            'profile': profile,
            'profile_form': profile_form
        }
        return render(request, 'profiles/profile.template.html', context)

    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        updated_form = UserProfileForm(request.POST, instance=profile)
        if updated_form.is_valid():
            updated_form.save()
            messages.success(request, f'Profile for {request.user.username} has been updated.')

        return redirect(reverse(index))
