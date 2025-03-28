# write urls here
from django.urls import path, include
from rest_framework import routers
from .views import GenreViewSet, ActorViewSet, MovieViewSet, CinemaHallViewSet, MovieSessionViewSet

router = routers.DefaultRouter()
router.register('genre', GenreViewSet)
router.register('actor', ActorViewSet)
router.register('movie', MovieViewSet)
router.register('cinema_hall', CinemaHallViewSet)
router.register('movie_session', MovieSessionViewSet)



urlpatterns = [
    path('', include(router.urls)),
]

app_name = 'cinema'
