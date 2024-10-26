from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from  store.models import Product
from .models import Cart, CartItem


# Create your views here.


def cart(request):
    cart=Cart.objects.get(user=request.user)
    cart_items=CartItem.objects.filter(cart=cart)
    total_price=sum(item.product.price * item.quantity for item in cart_items)
    shipping_fee=3
    total = total_price + shipping_fee
    context={
        'cart_items':cart_items,
        'total_price':total_price,
        'shipping_fee':shipping_fee,
        'total':total,
    }
    return render(request, 'order/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    cart, created = Cart.objects.get_or_create(user=request.user)
    product=get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('order:cart')


def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, product_id=product_id)
    cart_item.delete()
    return redirect('order:cart')



def checkout(request):
    return render('order/checkout.html')