from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from order.models import Cart, CartItem
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from order.models import Cart, CartItem
from django.db.models import Q
from django.core.paginator import Paginator


class StoreView(View):
    def get(self, request):
        products = Product.objects.all()
        query = request.GET.get('q')
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_quantity = sum(item.quantity for item in cart_items)

        if query:
            keywords = query.split()
            query_filter = Q()
            for keyword in keywords:
                query_filter &= Q(product_name__icontains=keyword)
            products = Product.objects.filter(query_filter)

            return render(request, 'shop/shop.html', {'products': products})

        context = {
            'products': products,
            'cart': cart,
            'cart_items': cart_items,
            'total_quantity': total_quantity,
        }
        return render(request, 'index/index.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html')


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        paginator = Paginator(products, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_quantity = sum(item.quantity for item in cart_items)

        content = {
            'page_obj': page_obj,
            'categories': categories,
            'cart': cart,
            'cart_items': cart_items,
            'total_quantity': total_quantity,
        }
        return render(request, 'shop/shop.html', content)


class ShopDetailsView(View):
    def get(self, request):
        return render(request, 'shop/shop-details.html')


class CategoryView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category_name=category)

        context = {
            'category': category,
            'products': products,
        }

        return render(request, 'shop/shop.html', context)

# def store(request):
#     products = Product.objects.all()
#     query = request.GET.get('q')
#     cart = Cart.objects.get(user=request.user)
#     cart_items=CartItem.objects.filter(cart=cart)
#     total_quantity=sum(item.quantity for item in cart_items)
#     if query:
#         keywords = query.split()
#         query_filter = Q()
#         for keyword in keywords:
#             query_filter &= Q(product_name__icontains=keyword)
#         products = Product.objects.filter(query_filter)
#
#         return render(request, 'shop/shop.html', {'products': products})
#
#     context = {
#         'products': products,
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_quantity': total_quantity,
#     }
#     return render(request, 'index/index.html', context)
#
# def contact(request):
#     return render(request, 'contact/contact.html')
#
# def shop(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     paginator = Paginator(products, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     cart = Cart.objects.get(user=request.user)
#     cart_items=CartItem.objects.filter(cart=cart)
#     total_quantity=sum(item.quantity for item in cart_items)
#     content = {
#         'page_obj': page_obj,
#         'categories': categories,
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_quantity': total_quantity,
#     }
#     return render(request, 'shop/shop.html', content)
#
#
# def shop_details(request):
#     return render(request, 'shop/shop-details.html')
#
# def category_view(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     products=Product.objects.filter(category_name=category)
#
#     context = {
#         'category': category,
#         'products': products,
#     }
#
#     return render(request, 'shop/shop.html', context)
#

