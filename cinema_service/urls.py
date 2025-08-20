from django.urls import path, include

urlpatterns = [
    path("api/", include(("cinema.urls", "cinema"),
                         namespace="cinema")),
]
