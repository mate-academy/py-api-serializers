from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionListSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> (
            Type[MovieListSerializer]
            | Type[MovieRetrieveSerializer]
            | Type[MovieSerializer]
    ):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            self.queryset = Movie.objects.prefetch_related("actors", "genres")

        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> (
            Type[MovieSessionListSerializer]
            | Type[MovieSessionRetrieveSerializer]
            | Type[MovieSessionSerializer]
    ):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            self.queryset = (MovieSession.objects
                             .select_related("cinema_hall", "movie"))

        return self.queryset
