from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import Movie, MovieSession, Actor, Genre, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    ActorListSerializer,
    ActorRetrieveSerializer,
    GenreSerializer,
    GenreListSerializer,
    GenreRetrieveSerializer,
    CinemaHallSerializer,
    CinemaHallListSerializer,
    CinemaHallRetrieveSerializer
)


# Movie
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        return self.queryset


# MovieSession
class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        return self.queryset


# Actor
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return ActorListSerializer
        elif self.action == "retrieve":
            return ActorRetrieveSerializer
        return ActorListSerializer


# Genre
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return GenreListSerializer
        elif self.action == "retrieve":
            return GenreRetrieveSerializer
        return GenreSerializer


# CinemaHall
class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "list":
            return CinemaHallListSerializer
        elif self.action == "retrieve":
            return CinemaHallRetrieveSerializer
        return CinemaHallSerializer
