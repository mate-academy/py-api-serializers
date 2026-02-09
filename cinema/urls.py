from django.urls import include, path
from rest_framework import routers

from cinema.views import ActorViewSet, GenreViewSet, MovieSessionViewSet, MovieViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
