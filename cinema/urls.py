from django.urls import path, include
from rest_framework import routers

from cinema.views import CinemaHallViewSet, GenreViewSet, ActorViewSet, MovieViewSet, MovieSessionViewSet

routers = routers.DefaultRouter()
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("genres", GenreViewSet)
routers.register("actors", ActorViewSet)
routers.register("movies", MovieViewSet)
routers.register("movies_sessions", MovieSessionViewSet)

urlpatterns = [
        path('', include(routers.urls))
    ]

app_name = 'cinema'
