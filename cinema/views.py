from rest_framework import viewsets

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession
from cinema import serializers


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = serializers.CinemaHallsSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")
    serializer_class = serializers.MovieListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieListSerializer
        elif self.action == "retrieve":
            return serializers.MovieRetrieveSerializer
        return serializers.MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.prefetch_related("movie", "cinema_hall")
    serializer_class = serializers.MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieSessionListSerializer
        elif self.action == "retrieve":
            return serializers.MovieSessionRetrieveSerializer
        return serializers.MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == ("list", "retrieve"):
            return queryset.prefetch_related("movie", "cinema_hall")
        return queryset
