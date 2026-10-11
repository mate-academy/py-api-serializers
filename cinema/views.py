from django.db.models import QuerySet
from rest_framework import viewsets

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieListSessionSerializer,
    MovieSessionWriteSerializer,
    MovieWriteSerializer
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

    def get_serializer_class(self) -> type:
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ("create", "update", "partial_update"):
            return MovieWriteSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> type:
        if self.action == "list":
            return MovieListSessionSerializer
        elif self.action in ("create", "update", "partial_update"):
            return MovieSessionWriteSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset
