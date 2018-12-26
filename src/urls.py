"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.core.exceptions import PermissionDenied
from django.urls import path
from rest_framework.documentation import include_docs_urls
from .auth.urls import urlpatters as auth_urls
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application as oscar
from oscarapi.app import application as oscar_api
from django.conf import settings
from django.conf.urls.static import static

def forbidden(r):
    raise PermissionDenied

urlpatterns = [
    path('tech_admin/', admin.site.urls),
    url(r'oscar-api', oscar_api.urls),
    url(r'commerce/$', forbidden),
    url(r'commerce/(?!dashboard).*$', forbidden),
    url(r'commerce/', oscar.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^docs/', include_docs_urls(title='Midburn Tech API', public=False))
] + auth_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)