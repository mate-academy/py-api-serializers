from django.urls import path, include

from .models import MovieSession
from .views import MovieViewSet, GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieSessionViewSet

from rest_framework import routers

app_name = 'cinema'
router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('genres', GenreViewSet)
router.register('actors', ActorViewSet)
router.register('cinema_halls', CinemaHallViewSet)
router.register('movie_sessions', MovieSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]

