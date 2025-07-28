from rest_framework import viewsets

from cinema.models import Movie, CinemaHall, Actor, Genre, MovieSession
from cinema.serializers import (
    MovieSerializer,
    CinemaHallSerializer,
    ActorSerializer,
    GenreSerializer,
    MovieRetrieveSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("actors", "genres")
        return self.queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related("movie", "cinema_hall")
        return self.queryset
