from django.db.models import QuerySet
from typing import Type
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer
from cinema.models import MovieSession, Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSessionSerializer,
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSessionListSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer, MovieSessionRetrieveSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related(
                "movie", "cinema_hall"
            ).prefetch_related(
                "movie__genres", "movie__actors"
            )
        return queryset
