from django.shortcuts import render


# Create your views here.

def store(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'chackout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def shop_details(request):
    return render(request, 'shop-details.html')
