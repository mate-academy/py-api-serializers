from django.db.models import QuerySet
from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting cinema halls.
    """
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting genres.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting actors.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting movies.
    """
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type:
        """
        Return serializer based on action: list → MovieListSerializer,
        retrieve → MovieRetrieveSerializer
        """
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        """
        Prefetch related genres and actors for list and retrieve actions to optimize queries
        """
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving,
    updating and deleting movie sessions.
    """
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type:
        """
        Return serializer based on action: list → MovieSessionListSerializer,
        retrieve → MovieSessionRetrieveSerializer
        """
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        """
        Select related movie and cinema_hall for list and retrieve actions to optimize queries
        """
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related()
        return queryset
