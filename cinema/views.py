from typing import Type

from rest_framework import viewsets

from cinema.models import Genre, CinemaHall, Actor, MovieSession, Movie
from cinema.serializers import (
    GenreSerializer,
    CinemaHallSerializer,
    ActorSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSessionDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(
        self,
    ) -> Type[
        MovieSessionDetailSerializer
        | MovieSessionListSerializer
        | MovieSessionSerializer
    ]:
        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        if self.action == "list":
            return MovieSessionListSerializer

        return self.serializer_class


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("actors", "genres")
        return queryset

    def get_serializer_class(
        self,
    ) -> Type[MovieListSerializer | MovieDetailSerializer | MovieSerializer]:
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return self.serializer_class
