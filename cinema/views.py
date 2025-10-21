from django.db.models import QuerySet, Model
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionListSerializer,
    CinemaHallSerializer,
    ActorDetailSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "retrieve":
            return ActorDetailSerializer
        return ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieListSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Model]:
        return  self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.prefetch_related("movie", "cinema_hall")
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[Model]:
        return self.queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
