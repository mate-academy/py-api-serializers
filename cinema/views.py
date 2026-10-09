from django.db.models.query import QuerySet

from rest_framework import viewsets
from rest_framework import serializers

from .models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)
from .serializers import (
    GenreSerializer,
    GenreListSerializer,
    GenreRetrieveSerializer,
    ActorSerializer,
    ActorListSerializer,
    ActorRetrieveSerializer,
    CinemaHallSerializer,
    CinemaHallListSerializer,
    CinemaHallRetrieveSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return ActorListSerializer
        elif self.action == "retrieve":
            return ActorRetrieveSerializer
        return ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return GenreListSerializer
        elif self.action == "retrieve":
            return GenreRetrieveSerializer
        return GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return CinemaHallListSerializer
        elif self.action == "retrieve":
            return CinemaHallRetrieveSerializer
        return CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset
