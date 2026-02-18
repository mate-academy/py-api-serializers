from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Movie,
    MovieSession,
    Actor,
    Genre,
    CinemaHall,
)
from cinema.serializers import (
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
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

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            queryset.prefetch_related("genres", "actors")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all().select_related(
        "movie",
        "cinema_hall",
    )

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer
