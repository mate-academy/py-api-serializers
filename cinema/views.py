from typing import Any
from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieCreateSerializer,
    MovieSessionCreateSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieCreateSerializer
        return MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action == "retrieve":
            return MovieSession.objects.select_related(
                "movie", "cinema_hall"
            ).prefetch_related(
                "movie__genres", "movie__actors"
            )
        return MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateSerializer
        return MovieSessionSerializer
