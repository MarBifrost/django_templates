from django.urls import path
from .views import profile_view
from django.contrib.auth.views import LogoutView

app_name='accounts'
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]