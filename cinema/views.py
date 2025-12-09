from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession

from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MoviePostSerializer,
    MovieSessionPostSerializer,
)


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallsViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("actors", "genres")
        return self.queryset.all()

    def get_serializer_class(self) -> Serializer:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "create":
            return MoviePostSerializer
        return MovieSerializer


class MovieSessionsViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_queryset(self) -> QuerySet:
        return self.queryset.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> Serializer:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "create":
            return MovieSessionPostSerializer
        return MovieSessionSerializer
