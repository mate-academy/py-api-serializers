from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, MovieSessionViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
