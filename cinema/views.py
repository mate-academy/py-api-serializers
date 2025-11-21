# write views here

from cinema.models import Actor, CinemaHall, Genre, MovieSession, Movie
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
)
from rest_framework import viewsets


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
    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        else:
            return MovieDetailSerializer

    def get_queryset(self):
        return Movie.objects.all().prefetch_related("genres", "actors")


class MovieSessionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        else:
            return MovieSessionDetailSerializer

    def get_queryset(self):
        return (
            MovieSession.objects.all()
            .select_related("movie", "cinema_hall")
            .prefetch_related("movie__genres", "movie__actors")
        )
