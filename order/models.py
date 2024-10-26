from django.contrib.auth.models import User
from django.db import models


# from store.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.product.price * self.quantity if self.product else 0

    def save(self, *args, **kwargs):
        if self.product:
            self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.product_name if self.product else 'კალათა ცარიელია'} - {self.quantity} X {self.price}"
        # product_name = self.product.product_name if self.product else "კალათა ცარიელია"
        # return f"{product_name}{self.quantity}{self.total_price}"
