from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("admin/", admin.site.urls),
]
