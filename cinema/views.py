from typing import Type

from rest_framework import viewsets, serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionWriteSerializer,
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
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieWriteSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        MovieSession.objects
        .select_related("movie", "cinema_hall")
        .prefetch_related("movie__genres", "movie__actors")
    )

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action in ["list"]:
            return MovieSessionListSerializer
        if self.action in ["retrieve"]:
            return MovieSessionDetailSerializer
        return MovieSessionWriteSerializer
