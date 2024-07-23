from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("cinema.urls", namespace="cinema")),
] + debug_toolbar_urls()
