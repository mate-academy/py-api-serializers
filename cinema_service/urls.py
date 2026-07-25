from django.contrib import admin
from django.urls import path, include

from cinema_service import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/",
         include("cinema.urls", namespace="cinema"),
         name="cinema"
         ),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
