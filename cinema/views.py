from rest_framework import viewsets

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession, Ticket
from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                TicketSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer,
                                MovieSessionSerializer,
                                MovieSerializer)


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
    queryset = MovieSession.objects.all().select_related("movie",
                                                         "cinema_hall")

    def get_serializer_class(self) -> type[
        MovieListSerializer
        | MovieDetailSerializer
        | MovieSerializer
    ]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("actors", "genres")

    def get_serializer_class(self) -> type[
        MovieListSerializer
        | MovieDetailSerializer
        | MovieSerializer
    ]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer
