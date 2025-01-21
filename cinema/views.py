from rest_framework import viewsets

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession
from cinema.serializers import GenreSerializer, ActorSerializer, CinemaHallSerializer, \
    MovieSessionSerializer, MovieListGenreActorSerializer, MovieSerializer, MovieSessionListSerializer, \
    MovieRetrieveSerializer, MovieRetrieveSessionSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListGenreActorSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSessionSerializer
        return MovieSessionSerializer
