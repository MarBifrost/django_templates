from enum import unique

from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            slug=slugify(str(self.name))
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug=f"{slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)



    def __str__(self):
        return self.name


class Product(models.Model):
    id=models.AutoField(primary_key=True, auto_created=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    image = models.ImageField('image', upload_to='static/img/', max_length=255, default='df_image.png')
    category_name = models.ManyToManyField(Category, related_name='products')
    quantity=models.IntegerField(null=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    product_description = models.CharField(max_length=255, null=True, blank=True)
    for_piano = models.BooleanField(default=False)
    for_orchestra = models.BooleanField(default=False)
    sales=models.BooleanField(default=False)
    discount=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


