from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet
)


router = DefaultRouter()


router.register("genre", GenreViewSet)
router.register("actor", ActorViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
