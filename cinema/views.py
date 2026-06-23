from rest_framework.viewsets import ModelViewSet

from cinema.models import (Genre,
                           Actor,
                           CinemaHall,
                           Movie,
                           MovieSession)
from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieSessionSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        else:
            return MovieSerializer

    def get_queryset(self):
        if self.action in ["list", "retrieve"]:
            return Movie.objects.all().prefetch_related("genres", "actors")
        else:
            return Movie.objects.all()


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        else:
            return MovieSessionSerializer

    def get_queryset(self):
        if self.action in ["list", "retrieve"]:
            return MovieSession.objects.all().select_related(
                "movie",
                "cinema_hall").prefetch_related(
                "movie__actors",
                "movie__genres")
        else:
            return MovieSession.objects.all()
