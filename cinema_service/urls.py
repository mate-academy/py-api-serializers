from django.contrib import admin
from django.urls.conf import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls"), name="cinema"),
]
