from modeltranslation.translator import TranslationOptions, register
from .models import Product, Category

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("product_name", "product_description", )

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )
