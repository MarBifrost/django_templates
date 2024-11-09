from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from  store.models import Product
from .models import Cart, CartItem
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils.translation import gettext as _

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'order/cart.html'
    login_url = 'store:login'
    redirect_field_name = "next"


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, _('კალათის შიგთავსის სანახავად, გთხოვთ გაიაროთ ავტორიზაცია'))
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        cart=Cart.objects.get(user=request.user)
        cart_items=CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        shipping_fee = 3
        total = total_price + shipping_fee
        total_quantity = sum(item.quantity for item in cart_items)

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'shipping_fee': shipping_fee,
            'total': total,
            'total_quantity': total_quantity
        }
        return render(request, self.template_name, context)

class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
        cart_item.save()
        # return redirect('order:cart')
        return redirect(request.META.get('HTTP_REFERER', 'store:store'))

class RemoveFromCartView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        cart_item = CartItem.objects.filter(product_id=product_id)
        cart_item.delete()
        return redirect('order:cart')

class PriceRangeView(View):
    def get(self, request):
        price_range = request.GET.get('rangeInput', None)
        products = Product.objects.all()

        if price_range:
            try:
                max_price = int(price_range)
                products = products.filter(price__lte=max_price)
            except ValueError:
                products = Product.objects.none()

        context = {
            'products': products,
            'price_range': price_range,
        }

        return render(request, 'shop/shop.html', context)

class RefreshView(View):
    def get(self, request):
        return redirect('shop/shop.html')

class CheckoutView(View):
    def get(self, request):
        return render(request, 'order/checkout.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


