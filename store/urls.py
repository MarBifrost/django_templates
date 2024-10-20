from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('order/cart/', views.cart, name='cart'),
    path('order/checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.shop, name='shop'),
    path('ptoduct/', views.shop_details, name='shop_details'),
]