from rest_framework import viewsets

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession
from cinema.serializers import (ActorSerializer,
                                GenreSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieSessionSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionRetrieveSerializer,
                                MovieSessionListSerializer)


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallsViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("actors", "genres")
        return Movie.objects.all()


class MovieSessionsViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return MovieSession.objects.select_related("movie", "cinema_hall")
        return MovieSession.objects.all()
