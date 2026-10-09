from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer

from cinema.models import (CinemaHall,
                           Genre,
                           Actor,
                           Movie,
                           MovieSession)
from cinema.serializers import (CinemaHallSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer,
                                MovieSessionSerializer)


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
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related("genres", "actors")
        return super().get_queryset()


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action == "list":
            return MovieSession.objects.select_related(
                "movie",
                "cinema_hall",
            )
        if self.action == "retrieve":
            return MovieSession.objects.select_related(
                "movie",
                "cinema_hall",
            ).prefetch_related(
                "movie__actors",
                "movie__genres",
            )
        return super().get_queryset()
