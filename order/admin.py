from django.contrib import admin
from .models import CartItem, Cart


# Register your models here.
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price', 'total_price')
    search_fields = ('product_product_name',)
    list_filter = ('cart', 'product')



admin.site.register(CartItem, CartItemsAdmin)
admin.site.register(Cart)