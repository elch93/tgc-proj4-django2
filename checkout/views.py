from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_product.models import Product, Category
from django.contrib import messages
from django.conf import settings
import stripe
from django.contrib.sites.models import Site
# Create your views here.
