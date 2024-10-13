from typing import Type
from rest_framework import viewsets, serializers
from django.db.models import QuerySet

from cinema.models import Movie, MovieSession, CinemaHall, Actor, Genre
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetireveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetireveSerializer,
    CinemaHallSerializer,
    ActorSerializer,
    GenreSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetireveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetireveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset
