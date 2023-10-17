from rest_framework import viewsets

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer
)


class GenreViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Genre.objects.all()
        return queryset

    def get_serializer_class(self):
        return GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Actor.objects.all()
        return queryset

    def get_serializer_class(self):
        return ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = CinemaHall.objects.all()
        return queryset

    def get_serializer_class(self):
        return CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Movie.objects.all()

        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = MovieSession.objects.all()

        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("movie", "cinema_hall")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer
