from rest_framework import viewsets, serializers

from django.db.models import QuerySet

from cinema.models import (
    MovieSession,
    Actor,
    CinemaHall,
    Movie, Genre
)

from user.serializers import (
    MovieSessionSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionListSerializer
)


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return MovieSession.objects.select_related(
                "movie",
                "cinema_hall",
            ).prefetch_related(
                "movie__genres",
                "movie__actors",
            )

        return MovieSession.objects.all()


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("actors", "genres")
        return Movie.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer
