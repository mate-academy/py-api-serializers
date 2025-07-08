from cmath import acosh

from rest_framework import viewsets

from cinema.models import Actor, Movie, Genre, CinemaHall, MovieSession
from cinema.serializers import ActorSerializer, GenreSerializer, CinemaHallSerializer, MovieSerializer, \
    MovieSessionSerializer, MovieListSerializer, MovieSessionListSerializer, MovieSessionRetrieveSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().select_related()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().select_related()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all().select_related()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        if self.action in ('list', 'retrieve'):
            return Movie.objects.all() \
                .prefetch_related('actors', 'genres')
        return super().get_queryset()

    def get_serializer_class(self):
        return MovieListSerializer if self.action == 'list' else MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSessionListSerializer
    queryset = MovieSession.objects.all().select_related()

    def get_queryset(self):
        base_qs = MovieSession.objects.all()
        if self.action in ('list', 'retrieve'):
            return base_qs.select_related('movie', 'cinema_hall')
        return base_qs  # or super().get_queryset()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer




