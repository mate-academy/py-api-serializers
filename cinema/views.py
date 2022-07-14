from rest_framework import viewsets

from cinema.models import Movie, Actor, CinemaHall, Genre, MovieSession
from cinema.serializers import MovieDetailSerialiser, ActorSerialiser, \
    CinemaHallSerialiser, GenreSerialiser, MovieSessionSerialiser, \
    MovieListSerializer, MovieSerializer, MovieSessionListSerializer, \
    MovieSessionDetailSerialiser


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):

        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerialiser

        return MovieSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerialiser


class CinemaHallsViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerialiser


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerialiser


class MovieSessionsViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all().select_related("movie",
                                                         "cinema_hall")
    serializer_class = MovieSessionSerialiser

    def get_serializer_class(self):

        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerialiser

        return MovieSessionSerialiser
