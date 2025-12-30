from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import BaseSerializer
from typing import Type
from .models import Actor, Genre, Movie, MovieSession, CinemaHall
from .serializers import (
    ActorSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    CinemaHallSerializer,
    MovieCreateUpdateSerializer, MovieSessionCreateSerializer
)


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
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieCreateUpdateSerializer
        return MovieDetailSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "movie", "cinema_hall"
    )

    def get_serializer_class(self) -> Type[BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateSerializer
        return MovieSessionDetailSerializer
