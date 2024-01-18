from rest_framework import viewsets

from cinema.models import Actor, Genre, CinemaHall, Movie, Ticket, MovieSession
from cinema.serializers import (MovieSerializer,
                                ActorSerializer,
                                MovieListSerializer,
                                CinemaHallSerializer,
                                MovieDetailSerializer,
                                TicketSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                ActorDetailSerializer, CinemaHallDetailSerializer, GenreSerializer,
                                MovieSessionDetailSerializer)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CinemaHallDetailSerializer
        return CinemaHallSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all().select_related("movie", "cinema_hall")
    serializer = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
