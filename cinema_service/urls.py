from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Підключаємо URL-адреси додатка cinema з правильним префіксом
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
]
