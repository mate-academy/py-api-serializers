from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from .serializers import (MovieSerializer,
                          ActorSerializer,
                          MovieSessionSerializer,
                          CinemaHallSerializer,
                          GenreSerializer,
                          MovieDetailSerializer,
                          MovieListSerializer,
                          MovieSessionListSerializer,
                          MovieSessionDetailSerializer)
from .models import (Genre,
                     Actor,
                     CinemaHall,
                     Movie,
                     MovieSession,
                     Ticket,
                     Order)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    def get_queryset(self):

        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.prefetch_related("actors", "genres")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self):

        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.select_related("movie", "cinema_hall")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return self.serializer_class


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
