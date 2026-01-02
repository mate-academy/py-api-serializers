from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreListSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieCreateUpdateSerializer,
    MovieSessionListSerializer,
    MovieSessionCreateUpdateSerializer,
    MovieSessionDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ("update", "create", "partial_update"):
            return MovieCreateUpdateSerializer
        return MovieDetailSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        return Movie.objects.prefetch_related("genres", "actors")


class MovieSessionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionCreateUpdateSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        return MovieSession.objects.select_related("movie", "cinema_hall")
