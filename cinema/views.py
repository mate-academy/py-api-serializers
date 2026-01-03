from django.db.models import QuerySet
from rest_framework import viewsets

from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer
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

    def get_serializer_class(self) -> type[
        MovieDetailSerializer | MovieListSerializer
    ]:
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieListSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        return Movie.objects.prefetch_related("actors", "genres")


class MovieSessionViewSet(viewsets.ModelViewSet):

    def get_queryset(self) -> QuerySet[MovieSession]:
        return MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> type[
        MovieSessionDetailSerializer | MovieSessionSerializer
    ]:
        if self.action == "retrieve":  # detail view
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
