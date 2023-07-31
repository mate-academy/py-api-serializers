from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre, Actor, CinemaHall, Movie, MovieSession
)
from cinema.serializers import (
    GenreSerializer, ActorSerializer, CinemaHallSerializer, MovieSerializer,
    MovieListSerializer, MovieDetailSerializer, MovieSessionSerializer,
    MovieSessionListSerializer, MovieSessionDetailSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):

    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
