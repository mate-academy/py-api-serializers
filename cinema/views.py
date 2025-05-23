from rest_framework import mixins, viewsets, generics

from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession
)
from .serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    MovieRetrieveSerializer,
    OrderSerializer,
    TicketSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


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
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
