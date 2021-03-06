"""insurer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from django.utils.translation import gettext as _

from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.i18n import JavaScriptCatalog

admin.site.site_header = _('Insurer administration')
admin.site.site_title = _('Insurer administration')
admin.site.index_title = _('Site administration')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/customer-service/',
                       include('customer_service.api.urls',
                               namespace='api-v1-customer-service')),
                  path('customer-service/',
                       include('customer_service.urls',
                               namespace='customer-service')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('jsi18n/', JavaScriptCatalog.as_view(),
                       name='javascript-catalog'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
