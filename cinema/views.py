from rest_framework import viewsets

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("retrieve", "list"):
            queryset = queryset.prefetch_related("actors", "genres")

        return queryset.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("retrieve", "list"):
            queryset = queryset.select_related("movie", "cinema_hall")

        return queryset.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
