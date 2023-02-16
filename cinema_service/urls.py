from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "cinema_service/",
        include("cinema.urls", namespace="cinema-service")
    ),
]
