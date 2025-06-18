from rest_framework.viewsets import ModelViewSet
from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall
from cinema.serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    MovieCreateUpdateSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    MovieSessionCreateUpdateSerializer,
    CinemaHallSerializer,
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieCreateUpdateSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie",
                                                   "cinema_hall"
                                                   ).all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionCreateUpdateSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
