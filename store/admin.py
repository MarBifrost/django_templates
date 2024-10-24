from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'image', 'product_description', 'for_piano', 'for_orchestra', 'sales', 'discount')
    list_filter = ('product_name', )
    search_fields = ('product_name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)