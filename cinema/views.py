from rest_framework import viewsets
from cinema.models import (Movie,
                           MovieSession,
                           Actor,
                           CinemaHall,
                           Genre)
from cinema.serializers import (MovieSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                GenreSerializer,
                                MovieSessionSerializer,
                                MovieListSerializer,
                                MovieSessionDetailSerializer,
                                CinemaHallDetailSerializer,
                                MovieDetailSerializer,
                                MovieSessionListSerializer)


class MovieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.prefetch_related("genres", "actors")
        elif self.action == "retrieve":
            return queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related(
                "movie", "cinema_hall").prefetch_related(
                "movie__genres", "movie__actors"
            )
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer


class ActorSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CinemaHallDetailSerializer
        return CinemaHallSerializer
