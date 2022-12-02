from django.db.migrations import serializer
from rest_framework import viewsets

from cinema.models import (
    Movie,
    CinemaHall,
    Genre,
    Actor,
    MovieSession,
    Order,
    Ticket,
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSerializer,
    OrderSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    TicketSerializer,
    TicketListDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> serializer:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "movie",
        "cinema_hall"
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> serializer:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related("user")
    serializer_class = OrderSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related("movie_session", "order")
    serializer_class = TicketSerializer

    def get_serializer_class(self) -> serializer:
        if self.action in (
            "list",
            "retrieve",
        ):
            return TicketListDetailSerializer
        return TicketSerializer
