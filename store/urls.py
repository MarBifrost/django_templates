from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.shop_details, name='shop_details'),
]