from django.urls import path, include

urlpatterns = [
    path("cinema/", include("cinema.urls")),
]
