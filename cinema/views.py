# write views here
from rest_framework import viewsets

from cinema.models import Movie, MovieSession, CinemaHall, Genre, Order, Actor
from cinema.serializers import (
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieListSessionSerializer,
    MovieRetrieveSessionSerializer,
    MovieSessionSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    OrderSerializer,
    TicketSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self, *args, **kwargs):
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("actors", "genres")
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            return MovieListSerializer(*args, **kwargs)
        elif self.action == "retrieve":
            return MovieRetrieveSerializer(*args, **kwargs)
        return MovieSerializer(*args, **kwargs)


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self, *args, **kwargs):
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related("movie", "cinema_hall")
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            return MovieListSessionSerializer(*args, **kwargs)
        elif self.action == "retrieve":
            return MovieRetrieveSessionSerializer(*args, **kwargs)
        return MovieSessionSerializer(*args, **kwargs)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = TicketSerializer
