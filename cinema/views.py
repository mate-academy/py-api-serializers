from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets, serializers
from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    CinemaHallSerializer,
    MovieSessionListSerializer,
    MovieSessionSerializer,
    MovieSessionDetailListSerializer,
    MovieDetailSerializer,
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

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        return Movie.objects.prefetch_related("genres", "actors")


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailListSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        return (
            MovieSession.objects
            .select_related("movie", "cinema_hall")
            .prefetch_related("movie__genres", "movie__actors")
        )
