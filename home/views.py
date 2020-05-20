from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'home/index.template.html')