from rest_framework import viewsets
from .models import Genre, Actor, CinemaHall, Movie, MovieSession
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


# -------- Genre --------
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# -------- Actor --------
class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# -------- CinemaHall --------
class CinemaHallViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


# -------- Movie --------
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer


# -------- MovieSession --------
class MovieSessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer
