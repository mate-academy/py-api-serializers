from typing import Type
from django.db.models import Prefetch, QuerySet
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionWriteSerializer,
)

class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def get_queryset(self) -> QuerySet[Genre]:
        qs = self.queryset
        if self.action == "list":
            return qs.only("id", "name")
        return qs

class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

    def get_queryset(self) -> QuerySet[Actor]:
        qs = self.queryset
        if self.action == "list":
            return qs.only("id", "first_name", "last_name")
        return qs

class CinemaHallViewSet(ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()

    def get_queryset(self) -> QuerySet[CinemaHall]:
        qs = self.queryset
        if self.action == "list":
            return qs.only("id", "name", "rows", "seats_in_row")
        return qs

class MovieViewSet(ModelViewSet):
    serializer_class = MovieWriteSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action == "list":
            return Movie.objects.only("id", "title", "description", "duration").prefetch_related(
                Prefetch("genres", queryset=Genre.objects.only("id", "name")),
                Prefetch("actors", queryset=Actor.objects.only("id", "first_name", "last_name")),
            )
        return Movie.objects.prefetch_related(
            Prefetch("genres", queryset=Genre.objects.only("id", "name")),
            Prefetch("actors", queryset=Actor.objects.only("id", "first_name", "last_name")),
        )

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieWriteSerializer

class MovieSessionViewSet(ModelViewSet):
    serializer_class = MovieSessionWriteSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action == "list":
            return MovieSession.objects.select_related("movie", "cinema_hall").only(
                "id",
                "show_time",
                "movie__id",
                "movie__title",
                "cinema_hall__id",
                "cinema_hall__name",
                "cinema_hall__rows",
                "cinema_hall__seats_in_row",
            )
        return MovieSession.objects.select_related("movie", "cinema_hall").prefetch_related(
            Prefetch("movie__genres", queryset=Genre.objects.only("id", "name")),
            Prefetch("movie__actors", queryset=Actor.objects.only("id", "first_name", "last_name")),
        )

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionWriteSerializer
