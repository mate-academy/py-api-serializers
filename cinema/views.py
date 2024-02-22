from rest_framework import viewsets

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (CinemaHallSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionCreateSerializer,
                                MovieDetailSerializer)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "cinema_hall", "movie"
    ).prefetch_related("movie__actors", "movie__genres")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "create":
            return MovieSessionCreateSerializer

        return MovieSessionSerializer
