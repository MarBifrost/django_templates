"""
URL configuration for Django_Templates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns
# from django.shortcuts import redirect
# from django.utils.translation import get_language, activate
#
# def redirect_to_default_language(request):
#     activate('ka')
#     return redirect(f'/{get_language()}')

urlpatterns = [
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('store.urls', namespace='store')),
    path('order/', include('order.urls', namespace='order')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ]

# if 'rosseta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         re_path(r'^rosetta/', include('rosetta.urls')),
#     ]