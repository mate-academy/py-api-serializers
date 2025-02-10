from rest_framework import viewsets

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema import serializers


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = serializers.CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = Movie.objects.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieListSerializer
        if self.action == "retrieve":
            return serializers.MovieRetrieveSerializer
        return serializers.MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieSessionListSerializer
        elif self.action == "retrieve":
            return serializers.MovieSessionRetrieveSerializer
        return serializers.MovieSessionSerializer
