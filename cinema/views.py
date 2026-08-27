from django.db.models import QuerySet
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from cinema.models import Actor, Movie, MovieSession, CinemaHall, Genre
from cinema.serializers import (ActorSerializer, MovieSerializer,
                                MovieSessionSerializer, CinemaHallSerializer,
                                GenreSerializer, MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer)


class ActorsViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related(
                "movie",
                "cinema_hall",
            )
        return self.queryset


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
