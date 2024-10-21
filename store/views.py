from django.shortcuts import render


# Create your views here.

def store(request):
    return render(request, 'index/index.html')

def contact(request):
    return render(request, 'contact/contact.html')

def shop(request):
    return render(request, 'shop/shop.html')

def shop_details(request):
    return render(request, 'shop/shop-details.html')
