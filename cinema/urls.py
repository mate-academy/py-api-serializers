from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreViewSet, MovieViewSet

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls))
]
