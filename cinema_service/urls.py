from django.contrib import admin
from django.urls import path, include

import cinema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls")),
]
