from django.urls import path, include
from rest_framework import routers

from cinema.views import ActorViewSet, MovieViewSet, GenreViewSet, CinemaHallViewSet, MovieSessionViewSet

app_name = 'cinema'

router = routers.DefaultRouter()

router.register('actors', ActorViewSet)
router.register('genres', GenreViewSet)
router.register('cinema-halls', CinemaHallViewSet)
router.register('movies', MovieViewSet)
router.register('movie-sessions', MovieSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]