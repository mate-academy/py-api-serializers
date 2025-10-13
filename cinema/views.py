from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from cinema.models import (
    Actor,
    Genre,
    CinemaHall,
    Movie,
    MovieSession
)
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> Type[ModelSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> Type[ModelSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            queryset = MovieSession.objects.select_related(
                "movie", "cinema_hall"
            )
            return queryset.prefetch_related(
                "movie__actors",
                "movie__genres"
            )
        return self.queryset
