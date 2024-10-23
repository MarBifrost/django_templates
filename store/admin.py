from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'product_description', 'organic', 'fresh', 'sales', 'discount', 'expired')
    list_filter = ('product_name', )
    search_fields = ('product_name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)