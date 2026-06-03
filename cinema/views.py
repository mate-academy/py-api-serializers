from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    CinemaHallSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionSerializer,
    MovieCreateSerializer,
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
    serializer_class = MovieListSerializer

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "create":
            return MovieCreateSerializer
        return MovieDetailSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action == "list":
            return MovieSession.objects.select_related("movie", "cinema_hall")
        return MovieSession.objects.select_related(
            "movie", "cinema_hall"
        ).prefetch_related("movie__genres", "movie__actors")

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "create":
            return MovieSessionSerializer
        return MovieSessionDetailSerializer
