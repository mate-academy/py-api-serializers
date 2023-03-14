from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Actor,
    Genre,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    ActorRetrieveSerializer,
    MovieSessionListSerializer, MovieSessionRetrieveSerializer,
)


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def get_queryset(self):
    #     queryset = self.queryset
    #     if self.action == "list":
    #         queryset = queryset.prefetch_related("genres", "actors")
    #     return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        if self.action == "list":
            return MovieListSerializer
        return self.serializer_class


class MovieSessionView(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return self.serializer_class


class CinemaHallView(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ActorRetrieveSerializer
        return self.serializer_class
