from django.contrib import admin
from django.urls import path, include

from cinema.urls import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include(router.urls))
]
