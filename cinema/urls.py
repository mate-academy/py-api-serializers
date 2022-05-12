
from rest_framework import routers
from django.urls import path, include

from cinema.views import GenreViewSet, ActorViewSet, MovieListViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieListViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
