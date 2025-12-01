from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Movie, Actor, Genre
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    # 🚀 Correção N+1: otimização usando select_related + prefetch_related
    queryset = (
        Movie.objects
        .select_related("genre")          # FK
        .prefetch_related("actors")       # M2M
    )

    def list(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.prefetch_related("movies")

    def list(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.prefetch_related("movies")

    def list(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)
