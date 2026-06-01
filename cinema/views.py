from django.db.models import QuerySet
from rest_framework import viewsets

from cinema.models import CinemaHall, Movie, MovieSession, Genre, Actor
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> type[MovieSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("cinema_hall", "movie")
        return queryset

    def get_serializer_class(self) -> type[MovieSessionSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
