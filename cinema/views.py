# write views here
from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import Genre, Movie, Actor, MovieSession, CinemaHall
from cinema.serializers import (
    GenreSerializer,
    MovieSerializer,
    ActorSerializer,
    MovieSessionSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieSessionListSerializer,
    MovieDetailSerializer,
    MovieSessionDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        if self.action == "list":
            return Movie.objects.prefetch_related("genres", "actors")
        elif self.action == "retrieve":
            return Movie.objects.prefetch_related("genres", "actors")
        return self.queryset


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action == "list":
            return MovieSession.objects.select_related("movie", "cinema_hall")
        elif self.action == "retrieve":
            return MovieSession.objects.select_related("movie", "cinema_hall")
        return self.queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
