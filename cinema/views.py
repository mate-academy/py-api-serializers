from rest_framework import viewsets

from .models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieDetailSerializer,
    MovieListSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class CinemaHallViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer

    def get_queryset(self):
        return Movie.objects.all().prefetch_related("genres", "actors")


class MovieSessionViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = MovieSession.objects.select_related("movie", "cinema_hall")
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("movie__genres", "movie__actors")
        return queryset

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer
