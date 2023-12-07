from rest_framework import viewsets
from rest_framework import serializers

from cinema.models import (Actor,
                           Genre,
                           CinemaHall,
                           Movie,
                           MovieSession,)

from cinema.serializers import (ActorSerializer,
                                GenreSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionSerializer,
                                MovieSessionDetailSerializer,
                                MovieSessionListSerializer,)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self) -> queryset:
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("actors", "genres")
        return self.queryset

    def get_serializer_class(self) -> serializers:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> queryset:
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related("movie", "cinema_hall")
        return self.queryset
      
    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
