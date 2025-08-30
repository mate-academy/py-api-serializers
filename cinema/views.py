from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework import viewsets, mixins
from .models import Movie, Genre, Actor, CinemaHall, MovieSession

from .serializers import MovieUpdateSerializer, MovieListSerializer, GenresSerializer, ActorSerializer, \
    CinemaHallSerializer, MovieSessionSerializer, MovieSessionListSerializer, MovieSerializer, \
    MovieSessionUpdateSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == 'list':
            return MovieListSerializer
        elif self.action in ['update', 'create', 'partial_update']:
            return MovieUpdateSerializer
        return  MovieSerializer

    def get_queryset(self) ->  QuerySet[Movie]:
        queryset = self.queryset
        if self.action in ['list', 'retrieve']:
            return Movie.objects.prefetch_related("genres", "actors")
        return queryset


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ["update", "partial_update", "create"]:
            return MovieSessionUpdateSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.select_related("cinema_hall", "movie").prefetch_related(
            "movie__actors",
            "movie__genres"
        )
        return queryset


