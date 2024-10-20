from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('error/', views.error_404, name='error'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('shop-details/', views.shop_details, name='shop_details'),
    path('testimonials/', views.testimonials, name='testimonials'),
]