from rest_framework import viewsets

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
    Order,
    Ticket
)
from cinema.serializers import GenreSerializer, ActorSerializer, \
    CinemaHallSerializer, MovieSerializer, MovieSessionSerializer, \
    OrderSerializer, TicketSerializer, MovieListSerializer, \
    MovieSessionListSerializer, MovieDetailSerializer, \
    MovieSessionDetailsSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return MovieSessionSerializer
        if self.action == "retrieve":
            return MovieSessionDetailsSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
