from django.urls import path, include
urlpatterns = [
    path("api/cinema/", include("cinema.urls")),
]
