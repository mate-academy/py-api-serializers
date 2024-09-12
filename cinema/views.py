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
    MoviesSessionListSerializer,
    MovieSessionDetailSerializer,
)


class GenresView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorsView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallsView(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        if self.action in ["retrieve", "list"]:
            return self.queryset.prefetch_related("genres").prefetch_related(
                "actors"
            )

        return self.queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer

        if self.action == "list":
            return MovieListSerializer

        return MovieSerializer


class MovieSessionView(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        if self.action == "retrieve":
            return self.queryset.select_related("movie").select_related(
                "cinema_hall"
            )

        return self.queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MoviesSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer
