from rest_framework import viewsets
from cinema.models import Movie, CinemaHall, Genre, Actor, MovieSession
from cinema.serializers import (
    CinemaHallSerializer,
    ActorSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionListSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieSessionCreateSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("actors", "genres")
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")

        return queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "movie", "cinema_hall"
    ).prefetch_related("movie__genres", "movie__actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        elif self.action in ["create", "update"]:
            return MovieSessionCreateSerializer
        return MovieSessionRetrieveSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related(
                "movie",
                "cinema_hall").prefetch_related(
                "movie__genres", "movie__actors"
            )
        return queryset
