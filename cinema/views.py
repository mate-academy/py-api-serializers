from typing import Type

from rest_framework import viewsets
from rest_framework.serializers import Serializer

from .models import Movie, MovieSession, Actor, Genre, CinemaHall
from .serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_queryset(self) -> queryset:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = self.queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> queryset:
        queryset = self.queryset
        if self.action == "list":
            queryset = self.queryset.select_related()
        elif self.action == "retrieve":
            queryset = self.queryset.prefetch_related(
                "movie__genres",
                "movie__actors"
            )
        return queryset

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
