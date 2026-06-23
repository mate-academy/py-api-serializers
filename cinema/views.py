from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, MovieSession, CinemaHall, Genre, Actor
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSessionRetrieveSerializer,
)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> type[MovieSerializer]:

        if self.action == "create":
            return MovieSerializer

        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieListSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> type[MovieSessionSerializer]:
        if self.action == "create":
            return MovieSessionSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionListSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
