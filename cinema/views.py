from django.db.models import Prefetch
from rest_framework import viewsets

from .models import (
    Movie,
    Actor,
    Genre,
    MovieSession,
    CinemaHall,
)
from .serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("genres__movies__actors")
        return self.queryset


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("cinema_hall", "movie")
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return self.serializer_class
