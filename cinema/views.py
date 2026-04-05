
from rest_framework import viewsets
from django.db.models import QuerySet
from rest_framework.serializers import Serializer

from cinema.models import Movie, MovieSession, Genre, Actor, CinemaHall
from cinema.serializers import (MovieSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionSerializer,
                                MovieSessionRetrieveSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                ActorListSerializer,
                                MovieSessionListSerializer, )


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("genres", "actors")
        return Movie.objects.all()


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return ActorListSerializer
        return ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):

    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action in ("list", "retrieve"):
            return MovieSession.objects.select_related("movie", "cinema_hall")
        return MovieSession.objects.all()
