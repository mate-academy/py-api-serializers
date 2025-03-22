from rest_framework import viewsets, status
from rest_framework.response import Response

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    MovieCreateUpdateSerializer,
    MovieSessionCreateUpdateSerializer
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
    queryset = Movie.objects.prefetch_related("actors", "genres").all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        elif self.action == "list":
            return MovieSerializer
        return MovieCreateUpdateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        MovieSession.objects.select_related("movie", "cinema_hall").all())

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        elif self.action == "list":
            return MovieSessionSerializer
        return MovieSessionCreateUpdateSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class TicketViewSet(viewsets.ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
