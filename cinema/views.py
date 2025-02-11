from typing import Type

from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, Actor, Genre, MovieSession, CinemaHall
from cinema.serializers import (
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    ActorSerializer,
    GenreSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer,
    CinemaHallSerializer
)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset
        if self.action in (
            "list",
            "retrieve",
        ):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in (
            "list",
            "retrieve",
        ):
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        return CinemaHallSerializer
