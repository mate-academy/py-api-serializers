from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession
from cinema.serializers import MovieSerializer, GenreSerializer, ActorSerializer, CinemaHallSerializer, \
    MovieSessionSerializer, MovieDetailSerializer, MovieListSerializer, MovieSessionListSerializer, \
    MovieSessionDetailSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("genres").prefetch_related("actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
