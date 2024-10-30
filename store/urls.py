from django.contrib.auth.views import LoginView
from django.urls import path
from .views import StoreView, ContactView, ShopView, ShopDetailsView, CategoryView, Registration

app_name = 'store'

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/', ShopDetailsView.as_view(), name='shop_details'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category_view'),
    path('account/', LoginView.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
]

# urlpatterns = [
#     path('', views.store, name='store'),
#     path('contact/', views.contact, name='contact'),
#     path('shop/', views.shop, name='shop'),
#     path('product/', views.shop_details, name='shop_details'),
#     path('category/<slug:slug>', views.category_view, name='category_view'),
# ]