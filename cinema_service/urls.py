from django.contrib import admin
from django.urls import path, include

import cinema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("cinema.urls"), name="api"),
]
