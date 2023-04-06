from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
