from rest_framework import viewsets, serializers

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall,
    MovieSession,
)

from cinema.serializers import (
    MovieListSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    GenreSerializer,
    MovieDetailSerializer,
    MovieSessionDetailSerializer,
    MovieCreateSerializer,
    ActorDetailSerializer,
    MovieSessionCreateSerializer,

)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        elif self.action == "list":
            return MovieSessionSerializer

        return MovieSessionCreateSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action == "list":
            return MovieListSerializer
        return MovieCreateSerializer
