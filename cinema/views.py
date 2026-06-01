from rest_framework import viewsets

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
