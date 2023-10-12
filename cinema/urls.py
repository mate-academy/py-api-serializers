from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("movie_sessions", MovieSessionViewSet, basename="movie_sessions")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
