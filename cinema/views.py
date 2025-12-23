from typing import Type
from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import CinemaHall, Genre, Actor, MovieSession, Movie
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSessionSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[CinemaHall] = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Genre] = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Actor] = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Movie] = Movie.objects.all()

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:

        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[MovieSession] = MovieSession.objects.all()

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:

        if self.action in ("list", "retrieve"):
            return self.queryset.select_related(
                "movie", "cinema_hall"
            )
        return self.queryset
