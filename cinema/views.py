from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre, Actor, CinemaHall, Movie
)
from cinema.serializers import (
    GenreSerializer, ActorSerializer, CinemaHallSerializer, MovieSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
