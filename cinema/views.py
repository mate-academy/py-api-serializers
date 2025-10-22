from rest_framework import viewsets

from cinema.models import Movie, MovieSession, CinemaHall, Actor, Genre
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    CinemaHallSerializer,
    ActorSerializer,
    GenreSerializer,
)


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        qs = self.queryset
        if self.action == "list":
            return qs.select_related()
        return qs

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("actors", "genres")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class CinemaHallsViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
