from rest_framework.viewsets import ModelViewSet

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionCreateSerializer,
    MovieCreateSerializer,
)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return Movie.objects.prefetch_related("genres", "actors")
        else:
            return Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        elif self.action == "create":
            return MovieCreateSerializer
        else:
            return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return MovieSession.objects.select_related("movie", "cinema_hall")
        else:
            return MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        elif self.action == "create":
            return MovieSessionCreateSerializer
        else:
            return MovieSessionSerializer
