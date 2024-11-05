from .models import CartItem, Cart


def cart_quantity(request):
    total_quantity=0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)

    return {'total_quantity':total_quantity}