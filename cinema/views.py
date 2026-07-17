from rest_framework import viewsets

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


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
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("genres", "actors")
        return Movie.objects.all()


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        if self.action == "list":
            return MovieSession.objects.select_related("movie", "cinema_hall")
        elif self.action == "retrieve":
            return MovieSession.objects.select_related(
                "cinema_hall",
                "movie"
            ).prefetch_related(
                "movie__genres",
                "movie__actors"
            )
        return MovieSession.objects.all()
