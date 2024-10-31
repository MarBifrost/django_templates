from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from order.models import Cart

@receiver
def customer_cart(signals, sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)