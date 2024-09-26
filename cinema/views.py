from rest_framework import viewsets

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
from cinema import serializers as s


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = s.ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = s.CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = s.GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = s.MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("actors", "genres")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return s.MovieListSerializer
        if self.action == "retrieve":
            return s.MovieDetailSerializer
        return s.MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = s.MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return s.MovieSessionListSerializer
        if self.action == "retrieve":
            return s.MovieSessionDetailSerializer
        return s.MovieSessionSerializer
