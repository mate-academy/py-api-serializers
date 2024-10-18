from rest_framework import viewsets
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieSessionSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.prefetch_related("movie_set")
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.prefetch_related("movie_set")
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionSerializer
