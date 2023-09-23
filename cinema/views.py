# write views here
from rest_framework import viewsets

from cinema.models import (
    Movie,
    CinemaHall,
    Genre,
    Actor,
    MovieSession
)
from cinema.serializers import (
    MovieSerializers,
    MovieListSerializers,
    MovieRetrieveSerializers,
    MovieSessionSerializers,
    MovieSessionListSerializers,
    MovieSessionRetrieveSerializers,
    CinemaHallSerializers,
    GenreSerializers,
    ActorSerializers,


)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializers
        if self.action == "retrieve":
            return MovieRetrieveSerializers
        return MovieSerializers


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializers


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializers

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializers
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializers
        return MovieSessionSerializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers
