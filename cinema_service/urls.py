from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/",
         include(("cinema.urls", "cinema"), namespace="apiv1")),

    path("api/cinema/", include("cinema.urls")),


]
