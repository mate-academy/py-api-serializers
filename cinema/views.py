from rest_framework import viewsets
from django.db.models import QuerySet
from rest_framework.serializers import ModelSerializer

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieListSessionSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer,
    MovieRetrieveSerializer
)


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
    def get_queryset(self) -> QuerySet[Movie]:
        return Movie.objects.prefetch_related("actors", "genres")

    def get_serializer_class(self) -> type[ModelSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):

    def get_queryset(self) -> QuerySet[MovieSession]:
        return MovieSession.objects.select_related()

    def get_serializer_class(self) -> type[ModelSerializer]:
        if self.action == "list":
            return MovieListSessionSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer
