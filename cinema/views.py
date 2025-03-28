# write views here
from rest_framework import viewsets
from .models import Genre, Actor, Movie, CinemaHall, MovieSession
from .serializers import (GenreSerializer,
                          ActorSerializer,
                          MovieSerializer,
                          CinemaHallSerializer,
                          MovieSessionSerializer,
                          MovieListSerializer,
                          MovieRetrieveSerializer,
                          MovieSessionListSerializer,
                          MovieSessionRetrieveSerializer,
                          )


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieRetrieveSerializer
        return MovieListSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == ('list', 'retrieve'):
            return queryset.prefetch_related('genres', 'actors')
        return queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieSessionListSerializer
        elif self.action == 'retrieve':
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == ('list', 'retrieve'):
            return queryset.prefetch_related('movie', 'cinema_hall')
        return queryset

