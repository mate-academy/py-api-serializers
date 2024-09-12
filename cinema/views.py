from rest_framework import viewsets

from cinema.models import (
    CinemaHall, Genre, Actor, Movie, MovieSession
)
from cinema.serializers import (
    CinemaHallSerializer, GenreSerializer,
    ActorSerializer, MovieSerializer,
    MovieSessionSerializer, MovieDetailSerializer,
    MovieListSerializer, MovieSessionDetailSerializer,
    MovieSessionListSerializer
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

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("actors", "genres")
        return self.queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        if self.action == "list":
            return MovieSession.objects.select_related("movie", "cinema_hall")
        if self.action == "retrieve":
            return MovieSession.objects.select_related(
                "movie", "cinema_hall"
            ).prefetch_related("movie__actors", "movie__genres")
        return self.queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
