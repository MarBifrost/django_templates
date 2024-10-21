from django.contrib.auth.models import User
from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price= models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name}{self.quantity}{self.total_price}"
