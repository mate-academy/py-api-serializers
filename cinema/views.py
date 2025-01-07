# write views here
from rest_framework import viewsets

from cinema.models import Genre, Actor, CinemaHall, MovieSession, Movie
from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer,
                                MovieSerializer,
                                MovieRetrieveSerializer,
                                MovieListSerializer)


class CinemaHallViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return Movie.objects.all().prefetch_related("genres", "actors")
        return Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return MovieSession.objects.all().select_related(
                "movie", "cinema_hall"
            )
        return MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
