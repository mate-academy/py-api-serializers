from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/cinema/", include("cinema.urls"), name="cinema"),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()
