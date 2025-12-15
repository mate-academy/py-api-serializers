from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import CinemaHall, Genre, Actor, MovieSession, Movie
from cinema.serializers import (CinemaHallSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionRetrieveSerializer)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset.all()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieListSerializer

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")
        return queryset.all()
