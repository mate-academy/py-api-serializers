from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer

from cinema.models import Movie, MovieSession, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Movie] = Movie.objects

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = (
                queryset
                .prefetch_related("actors", "genres")
            )
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[MovieSession] = MovieSession.objects

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = (
                queryset
                .select_related("movie", "cinema_hall")
            )
        return queryset


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
