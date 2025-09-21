from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path(settings.BASE_API_URL, include("cinema.urls"))
] + debug_toolbar_urls()
