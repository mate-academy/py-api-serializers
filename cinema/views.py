from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer

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
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionCreateUpdateSerializer,
    MovieCreateUpdateSerializer,
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

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieCreateUpdateSerializer
        return MovieListSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            queryset = Movie.objects.prefetch_related("actors", "genres")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieSessionCreateUpdateSerializer
        return MovieSessionListSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action == "list":
            queryset = MovieSession.objects.select_related("movie", "cinema_hall")
        elif self.action == "retrieve":
            queryset = queryset.select_related(
                "movie",
                "cinema_hall"
            ).prefetch_related(
                "movie__actors",
                "movie__genres"
            )
        return queryset
