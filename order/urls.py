from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, PriceRangeView, RefreshView, CheckoutView

app_name = 'order'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/', PriceRangeView.as_view(), name='get_price_range'),
    path('refresh/', RefreshView.as_view(), name='refresh'),
]

# urlpatterns = [
#     path('cart/', views.cart, name='cart'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
#     path('checkout/', views.checkout, name='checkout'),
#     path('accounts/login/', admin.site.urls),
#     path('filter-price/', views.get_price_range, name='get_price_range'),
#
# ]