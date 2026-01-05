from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

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
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action in ("retrieve", "list"):
            return self.queryset.prefetch_related("actors", "genres")
        return self.queryset.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action in ("retrieve", "list"):
            return self.queryset.select_related("movie", "cinema_hall")
        return self.queryset.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer
