from rest_framework.viewsets import ModelViewSet
from .models import Genre, Actor, CinemaHall, Movie, MovieSession
from .serializers import (
    GenreSerializer, ActorSerializer, CinemaHallSerializer,
    MovieListSerializer, MovieDetailSerializer,
    MovieSessionListSerializer, MovieSessionDetailSerializer, MovieCreateUpdateSerializer
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


# у файлі views.py
class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors").all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieCreateUpdateSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall").all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer
