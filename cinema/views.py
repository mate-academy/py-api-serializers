from typing import Type

from rest_framework import viewsets

from cinema.models import Movie, MovieSession, Actor, Genre, CinemaHall
from cinema.serializers import (
    CinemaHallSerializer,
    ActorSerializer,
    GenreSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")
    model = Movie
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> Type[
        MovieListSerializer
        | MovieDetailSerializer
        | MovieSerializer
    ]:
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.prefetch_related(
        "cinema_hall",
        "movie__actors",
        "movie__genres"
    )
    model = MovieSession
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> Type[
        MovieSessionListSerializer
        | MovieSessionDetailSerializer
        | MovieSessionSerializer
    ]:
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    model = Actor
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    model = Genre
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    model = CinemaHall
    serializer_class = CinemaHallSerializer
