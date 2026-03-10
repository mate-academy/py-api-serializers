from django.db.models.query import QuerySet
from rest_framework import viewsets

from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer,
)
from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
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
    queryset = Movie.objects

    def get_serializer_class(self) -> MovieSerializer:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("genres", "actors")

        return self.queryset.all()


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self) -> MovieSessionSerializer:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related("movie", "cinema_hall")

        return self.queryset.all()
