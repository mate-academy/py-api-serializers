from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieCreateUpdateSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionCreateUpdateSerializer,
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
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieCreateUpdateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateUpdateSerializer
        return MovieSessionDetailSerializer

    def get_queryset(self):
        if self.action != "list":
            return self.queryset.prefetch_related(
                "movie__genres", "movie__actors"
            )
        return self.queryset
