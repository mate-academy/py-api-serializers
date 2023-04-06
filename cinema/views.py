from rest_framework import viewsets

from . import models
from . import serializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = models.CinemaHall.objects.all()
    serializer_class = serializers.CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = models.Movie.objects.all()
        if self.action in ["list", "retrieve"]:
            queryset = models.Movie.objects.prefetch_related(
                "genres", "actors"
            )
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieListSerializer

        if self.action == "retrieve":
            return serializers.MovieDetailSerializer

        return serializers.MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = models.MovieSession.objects.select_related(
        "movie", "cinema_hall"
    )

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MovieSessionListSerializer

        if self.action == "retrieve":
            return serializers.MovieSessionDetailSerializer

        return serializers.MovieSessionSerializer
