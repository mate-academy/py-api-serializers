from rest_framework import viewsets

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()\
        .prefetch_related("genres")\
        .prefetch_related("actors")

    def get_serializer_class(self) -> (
            MovieSerializer,
            MovieListSerializer,
            MovieDetailSerializer
    ):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()\
        .select_related("movie")\
        .select_related("cinema_hall")

    def get_serializer_class(self) -> (
            MovieSessionListSerializer,
            MovieSessionDetailSerializer,
            MovieSessionSerializer
    ):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
