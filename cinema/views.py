from rest_framework import viewsets

from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieCreateSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionCreateSerializer,
)
from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ["retrieve"]:
            return MovieDetailSerializer
        return MovieCreateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ["retrieve"]:
            return MovieSessionDetailSerializer
        return MovieSessionCreateSerializer
