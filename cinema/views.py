from rest_framework import viewsets

from cinema import models
from cinema import serializers


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = models.CinemaHall.objects
    serializer_class = serializers.CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects
    serializer_class = serializers.GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects
    serializer_class = serializers.ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.prefetch_related("genres", "actors")
    serializer_class = serializers.MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieListSerializer
        if self.action == "retrieve":
            return serializers.MovieRetrieveSerializer
        return self.serializer_class


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        models.MovieSession.objects
        .select_related("movie", "cinema_hall")
    )
    serializer_class = serializers.MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieSessionListSerializer
        if self.action == "retrieve":
            return serializers.MovieSessionRetrieveSerializer
        return self.serializer_class
