from cmath import acosh

from rest_framework import viewsets

from cinema.models import Actor, Movie, Genre, CinemaHall, MovieSession
from cinema.serializers import ActorSerializer, GenreSerializer, CinemaHallSerializer, MovieSerializer, \
    MovieSessionSerializer, MovieListSerializer


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
        if self.action == 'list':

            return Movie.objects.all().prefetch_related('actors', 'genres')
        # fallback for retrieve/create/update/destroy
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all().select_related()
    serializer_class = MovieSessionSerializer






