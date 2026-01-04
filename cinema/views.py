from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Actor,
    Genre,
    CinemaHall,
    Movie,
    MovieSession
)
from cinema.serializers import ActorSerializer, GenreSerializer, \
    CinemaHallSerializer, MovieSerializer, MovieSessionSerializer, \
    MovieListSerializer, MovieRetrieveSerializer, MovieSessionListSerializer, \
    MovieSessionRetrieveSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action in ["list", "retrieve"]:
            return Movie.objects.prefetch_related("genres", "actors")
        return Movie.objects.all()


class MovieSessionViewSet(ModelViewSet):
    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action in ["list", "retrieve"]:
            return MovieSession.objects.select_related(
                "movie",
                "cinema_hall"
            )
        return MovieSession.objects.all()

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer
