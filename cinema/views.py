from rest_framework import viewsets

from cinema.models import Movie, MovieSession, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = Movie.objects.all()

        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related(
                "genres",
                "actors",
            )

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSessionSerializer
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = MovieSession.objects.all()

        if self.action == "list":
            queryset = queryset.select_related(
                "movie",
                "cinema_hall",
            )

        if self.action == "retrieve":
            queryset = queryset.select_related(
                "movie",
                "cinema_hall",
            ).prefetch_related(
                "movie__actors",
                "movie__genres",
            )

        return queryset


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
