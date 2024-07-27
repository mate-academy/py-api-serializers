from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema"))
] + debug_toolbar_urls()
