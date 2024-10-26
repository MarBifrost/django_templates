from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def store(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        keywords = query.split()
        query_filter = Q()
        for keyword in keywords:
            query_filter &= Q(product_name__icontains=keyword)
        products = Product.objects.filter(query_filter)

    return render(request, 'index/index.html', {'products': products})

def contact(request):
    return render(request, 'contact/contact.html')

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content = {
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'shop/shop.html', content)


def shop_details(request):
    return render(request, 'shop/shop-details.html')


