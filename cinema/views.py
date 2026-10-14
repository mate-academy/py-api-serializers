from rest_framework import serializers, viewsets
from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieDetailSerializer,
    \
    MovieListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionCreateSerializer,
    \
    MovieCreateUpdateSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieDetailSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieCreateUpdateSerializer
        return MovieDetailSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateSerializer
        return MovieSessionDetailSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset
