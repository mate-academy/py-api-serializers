from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import Genre, Movie, Actor, CinemaHall, MovieSession
from cinema.serializers import (
    GenreSerializer,
    MovieSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieSessionListSerializer,
    MovieUpdateSerializer,
    MovieSessionUpdateSerializer)


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
    serializer_class = MovieListSerializer

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ("update", "partial_update", "create"):
            return MovieUpdateSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ("update", "partial_update", "create"):
            return MovieSessionUpdateSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return (queryset.select_related(
                "cinema_hall", "movie").prefetch_related(
                "movie__actors", "movie__genres"))
        return queryset
