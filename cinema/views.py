from rest_framework import viewsets

from .models import Actor, Genre, CinemaHall, Movie, MovieSession
from .serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSerializer,
    MovieSessionSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("genres", "actors")

        return self.queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer

        if self.action == "list":
            return MovieListSerializer

        return MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.select_related("movie", "cinema_hall")

        if self.action == "retrieve":
            return self.queryset.select_related(
                "movie", "cinema_hall"
            ).prefetch_related("movie__actors", "movie__genres")

        return self.queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        if self.action == "list":
            return MovieSessionListSerializer

        return MovieSessionSerializer
