from django.shortcuts import render
from .models import Product, Category
from django.db.models import *

# Create your views here.

def store(request):
    return render(request, 'index/index.html')

def contact(request):
    return render(request, 'contact/contact.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})

def shop_details(request):
    return render(request, 'shop/shop-details.html')


