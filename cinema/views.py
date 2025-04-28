from rest_framework import viewsets

from cinema.models import (Actor,
                           CinemaHall,
                           Movie,
                           MovieSession,
                           Genre)
from cinema.serializers import (GenreSerializer,
                                CinemaHallSerializer,
                                CinemaHallDetailSerializer,
                                MovieSerializer,
                                MovieDetailSerializer,
                                MovieListSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer,
                                ActorSerializer)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.prefetch_related("actors", "genres")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CinemaHallDetailSerializer
        return CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in {"retrieve", "list"}:
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
