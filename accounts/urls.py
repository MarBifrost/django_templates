from django.urls import path
from .views import profile_view, send_mail_page
from django.contrib.auth.views import LogoutView

app_name='accounts'
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mail/', send_mail_page, name='email'),
]