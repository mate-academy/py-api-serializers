from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import Genre, Movie, MovieSession, Actor, CinemaHall
from cinema.serializers import (GenreSerializer,
                                MovieSessionSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == 'list':
            return MovieListSerializer
        if self.action == 'retrieve':
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        return Movie.objects.prefetch_related('genres', 'actors')


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == 'list':
            return MovieSessionListSerializer
        if self.action == 'retrieve':
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        return MovieSession.objects.select_related('movie', 'cinema_hall')


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
