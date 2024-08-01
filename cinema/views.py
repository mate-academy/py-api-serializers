from rest_framework import viewsets

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie").all()

    def get_serializer_class(self):
        self.serializer_class = MovieSessionListSerializer
        if self.action == "retrieve":
            self.serializer_class = MovieSessionRetrieveSerializer
        elif self.action == "create":
            self.serializer_class = MovieSessionSerializer
        return self.serializer_class


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors").all()

    def get_serializer_class(self):
        self.serializer_class = MovieSerializer
        if self.action == "list":
            self.serializer_class = MovieListSerializer
        elif self.action == "retrieve":
            self.serializer_class = MovieRetrieveSerializer
        return self.serializer_class
