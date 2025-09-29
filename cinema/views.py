from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall,
    MovieSession
)
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionRetrieveSerializer,
    MovieListSerializer,
    MovieSessionListSerializer,
    MovieRetrieveSerializer
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
    queryset = Movie.objects.prefetch_related("actors", "genres")

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset
