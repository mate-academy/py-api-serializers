from django.contrib import admin
from django.urls import path, include

from cinema import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include(urls, namespace="cinema"))
]
