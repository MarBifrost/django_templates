from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    category_name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug=slugify(str(self.category_name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    img_path = models.CharField(max_length=255, null=True)
    category = models.ManyToManyField(Category, related_name='products')
    quantity=models.IntegerField(null=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    product_description = models.CharField(max_length=255, null=True)
    organic = models.BooleanField(default=False)
    fresh= models.BooleanField(default=False)
    sales=models.BooleanField(default=False)
    discount=models.BooleanField(default=False)
    Expired = models.BooleanField(default=False)
    popularity=models.BooleanField(null=True)
    fantastic=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug=slugify(str(self.name))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


