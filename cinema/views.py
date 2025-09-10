from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Genre, Actor, CinemaHall, Movie, MovieSession
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieWriteSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny,)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by("id")
    serializer_class = ActorSerializer
    permission_classes = (AllowAny,)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
    permission_classes = (AllowAny,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action in ("retrieve",):
            return MovieDetailSerializer
        return MovieWriteSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all().order_by("-show_time")
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action in ("retrieve",):
            return MovieSessionDetailSerializer
        return MovieSessionWriteSerializer
