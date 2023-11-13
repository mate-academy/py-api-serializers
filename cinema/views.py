from rest_framework import viewsets

from cinema.models import (Genre,
                           Movie,
                           Actor,
                           CinemaHall,
                           MovieSession
                           )

from cinema.serializers import (CinemaHallSerializer,
                                ActorSerializer,
                                GenreSerializer,
                                MovieSerializer,
                                MovieSessionSerializer
                                )


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):

    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):

    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer
