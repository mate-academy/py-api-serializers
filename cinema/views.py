from rest_framework import viewsets

from .serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer,
)

from .models import Actor, Genre, CinemaHall, Movie, MovieSession


class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallView(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionView(viewsets.ModelViewSet):
    queryset = (MovieSession.objects.
                select_related("movie", "cinema_hall").
                prefetch_related("movie__actors", "movie__genres"))

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer
