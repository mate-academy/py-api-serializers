from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import Movie, MovieSession, CinemaHall, Genre, Actor
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action == "list":
            return self.queryset.prefetch_related(
                "genres",
                "actors"
            )
        elif self.action == "retrieve":
            return self.queryset.prefetch_related(
                "genres",
                "actors"
            )
        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action == "list":
            return self.queryset.select_related(
                "movie",
                "cinema_hall"
            )
        if self.action == "retrieve":
            return self.queryset.select_related(
                "movie",
                "cinema_hall"
            ).prefetch_related(
                "movie__genres",
                "movie__actors"
            )
        return self.queryset


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
