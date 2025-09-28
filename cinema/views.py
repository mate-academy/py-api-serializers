from rest_framework.viewsets import ModelViewSet

from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieSessionRetrieveListSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionDetailSerializer,
    CinemaHallCreateSerializer,
    MovieCreateSerializer
)
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CinemaHallCreateSerializer
        return self.serializer_class


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSerializer
        elif self.action == "retrieve":
            return MovieListSerializer
        elif self.action == "create":
            return MovieCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            return Movie.objects.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionRetrieveListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            return MovieSession.objects.select_related(
                "movie",
                "cinema_hall")
        return self.queryset
